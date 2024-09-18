import sys
from datetime import datetime, timedelta

import well_data

from collections import namedtuple
from normir.files_with_list import cause_presence_of_jamming
from normir.norms import LIFTING_NORM_NKT, DESCENT_NORM_NKT
from PyQt5.QtGui import QIntValidator, QDoubleValidator
from PyQt5.QtWidgets import QWidget, QLabel, QComboBox, QLineEdit, QGridLayout, QTabWidget, QMainWindow, QPushButton, \
    QMessageBox, QApplication, QHeaderView, QTableWidget, QTableWidgetItem, QTextEdit, QDateEdit, QDateTimeEdit
from PyQt5.QtCore import Qt

from normir.relocation_brigade import TextEditTableWidgetItem
from normir.TabPageAll import TabPage, TemplateWork


class TabPage_SO_Timplate(TabPage):
    def __init__(self, parent=None):
        super().__init__()

        self.select_type_combo_label = QLabel('Выбор компоновки спуска')
        self.select_type_combo = QComboBox(self)
        self.select_type_combo.addItems(['', 'РИР на пере', 'ГР на пере', 'Отсыпка песком'])

        self.grid = QGridLayout(self)

        self.grid.addWidget(self.date_work_label, 4, 2)
        self.grid.addWidget(self.date_work_line, 5, 2)

        self.grid.addWidget(self.select_type_combo_label, 4, 3)
        self.grid.addWidget(self.select_type_combo, 5, 3)

        self.select_type_combo.currentTextChanged.connect(self.update_select_type_combo)

    def update_select_type_combo(self, index):

        self.complications_during_tubing_running_combo = QComboBox(self)
        self.complications_during_tubing_running_combo.addItems(['Нет', 'Да'])

        self.complications_of_failure_combo = QComboBox(self)
        self.complications_of_failure_combo.addItems(['Нет', 'Да'])

        self.complications_when_lifting_combo = QComboBox(self)
        self.complications_when_lifting_combo.addItems(['Нет', 'Да'])

        # self.grid.addWidget(self.complications_of_failure_label, 10, 1)
        # self.grid.addWidget(self.complications_of_failure_combo, 11, 1)

        self.nkt_label()

        self.grid.addWidget(self.complications_during_tubing_running_label, 26, 1)
        self.grid.addWidget(self.complications_during_tubing_running_combo, 27, 1)

        self.grid.addWidget(self.complications_of_failure_label, 28, 1)
        self.grid.addWidget(self.complications_of_failure_combo, 29, 1)

        self.grid.addWidget(self.complications_when_lifting_label, 46, 1)
        self.grid.addWidget(self.complications_when_lifting_combo, 47, 1)

        self.solvent_injection_combo = QComboBox(self)
        self.solvent_injection_combo.addItems(['Нет', 'Да'])

        self.grid.addWidget(self.solvent_injection_label, 32, 1)
        self.grid.addWidget(self.solvent_injection_combo, 33, 1)

        self.nkt_is_same_combo = QComboBox(self)
        self.nkt_is_same_combo.addItems(['Да', 'Нет'])

        self.grid.addWidget(self.nkt_is_same_label, 80, 1)
        self.grid.addWidget(self.nkt_is_same_combo, 81, 1)

        self.pressuar_ek_combo = QComboBox(self)
        self.pressuar_ek_combo.addItems(['Нет', 'Да'])

        self.pressuar_ek_combo_label = QLabel('Была ли опрессовка')

        self.grid.addWidget(self.pressuar_ek_combo_label, 66, 0)
        self.grid.addWidget(self.pressuar_ek_combo, 67, 0)

        self.technological_crap_question_combo = QComboBox(self)
        self.technological_crap_question_combo.addItems(['Нет', 'Да'])

        self.grid.addWidget(self.technological_crap_question_label, 52, 1)
        self.grid.addWidget(self.technological_crap_question_combo, 53, 1)



        self.equipment_audit_label = QLabel('Была ли ревизия')
        self.equipment_audit_combo = QComboBox(self)
        self.equipment_audit_combo.addItems(['Нет', 'Да'])

        self.grid.addWidget(self.equipment_audit_label, 94, 1)
        self.grid.addWidget(self.equipment_audit_combo, 95, 1)

        self.equipment_audit_combo.currentTextChanged.connect(self.update_equipment_audit_combo)
        # self.pressuar_gno_combo.currentTextChanged.connect(self.update_pressuar_gno_combo)
        self.technological_crap_question_combo.currentTextChanged.connect(self.update_technological_crap_question_combo)
        self.solvent_injection_combo.currentTextChanged.connect(self.update_solvent_injection_combo)
        # self.pressuar_gno_combo.currentTextChanged.connect(self.update_pressuar_gno_combo)
        self.pressuar_ek_combo.currentTextChanged.connect(self.update_pressuar_ek_combo)
        self.complications_of_failure_combo.currentTextChanged.connect(self.update_complications_of_failure)
        self.complications_when_lifting_combo.currentTextChanged.connect(self.update_complications_when_lifting)

        self.complications_during_tubing_running_combo.currentTextChanged.connect(
            self.update_complications_during_tubing_running_combo)
        self.nkt_is_same_combo.currentTextChanged.connect(self.update_nkt_is_same_combo)
        self.nkt_is_same_combo.setCurrentIndex(1)

        self.rir_with_pero_text_edit = QLineEdit(self)

        self.volume_cement_line = QLineEdit(self)
        self.volume_cement_line.setValidator(self.validator_float)

        if index in ['РИР на пере', 'ГР на пере', 'Отсыпка песком']:
            self.text_zakachki_label = QLabel('Текст закачки')
            self.text_zakachki_line = QLineEdit(self)

            self.volume_zatrub_label = QLabel('Объем продавки')
            self.volume_zatrub_line = QLineEdit(self)
            self.volume_zatrub_line.setValidator(self.validator_int)

            self.count_nkt_lifting_label = QLabel('Кол-во на НКТ на подьем перед срезкой')
            self.count_nkt_lifting_line = QLineEdit(self)
            self.count_nkt_lifting_line.setValidator(self.validator_int)

            self.volume_well_flush_line = QLineEdit(self)
            self.volume_well_flush_line.setValidator(self.validator_float)
            self.volume_well_flush_label.setText('Объем срезки')

            self.count_nkt_lifting_after_label = QLabel('Кол-во на НКТ на подьем после срезки')
            self.count_nkt_lifting_line_after = QLineEdit(self)
            self.count_nkt_lifting_line_after.setValidator(self.validator_int)

            self.grid.addWidget(self.rir_with_pero_text_label, 30, 1)
            self.grid.addWidget(self.rir_with_pero_text_edit, 31, 1)

            self.grid.addWidget(self.volume_cement_line_label, 30, 2)
            self.grid.addWidget(self.volume_cement_line, 31, 2)

            self.grid.addWidget(self.text_zakachki_label, 30, 3)
            self.grid.addWidget(self.text_zakachki_line, 31, 3)

            self.grid.addWidget(self.volume_zatrub_label, 30, 4)
            self.grid.addWidget(self.volume_zatrub_line, 31, 4)

            self.grid.addWidget(self.count_nkt_lifting_label, 30, 5)
            self.grid.addWidget(self.count_nkt_lifting_line, 31, 5)

            self.grid.addWidget(self.volume_well_flush_label, 30, 6)
            self.grid.addWidget(self.volume_well_flush_line, 31, 6)

            self.grid.addWidget(self.count_nkt_lifting_after_label, 30, 7)
            self.grid.addWidget(self.count_nkt_lifting_line_after, 31, 7)

            self.ovtr_work_combo_label = QLabel('Наличие ОЗЦ')
            self.ovtr_work_combo = QComboBox(self)
            self.ovtr_work_combo.addItems(['Нет', 'Да'])

            self.grid.addWidget(self.ovtr_work_combo_label, 50, 3)
            self.grid.addWidget(self.ovtr_work_combo, 51, 3)

            self.ovtr_work_combo.currentTextChanged.connect(self.update_ovtr_work_combo)
            self.ovtr_work_combo.setCurrentIndex(1)

            # self.ovtr_work_text_line.setText('ОЗЦ')
            self.ovtr_work_time_begin_label.setText('Начало ОЗЦ')
            self.ovtr_work_time_end_label.setText('Окончание ОЗЦ')
            self.ovtr_work_text_label.setText('ОЗЦ')
            # self.extra_work_question_combo.setCurrentIndex(1)



    def update_date_ovtr_work(self):
        time_begin = self.ovtr_work_time_begin_date.dateTime()
        time_end = self.ovtr_work_time_end_date.dateTime()

        time_difference = self.calculate_date(time_begin, time_end)
        self.ovtr_work_time_line.setText(str(time_difference))

    def update_rir_with_pero(self):
        text = self.rir_with_pero_text_edit.text()
        count_skm = 0
        if ',' in text and '-' in text:
            for interval in text.split(','):
                if len(interval.split('-')) == 2:
                    roof, sole = list(map(int, interval.split('-')))
                    count_skm += (sole - roof)
        elif '-' in text:
            if len(text.split('-')) == 2:
                roof, sole = list(map(int, text.split('-')))
                count_skm += int((sole - roof))

        self.volume_cement_line.setText(str(count_skm))

    def update_date_when_lifting(self):
        time_begin = self.complications_when_lifting_time_begin_date.dateTime()
        time_end = self.complications_when_lifting_time_end_date.dateTime()

        time_difference = self.calculate_date(time_begin, time_end)
        self.complications_when_lifting_time_line.setText(str(time_difference))

    def update_esp_dismantling_time(self):
        time_end = self.esp_dismantling_time_end_date.dateTime()
        time_begin = self.esp_dismantling_time_begin_date.dateTime()

        time_difference = self.calculate_date(time_begin, time_end)
        self.esp_dismantling_time_line.setText(str(time_difference))

    def update_date_during_disassembly_q(self):
        time_begin = self.complications_during_disassembly_q_time_begin_date.dateTime()
        time_end = self.complications_during_disassembly_q_time_end_date.dateTime()

        time_difference = self.calculate_date(time_begin, time_end)
        self.complications_during_disassembly_time_line.setText(str(time_difference))

    def update_date_of_normalization(self):
        time_begin = self.normalization_question_time_begin_date.dateTime()
        time_end = self.normalization_question_time_end_date.dateTime()

        time_difference = self.calculate_date(time_begin, time_end)
        self.normalization_question_time_line.setText(str(time_difference))

    def update_date_technological_crap(self):
        time_begin = self.technological_crap_question_time_begin_date.dateTime()
        time_end = self.technological_crap_question_time_end_date.dateTime()

        time_difference = self.calculate_date(time_begin, time_end)

        self.technological_crap_question_time_line.setText(str(time_difference))

    def update_date_of_failure(self):
        time_begin = self.complications_of_failure_time_begin_date.dateTime()
        time_end = self.complications_of_failure_time_end_date.dateTime()

        time_difference = self.calculate_date(time_begin, time_end)
        self.complications_of_failure_time_line.setText(str(time_difference))

    def update_date_tubing_running(self):
        time_begin = self.complications_during_tubing_running_time_begin_date.dateTime()
        time_end = self.complications_during_tubing_running_time_end_date.dateTime()

        time_difference = self.calculate_date(time_begin, time_end)
        self.complications_during_tubing_running_time_line.setText(str(time_difference))

    def update_date_solvent_volume(self):
        time_begin = self.solvent_volume_time_begin_date.dateTime()
        time_end = self.solvent_volume_time_end_date.dateTime()

        time_difference = self.calculate_date(time_begin, time_end)
        self.solvent_volume_time_line.setText(str(time_difference))


