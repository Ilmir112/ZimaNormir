import sys
from datetime import datetime, timedelta
import re

from PyQt5.QtCore import QDate

import well_data

from PyQt5.QtWidgets import QWidget, QLabel, QComboBox, QLineEdit, QGridLayout, QTabWidget, QMainWindow, QPushButton, \
    QMessageBox, QApplication, QHeaderView, QTableWidget, QTableWidgetItem, QTextEdit, QDateEdit, QDateTimeEdit

from normir.TabPageAll import TabPage, TemplateWork


class TabPage_SO_Timplate(TabPage):
    def __init__(self, parent=None):
        super().__init__()

        self.select_paker_combo_label = QLabel('Выбор компоновки спуска')
        self.select_paker_combo = QComboBox(self)
        self.select_paker_combo.addItems(['', 'пакер', 'два пакера', 'пакер с заглушкой'])

        self.grid = QGridLayout(self)

        self.grid.addWidget(self.date_work_label, 4, 2)
        self.grid.addWidget(self.date_work_line, 5, 2)

        self.date_work_line.dateTimeChanged.connect(self.insert_date_in_ois)

        self.grid.addWidget(self.select_paker_combo_label, 4, 3)
        self.grid.addWidget(self.select_paker_combo, 5, 3)


        self.descent_layout_line = QLineEdit(self)

        self.grid.addWidget(self.descent_layout_label, 6, 1)
        self.grid.addWidget(self.descent_layout_line, 8, 1, 2, 3)

        self.select_paker_combo.currentTextChanged.connect(self.update_select_paker_combo)

        self.complications_during_tubing_running_label = QLabel('Осложнение при спуске НКТ')
        self.complications_of_failure_label = QLabel('Получен ли прихват, наличие рассхаживания')
        self.complications_when_lifting_label = QLabel('Осложнения при подъеме НКТ')
        self.nkt_48_lenght_label = QLabel('Длина на спуск НКТ48')
        self.nkt_48_count_label = QLabel('Кол-во на спуск НКТ48')
        self.nkt_60_lenght_label = QLabel('Длина на спуск НКТ60')
        self.extra_work_question_label = QLabel('Дополнительные работы')
        self.nkt_60_count_label = QLabel('Кол-во на спуск НКТ60')
        self.nkt_73_lenght_label = QLabel('Длина НКТ73')
        self.nkt_73_count_label = QLabel('Кол-во НКТ73')
        self.nkt_89_lenght_label = QLabel('Длина НКТ89-102')
        self.nkt_89_count_label = QLabel('Кол-во НКТ89-102')
        self.depth_zumpf_paker_combo_label = QLabel('Опрессовка ЗУМПФа')
        self.depth_zumpf_paker_label = QLabel('Глубина посадки пакера ЗУМФПа')
        self.solvent_injection_label = QLabel('Закачка растворителя')
        self.nkt_is_same_label = QLabel('Кол-во НКТ на подъем совпадает со спуском')
        self.pressuar_tnkt_label = QLabel('Была ли опрессовка ТНКТ и вымыв шара')
        self.depth_paker_text_label = QLabel('Глубины посадки пакера')
        self.pressuar_ek_label = QLabel('Давление опрессовки')
        self.rezult_pressuar_combo_label = QLabel('Результат опрессовки')

        self.determination_of_pickup_combo_label = QLabel('Было ли определение Q?')

        self.saturation_volume_label = QLabel('Насыщение')
        self.determination_of_pickup_text_label = QLabel('Текст определение Q')
        self.saturation_volume_zumpf_label = QLabel('Насыщение')
        self.determination_of_pickup_zumpf_text_label = QLabel('Текст определение Q')


class TabWidget(QTabWidget):
    def __init__(self):
        super().__init__()
        self.addTab(TabPage_SO_Timplate(self), 'пакер')


