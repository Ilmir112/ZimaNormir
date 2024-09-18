import sys
from datetime import datetime, timedelta

import well_data

from normir.norms import LIFTING_NORM_SUCKER_POD, DESCENT_NORM_SUCKER_POD
from PyQt5.QtGui import QIntValidator, QDoubleValidator
from PyQt5.QtWidgets import QWidget, QLabel, QComboBox, QLineEdit, QGridLayout, QTabWidget, QMainWindow, QPushButton, \
    QMessageBox, QApplication, QHeaderView, QTableWidget, QTableWidgetItem, QTextEdit, QDateTimeEdit

from normir.TabPageAll import TabPage, TemplateWork


class TabPage_SO_Lifting_Shgn(TabPage):
    def __init__(self, parent=None):
        super().__init__()

        self.grid = QGridLayout(self)

        self.grid.addWidget(self.date_work_label, 4, 2)
        self.grid.addWidget(self.date_work_line, 5, 2)

        self.complications_of_failure_label = QLabel('Рассхаживание')
        self.complications_of_failure_combo = QComboBox(self)
        self.complications_of_failure_combo.addItems(['Нет', 'Да'])

        self.complications_when_lifting_label = QLabel('Осложнения при подьеме штанг')
        self.complications_when_lifting_combo = QComboBox(self)
        self.complications_when_lifting_combo.addItems(['Нет', 'Да'])

        self.grid.addWidget(self.complications_of_failure_label, 28, 1)
        self.grid.addWidget(self.complications_of_failure_combo, 29, 1)

        self.grid.addWidget(self.complications_when_lifting_label, 46, 1)
        self.grid.addWidget(self.complications_when_lifting_combo, 47, 1)

        self.fishing_works_combo_label = QLabel('Ловильные работы')
        self.fishing_works_combo = QComboBox(self)
        self.fishing_works_combo.addItems(['Нет', 'Да'])

        self.equipment_audit_label = QLabel('Была ли ревизия')
        self.equipment_audit_combo = QComboBox(self)
        self.equipment_audit_combo.addItems(['Нет', 'Да'])

        self.grid.addWidget(self.equipment_audit_label, 94, 1)
        self.grid.addWidget(self.equipment_audit_combo, 95, 1)

        self.sucker_up()

        self.count_rods_is_same_label = QLabel('Кол-во штанг на подьем совпадает')
        self.count_rods_is_same_combo = QComboBox(self)
        self.count_rods_is_same_combo.addItems(['Да', 'Нет'])
        self.grid.addWidget(self.count_rods_is_same_label, 36, 1)
        self.grid.addWidget(self.count_rods_is_same_combo, 37, 1)

        self.grid.addWidget(self.fishing_works_combo_label, 30, 1)
        self.grid.addWidget(self.fishing_works_combo, 31, 1)

        self.equipment_audit_combo.currentTextChanged.connect(self.update_equipment_audit_combo)
        self.fishing_works_combo.currentTextChanged.connect(self.update_fishing_works_combo)
        self.complications_of_failure_combo.currentTextChanged.connect(self.update_complications_of_failure)
        self.complications_when_lifting_combo.currentTextChanged.connect(self.update_complications_when_lifting)

        self.count_rods_is_same_combo.currentTextChanged.connect(self.sucker_down)

    def update_fishing_works(self):
        time_begin = self.fishing_works_time_begin_date.dateTime()
        time_end = self.fishing_works_time_end_date.dateTime()

        time_difference = self.calculate_date(time_begin, time_end)
        self.fishing_works_time_line.setText(str(time_difference))

    def update_date_when_lifting(self):
        time_begin = self.complications_when_lifting_time_begin_date.dateTime()
        time_end = self.complications_when_lifting_time_end_date.dateTime()

        time_difference = self.calculate_date(time_begin, time_end)
        self.complications_when_lifting_time_line.setText(str(time_difference))

    def update_date_during_disassembly_q(self):
        time_begin = self.complications_during_disassembly_q_time_begin_date.dateTime()
        time_end = self.complications_during_disassembly_q_time_end_date.dateTime()

        time_difference = self.calculate_date(time_begin, time_end)
        self.complications_during_disassembly_time_line.setText(str(time_difference))

    def update_date_of_failure(self):
        time_begin = self.complications_of_failure_time_begin_date.dateTime()
        time_end = self.complications_of_failure_time_end_date.dateTime()

        time_difference = self.calculate_date(time_begin, time_end)
        self.complications_of_failure_time_line.setText(str(time_difference))


class TabWidget(QTabWidget):
    def __init__(self):
        super().__init__()
        self.addTab(TabPage_SO_Lifting_Shgn(self), 'СПО штанголовки')