class TabWidget(QTabWidget):
    def __init__(self):
        super().__init__()
        self.addTab(TabPage_SO_Timplate(self), 'РИР на пере')


class RirWithPero(TemplateWork):
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

        self.date_work_line = None
        self.complications_of_failure_text_line = 0

        self.dict_nkt = {}
        self.dict_nkt_up = {}

        self.need_saturation_well_text_line = None
        self.need_saturation_q_text_line = None
        self.cycle_count_combo = None
        self.volume_jamming_line = None
        self.complications_during_disassembly_text_line = None
        self.complications_during_disassembly_time_line = None
        self.complications_when_lifting_text_line = None
        self.complications_when_lifting_time_line = None
        self.complications_when_lifting_time_begin_date = None
        self.complications_when_lifting_time_end_date = None
        self.determination_of_the_weight_text_line = None
        self.fluid_well_line = None
        self.time_work_line = None
        self.source_of_work_line = None
        self.couse_of_work_combo = None
        self.pressuar_gno_text_line = None
        self.complications_of_failure_time_line = None
        self.complications_of_failure_time_begin_date = None
        self.complications_of_failure_time_end_date = None
        self.nkt_48_lenght_edit = None
        self.nkt_48_count_edit = None
        self.nkt_60_lenght_edit = None
        self.coefficient_lifting = 1
        self.nkt_60_count_edit = None
        self.nkt_73_lenght_edit = None
        self.nkt_73_count_edit = None
        self.volume_of_finishing_line = None
        self.volume_flush_line = None
        self.nkt_89_lenght_edit = None
        self.nkt_89_count_edit = None
        self.type_equipment = None

        self.roof_definition_depth_line = None

        self.count_nkt_line = None
        self.pressuar_bop_text_line = None
        self.line_lenght_bop_line = None

        self.count_sections_esp_combo = None
        self.count_sections_ped_combo = None

        self.esp_dismantling_time_begin_date = None
        self.esp_dismantling_time_end_date = None
        self.esp_dismantling_time_line = None

    def add_work(self):
        from main import MyWindow

        current_widget = self.tabWidget.currentWidget()

        self.date_work_line = current_widget.date_work_line.text()
        self.select_type_combo = current_widget.select_type_combo.currentText()
        if self.select_type_combo == '':
            return
        elif self.select_type_combo in ['РИР на пере', 'ГР на пере', 'Отсыпка песком']:
            self.type_equipment = 'Перо,воронка'
            self.coefficient_lifting = 1

            self.rir_with_pero_text_edit = current_widget.rir_with_pero_text_edit.text()

            if self.rir_with_pero_text_edit == '':
                QMessageBox.warning(self, 'РИР', 'Нужно ввести текст РИР')
                return

            self.volume_cement_line = current_widget.volume_cement_line.text()
            if self.volume_cement_line != '':
                self.volume_cement_line = float(self.volume_cement_line)
            else:
                QMessageBox.warning(self, 'цемент', 'Объем цемента не введен?')
                return

            self.text_zakachki_line = current_widget.text_zakachki_line.text()

            if self.text_zakachki_line == '':
                QMessageBox.warning(self, 'РИР', 'Нужно ввести текст Закачки')
                return

            self.volume_zatrub_line = current_widget.volume_zatrub_line.text()
            if self.volume_zatrub_line != '':
                self.volume_zatrub_line = float(self.volume_zatrub_line)
            else:
                QMessageBox.warning(self, 'цемент', 'Объем закачки не введен?')
                return

            self.count_nkt_lifting_line = current_widget.count_nkt_lifting_line.text()
            if self.count_nkt_lifting_line != '':
                self.count_nkt_lifting_line = int(self.count_nkt_lifting_line)
            else:
                QMessageBox.warning(self, 'цемент', 'Кол-во НКТ перед срезкой не введено')
                return

            self.count_nkt_lifting_line_after = current_widget.count_nkt_lifting_line_after.text()
            if self.count_nkt_lifting_line_after != '':
                self.count_nkt_lifting_line_after = int(self.count_nkt_lifting_line_after)
            else:
                QMessageBox.warning(self, 'цемент', 'Кол-во НКТ после срезки не введено')
                return

            self.pressuar_ek_combo = current_widget.pressuar_ek_combo.currentText()
            if self.pressuar_ek_combo == 'Да':
                read_data = self.read_pressuar_combo(current_widget)
                if read_data is None:
                    return

            self.volume_well_flush_line = current_widget.count_nkt_lifting_line.text()
            if self.volume_well_flush_line != '':
                self.volume_well_flush_line = float(self.volume_well_flush_line)
            else:
                QMessageBox.warning(self, 'цемент', 'Объем закачки не введен?')
                return
            self.ovtr_work_combo = current_widget.ovtr_work_combo.currentText()
            if self.ovtr_work_combo == 'Да':
                read_data = self.read_ovtr_work_combo(current_widget)
                if read_data is None:
                    return

        self.nkt_is_same_combo = current_widget.nkt_is_same_combo.currentText()
        self.equipment_audit_combo = current_widget.equipment_audit_combo.currentText()
        if self.equipment_audit_combo == 'Да':
            self.equipment_audit_text_line = current_widget.equipment_audit_text_line.text()

        self.volume_well_flush_line = current_widget.volume_well_flush_line.text().replace(',', '.')
        if self.volume_well_flush_line != ['', None]:
            self.volume_well_flush_line = int(float(self.volume_well_flush_line))
        else:
            question = QMessageBox.question(self, 'Промывка', 'Промывки не было?')
            if question == QMessageBox.StandardButton.No:
                return

        read_data = self.read_nkt_up(current_widget)
        if read_data is None:
            return

        if self.nkt_is_same_combo == 'Нет':
            read_data = self.read_nkt_down(current_widget)
            if read_data is None:
                return
        else:
            self.dict_nkt_up = self.dict_nkt

        self.complications_of_failure_combo = current_widget.complications_of_failure_combo.currentText()
        self.complications_during_tubing_running_combo = current_widget.complications_during_tubing_running_combo.currentText()

        self.solvent_injection_combo = current_widget.solvent_injection_combo.currentText()
        self.technological_crap_question_combo = current_widget.technological_crap_question_combo.currentText()
        self.complications_when_lifting_combo = current_widget.complications_when_lifting_combo.currentText()

        if self.solvent_injection_combo == 'Да':
            self.read_solvent_volume(current_widget)

        if self.technological_crap_question_combo == 'Да':
            read_data = self.read_technological_crap_question(current_widget)
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

        work_list = self.template_with_skm()

        well_data.date_work = self.date_work_line

        self.populate_row(self.ins_ind, work_list, self.table_widget)

        well_data.pause = False
        self.close()


    def template_with_skm(self):
        complications_of_failure_list = []
        complications_during_disassembly_list = []
        work_list = [
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', 'Перо,воронка',
             'ПЗР СПО работы перед спуском  НКТ ',
             None, None, None, None,
             None, None, None, None, None, None, None, None, '§177разд.1', None, 'шт', 1, 0.17, 1,
             '=V530*W530*X530', '=Y530-AA530-AB530-AC530-AD530', None, None, None, None, None]]

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

        if self.select_type_combo in ['РИР на пере']:
            work_list.extend(self.rir_with_pero_work())

        if self.ovtr_work_combo == 'Да':
            work_list.extend(self.ozc_work())
        if self.technological_crap_question_combo == 'Да':
            work_list.extend(self.dopusk())
            work_list.extend(self.technological_crap_question_work()[1:])
        if self.pressuar_ek_combo == 'Да':
            work_list.extend(self.pressuar_work())

        work_list.extend(self.lifting_nkt())

        if self.complications_when_lifting_combo == 'Да':
            work_list.extend(self.complications_when_lifting_work())


        if self.equipment_audit_combo == 'Да':
            work_list.extend([
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
                 f'Ревизия:{self.equipment_audit_text_line}',
                 None, None, None, None, None, None, None, None, None, None, None,
                 None, 'факт', None, 'час', 0.5, 1, 1, '=V480*W480*X480', '=Y480-AA480-AB480-AC480-AD480', None,
                 None, None, None, None]]
            )

        return work_list

    def rir_with_pero_work(self):

        nkt_lenght = sum(list(map(lambda x: x[0], self.dict_nkt.values())))

        work_list = [
            ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', 'цементаж', 'ПЗР перед закачкой цемент.раствора', None,
             None, None, None, None, None, None, None, None, None, None, None, '§283,288разд.1', None, 'шт', 1, 0.96, 1,
             '=V807*W807*X807', '=Y807-AA807-AB807-AC807-AD807', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', 'цементаж',
             f'Приготовление цем.р-ра УЦМ в ЭК в инт.{self.rir_with_pero_text_edit}',
             None, None, None, None, None, 'Исполнитель', 'ПО ТКРС', None, 'АКТ№', 'ЦЕМЕНТ', 'Цемент', None,
             '§284разд.1', None, 'м3', self.volume_cement_line, 0.32, 1, '=W808+(V808-1)*0.04',
             '=Y808-AA808-AB808-AC808-AD808', None, None,
             None, None, None],
            ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', 'цементаж',
             self.text_zakachki_line,
             None, None, None, None, None, None, None, None, 'АКТ№', None, None, None, '§284разд.1',
             None, 'м', nkt_lenght, 0.34, 1, '=W809+(V809-200)/200*0.02', '=Y809-AA809-AB809-AC809-AD809',
             None, None, None, None, None],
            ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', 'цементаж', 'Доводка тех.водой', None, None, None, None,
             None, None, None, None, 'АКТ№', None, None, None, '§284разд.1', None, 'м', nkt_lenght, 0.34, 1,
             '=W810+(V810-200)/200*0.02', '=Y810-AA810-AB810-AC810-AD810', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', 'цементаж', 'Продавка по затрубу', None, None, None, None,
             None, None, None, None, 'АКТ№', None, None, None, '§284разд.1', None, 'м3', self.volume_zatrub_line,
             0.0417, 1,
             '=V811*W811*X811', '=Y811-AA811-AB811-AC811-AD811', None, None, None, None, None]]

        work_list.extend(self.dopusk_lifting(self.count_nkt_lifting_line))

        work_list.extend([
            ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', 'цементаж', 'Доводка тех водой ', None, None, None, None,
             None, None, None, None, None, None, None, None, '§286разд.1', None, 'м3', 0.3, 0.0417, 1,
             '=V813*W813*X813', '=Y813-AA813-AB813-AC813-AD813', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', 'цементаж',
             'ПР  перед вымывом излишков  цементного раствора', None, None, None, None, None, None, None, None, None,
             None, None, None, '§285разд.1', None, 'шт', 1, 0.15, 1, '=V814*W814*X814', '=Y814-AA814-AB814-AC814-AD814',
             None, None, None, None, None],
            ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', 'цементаж', 'Вымыв излишков цементного раствора (срезка)',
             None, None, None, None, None, None, None, None, None, None, None, None, '§286разд.1', None, 'м3', 16, 0.04,
             1, '=V815*W815*X815', '=Y815-AA815-AB815-AC815-AD815', None, None, None, None, None]])

        work_list.extend(self.dopusk_lifting(self.count_nkt_lifting_line_after))




        return work_list


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = RirWithPero(22, 22)
    window.show()
    sys.exit(app.exec_())
