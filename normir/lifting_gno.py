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

class TabPage_SO_Lifting_gno(TabPage):
    def __init__(self, parent=None):
        super().__init__()

        self.validator_int = QIntValidator(0, 6000)
        self.validator_float = QDoubleValidator(0.2, 1000, 1)

        self.gno_label = QLabel('Вид поднимаемого ГНО')
        self.gno_combo = QComboBox(self)
        self.gno_combo.addItems(['', 'ЗО', 'Фондовый пакер', 'Воронка', 'ЭЦН'])



        self.grid = QGridLayout(self)

        self.grid.addWidget(self.gno_label, 4, 1)
        self.grid.addWidget(self.gno_combo, 5, 1)
        self.grid.addWidget(self.date_work_label, 4, 2)
        self.grid.addWidget(self.date_work_line, 5, 2)


        self.gno_combo.currentTextChanged.connect(self.update_gno)


    def update_gno(self, index):
        self.nkt_label()

        self.complications_of_failure_armatura_label = QLabel('осложнения при демонтаже арматуры')
        self.complications_of_failure_armatura_combo = QComboBox(self)
        self.complications_of_failure_armatura_combo.addItems(['Нет', 'Да'])

        self.complications_of_failure_label = QLabel('осложнения при срыве ПШ (рассхаживание)')
        self.complications_of_failure_combo = QComboBox(self)
        self.complications_of_failure_combo.addItems(['Нет', 'Да'])

        self.complications_during_disassembly_label = QLabel('осложнения при демонтаже крестовины')
        self.complications_during_disassembly_combo = QComboBox(self)
        self.complications_during_disassembly_combo.addItems(['Нет', 'Да'])

        self.complications_when_lifting_label = QLabel('Осложнения при подьеме НКТ')
        self.complications_when_lifting_combo = QComboBox(self)
        self.complications_when_lifting_combo.addItems(['Нет', 'Да'])

        self.grid.addWidget(self.complications_of_failure_armatura_label, 6, 1)
        self.grid.addWidget(self.complications_of_failure_armatura_combo, 7, 1)

        self.grid.addWidget(self.complications_of_failure_label, 28, 1)
        self.grid.addWidget(self.complications_of_failure_combo, 29, 1)

        # self.grid.addWidget(self.complications_of_failure_label, 10, 1)
        # self.grid.addWidget(self.complications_of_failure_combo, 11, 1)

        self.grid.addWidget(self.complications_during_disassembly_label, 48, 1)
        self.grid.addWidget(self.complications_during_disassembly_combo, 49, 1)

        self.scheme_bop_installation_label = QLabel('Монтаж превентора')
        self.scheme_bop_installation_combo = QComboBox(self)
        self.scheme_bop_installation_combo.addItems(['Вторая', 'Первая'])

        self.scheme_bop_installation_combo_problem_label = QLabel('Осложнения при монтаже ПВО')
        self.scheme_bop_installation_problem_combo = QComboBox(self)
        self.scheme_bop_installation_problem_combo.addItems(["Нет", "Да"])

        self.grid.addWidget(self.scheme_bop_installation_label, 10, 1)
        self.grid.addWidget(self.scheme_bop_installation_combo, 11, 1)

        self.grid.addWidget(self.scheme_bop_installation_combo_problem_label, 12, 1)
        self.grid.addWidget(self.scheme_bop_installation_problem_combo, 13, 1)

        self.lowering_for_pressure_testing_label = QLabel('Спуск НКТ под опрессовку ПВО')
        self.lowering_for_pressure_testing_combo = QComboBox(self)
        self.lowering_for_pressure_testing_combo.addItems(["Нет", "Да"])

        self.grid.addWidget(self.lowering_for_pressure_testing_label, 10, 2)
        self.grid.addWidget(self.lowering_for_pressure_testing_combo, 11, 2)

        self.grid.addWidget(self.complications_when_lifting_label, 46, 1)
        self.grid.addWidget(self.complications_when_lifting_combo, 47, 1)

        self.lowering_for_pressure_testing_combo.currentTextChanged.connect(
            self.update_lowering_for_pressure_testing)
        self.lowering_for_pressure_testing_combo.setCurrentIndex(1)
        # self.pressuar_gno_combo.currentTextChanged.connect(self.update_pressuar_gno_combo)
        self.complications_during_disassembly_combo.currentTextChanged.connect(
            self.update_complications_during_disassembly)
        self.complications_of_failure_combo.currentTextChanged.connect(self.update_complications_of_failure)
        self.complications_when_lifting_combo.currentTextChanged.connect(self.update_complications_when_lifting)
        self.scheme_bop_installation_problem_combo.currentTextChanged.connect(
            self.update_scheme_bop_installation_combo_problem)
        self.scheme_bop_installation_combo.currentTextChanged.connect(self.update_scheme_bop_installation_combo)
        self.complications_of_failure_armatura_combo.currentTextChanged.connect(
            self.update_complications_of_failure_armatura)

        self.count_sections_esp_label = QLabel('Кол-во секций ЭЦН')
        self.count_sections_esp_combo = QComboBox(self)
        self.count_sections_esp_combo.addItems(['1', '2', '3', '4', '5', '6', '7', '8'])

        self.count_sections_ped_label = QLabel('Кол-во секций ПЭД')
        self.count_sections_ped_combo = QComboBox(self)
        self.count_sections_ped_combo.addItems(['1', '2', '3', '4', '5', '6', '7', '8'])

        self.esp_dismantling_text_line = QLabel('Демонтаж ЭЦН')
        self.esp_dismantling_text_line = QLineEdit(self)

        self.esp_dismantling_time_begin_label = QLabel('начало демонтажа')
        self.esp_dismantling_time_begin_date = QDateTimeEdit(self)
        self.esp_dismantling_time_begin_date.setDisplayFormat("dd.MM.yyyy HH:mm")
        self.esp_dismantling_time_begin_date.setDateTime(self.date_work_str)

        self.esp_dismantling_time_end_label = QLabel('Окончание демонтажа')
        self.esp_dismantling_time_end_date = QDateTimeEdit(self)
        self.esp_dismantling_time_end_date.setDisplayFormat("dd.MM.yyyy HH:mm")
        self.esp_dismantling_time_end_date.setDateTime(self.date_work_str)

        self.esp_dismantling_time_label = QLabel('затраченное время')
        self.esp_dismantling_time_line = QLineEdit(self)
        self.esp_dismantling_time_line.setValidator(self.validator_float)

        self.esp_dismantling_time_begin_date.dateTimeChanged.connect(
            self.update_esp_dismantling_time)
        self.esp_dismantling_time_end_date.dateTimeChanged.connect(
            self.update_esp_dismantling_time)

        self.equipment_audit_label = QLabel('Была ли ревизия')
        self.equipment_audit_combo = QComboBox(self)
        self.equipment_audit_combo.addItems(['Нет', 'Да'])

        self.grid.addWidget(self.equipment_audit_label, 94, 1)
        self.grid.addWidget(self.equipment_audit_combo, 95, 1)

        self.equipment_audit_combo.currentTextChanged.connect(self.update_equipment_audit_combo)

        if index in 'ЭЦН':

            self.grid.addWidget(self.count_sections_esp_label, 40, 1)
            self.grid.addWidget(self.count_sections_esp_combo, 41, 1)
            self.grid.addWidget(self.count_sections_ped_label, 40, 2)
            self.grid.addWidget(self.count_sections_ped_combo, 41, 2)
            self.grid.addWidget(self.esp_dismantling_time_begin_label, 40, 3)
            self.grid.addWidget(self.esp_dismantling_time_begin_date, 41, 3)
            self.grid.addWidget(self.esp_dismantling_time_end_label, 40, 4)
            self.grid.addWidget(self.esp_dismantling_time_end_date, 41, 4)
            self.grid.addWidget(self.esp_dismantling_time_label, 40, 5)
            self.grid.addWidget(self.esp_dismantling_time_line, 41, 5)

        else:
            self.count_sections_esp_label.setParent(None)
            self.count_sections_esp_combo.setParent(None)

            self.count_sections_ped_label.setParent(None)
            self.count_sections_ped_combo.setParent(None)

            self.esp_dismantling_time_begin_label.setParent(None)
            self.esp_dismantling_time_begin_date.setParent(None)

            self.esp_dismantling_time_end_label.setParent(None)
            self.esp_dismantling_time_end_date.setParent(None)

            self.esp_dismantling_time_label.setParent(None)
            self.esp_dismantling_time_line.setParent(None)

        if index in ['Фондовый пакер', 'пакер ГРП']:
            self.depth_paker_text_combo_label = QLabel('Была ли опрессовка перед срывом')
            self.depth_paker_text_combo = QComboBox(self)
            self.depth_paker_text_combo.addItems(['Нет', 'Да'])

            self.grid.addWidget(self.depth_paker_text_combo_label, 30, 0)
            self.grid.addWidget(self.depth_paker_text_combo, 31, 0)

            self.depth_paker_text_combo.currentTextChanged.connect(self.update_pressuar_combo)

    def update_scheme_bop_installation_combo(self, index):
        if index == 'Первая':
            self.line_lenght_bop_label = QLabel('Длина линии 1 Категории')
            self.line_lenght_bop_line = QLineEdit(self)
            self.line_lenght_bop_line.setValidator(self.validator_int)
            self.line_lenght_bop_line.setText('30')
            self.grid.addWidget(self.line_lenght_bop_label, 10, 6)
            self.grid.addWidget(self.line_lenght_bop_line, 11, 6)
        else:
            self.line_lenght_bop_label.setParent(None)
            self.line_lenght_bop_line.setParent(None)

    def update_scheme_bop_installation_combo_problem(self, index):
        if index == 'Нет':
            self.scheme_bop_installation_text_label.setParent(None)
            self.scheme_bop_installation_text_line.setParent(None)

            self.scheme_bop_installation_time_begin_label.setParent(None)
            self.scheme_bop_installation_time_begin_date.setParent(None)

            self.scheme_bop_installation_time_end_label.setParent(None)
            self.scheme_bop_installation_time_end_date.setParent(None)

            self.scheme_bop_installation_time_label.setParent(None)
            self.scheme_bop_installation_time_line.setParent(None)
        else:
            self.scheme_bop_installation_text_label = QLabel('Текст осложнения')
            self.scheme_bop_installation_text_line = QLineEdit(self)

            self.scheme_bop_installation_time_begin_label = QLabel('начало осложнения')
            self.scheme_bop_installation_time_begin_date = QDateTimeEdit(self)
            self.scheme_bop_installation_time_begin_date.setDisplayFormat("dd.MM.yyyy HH:mm")
            self.scheme_bop_installation_time_begin_date.setDateTime(self.date_work_str)

            self.scheme_bop_installation_time_end_label = QLabel('Окончание осложнения')
            self.scheme_bop_installation_time_end_date = QDateTimeEdit(self)
            self.scheme_bop_installation_time_end_date.setDisplayFormat("dd.MM.yyyy HH:mm")
            self.scheme_bop_installation_time_end_date.setDateTime(self.date_work_str)

            self.scheme_bop_installation_time_label = QLabel('затраченное время')
            self.scheme_bop_installation_time_line = QLineEdit(self)
            self.scheme_bop_installation_time_line.setValidator(self.validator_float)

            self.grid.addWidget(self.scheme_bop_installation_text_label, 12, 2)
            self.grid.addWidget(self.scheme_bop_installation_text_line, 13, 2)
            self.grid.addWidget(self.scheme_bop_installation_time_begin_label, 12, 3)
            self.grid.addWidget(self.scheme_bop_installation_time_begin_date, 13, 3)
            self.grid.addWidget(self.scheme_bop_installation_time_end_label, 12, 4)
            self.grid.addWidget(self.scheme_bop_installation_time_end_date, 13, 4)
            self.grid.addWidget(self.scheme_bop_installation_time_label, 12, 5)
            self.grid.addWidget(self.scheme_bop_installation_time_line, 13, 5)

            self.scheme_bop_installation_time_begin_date.dateTimeChanged.connect(
                self.update_date_of_scheme_bop_installation)
            self.scheme_bop_installation_time_end_date.dateTimeChanged.connect(
                self.update_date_of_scheme_bop_installation)

    def update_lowering_for_pressure_testing(self, index):
        if index == 'Нет':
            self.count_nkt_label.setParent(None)
            self.count_nkt_line.setParent(None)
            self.pressuar_bop_text_label.setParent(None)
            self.pressuar_bop_text_line.setParent(None)
        else:
            self.count_nkt_label = QLabel('Количество НКТ')
            self.count_nkt_line = QLineEdit(self)
            self.count_nkt_line.setValidator(self.validator_int)
            self.count_nkt_line.setText('3')
            self.pressuar_bop_text_label = QLabel('Текст опрессовки ПВО')
            self.pressuar_bop_text_line = QLineEdit(self)
            # self.pressuar_bop_text_line.setText(f'Опрессовка ПВО {well_data.max_admissible_pressure._value}(+)')
            self.grid.addWidget(self.count_nkt_label, 10, 3)
            self.grid.addWidget(self.count_nkt_line, 11, 3)
            self.grid.addWidget(self.pressuar_bop_text_label, 10, 4)
            self.grid.addWidget(self.pressuar_bop_text_line, 11, 4)

    def update_pressuar_gno_combo(self, index):
        if index == 'Нет':
            self.pressuar_gno_text_label.setParent(None)
            self.pressuar_gno_text_line.setParent(None)
        else:
            self.pressuar_gno_text_label = QLabel('Текст опрессовки ГНО')
            self.pressuar_gno_text_line = QLineEdit(self)
            self.grid.addWidget(self.pressuar_gno_text_label, 6, 2)
            self.grid.addWidget(self.pressuar_gno_text_line, 7, 2)



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

    def update_date_of_scheme_bop_installation(self):
        time_begin = self.scheme_bop_installation_time_begin_date.dateTime()
        time_end = self.scheme_bop_installation_time_end_date.dateTime()

        time_difference = self.calculate_date(time_begin, time_end)
        self.scheme_bop_installation_time_line.setText(str(time_difference))

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

    def update_date_of_armatura(self):
        time_begin = self.complications_of_failure_armatura_time_begin_date.dateTime()
        time_end = self.complications_of_failure_armatura_time_end_date.dateTime()

        time_difference = self.calculate_date(time_begin, time_end)
        self.complications_of_failure_armatura_time_line.setText(str(time_difference))

    def calculate_date(self, time_begin, time_end):
        # Вычисляем разницу в секундах
        difference_in_seconds = time_begin.secsTo(time_end)

        # Преобразуем в часы
        difference_in_hours = round(difference_in_seconds / 3600, 1)
        return difference_in_hours