class LiftingRodHeadWindow(TemplateWork):
    def __init__(self, ins_ind, table_widget, parent=None):
        super(TemplateWork, self).__init__()
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

        self.date_work_line = None
        self.complications_of_failure_text_line = 0
        self.dict_sucker_pod = {}
        self.dict_sucker_pod_up = {}

    def add_work(self):
        from main import MyWindow

        current_widget = self.tabWidget.currentWidget()

        self.date_work_line = current_widget.date_work_line.text()
        self.fishing_works_combo = current_widget.fishing_works_combo.currentText()
        if self.fishing_works_combo == 'Да':
            read_data = self.read_fishing_works(current_widget)
            if read_data is None:
                return

        self.type_equipment = 'Ловильный инструмент'

        self.count_rods_is_same_combo = current_widget.count_rods_is_same_combo.currentText()

        try:
            self.read_sucker_up(current_widget)
        except Exception as e:
            QMessageBox.warning(self, 'Ошибка', f'ВВедены не все значения {e}')
            return

        self.equipment_audit_combo = current_widget.equipment_audit_combo.currentText()
        if self.equipment_audit_combo == 'Да':
            self.equipment_audit_text_line = current_widget.equipment_audit_text_line.text()
            if self.equipment_audit_text_line == '':
                QMessageBox.warning(self, 'Ошибка', 'Нужно внести текст ревизии')
                return

        if self.count_rods_is_same_combo == 'Нет':
            try:
                self.read_sucker_down(current_widget)
            except Exception as e:
                QMessageBox.warning(self, 'Ошибка', f'ВВедены не все значения {e}')
                return
        else:
            self.dict_sucker_pod_up = self.dict_sucker_pod

        self.complications_of_failure_combo = current_widget.complications_of_failure_combo.currentText()

        self.complications_when_lifting_combo = current_widget.complications_when_lifting_combo.currentText()

        if self.complications_of_failure_combo == 'Да':
            read_data = self.read_complications_of_failure(current_widget)
            if read_data is None:
                return

        if self.complications_when_lifting_combo == 'Да':
            read_data = self.read_complications_when_lifting(current_widget)
            if read_data is None:
                return

        work_list = self.lifting_shgn()
        if len(self.dict_sucker_pod) == 0:
            question = QMessageBox.question(self, 'Ошибка', f'НКТ отсутствуют?')
            if question == QMessageBox.StandardButton.No:
                return

        well_data.date_work = self.date_work_line

        self.populate_row(self.ins_ind, work_list, self.table_widget)
        well_data.pause = False
        self.close()

    def lifting_shgn(self):

        work_list = [
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', self.type_equipment, 'ПЗР СПО при спуске штанг',
             None, None,
             None, None, None, None, None, None, None, None, None, None, '§196,199разд.1', None, 'шт', 1, 0.74, 1,
             '=V157*W157*X157', '=Y157-AA157-AB157-AC157-AD157', None, None, None, None, None]]
        work_list.extend(self.descent_sucker_pod(self.dict_sucker_pod, self.type_equipment))
        if self.fishing_works_combo == 'Да':
            work_list.append(
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
                 f'{self.fishing_works_text_line} {self.fishing_works_time_begin_date} '
                 f'{self.fishing_works_time_end_date}', None,
                 None, None, None, None, None, None, None, None, None, None, None, '§254разд.1', None, 'шт',
                 1, 0.33, 1, '=V161*W161*X161', '=Y161-AA161-AB161-AC161-AD161', None, None, None, None, None])
        if self.complications_of_failure_combo == 'Да':
            work_list.extend([
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
                 f'{self.complications_of_failure_text_line} '
                 f'{self.complications_of_failure_time_begin_date}-{self.complications_of_failure_time_end_date}',
                 None, None, None, None, None, None, None, None,
                 'АКТ№', None, None, None, 'факт', None, 'час', 1, 1, 1, '=V162*W162*X162',
                 '=Y162-AA162-AB162-AC162-AD162',
                 None, None, None, None, None],
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
                 f'Срыв {well_data.dict_sucker_rod}', None, None, None, None, None, None,
                 None, None, "'АКТ №1'!A1", None, None, None, '§301разд.1', None, 'шт', 1, 0.15, 1,
                 '=V163*W163*X163',
                 '=Y163-AA163-AB163-AC163-AD163', None, None, None, None, None]])
        # нормирование штанг
        work_list.extend(self.lifting_sucker_pod(self.dict_sucker_pod_up, self.type_equipment))
        work_list.append(
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'Демонтаж ПШМ', None, None, None, None, None, None,
             None, None, None, None, None, None, '§120разд.1', None, 'шт', 1, 0.25, 1, '=V167*W167*X167',
             '=Y167-AA167-AB167-AC167-AD167', None, None, None, None, None])

        if self.equipment_audit_combo == 'Да':
            work_list.extend([
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
                 f'Ревизия:{self.equipment_audit_text_line}',
                 None, None, None, None, None, None, None, None, None, None, None,
                 None, 'факт', None, 'час', 0.5, 1, 1, '=V480*W480*X480', '=Y480-AA480-AB480-AC480-AD480', None,
                 None, None, None, None]]
            )
        return work_list

    def descent_sucker_pod(self, dict_sucker_pod, type_equipment):
        work_list = [
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', type_equipment, 'ПЗР СПО перед спуском штанг',
             None, None, None, None, None,
             None, None, None, None, None, None, None, '§191разд.1', None, 'шт', 1, 0.74, 1, '=V145*W145*X145',
             '=Y145-AA145-AB145-AC145-AD145', None, None, None, None, None]]
        sucker_count_all = sum(map(lambda x: x[1], dict_sucker_pod.values()))
        for sucker_key, sucker in dict_sucker_pod.items():
            sucker_lenght = sucker[0]
            sucker_count = sucker[1]

            koef_norm = DESCENT_NORM_SUCKER_POD[well_data.lifting_unit_combo][sucker_key]
            razdel_3 = DESCENT_NORM_SUCKER_POD[well_data.lifting_unit_combo]['раздел']
            work_list.append(
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', type_equipment,
                 f'Спуск штанг {sucker_key}мм (L={sucker_lenght}м )',
                 None, None,
                 None, None, None, None, None, None, None, None, None, None, razdel_3, None,
                 'шт', sucker_count, koef_norm, 1,
                 '=V158*W158*X158', '=Y158-AA158-AB158-AC158-AD158', None, None, None, None, None])

        return work_list

    def lifting_sucker_pod(self, dict_sucker_pod, type_equipment):
        if type_equipment != 'ШТАНГИ':
            work_list = [
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', type_equipment, 'ПЗР СПО перед подъемом штанг',
                 None, None, None, None, None,
                 None, None, None, None, None, None, None, '§191разд.1', None, 'шт', 1, 0.74, 1, '=V145*W145*X145',
                 '=Y145-AA145-AB145-AC145-AD145', None, None, None, None, None]]
        else:
            work_list = []
        sucker_count_all = sum(map(lambda x: x[1], dict_sucker_pod.values()))
        for sucker_key, sucker in dict_sucker_pod.items():
            sucker_lenght = sucker[0]
            sucker_count = sucker[1]
            aderg = LIFTING_NORM_SUCKER_POD[well_data.lifting_unit_combo]
            if well_data.lifting_unit_combo not in ['УПА-60/80 (Оснастка 3×4)', 'УПТ-32 (Оснастка 3×4)']:
                max_count = LIFTING_NORM_SUCKER_POD[well_data.lifting_unit_combo][sucker_key]['III'][1]
                koef_norm = LIFTING_NORM_SUCKER_POD[well_data.lifting_unit_combo][sucker_key]['III'][0]
                razdel_3 = LIFTING_NORM_SUCKER_POD[well_data.lifting_unit_combo][sucker_key]['раздел']
            else:
                max_count = LIFTING_NORM_SUCKER_POD[well_data.lifting_unit_combo][sucker_key]['IV'][1]
                koef_norm = LIFTING_NORM_SUCKER_POD[well_data.lifting_unit_combo][sucker_key]['IV'][0]
                razdel_3 = LIFTING_NORM_SUCKER_POD[well_data.lifting_unit_combo][sucker_key]['раздел']
            work_list.append(
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', type_equipment,
                 f'Подъем штанг {sucker_key}мм (L={sucker_lenght}м )',
                 None, None,
                 None, None, None, None, None, max_count, None, None, None, None,
                 razdel_3, None, 'шт', sucker_count,
                 koef_norm, 1, '=V147*W147*X147', '=Y147-AA147-AB147-AC147-AD147', None, None, None, None, None])

        work_list.append(
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', 'ШТАНГИ',
             'Очистка штанг от окалини солей (АСПО)(акт ревизии)',
             None,
             None, None, None, None, None, None, None, None, None, None, None, '§9разд.1', None, 'час',
             sucker_count_all,
             0.017, 1, '=V149*W149*X149', '=Y149-AA149-AB149-AC149-AD149', None, None, None, None, None])

        return work_list


if __name__ == "__main__":
    # app3 = QApplication(sys.argv)

    app = QApplication(sys.argv)
    window = LiftingRodHeadWindow(22, 22)
    window.show()
    sys.exit(app.exec_())