class SpoPakerAction(TemplateWork):
    def __init__(self, ins_ind, table_widget, parent=None):
        super(QMainWindow, self).__init__()
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.table_widget = table_widget
        self.ins_ind = ins_ind

        self.tabWidget = TabWidget()

        self.tableWidget = QTableWidget(0, 2)
        self.tableWidget.setHorizontalHeaderLabels(
            ["дата", "работы"])
        for i in range(1):
            self.tableWidget.horizontalHeader().setSectionResizeMode(i, QHeaderView.Stretch)

        self.update_data_in_ois()

        self.tableWidget.resizeColumnsToContents()

        self.tableWidget.setWordWrap(False)
        # Устанавливаем ширину столбцов
        self.tableWidget.setColumnWidth(0, 200)  # Устанавливаем ширину столбца "дата"
        self.tableWidget.setColumnWidth(1, 1500)  # Устанавливаем ширину столбца "работы"

        self.buttonAdd = QPushButton('Добавить данные в план работ')
        self.buttonAdd.clicked.connect(self.add_work)

        vbox = QGridLayout(self.centralWidget)

        vbox.addWidget(self.tabWidget, 0, 0, 1, 2)
        vbox.addWidget(self.tableWidget, 1, 0, 1, 2)
        vbox.addWidget(self.buttonAdd, 2, 0)

        self.complications_of_failure_text_line = 0

        self.dict_nkt = {}
        self.dict_nkt_up = {}

    def add_work(self):
        from main import MyWindow

        current_widget = self.tabWidget.currentWidget()

        self.date_work_line = current_widget.date_work_line.text()
        self.select_paker_combo = current_widget.select_paker_combo.currentText()

        self.equipment_audit_combo = current_widget.equipment_audit_combo.currentText()
        if self.equipment_audit_combo == 'Да':
            self.equipment_audit_text_line = current_widget.equipment_audit_text_line.text()
            if self.equipment_audit_text_line == '':
                QMessageBox.warning(self, 'Ошибка', 'Нужно внести текст ревизии')
                return

        if self.select_paker_combo == '':
            QMessageBox.warning(self, 'Ошибка', 'Не выбрана компоновка')
            return
        elif self.select_paker_combo == 'пакер':

            self.type_equipment = 'пакер'
            self.coefficient_lifting = 1.2

        read_data = self.read_nkt_up(current_widget)
        if read_data is None:
            return


        self.nkt_is_same_combo = current_widget.nkt_is_same_combo.currentText()

        if self.nkt_is_same_combo == 'Нет':
            read_data = self.read_nkt_down(current_widget)
            if read_data is None:
                return

        self.complications_of_failure_combo = current_widget.complications_of_failure_combo.currentText()
        self.complications_during_tubing_running_combo = current_widget.complications_during_tubing_running_combo.currentText()
        self.pressuar_tnkt_combo = current_widget.pressuar_tnkt_combo.currentText()
        # self.solvent_injection_combo = current_widget.solvent_injection_combo.currentText()
        self.extra_work_question_combo = current_widget.extra_work_question_combo.currentText()
        self.complications_when_lifting_combo = current_widget.complications_when_lifting_combo.currentText()
        self.depth_zumpf_paker_combo = current_widget.depth_zumpf_paker_combo.currentText()
        self.determination_of_pickup_combo = current_widget.determination_of_pickup_combo.currentText()

        # self.pressuar_gno_combo = current_widget.pressuar_gno_combo.currentText()

        self.pressuar_ek_combo = current_widget.pressuar_ek_combo.currentText()
        if self.pressuar_ek_combo == 'Да':
            read_data = self.read_pressuar_combo(current_widget)
            if read_data is None:
                return

        self.descent_layout_line = current_widget.descent_layout_line.text()

        if self.depth_zumpf_paker_combo == 'Да':
            read_data = self.read_pressuar_zumpf(current_widget)
            if read_data is None:
                return

        if self.pressuar_tnkt_combo == 'Да':
            self.pressuar_tnkt_text_line = current_widget.pressuar_tnkt_text_line.text()


            if self.pressuar_tnkt_text_line == '':
                QMessageBox.warning(self, 'Ошибка', f'Не введены текст осложнения при срыве ПШ')
                return



        if self.extra_work_question_combo == 'Да':
            self.read_extra_work_question(current_widget)
            if self.type_combo_work == 'Крезол':
                self.determination_of_pickup_sko_combo =current_widget.determination_of_pickup_sko_combo.currentText()
                if self.determination_of_pickup_sko_combo == 'Да':
                    read_data = self.read_determination_of_pickup_sko_combo(current_widget)
                    if read_data is None:
                        return



        if self.complications_of_failure_combo == 'Да':
            read_data = self.read_complications_of_failure(current_widget)
            if read_data is None:
                return

        if self.complications_during_tubing_running_combo == 'Да':
            read_data = self.read_complications_during_tubing_running_combo(current_widget)
            if read_data is None:
                return

        if self.complications_when_lifting_combo == 'Да':
            read_data = self.read_complications_when_lifting(current_widget)
            if read_data is None:
                return

        if len(self.dict_nkt) == 0:
            question = QMessageBox.question(self, 'Ошибка', f'НКТ отсутствуют?')
            if question == QMessageBox.StandardButton.No:
                return
        if len(self.dict_nkt_up) == 0 and self.nkt_is_same_combo == 'Нет':
            question = QMessageBox.question(self, 'Ошибка', f'НКТ отсутствуют?')
            if question == QMessageBox.StandardButton.No:
                return

        work_list = self.depth_paker_work()

        well_data.date_work = self.date_work_line

        self.populate_row(self.ins_ind, work_list, self.table_widget)
        well_data.pause = False
        self.close()

    def krezol_work(self):
        work_list = [
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'ОПЗ',
             f'{self.extra_work_text_line} {self.extra_work_time_begin_date}-{self.extra_work_time_end_date}',
             None, None,
             None, 'Крезол-НС', None, None, 'перед началом работ на скважине', None, 'АКТ№', None, None, None, 'факт',
             None, 'час', self.extra_work_time_line, 1, 1, '=V555*W555*X555', '=Y555-AA555-AB555-AC555-AD555', None,
             None, None, None, None]]
        if self.response_text_line != '':
            work_list.extend((self.response_sko()))
        self.date_work_line = self.extra_work_time_end_date.split(' ')[0]

        return work_list



    @staticmethod
    def change_string_in_date(date_str):
        # Преобразуем строку в объект datetime

        formatted_date = date_str.strftime("%d.%m.%Y %H:%M")
        return formatted_date

    def depth_paker_work(self):
        from normir.template_without_skm import TemplateWithoutSKM
        complications_of_failure_list = []
        complications_during_disassembly_list = []
        if self.select_paker_combo in ['пакер']:
            work_list = [
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'М/ж спайдера', None, None, None, None, None,
                 None,
                 None, None, None, None, None, None, '§185разд.1', None, 'час', 1, 0.07, 1, '=V529*W529*X529',
                 '=Y529-AA529-AB529-AC529-AD529', None, None, None, None, None]]

            work_list.extend(self.work_pzr(self.descent_layout_line))

        if len(self.dict_nkt) != 0:
            work_list.extend(self.descent_nkt_work())

        if self.complications_during_tubing_running_combo == 'Да':
            complications_during_tubing_running_list = [
                '=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', self.type_equipment,
                f'{self.complications_during_tubing_running_text_line} '
                f'{self.complications_during_tubing_running_time_begin_date}-'
                f'{self.complications_during_tubing_running_time_end_date}', None, None, None, None, None,
                None, 'Объем', None, 'АКТ№', None, None, None, 'факт', None, 'час',
                self.complications_during_tubing_running_time_line - 0.3, 1, 1, '=V280*W280*X280',
                '=Y280-AA280-AB280-AC280-AD280', None, None, None, None, None]
            work_list.append(complications_during_tubing_running_list)

            self.date_work_line = self.complications_during_tubing_running_time_end_date.split(' ')[0]

        if self.complications_of_failure_combo == 'Да':
            complications_of_failure_list = [
                '=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
                f'{self.complications_of_failure_text_line} {self.complications_of_failure_time_begin_date}-'
                f'{self.complications_of_failure_time_end_date}', None, None, None, None, None,
                None, None, None, 'АКТ№', None, None, None, 'факт', None, 'час',
                self.complications_of_failure_time_line, 1, 1, '=V280*W280*X280',
                '=Y280-AA280-AB280-AC280-AD280', None, None, None, None, None]
            work_list.append(complications_of_failure_list)
            self.date_work_line = self.complications_of_failure_time_end_date.split(' ')[0]

        if self.pressuar_ek_combo == 'Да':
            work_list.extend(self.pressuar_work())
        if self.depth_zumpf_paker_combo == 'Да':
            if self.depth_zumpf_paker_line != '':
                work_list.extend(self.pressuar_work())

        if self.pressuar_tnkt_combo == 'Да':
            pressuar_tnkt_list = self.pressuar_tnkt_combo_def()
            work_list.extend(pressuar_tnkt_list)

        # if self.solvent_injection_combo == 'Да':
        #     work_list.extend(TemplateWithoutSKM.solvent_injection_work(self))

        if self.extra_work_question_combo == 'Да':
            if self.type_combo_work in ['Крезол']:
                work_list.extend(self.krezol_work())

                if self.volume_flush_line_combo == 'Да':
                    work_list.extend(self.volume_after_sko_work_2())
                aaa = self.determination_of_pickup_sko_combo
                if self.determination_of_pickup_sko_combo == 'Да':
                    work_list.extend(self.determination_of_pickup_work(
                        self.saturation_volume_sko_line, self.determination_of_pickup_sko_text_line))
            elif self.type_combo_work in ['РИР 2С']:
                work_list.extend(self.rir_work())
                # if self.combo_nkt_true == 'Да':
                if self.count_nkt_combo == 'Да':
                    work_list.extend(self.dopusk(self.count_nkt_line))
                    aaaa = self.dict_nkt
                    if '73мм' in list(self.dict_nkt.keys()):
                        self.dict_nkt['73мм'] = (
                            int(self.roof_definition_depth_line), self.dict_nkt['73мм'][1] + self.count_nkt_line)
                    elif '60мм' in list(self.dict_nkt.keys()):
                        self.dict_nkt['60мм'] = (
                            int(self.roof_definition_depth_line), self.dict_nkt['60мм'][1] + self.count_nkt_line)
                    aaa = self.dict_nkt
                    work_list.extend(self.pressuar_ek_rir())

            self.date_work_line = self.extra_work_time_end_date.split(' ')[0]

        work_list.extend(self.lifting_nkt())
        if self.equipment_audit_combo == 'Да':
            work_list.extend([
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
                 f'Ревизия:{self.equipment_audit_text_line}',
                 None, None, None, None, None, None, None, None, None, None, None,
                 None, 'факт', None, 'час', 0.5, 1, 1, '=V480*W480*X480', '=Y480-AA480-AB480-AC480-AD480', None,
                 None, None, None, None]])
        return work_list

    def pressuar_work(self):
        work_list = []

        pressuar_work_list = [

            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
             f'Посадка пакера на гл.{self.depth_paker_text_edit}',
             None, None, None, None,
             None, None, None, None, None, None, None, None, '§138разд.1', None, 'шт', 1, 0.23, 1, '=V547*W547*X547',
             '=Y547-AA547-AB547-AC547-AD547', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'ПЗР перед опрессовкой ', None, None,
             None, None,
             None,
             None, None, None, None, None, None, None, '§147,149разд.1', None, 'шт', 1, 0.43, 1, '=V548*W548*X548',
             '=Y548-AA548-AB548-AC548-AD548', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
             f'Опрессовка ЭК в инт. на Р={self.pressuar_ek_line}атм ({self.rezult_pressuar_combo})', None, None,
             None, None, None, None, None, None, 'АКТ№', None, None, None, '§148разд.1', None, 'шт', 1, 0.583, 1,
             '=V549*W549*X549', '=Y549-AA549-AB549-AC549-AD549', None, None, None, None, None]]
        work_list.extend(pressuar_work_list)
        if self.determination_of_pickup_combo == 'Да':
            determination_of_pickup_list = self.determination_of_pickup_work(
                self.saturation_volume_line, self.determination_of_pickup_text)
            work_list.extend(determination_of_pickup_list)

        work_list.extend([
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'Срыв пакера в эксплуатационной колонне', None,
             None,
             None, None, None, None, None, None, None, None, None, None, '§146разд.1', None, 'шт', 1, 0.15, 1,
             '=V554*W554*X554', '=Y554-AA554-AB554-AC554-AD554', None, None, None, None, None]])

        return work_list

    def pressuar_zumpf_work(self):
        work_list = []

        pressuar_work_list = [

            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
             f'Посадка пакера на гл.{self.depth_zumpf_paker_line}',
             None, None, None, None,
             None, None, None, None, None, None, None, None, '§138разд.1', None, 'шт', 1, 0.23, 1, '=V547*W547*X547',
             '=Y547-AA547-AB547-AC547-AD547', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'ПЗР перед опрессовкой ', None, None,
             None, None,
             None,
             None, None, None, None, None, None, None, '§147,149разд.1', None, 'шт', 1, 0.43, 1, '=V548*W548*X548',
             '=Y548-AA548-AB548-AC548-AD548', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
             f'Опрессовка ЭК в инт. на Р={self.pressuar_ek_line}атм ({self.rezult_pressuar_combo})', None, None,
             None, None, None, None, None, None, 'АКТ№', None, None, None, '§148разд.1', None, 'шт', 1, 0.583, 1,
             '=V549*W549*X549', '=Y549-AA549-AB549-AC549-AD549', None, None, None, None, None]]
        work_list.extend(pressuar_work_list)
        if self.determination_of_pickup_combo == 'Да':
            determination_of_pickup_list = self.determination_of_pickup_work(
                self.saturation_volume_zumpf_line, self.determination_of_pickup_zumpf_combo)
            work_list.extend(determination_of_pickup_list)

        work_list.extend([
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'Срыв пакера в эксплуатационной колонне', None,
             None,
             None, None, None, None, None, None, None, None, None, None, '§146разд.1', None, 'шт', 1, 0.15, 1,
             '=V554*W554*X554', '=Y554-AA554-AB554-AC554-AD554', None, None, None, None, None]])

        return work_list


    def pressuar_tnkt_combo_def(self):
        work_list = [
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'Сброс шара', None, None, None, None, None, None,
             None, None, 'АКТ№', None, None, None, 'факт', None, 'час', 0.5, 1, 1, '=V540*W540*X540',
             '=Y540-AA540-AB540-AC540-AD540', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'ПЗР перед опрессовкой ', None, None, None, None,
             None, None, None, None, None, None, None, None, '§150/152 разд.1 ', None, 'шт', 1, 0.43, 1,
             '=V541*W541*X541', '=Y541-AA541-AB541-AC541-AD541', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, f'{self.pressuar_tnkt_text_line}', None, None, None,
             None, None, None, None, None, 'АКТ№', None, None, None, '§151 разд.1', None, 'шт', 1, 0.25, 1,
             '=V542*W542*X542', '=Y542-AA542-AB542-AC542-AD542', None, None, None, None, None]]

        return work_list


if __name__ == "__main__":
    # app3 = QApplication(sys.argv)

    app = QApplication(sys.argv)
    window = SpoPakerAction(22, 22)
    window.show()
    sys.exit(app.exec_())