class TabWidget(QTabWidget):
    def __init__(self):
        super().__init__()
        self.addTab(TabPage_SO_Lifting_gno(self), 'Подьем ГНО')


class LiftingWindow(TemplateWork):
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
        self.dict_nkt = {}
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
        self.nkt_60_count_edit = None
        self.nkt_73_lenght_edit = None
        self.nkt_73_count_edit = None
        self.nkt_89_lenght_edit = None
        self.nkt_89_count_edit = None
        self.lowering_for_pressure_testing_combo = None
        self.scheme_bop_installation_combo = None
        self.count_nkt_line = None
        self.pressuar_bop_text_line = None
        self.line_lenght_bop_line = None
        self.scheme_bop_installation_problem_combo = None

        self.count_sections_esp_combo = None
        self.count_sections_ped_combo = None

        self.esp_dismantling_time_begin_date = None
        self.esp_dismantling_time_end_date = None
        self.esp_dismantling_time_line = None

        self.scheme_bop_installation_text_line = None
        self.scheme_bop_installation_time_begin_date = None
        self.scheme_bop_installation_time_end_date = None
        self.scheme_bop_installation_time_line = None
        self.gno_combo = None



    def add_work(self):
        from main import MyWindow

        current_widget = self.tabWidget.currentWidget()

        self.date_work_line = current_widget.date_work_line.text()
        self.gno_combo = current_widget.gno_combo.currentText()

        if self.gno_combo in ['Фондовый пакер']:
            self.coefficient_lifting = 1.2
            self.depth_paker_text_combo = current_widget.depth_paker_text_combo.currentText()
            if self.depth_paker_text_combo == 'Да':
                self.read_pressuar_combo(current_widget)


        elif self.gno_combo in ['ЭЦН']:
            self.coefficient_lifting = 1
            self.count_sections_esp_combo = int(current_widget.count_sections_esp_combo.currentText())
            self.count_sections_ped_combo = int(current_widget.count_sections_ped_combo.currentText())

            self.esp_dismantling_text_line = current_widget.esp_dismantling_text_line.text()
            self.esp_dismantling_time_begin_date = \
                current_widget.esp_dismantling_time_begin_date.dateTime().toPyDateTime()
            self.esp_dismantling_time_begin_date = \
                self.change_string_in_date(self.esp_dismantling_time_begin_date)

            self.esp_dismantling_time_end_date = \
                current_widget.esp_dismantling_time_end_date.dateTime().toPyDateTime()
            self.esp_dismantling_time_end_date = \
                self.change_string_in_date(self.esp_dismantling_time_end_date)

            if self.esp_dismantling_time_end_date == self.esp_dismantling_time_begin_date:
                QMessageBox.warning(self, 'Даты совпадают', 'Даты совпадают')
                return

            if self.esp_dismantling_text_line == '':
                QMessageBox.warning(self, 'Ошибка', f'Не введены текст демонтажа')
                return

            self.esp_dismantling_time_line = current_widget.esp_dismantling_time_line.text()
            if self.esp_dismantling_time_line != '':
                self.esp_dismantling_time_line = round(float(self.esp_dismantling_time_line), 1)
            else:
                QMessageBox.warning(self, 'Ошибка', f'Не введены время демонтажа ЭЦН')
                return

            if self.esp_dismantling_time_line <= 0:
                QMessageBox.warning(self, 'Ошибка', f'Затраченное время при срыве ПШ не может быть отрицательным')
                return

        else:
            self.coefficient_lifting = 1

        read_data = self.read_nkt_up(current_widget)
        if read_data is None:
            return

        self.complications_of_failure_combo = current_widget.complications_of_failure_combo.currentText()
        self.complications_of_failure_armatura_combo = current_widget.complications_of_failure_armatura_combo.currentText()
        self.complications_during_disassembly_combo = current_widget.complications_during_disassembly_combo.currentText()
        self.complications_when_lifting_combo = current_widget.complications_when_lifting_combo.currentText()
        self.scheme_bop_installation_problem_combo = current_widget.scheme_bop_installation_problem_combo.currentText()
        # self.pressuar_gno_combo = current_widget.pressuar_gno_combo.currentText()
        self.lowering_for_pressure_testing_combo = current_widget.lowering_for_pressure_testing_combo.currentText()
        self.scheme_bop_installation_combo = current_widget.scheme_bop_installation_combo.currentText()
        self.equipment_audit_combo = current_widget.equipment_audit_combo.currentText()

        if self.equipment_audit_combo == 'Да':
            self.equipment_audit_text_line = current_widget.equipment_audit_text_line.text()

        if self.scheme_bop_installation_combo == 'Первая':
            self.line_lenght_bop_line = current_widget.line_lenght_bop_line.text()
            if self.line_lenght_bop_line != '':
                self.line_lenght_bop_line = int(float(self.line_lenght_bop_line))
        if self.lowering_for_pressure_testing_combo == 'Да':
            self.count_nkt_line = current_widget.count_nkt_line.text()
            if self.count_nkt_line != '':
                self.count_nkt_line = int(float(self.count_nkt_line))
            self.pressuar_bop_text_line = current_widget.pressuar_bop_text_line.text()

        # if self.pressuar_gno_combo == 'Да':
        #     self.pressuar_gno_text_line = current_widget.pressuar_gno_text_line.text()
        #     if self.pressuar_gno_text_line == '':
        #         QMessageBox.warning(self, 'Ошибка', f'Не введены текст опрессовки ГНО')
        #         return

        if self.complications_of_failure_combo == 'Да':
            read_data = self.read_complications_of_failure(current_widget)
            if read_data is None:
                return

        if self.scheme_bop_installation_problem_combo == 'Да':
            self.scheme_bop_installation_text_line = current_widget.scheme_bop_installation_text_line.text()
            self.scheme_bop_installation_time_begin_date = \
                current_widget.scheme_bop_installation_time_begin_date.dateTime().toPyDateTime()
            self.scheme_bop_installation_time_begin_date = \
                self.change_string_in_date(self.scheme_bop_installation_time_begin_date)

            self.scheme_bop_installation_time_end_date = \
                current_widget.scheme_bop_installation_time_end_date.dateTime().toPyDateTime()
            self.scheme_bop_installation_time_end_date = \
                self.change_string_in_date(self.scheme_bop_installation_time_end_date)

            if current_widget.scheme_bop_installation_text_line.text() == self.scheme_bop_installation_time_begin_date:
                QMessageBox.warning(self, 'Даты совпадают', 'Даты совпадают')
                return

            if self.scheme_bop_installation_text_line == '':
                QMessageBox.warning(self, 'Ошибка', f'Не введены текст осложнения при срыве ПШ')
                return

            self.scheme_bop_installation_time_line = current_widget.scheme_bop_installation_time_line.text()
            if self.scheme_bop_installation_time_line != '':
                self.scheme_bop_installation_time_line = round(float(self.scheme_bop_installation_time_line), 1)

            else:
                QMessageBox.warning(self, 'Ошибка', f'Не введены время осложнения при срыве ПШ')
                return

            if self.scheme_bop_installation_time_line <= 0:
                QMessageBox.warning(self, 'Ошибка', f'Затраченное время при срыве ПШ не может быть отрицательным')
                return
            ass = self.scheme_bop_installation_time_line,
        if self.complications_of_failure_armatura_combo == 'Да':
            read_data = self.read_complications_of_failure_armatura(current_widget)
            if read_data is None:
                return

        if self.complications_when_lifting_combo == 'Да':
            read_data = self.read_complications_when_lifting_combo(current_widget)
            if read_data is None:
                return


        if self.complications_during_disassembly_combo == 'Да':
            read_data = self.read_complications_during_disassembly_combo(current_widget)
            if read_data is None:
                return

        if len(self.dict_nkt) == 0:
            question = QMessageBox.question(self, 'Ошибка', f'НКТ отсутствуют?')
            if question == QMessageBox.StandardButton.No:
                return


        work_list = self.lifting_paker_def()

        well_data.date_work = self.date_work_line

        self.populate_row(self.ins_ind, work_list, self.table_widget)
        well_data.pause = False
        self.close()
    @staticmethod
    def change_string_in_date(date_str):
        # Преобразуем строку в объект datetime

        formatted_date = date_str.strftime("%d.%m.%Y %H:%M")
        return formatted_date

    def lifting_nkt(self, dict_nkt, type_equipment):

        middle_nkt = ''
        for nkt_key, nkt_value in dict_nkt.items():
            middle_nkt_value = nkt_value[0] / nkt_value[1]
            nkt_lenght = nkt_value[0]
            nkt_count = nkt_value[1]
            if 6.5 <= middle_nkt_value <= 7.5:
                middle_nkt = '6.5-7.5'
            elif 7.6 <= middle_nkt_value <= 8.5:
                middle_nkt = '7.6-8.5'
            elif 8.6 <= middle_nkt_value <= 9.5:
                middle_nkt = '8.6-9.5'
            elif 9.6 <= middle_nkt_value <= 10.5:
                middle_nkt = '9.6-10.5'
            elif 10.6 <= middle_nkt_value <= 11.5:
                middle_nkt = '10.6-11.5'
            elif 11.6 <= middle_nkt_value <= 12.5:
                middle_nkt = '11.6-12.5'

            if middle_nkt == '':
                QMessageBox.warning(self, 'Средняя длина', 'Средняя длина НКТ не корректна')
                break

            max_count_3 = LIFTING_NORM_NKT[well_data.lifting_unit_combo][nkt_key]['III'][middle_nkt][1]
            koef_norm_3 = LIFTING_NORM_NKT[well_data.lifting_unit_combo][nkt_key]['III'][middle_nkt][0]
            razdel_3 = LIFTING_NORM_NKT[well_data.lifting_unit_combo][nkt_key]['III']['раздел']

            if max_count_3 >= nkt_lenght:
                max_count_3 = nkt_lenght

            lenght_nkt_3 = int(middle_nkt_value * max_count_3)

            work_list = [
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', type_equipment,
                 'ПЗР СПО перед подъемом труб из скважины',
                 None, None, None,
                 None, None, None, None, None, None, None, None, None, '§207разд.1', None, 'шт', 1, 0.07, 1,
                 '=V199*W199*X199', '=Y199-AA199-AB199-AC199-AD199', None, None, None, None, None]]

            podien_3_list = ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', type_equipment,
                             'Подъем НКТ  3 скорость',
                             None, None, None, None, nkt_key, lenght_nkt_3, middle_nkt, max_count_3,
                             None, None, None, None, razdel_3, None, 'шт', max_count_3, koef_norm_3,
                             self.coefficient_lifting, '=V202*W202*X202', '=Y202-AA202-AB202-AC202-AD202',
                             None, None, None, None, None]

            work_list.append(podien_3_list)

            nkt_count -= max_count_3

            nkt_sum = sum(list(map(lambda x: x[1], self.dict_nkt.values())))

            if nkt_count > 0:
                max_count_2 = LIFTING_NORM_NKT[well_data.lifting_unit_combo][nkt_key]['II'][middle_nkt][1]
                koef_norm_2 = LIFTING_NORM_NKT[well_data.lifting_unit_combo][nkt_key]['II'][middle_nkt][0]
                razdel_2 = LIFTING_NORM_NKT[well_data.lifting_unit_combo][nkt_key]['II']['раздел']
                if max_count_2 >= nkt_count:
                    max_count_2 = nkt_count
                lenght_nkt_2 = int(middle_nkt_value * max_count_2)
                podiem_list_2 = ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', type_equipment,
                                 'Подъем НКТ  2 скорость',
                                 None, None, None, None, nkt_key, lenght_nkt_2, middle_nkt, max_count_2,
                                 None, None, None, None, razdel_2, None, 'шт', max_count_2, koef_norm_2,
                                 self.coefficient_lifting, '=V202*W202*X202', '=Y202-AA202-AB202-AC202-AD202', None,
                                 None, None, None, None]
                nkt_count -= max_count_2
                work_list.insert(1, podiem_list_2)

            if nkt_count > 0:
                max_count_1 = LIFTING_NORM_NKT[well_data.lifting_unit_combo][nkt_key]['I'][middle_nkt][1]
                koef_norm_1 = LIFTING_NORM_NKT[well_data.lifting_unit_combo][nkt_key]['I'][middle_nkt][0]
                razdel_1 = LIFTING_NORM_NKT[well_data.lifting_unit_combo][nkt_key]['I']['раздел']

                if max_count_1 >= nkt_count:
                    max_count_1 = nkt_count

                lenght_nkt_1 = int(middle_nkt_value * max_count_1)
                podiem_list_1 = [
                    '=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', type_equipment, 'Подъем НКТ  1 скорость',
                    None, None, None, None, nkt_key, lenght_nkt_1, middle_nkt, max_count_1,
                    None, None, None, None, razdel_1, None, 'шт', max_count_1, koef_norm_1,
                    self.coefficient_lifting, '=V202*W202*X202', '=Y202-AA202-AB202-AC202-AD202', None, None, None,
                    None, None]
                nkt_count -= max_count_1
                work_list.insert(1, podiem_list_1)


            work_list.extend([
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', type_equipment, 'Долив скважины', None, None,
                 None, None,
                 None, None, None,
                 None, None, None, None, None, '§168разд.1', None, 'шт', nkt_sum/10, 0.003, 1, '=V204*W204*X204',
                 '=Y204-AA204-AB204-AC204-AD204', None, None, None, None, None],
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', type_equipment,
                 'Навернуть/отвернуть предохранительное кольцо', None, None,
                 None, None, None, None, None, None, None, None, None, None, '§300разд.1', None, 'шт',
                 nkt_sum,
                 0.003, 1, '=V205*W205*X205', '=Y205-AA205-AB205-AC205-AD205', None, None, None, None, None],
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', type_equipment, 'Замер НКТ ', None, None, None,
                 None, None,
                 None, None, None,
                 None, None, None, None, '§47разд.1', None, 'шт', nkt_sum, 0.008, 1,
                 '=V207*W207*X207',
                 '=Y207-AA207-AB207-AC207-AD207', None, None, None, None, None],

                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'Очистка от замазученности',
                 None, None, None, None,
                 None, None, None, None, 'АКТ№', None, None, None, 'факт', None, 'шт', 1, 0.67, 1, '=V209*W209*X209',
                 '=Y209-AA209-AB209-AC209-AD209', None, None, None, None, None],
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, self.equipment_audit_text_line,
                 None, None, None, None, None, None,
                 None, None, 'АКТ№', None, None, None, 'факт', None, 'час', 0.5, 1, 1, '=V210*W210*X210',
                 '=Y210-AA210-AB210-AC210-AD210', None, None, None, None, None]])

            if self.complications_when_lifting_combo == 'Да':
                work_list.insert(-4, ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', type_equipment,
                                      f'{self.complications_when_lifting_text_line} {self.complications_when_lifting_time_begin_date}'
                                      f'{self.complications_when_lifting_time_end_date}',
                                      None, None,
                                      None, None, None,
                                      None, 'Объем', 0, None, None, None, None, 'факт', None,
                                      'час', self.complications_when_lifting_time_end_date, 1, 1, '=V206*W206*X206',
                                      '=Y206-AA206-AB206-AC206-AD206', None, None, None, None, None])
            if nkt_sum > 201:
                work_list.insert(-3, ['=ROW()-ROW($A$46)', 'подъем 73мм', None, 'спо', type_equipment,
                                      'Откатывание труб с 201 трубы ',
                                      None, None, None,
                                      None, None, None, None, None, None, None, None, None, '§40разд.1', None, 'шт',
                                      sum(self.dict_nkt.values()) - 201, 0.008, 1,
                                      '=V208*W208*X208', '=Y208-AA208-AB208-AC208-AD208', None, None, None, None, None])

        return work_list

    def lifting_paker_def(self):
        complications_of_failure_list = []
        complications_during_disassembly_list = []
        work_list = []

        if self.depth_paker_text_combo == 'Да':
            work_list.extend(self.pressuar_work())


        if self.complications_of_failure_armatura_combo == 'Да':
            complications_of_failure_armatura_list = [
                '=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
                f'{self.complications_of_failure_armatura_text_line} {self.complications_of_failure_armatura_time_begin_date}-'
                f'{self.complications_of_failure_armatura_time_end_date}', None, None, None, None, None,
                None, None, None, 'АКТ№', None, None, None, 'факт', None, 'час',
                self.complications_of_failure_armatura_time_line - 0.3, 1, 1, '=V280*W280*X280',
                '=Y280-AA280-AB280-AC280-AD280', None, None, None, None, None]
            work_list.append(complications_of_failure_armatura_list)

            self.date_work_line = self.complications_of_failure_armatura_time_end_date.split(' ')[0]

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

        work_list.extend([
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'Демонтаж ПШ', None, None, None,
             None, None, None, None, None, None, None, None, None, '§121разд.1', None, 'шт', 1, 0.3, 1,
             '=V281*W281*X281', '=Y281-AA281-AB281-AC281-AD281', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
             'Срыв план-шайбы в эксплуатационной колонне', None, None, None, None, None, None, None, None,
             None, None, None, None, '§146разд.1', None, 'шт', 1, 0.15, 1, '=V282*W282*X282',
             '=Y282-AA282-AB282-AC282-AD282', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
             'Демонтаж планшайбы с устья скважины', None, None, None, None, None, None, None, None, None,
             None, None, None, '§107разд.1', None, 'шт', 1, 0.32, 1, '=V283*W283*X283',
             '=Y283-AA283-AB283-AC283-AD283', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'Демонтаж АУ фонтанной арматуры',
             None, None, None, None, None, None, None, None, None, None, None, None, '§102разд.1', None,
             'раз', 1, 0.75, 1, '=V284*W284*X284', '=Y284-AA284-AB284-AC284-AD284', None, None, None,
             None, None]])

        if self.complications_during_disassembly_combo == "Да":
            complications_during_disassembly_list = [
                '=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции',
                None,
                f'{self.complications_during_disassembly_q_line} '
                f'{self.complications_during_disassembly_q_time_begin_date}-'
                f'{self.complications_during_disassembly_q_time_end_date}', None,
                None, None, None, None, None,
                None, None, 'АКТ№', None, None, None, 'факт', None, 'час',
                self.complications_during_disassembly_time_line - 0.45, 1, 1,
                '=V286*W286*X286', '=Y286-AA286-AB286-AC286-AD286', None, None,
                None, None, None]
            work_list.append(complications_during_disassembly_list)
            self.date_work_line = self.complications_during_disassembly_q_time_end_date.split(' ')[0]

        if self.gno_combo == 'ЭЦН':
            work_list.append(['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'ЭЦН',
                              'Разборка кабельного ввода на планшайбе', None, None,
                              None, None, None, None, None, None, None, None, None, None, '§198разд.', None, 'час', 1,
                              0.17, 1, '=V226*W226*X226', '=Y226-AA226-AB226-AC226', None, None, None, None, None])

        relocation_list = [
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'Демонтаж крестовины', None,
             None, None, None, None, None, None, None, None, None, None, None, '§300разд.1', None, 'шт',
             1, 0.45, 1, '=V285*W285*X285', '=Y285-AA285-AB285-AC285-AD285', None, None, None, None,
             None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'Монтаж превентора ПМТ ', None,
             None, None, None, None, None, None, None, None, None, None, None, '§109разд.1', None, 'шт',
             1, 0.67, 1, '=V287*W287*X287', '=Y287-AA287-AB287-AC287-AD287', None, None, None, None,
             None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
             'Поднести тяги,штурвалы,присоеденить их к превентору,установить стойки под тяги и защитные щиты',
             None, None, None, None, None, None, None, None, None, None, None, None,
             '§110расд.1', None, 'шт', 1, 0.23, 1, '=V288*W288*X288',
             '=Y288-AA288-AB288-AC288-AD288', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'Монтаж выкидной линии', None, None,
             None, None, None, None, None, None, None, None, None, None, '§301разд.1', None, 'раз', 1,
             0.3, 1, '=V289*W289*X289', '=Y289-AA289-AB289-AC289-AD289', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'Устройство  рабочей площадки', None,
             None, None, None, None, None, None, None, None, None, None, None, '§54разд.1', None, 'шт',
             1, 0.83, 1, '=V291*W291*X291', '=Y291-AA291-AB291-AC291-AD291', None, None, None, None,
             None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'ПР.перед.ремонтом', None, 'Монтаж ГКШ-1200', None, None,
             None, None, None, None, None, None, None, None, None, None, '§184разд.1', None, 'шт', 1,
             0.33, 1, '=V292*W292*X292', '=Y292-AA292-AB292-AC292-AD292', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'ПР.перед.ремонтом', None, 'Монтаж СПГ', None, None, None,
             None, None, None, None, None, None, None, None, None, '§185разд.1', None, 'шт', 1, 0.07, 1,
             '=V293*W293*X293', '=Y293-AA293-AB293-AC293-AD293', None, None, None, None, None],
        ]
        time_bop = 0
        if self.scheme_bop_installation_time_line:

            time_bop = self.scheme_bop_installation_time_line - 2.43
            if time_bop <= 0:
                time_bop =2.43

        if self.scheme_bop_installation_combo == 'Первая':
            bop_list = [
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'первая.категория', '30м',
                 'Монтаж линии дросселирования и глушения.Опрессовка линии 1 схема', None, None, None, None,
                 None, None, None, None, None, None, None, None, '§23аразд.1', None, 'шт', 1, 2.43, 1,
                 '=V304*W304*X304', '=Y304-AA304-AB304-AC304-AD304', None, None, None, None, None],
                ['=ROW()-ROW($A$46)', '1кат', None, 'Тех.операции', None,
                  'Монтаж временного основания и станции (блока) управления превентором с гидравлическим приводом (СУП)',
                  None, None, None, None, None, None, None, None, None, None, None, None, '§127разд.1', None, 'шт', 1,
                  0.38, 1, '=V88*W88*X88', '=Y88-AA88-AB88-AC88-AD88', None, None, None, None, None],
                 ['=ROW()-ROW($A$46)', '1кат', None, 'Тех.операции', None,
                  'Демонтаж временного основания и станции (блока) управления превентором с '
                  'гидравлическим приводом (СУП) (монтируется отдельным блоком)',
                  None, None, None, None, None, None, None, None, None, None, None, None, '§132разд.1', None, 'шт', 1,
                  0.33, 1, '=V89*W89*X89', '=Y89-AA89-AB89-AC89-AD89', None, None, None, None, None],
                 ['=ROW()-ROW($A$46)', self.date_work_line, None, None, None, None, None, None, None, None, None, None, None, None,
                  None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 ['=ROW()-ROW($A$46)', '1кат', None, 'Тех.операции', None,
                  'Монтаж превентора плашечного гидравлического двойного действия типа ППСГ-СТЦ-2ФТ-156х21, '
                  'ПП2Г-2Ф-180х35 со станцией управления и системой обогрева превентора',
                  None, None, None, None, None, None, None, None, None, None, None, None, '§125разд.1', None, 'шт', 1,
                  1.13, 1, '=V92*W92*X92', '=Y92-AA92-AB92-AC92-AD92', None, None, None, None, None],
                 ['=ROW()-ROW($A$46)', '1кат', None, 'Тех.операции', None,
                  'Демонтаж превентора плашечного гидравлического двойного действия типа ППСГ- СТЦ-2ФТ-156х21, '
                  'ПП2Г-2Ф-180х35 со станцией управления и системой обогрева превентора',
                  None, None, None, None, None, None, None, None, None, None, None, None, '§130разд.1', None, 'шт', 1,
                  0.83, 1, '=V93*W93*X93', '=Y93-AA93-AB93-AC93-AD93', None, None, None, None, None]
            ]


            work_list.extend(bop_list)


        if self.scheme_bop_installation_problem_combo == 'Да':

            work_list.append(['=ROW()-ROW($A$46)', self.date_work_line, None, 'первая.категория', '30м',
             f'{self.scheme_bop_installation_text_line} '
             f'{self.scheme_bop_installation_time_begin_date}-{self.scheme_bop_installation_time_end_date}',
             None, None, None, None, None, None, None,
             None, None, None, None, None, 'факт', None, 'час', time_bop, 1, 1,
             '=V305*W305*X305',
             '=Y305-AA305-AB305-AC305-AD305', None, None, None, None, None])

            if self.scheme_bop_installation_time_end_date:
                self.date_work_line = self.scheme_bop_installation_time_end_date.split(' ')[0]
        if self.lowering_for_pressure_testing_combo == 'Да':
            work_list.extend(self.lowering_for_pressure())

        work_list.extend(relocation_list)
        work_nkt = self.lifting_nkt(self.dict_nkt, self.gno_combo)
        work_list.extend(work_nkt)

        if self.gno_combo in 'ЭЦН':

            ecn_list = [
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'ЭЦН',
                 'Разгрузить барабан, автонаматыватель', None,
                 None,
                 None, None, None, None, None, None, None, None, None, None, '§299разд.1', None, 'раз', 2,
                 0.3333333333333333, 1, '=V226*W226*X226', '=Y226-AA226-AB226-AC226', None, None, None, None, None],
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'ЭЦН', 'Разгрузить подвесной ролик',
                 None, None, None,
                 None, None, None, None, None, None, None, None, None, '§299разд.1', None, 'раз', 1, 0.05, 1,
                 '=V227*W227*X227', '=Y227-AA227-AB227-AC227', None, None, None, None, None]]
            for row in ecn_list[::-1]:
                work_list.insert(0, row)

            work_list.extend(self.lifting_ecn())

        return work_list

    def lowering_for_pressure(self):
        for nkt_key, nkt_value in self.dict_nkt.items():
            if '48' in nkt_key:
                nkt_key = '48мм'
            elif '60' in nkt_key:
                nkt_key = '60мм'
            elif '73' in nkt_key:
                nkt_key = '73мм'
            elif '89' in nkt_key or '102' in nkt_key:
                nkt_key = '89-102мм'
        middle_nkt = '9.6-10.5'
        aaaa = DESCENT_NORM_NKT[well_data.lifting_unit_combo]
        koef_norm_down = DESCENT_NORM_NKT[well_data.lifting_unit_combo][nkt_key][middle_nkt]
        razdel_2_down = DESCENT_NORM_NKT[well_data.lifting_unit_combo][nkt_key]['раздел']

        max_count_up = LIFTING_NORM_NKT[well_data.lifting_unit_combo][nkt_key]['I'][middle_nkt][1]
        koef_norm_up = LIFTING_NORM_NKT[well_data.lifting_unit_combo][nkt_key]['I'][middle_nkt][0]
        razdel_1_up = LIFTING_NORM_NKT[well_data.lifting_unit_combo][nkt_key]['I']['раздел']

        work_list = [
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', 'Пакер', 'ПЗР СПО пакера', None, None, None, None,
             None, None,
             None,
             None, None, None, None, None, '§136разд.1', None, 'шт', 1, 0.48, 1, 0, '=Y294-AA294-AB294-AC294-AD294',
             None,
             None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', 'Пакер', 'Спуск НКТ компоновка ', None, None, None,
             None, None,
             nkt_key, 10 * self.count_nkt_line,
             middle_nkt, None, None, None, None,
             razdel_2_down, None, 'шт', self.count_nkt_line,
             koef_norm_down, 1.2, 0, '=Y295-AA295-AB295-AC295-AD295', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', 'Пакер',
             'Навернуть/отвернуть предохранительное кольцо', None,
             None,
             None, None, None, None, None, None, None, None, None, None, '§300разд.1', None, 'шт', '=SUM(V295)',
             self.count_nkt_line / 1000, 1,
             0, '=Y296-AA296-AB296-AC296-AD296', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'Посадка пакера', None, None, None,
             None, None,
             None,
             None, None, None, None, None, None, '§138разд.1', None, 'шт', 1, 0.23, 1, 0,
             '=Y297-AA297-AB297-AC297-AD297',
             None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'Опрессовка превентора ', None, None,
             None, None,
             None,
             None, None, None, None, None, None, None, '§115разд.1', None, 'шт', 1, 0.62, 1, 0,
             '=Y298-AA298-AB298-AC298-AD298', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
             'Срыв пакера в эксплуатационной колонне', None,
             None,
             None, None, None, None, None, None, None, None, None, None, '§146разд.1', None, 'шт', 1, 0.15, 1, 0,
             '=Y299-AA299-AB299-AC299-AD299', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', 'Пакер', 'Подъем НКТ  3 скорость', None, None, None,
             None, nkt_key,
             10 * self.count_nkt_line,
             '9.6-10.5',
             max_count_up, None, None, None, None,
             razdel_1_up, None, 'шт', self.count_nkt_line,
             koef_norm_up, 1.2, 0, '=Y300-AA300-AB300-AC300-AD300', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', 'Пакер',
             'Навернуть/отвернуть предохранительное кольцо', None,
             None,
             None, None, None, None, None, None, None, None, None, None, '§300разд.1', None, 'шт', '=SUM(V300:V301)',
             0.003, 1, 0, '=Y302-AA302-AB302-AC302-AD302', None, None, None, None, None]]

        return work_list

    def lifting_ecn(self):
        lenght_nkt_ecn = sum(list(map(lambda x: x[0], self.dict_nkt.values())))

        time_differnce = round(
            (((74 + ((self.count_sections_esp_combo - 1) * 13)) + ((self.count_sections_ped_combo - 1) * 20)) / 60), 2)
        work_list = [

            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', 'ЭЦН',
             'Определить отклонение талевого блока, расслабить оттяжки, отцентрировать вышку и '
             'подтянуть оттяжки во время ремонта',
             None, None, None, None, None, None, None, None, None, None, None, None, '§59п.1 разд.1', None, 'час', 0.42,
             1, 1, '=V269*W269*X269', '=Y269-AA269-AB269-AC269-AD269', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', 'ЭЦН', 'Замер сопротивления через  300м.', None,
             None, None, None,
             None, None, None, None, None, None, None, None, '§221разд.1', None, 'м', lenght_nkt_ecn,
             '=(2+V270/300+2)*0.06', 1,
             '=W270', '=Y270-AA270-AB270-AC270-AD270', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
             'Снять с мачты подвесной ролик кабеля ЭНЦ', None,
             None, None, None, None, None, None, None, None, None, None, None, '§97п.12 разд.1', None, 'час', 1, 0.15,
             1, '=V271*W271*X271', '=Y271-AA271-AB271-AC271-AD271', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', 'ЭЦН', 'Погрузить барабан, автонаматыватель', None,
             None, None,
             None, None, None, None, None, None, None, None, None, '§299разд.1', None, 'час', 2, 0.23333333333333334, 1,
             '=V272*W272*X272', '=Y272-AA272-AB272-AC272-AD272', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'ЭЦН', 'Погрузить подвесной ролик', None,
             None, None,
             None, None, None, None, None, None, None, None, None, '§299разд.1', None, 'раз', 1, 0.05, 1,
             '=V273*W273*X273', '=Y273-AA273-AB273-AC273', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, self.equipment_audit_text_line, None, None, None,
             None, None, None,
             None, None, 'АКТ№', None, None, None, 'факт', None, 'час', 0.5, 1, 1, '=V274*W274*X274',
             '=Y274-AA274-AB274-AC274-AD274', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
             f'{self.esp_dismantling_text_line} {self.esp_dismantling_time_begin_date}-'
             f'{self.esp_dismantling_time_end_date} ', None, 'Кол-во секций ЭЦН',
             None, None, self.count_sections_esp_combo, 'Кол-во ПЭД', None, self.count_sections_ped_combo, 'АКТ№',
             None, None, None, 'факт', None, 'час', self.esp_dismantling_time_line - time_differnce, 1, 1,
             '=V275*W275*X275', '=Y275-AA275-AB275-AC275-AD275', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'Демонтаж УЭЦН  ', None,
             'Кол-во секций ЭЦН', None,
             None, 3, 'Кол-во ПЭД', None, 1, None, None, None, None, '§222разд.1', None, 'раз', 1,
             '=ROUND((((74+((K276-1)*13))+((N276-1)*20))/60),2)', 1, '=V276*W276*X276', '=Y276-AA276-AB276-AC276-AD276',
             None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
             'Снятие барабана на автонаматыватель', None, None,
             None, None, None, None, None, None, None, None, None, None, '§219разд.1', None, 'раз', 1, 0.25, 1,
             '=V277*W277*X277', '=Y277-AA277-AB277-AC277-AD277', None, None, None, None, None]]
        if self.esp_dismantling_time_line - time_differnce <= 0:
            work_list.pop(-2)
        return work_list


if __name__ == "__main__":
    # app3 = QApplication(sys.argv)

    app = QApplication(sys.argv)
    window = LiftingWindow(22, 22)
    window.show()
    sys.exit(app.exec_())
