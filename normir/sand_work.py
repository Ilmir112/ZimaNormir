import sys
from datetime import datetime, timedelta

import well_data

from collections import namedtuple
from normir.files_with_list import cause_presence_of_jamming, drilling_ek_list

from PyQt5.QtGui import QIntValidator, QDoubleValidator
from PyQt5.QtWidgets import QWidget, QLabel, QComboBox, QLineEdit, QGridLayout, QTabWidget, QMainWindow, QPushButton, \
    QMessageBox, QApplication, QHeaderView, QTableWidget, QTableWidgetItem, QTextEdit, QDateEdit, QDateTimeEdit
from normir.template_without_skm import TemplateWithoutSKM
from normir.TabPageAll import TabPage, TemplateWork
from PyQt5.QtCore import Qt

from normir.relocation_brigade import TextEditTableWidgetItem


class TabPage_SO_Timplate(TabPage):
    def __init__(self, parent=None):
        super().__init__()

        self.select_type_combo_label = QLabel('Выбор компоновки спуска')
        self.select_type_combo = QComboBox(self)
        self.select_type_combo.addItems(['', 'НКТ'])

        self.grid = QGridLayout(self)

        self.grid.addWidget(self.date_work_label, 4, 2)
        self.grid.addWidget(self.date_work_line, 5, 2)

        self.grid.addWidget(self.select_type_combo_label, 4, 3)
        self.grid.addWidget(self.select_type_combo, 5, 3)

        self.select_type_combo.currentTextChanged.connect(self.update_select_type_combo)

        self.complications_during_tubing_running_label = QLabel('Осложнение при спуске НКТ')
        self.complications_of_failure_label = QLabel('Получен ли прихват, наличие рассхаживания')
        self.complications_when_lifting_label = QLabel('Осложнения при подъеме НКТ')
        self.nkt_48_lenght_label = QLabel('Длина на спуск НКТ48')
        self.nkt_48_count_label = QLabel('Кол-во на спуск НКТ48')
        self.nkt_60_lenght_label = QLabel('Длина на спуск НКТ60')
        self.technological_crap_question_label = QLabel('Был ли тех. отстой')
        self.nkt_60_count_label = QLabel('Кол-во на спуск НКТ60')
        self.nkt_73_lenght_label = QLabel('Длина НКТ73')
        self.nkt_73_count_label = QLabel('Кол-во НКТ73')
        self.nkt_89_lenght_label = QLabel('Длина НКТ89-102')
        self.nkt_89_count_label = QLabel('Кол-во НКТ89-102')
        self.volume_well_flush_label = QLabel('Объем промывки')
        self.installation_pipe_perforator_label = QLabel('монтаж трубного перфоратора')
        self.nkt_is_same_label = QLabel('Кол-во НКТ на подъем совпадает со спуском')
        self.deinstallation_perforation_label = QLabel('Был ли демонтаж трубного перфоратора')

        # self.count_of_nkt_extensions_label = QLabel('Кол-во метров райбирования')

    def update_select_type_combo(self, index):

        self.complications_during_tubing_running_combo = QComboBox(self)
        self.complications_during_tubing_running_combo.addItems(['Нет', 'Да'])

        self.complications_of_failure_combo = QComboBox(self)
        self.complications_of_failure_combo.addItems(['Нет', 'Да'])

        self.complications_when_lifting_combo = QComboBox(self)
        self.complications_when_lifting_combo.addItems(['Нет', 'Да'])

        # self.grid.addWidget(self.complications_of_failure_label, 10, 1)
        # self.grid.addWidget(self.complications_of_failure_combo, 11, 1)
        if index == 'НКТ':
            self.nkt_label()

        self.grid.addWidget(self.complications_during_tubing_running_label, 26, 1)
        self.grid.addWidget(self.complications_during_tubing_running_combo, 27, 1)

        self.grid.addWidget(self.complications_of_failure_label, 28, 1)
        self.grid.addWidget(self.complications_of_failure_combo, 29, 1)

        # self.volume_well_flush_line = QLineEdit(self)
        # self.volume_well_flush_line.setValidator(self.validator_float)
        #
        # self.grid.addWidget(self.volume_well_flush_label, 30, 3)
        # self.grid.addWidget(self.volume_well_flush_line, 31, 3)

        self.grid.addWidget(self.complications_when_lifting_label, 46, 1)
        self.grid.addWidget(self.complications_when_lifting_combo, 47, 1)

        self.installation_pipe_perforator_combo = QComboBox(self)
        self.installation_pipe_perforator_combo.addItems(['Нет', 'Да'])

        self.grid.addWidget(self.installation_pipe_perforator_label, 12, 1)
        self.grid.addWidget(self.installation_pipe_perforator_combo, 13, 1)

        self.nkt_is_same_combo = QComboBox(self)
        self.nkt_is_same_combo.addItems(['Да', 'Нет'])

        self.grid.addWidget(self.nkt_is_same_label, 34, 1)
        self.grid.addWidget(self.nkt_is_same_combo, 35, 1)

        self.deinstallation_perforation_combo = QComboBox(self)
        self.deinstallation_perforation_combo.addItems(['Нет', 'Да'])

        self.grid.addWidget(self.deinstallation_perforation_label, 50, 1)
        self.grid.addWidget(self.deinstallation_perforation_combo, 51, 1)

        self.equipment_audit_label = QLabel('Была ли ревизия')
        self.equipment_audit_combo = QComboBox(self)
        self.equipment_audit_combo.addItems(['Нет', 'Да'])

        self.grid.addWidget(self.equipment_audit_label, 94, 1)
        self.grid.addWidget(self.equipment_audit_combo, 95, 1)

        self.equipment_audit_combo.currentTextChanged.connect(self.update_equipment_audit_combo)
        # self.pressuar_gno_combo.currentTextChanged.connect(self.update_pressuar_gno_combo)
        # self.technological_crap_question_combo.currentTextChanged.connect(self.update_technological_crap_question_combo)
        self.installation_pipe_perforator_combo.currentTextChanged.connect(
            self.update_installation_pipe_perforator_combo)
        # self.pressuar_gno_combo.currentTextChanged.connect(self.update_pressuar_gno_combo)
        self.deinstallation_perforation_combo.currentTextChanged.connect(self.update_deinstallation_perforation_combo)
        self.complications_of_failure_combo.currentTextChanged.connect(self.update_complications_of_failure)
        self.complications_when_lifting_combo.currentTextChanged.connect(self.update_complications_when_lifting)

        self.complications_during_tubing_running_combo.currentTextChanged.connect(
            self.update_complications_during_tubing_running_combo)
        self.nkt_is_same_combo.currentTextChanged.connect(self.update_nkt_is_same_combo)

        self.initition_combo_label = QLabel('Была ли инициация')
        self.initition_combo = QComboBox(self)
        self.initition_combo.addItems(['Нет', 'Да'])

        self.grid.addWidget(self.initition_combo_label, 30, 1)
        self.grid.addWidget(self.initition_combo, 31, 1)

        # self.grid.addWidget(self.count_of_nkt_extensions_label, 30, 4)
        # self.grid.addWidget(self.count_of_nkt_extensions_line, 31, 4)

        self.installation_pipe_perforator_combo.setCurrentIndex(1)

        self.initition_combo.currentTextChanged.connect(self.update_initition_combo)
        self.initition_combo.setCurrentIndex(1)
        self.deinstallation_perforation_combo.setCurrentIndex(1)
        self.equipment_audit_combo.setCurrentIndex(1)

    def update_initition_combo(self, index):
        if index == 'Нет':

            self.initition_perforator_text_label.setParent(None)
            self.initition_perforator_text_edit.setParent(None)

            self.initition_perforator_time_begin_label.setParent(None)
            self.initition_perforator_time_begin_date.setParent(None)

            self.initition_perforator_time_end_label.setParent(None)
            self.initition_perforator_time_end_date.setParent(None)

            self.initition_perforator_time_label.setParent(None)
            self.initition_perforator_time_line.setParent(None)

        else:

            self.initition_perforator_text_label = QLabel('Текст инициации перфорации')
            self.initition_perforator_text_edit = QLineEdit(self)

            self.initition_perforator_time_begin_label = QLabel('начало инициации')
            self.initition_perforator_time_begin_date = QDateTimeEdit(self)
            self.initition_perforator_time_begin_date.setDisplayFormat("dd.MM.yyyy HH:mm")
            self.initition_perforator_time_begin_date.setDateTime(self.date_work_str)

            self.initition_perforator_time_end_label = QLabel('Окончание инициации')
            self.initition_perforator_time_end_date = QDateTimeEdit(self)
            self.initition_perforator_time_end_date.setDisplayFormat("dd.MM.yyyy HH:mm")
            self.initition_perforator_time_end_date.setDateTime(self.date_work_str)

            self.initition_perforator_time_label = QLabel('затраченное время')
            self.initition_perforator_time_line = QLineEdit(self)
            self.initition_perforator_time_line.setValidator(self.validator_float)

            self.grid.addWidget(self.initition_perforator_time_begin_label, 30, 5)
            self.grid.addWidget(self.initition_perforator_time_begin_date, 31, 5)
            self.grid.addWidget(self.initition_perforator_time_end_label, 30, 6)
            self.grid.addWidget(self.initition_perforator_time_end_date, 31, 6)
            self.grid.addWidget(self.initition_perforator_time_label, 30, 7)
            self.grid.addWidget(self.initition_perforator_time_line, 31, 7)

            self.initition_perforator_time_end_date.dateTimeChanged.connect(self.update_date_of_raid)
            self.initition_perforator_time_begin_date.dateTimeChanged.connect(self.update_date_of_raid)

            self.grid.addWidget(self.initition_perforator_text_label, 30, 2)
            self.grid.addWidget(self.initition_perforator_text_edit, 31, 2)

    def update_deinstallation_perforation_combo(self, index):

        if index == 'Нет':
            self.deinstallation_perforation_text_label.setParent(None)
            self.deinstallation_perforation_text_line.setParent(None)
            self.deinstallation_perforation_time_label.setParent(None)
            self.deinstallation_perforation_time_line.setParent(None)
            self.deinstallation_perforation_time_end_label.setParent(None)
            self.deinstallation_perforation_time_end_date.setParent(None)
            self.deinstallation_perforation_time_begin_label.setParent(None)
            self.deinstallation_perforation_time_begin_date.setParent(None)
        else:
            self.deinstallation_perforation_text_label = QLabel('Текст демонтажа')
            self.deinstallation_perforation_text_line = QLineEdit(self)

            self.deinstallation_perforation_time_begin_label = QLabel('начало демонтажа')
            self.deinstallation_perforation_time_begin_date = QDateTimeEdit(self)
            self.deinstallation_perforation_time_begin_date.setDisplayFormat("dd.MM.yyyy HH:mm")
            self.deinstallation_perforation_time_begin_date.setDateTime(self.date_work_str)

            self.deinstallation_perforation_time_end_label = QLabel('Окончание демонтажа')
            self.deinstallation_perforation_time_end_date = QDateTimeEdit(self)
            self.deinstallation_perforation_time_end_date.setDisplayFormat("dd.MM.yyyy HH:mm")
            self.deinstallation_perforation_time_end_date.setDateTime(self.date_work_str)

            self.deinstallation_perforation_time_label = QLabel('затраченное время')
            self.deinstallation_perforation_time_line = QLineEdit(self)
            self.deinstallation_perforation_time_line.setValidator(self.validator_float)

            self.grid.addWidget(self.deinstallation_perforation_text_label, 50, 2)
            self.grid.addWidget(self.deinstallation_perforation_text_line, 51, 2)
            self.grid.addWidget(self.deinstallation_perforation_time_begin_label, 50, 3)
            self.grid.addWidget(self.deinstallation_perforation_time_begin_date, 51, 3)
            self.grid.addWidget(self.deinstallation_perforation_time_end_label, 50, 4)
            self.grid.addWidget(self.deinstallation_perforation_time_end_date, 51, 4)
            self.grid.addWidget(self.deinstallation_perforation_time_label, 50, 5)
            self.grid.addWidget(self.deinstallation_perforation_time_line, 51, 5)

            self.deinstallation_perforation_time_end_date.dateTimeChanged.connect(self.update_date_of_normalization)
            self.deinstallation_perforation_time_begin_date.dateTimeChanged.connect(self.update_date_of_normalization)

    def update_installation_pipe_perforator_combo(self, index):

        if index == 'Нет':
            self.installation_pipe_perforator_text_label.setParent(None)
            self.installation_pipe_perforator_text_line.setParent(None)
            self.installation_pipe_perforator_time_label.setParent(None)
            self.installation_pipe_perforator_time_line.setParent(None)
            self.installation_pipe_perforator_time_end_label.setParent(None)
            self.installation_pipe_perforator_time_end_date.setParent(None)
            self.installation_pipe_perforator_time_begin_label.setParent(None)
            self.installation_pipe_perforator_time_begin_date.setParent(None)
            self.volume_of_finishing_label.setParent(None)
            self.volume_of_finishing_line.setParent(None)
            self.volume_flush_line.setParent(None)

            self.volume_flush_label.setParent(None)

        else:
            self.installation_pipe_perforator_text_label = QLabel('Текст монтажа трубного перфоратора')
            self.installation_pipe_perforator_text_line = QLineEdit(self)
            self.installation_pipe_perforator_text_line.setText('ГИС - м/ж трубного перфоратора')

            self.installation_pipe_perforator_time_begin_label = QLabel('начало монтажа')
            self.installation_pipe_perforator_time_begin_date = QDateTimeEdit(self)
            self.installation_pipe_perforator_time_begin_date.setDisplayFormat("dd.MM.yyyy HH:mm")
            self.installation_pipe_perforator_time_begin_date.setDateTime(self.date_work_str)

            self.installation_pipe_perforator_time_end_label = QLabel('Окончание монтажа')
            self.installation_pipe_perforator_time_end_date = QDateTimeEdit(self)
            self.installation_pipe_perforator_time_end_date.setDisplayFormat("dd.MM.yyyy HH:mm")
            self.installation_pipe_perforator_time_end_date.setDateTime(self.date_work_str)

            self.installation_pipe_perforator_time_label = QLabel('затраченное время ')
            self.installation_pipe_perforator_time_line = QLineEdit(self)
            self.installation_pipe_perforator_time_line.setValidator(self.validator_float)

            self.grid.addWidget(self.installation_pipe_perforator_text_label, 12, 2)
            self.grid.addWidget(self.installation_pipe_perforator_text_line, 13, 2)

            self.grid.addWidget(self.installation_pipe_perforator_time_begin_label, 12, 5)
            self.grid.addWidget(self.installation_pipe_perforator_time_begin_date, 13, 5)
            self.grid.addWidget(self.installation_pipe_perforator_time_end_label, 12, 6)
            self.grid.addWidget(self.installation_pipe_perforator_time_end_date, 13, 6)
            self.grid.addWidget(self.installation_pipe_perforator_time_label, 12, 7)
            self.grid.addWidget(self.installation_pipe_perforator_time_line, 13, 7)

            self.installation_pipe_perforator_time_end_date.dateTimeChanged.connect(
                self.update_date_installation_pipe_perforator)
            self.installation_pipe_perforator_time_begin_date.dateTimeChanged.connect(
                self.update_date_installation_pipe_perforator)

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
        time_begin = self.deinstallation_perforation_time_begin_date.dateTime()
        time_end = self.deinstallation_perforation_time_end_date.dateTime()

        time_difference = self.calculate_date(time_begin, time_end)
        self.deinstallation_perforation_time_line.setText(str(time_difference))

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

    def update_date_of_raid(self):
        time_begin = self.initition_perforator_time_begin_date.dateTime()
        time_end = self.initition_perforator_time_end_date.dateTime()

        time_difference = self.calculate_date(time_begin, time_end)
        self.initition_perforator_time_line.setText(str(time_difference))

    def update_date_tubing_running(self):
        time_begin = self.complications_during_tubing_running_time_begin_date.dateTime()
        time_end = self.complications_during_tubing_running_time_end_date.dateTime()

        time_difference = self.calculate_date(time_begin, time_end)
        self.complications_during_tubing_running_time_line.setText(str(time_difference))

    def update_date_installation_pipe_perforator(self):
        time_begin = self.installation_pipe_perforator_time_begin_date.dateTime()
        time_end = self.installation_pipe_perforator_time_end_date.dateTime()

        time_difference = self.calculate_date(time_begin, time_end)
        self.installation_pipe_perforator_time_line.setText(str(time_difference))


class TabWidget(QTabWidget):
    def __init__(self):
        super().__init__()
        self.addTab(TabPage_SO_Timplate(self), 'Трубный перфоратор')


class PipePerforator(TemplateWork):
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

        self.dict_nkt = {}
        self.dict_nkt_up = {}

    def add_work(self):
        from main import MyWindow

        current_widget = self.tabWidget.currentWidget()

        self.date_work_line = current_widget.date_work_line.text()
        self.select_type_combo = current_widget.select_type_combo.currentText()
        if self.select_type_combo == '':
            return
        elif self.select_type_combo in ['НКТ']:
            self.coefficient_lifting = 1

            self.initition_perforator_text_edit = current_widget.initition_perforator_text_edit.text()

        self.nkt_is_same_combo = current_widget.nkt_is_same_combo.currentText()
        self.type_equipment = 'Перфоратор'
        self.equipment_audit_combo = current_widget.equipment_audit_combo.currentText()
        if self.equipment_audit_combo == 'Да':
            self.equipment_audit_text_line = current_widget.equipment_audit_text_line.text()
            if self.equipment_audit_text_line == '':
                QMessageBox.warning(self, 'Ошибка', 'Нужно внести текст ревизии')
                return

        read_data = self.read_nkt_up(current_widget)
        if read_data is None:
            return

        if self.nkt_is_same_combo == 'Нет':
            try:
                read_data = self.read_nkt_down(current_widget)
                if read_data is None:
                    return
            except Exception as e:
                QMessageBox.warning(self, 'Ошибка', f'Введены не все значения {e}')
                return
        else:
            self.dict_nkt_up = self.dict_nkt

        self.complications_of_failure_combo = current_widget.complications_of_failure_combo.currentText()
        self.complications_during_tubing_running_combo = current_widget.complications_during_tubing_running_combo.currentText()

        self.installation_pipe_perforator_combo = current_widget.installation_pipe_perforator_combo.currentText()

        self.complications_when_lifting_combo = current_widget.complications_when_lifting_combo.currentText()
        self.initition_combo = current_widget.initition_combo.currentText()
        if self.initition_combo == 'Да':

            # self.pressuar_gno_combo = current_widget.pressuar_gno_combo.currentText()

            self.initition_perforator_time_begin_date = \
                current_widget.initition_perforator_time_begin_date.dateTime().toPyDateTime()
            self.initition_perforator_time_begin_date = \
                self.change_string_in_date(self.initition_perforator_time_begin_date)

            self.initition_perforator_time_end_date = \
                current_widget.initition_perforator_time_end_date.dateTime().toPyDateTime()
            self.initition_perforator_time_end_date = \
                self.change_string_in_date(self.initition_perforator_time_end_date)

            if self.initition_perforator_time_end_date == self.initition_perforator_time_begin_date:
                QMessageBox.warning(self, 'Даты совпадают', 'Даты совпадают')
                return

            self.initition_perforator_time_line = current_widget.initition_perforator_time_line.text()
            if self.initition_perforator_time_line != '':
                self.initition_perforator_time_line = round(float(self.initition_perforator_time_line), 1)

            else:
                QMessageBox.warning(self, 'Ошибка', f'Не введены время осложнения при срыве ПШ')
                return

            if self.initition_perforator_time_line <= 0:
                QMessageBox.warning(self, 'Ошибка', f'Затраченное время при срыве ПШ не может быть отрицательным')
                return

        if self.installation_pipe_perforator_combo == 'Да':

            self.installation_pipe_perforator_text_line = current_widget.installation_pipe_perforator_text_line.text()
            self.installation_pipe_perforator_time_begin_date = \
                current_widget.installation_pipe_perforator_time_begin_date.dateTime().toPyDateTime()
            self.installation_pipe_perforator_time_begin_date = \
                self.change_string_in_date(self.installation_pipe_perforator_time_begin_date)

            self.installation_pipe_perforator_time_end_date = \
                current_widget.installation_pipe_perforator_time_end_date.dateTime().toPyDateTime()
            self.installation_pipe_perforator_time_end_date = \
                self.change_string_in_date(self.installation_pipe_perforator_time_end_date)

            if current_widget.installation_pipe_perforator_text_line.text() == self.installation_pipe_perforator_time_begin_date:
                QMessageBox.warning(self, 'Даты совпадают', 'Даты совпадают')
                return

            if self.installation_pipe_perforator_text_line == '':
                QMessageBox.warning(self, 'Ошибка', f'Не введены обьем растворителя')
                return

            self.installation_pipe_perforator_time_line = current_widget.installation_pipe_perforator_time_line.text()
            a = self.installation_pipe_perforator_time_line
            if self.installation_pipe_perforator_time_line != '':
                self.installation_pipe_perforator_time_line = round(float(self.installation_pipe_perforator_time_line),
                                                                    1)

            else:
                QMessageBox.warning(self, 'Ошибка', f'Не введены время реагирования')
                return

            if self.installation_pipe_perforator_time_line <= 0:
                QMessageBox.warning(self, 'Ошибка', f'Затраченное время при срыве ПШ не может быть отрицательным')
                return

        if self.complications_of_failure_combo == 'Да':
            read_data = self.read_complications_of_failure(current_widget)
            if read_data is None:
                return

        if self.complications_during_tubing_running_combo == 'Да':
            read_data = self.read_complications_during_tubing_running_combo(current_widget)
            if read_data is None:
                return

        self.deinstallation_perforation_combo = current_widget.deinstallation_perforation_combo.currentText()

        if self.deinstallation_perforation_combo == 'Да':
            self.deinstallation_perforation_text_line = current_widget.deinstallation_perforation_text_line.text()
            self.deinstallation_perforation_time_begin_date = \
                current_widget.deinstallation_perforation_time_begin_date.dateTime().toPyDateTime()
            self.deinstallation_perforation_time_begin_date = \
                self.change_string_in_date(self.deinstallation_perforation_time_begin_date)

            self.deinstallation_perforation_time_end_date = \
                current_widget.deinstallation_perforation_time_end_date.dateTime().toPyDateTime()
            self.deinstallation_perforation_time_end_date = \
                self.change_string_in_date(self.deinstallation_perforation_time_end_date)

            if current_widget.deinstallation_perforation_text_line.text() == self.deinstallation_perforation_time_begin_date:
                QMessageBox.warning(self, 'Даты совпадают', 'Даты совпадают')
                return

            if self.deinstallation_perforation_text_line == '':
                QMessageBox.warning(self, 'Ошибка', f'Не введены текст осложнения при срыве ПШ')
                return

            self.deinstallation_perforation_time_line = current_widget.deinstallation_perforation_time_line.text()
            if self.deinstallation_perforation_time_line != '':
                self.deinstallation_perforation_time_line = round(float(self.deinstallation_perforation_time_line), 1)

            else:
                QMessageBox.warning(self, 'Ошибка', f'Не введены время осложнения при срыве ПШ')
                return

            if self.deinstallation_perforation_time_line <= 0:
                QMessageBox.warning(self, 'Ошибка', f'Затраченное время при срыве ПШ не может быть отрицательным')
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

        work_list = self.raid_work()

        well_data.date_work = self.date_work_line

        self.populate_row(self.ins_ind, work_list, self.table_widget)
        well_data.pause = False
        self.close()

    def skm_work(self):
        work_list = []
        if self.raid_work_text_edit != '':
            skm_list = self.raid_interval_work()
            work_list.extend(skm_list)

        return work_list

    def raid_interval_work(self):
        work_list = []
        if self.raid_work_text_edit != '':
            work_list = TemplateWithoutSKM.installation_of_washing_equipment(self)
            raid_list = [
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'Вызов циркуляции (+)', None,
                 None, None, None,
                 None, None, None, None, None, None, None, None, '§301разд.1 п.72', None, 'раз', 1, '=5/60', 1,
                 '=V742*W742*X742', '=Y742-AA742-AB742-AC742-AD742', None, None, None, None, None],
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'райбирование', 'ПЗР при райберовании',
                 None, None,
                 None,
                 None, None, None, None, None, None, None, None, None, '§159,161р.1', None, 'шт', 1, 1, 1,
                 '=V743*W743*X743', '=Y743-AA743-AB743-AC743-AD743', None, None, None, None, None],
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'райбирование',
                 f'Райберование в инт. {self.raid_work_text_edit}м '
                 f'{self.raid_work_time_begin_date}-{self.raid_work_time_end_date}',
                 None,
                 None, None, None, None, None, 'что бурили:', self.initition_combo, 'АКТ№', None, None, None,
                 'факт', None, 'час',
                 self.raid_work_time_line, 1, 1,
                 '=V744*W744*X744', '=Y744-AA744-AB744-AC744-AD744', None, None, None, None, None],
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'Наращивание', None, None, None,
                 None, None,
                 None,
                 None, None, None, None, None, None, '§300разд.1', None, 'шт', self.count_of_nkt_extensions_line / 10,
                 0.17, 1, '=V745*W745*X745',
                 '=Y745-AA745-AB745-AC745-AD745', None, None, None, None, None],
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'Промывка', 'Промывка ', None, None,
                 None, None, None,
                 None, None, None, 'АКТ№', None, None, None, '§301разд.1', None, 'м3', self.volume_flush_line, 0.033,
                 1, '=V746*W746*X746',
                 '=Y746-AA746-AB746-AC746-AD746', None, None, None, None, None]]
            work_list.extend(raid_list)

        return work_list

    def raid_work(self):
        complications_of_failure_list = []
        complications_during_disassembly_list = []
        work_list = [
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'ГИС', 'Прочие',
             f'{self.installation_pipe_perforator_text_line} '
             f'{self.installation_pipe_perforator_time_begin_date}-{self.installation_pipe_perforator_time_end_date}',
             None, None, None, None,
             None, None, None, None, 'АКТ№', None, None, None, 'Факт', None, 'час',
             self.installation_pipe_perforator_text_line, 1, 1, '=V901*W901*X901',
             '=Y901-AA901-AB901-AC901-AD901', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', 'Перфоратор', 'ПЗР СПО трубного перфоратора', None, None, None,
             None, None, None, None, None, None, None, None, None, '§311разд.1', None, 'шт', 1, 0.9, 1,
             '=V902*W902*X902', '=Y902-AA902-AB902-AC902-AD902', None, None, None, None, None]]

        if len(self.dict_nkt) != 0:
            work_list.extend(TemplateWithoutSKM.descent_nkt_work(self))

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

        work_list.extend(self.initiation_perforator())

        work_list.extend(TemplateWithoutSKM.lifting_nkt(self))
        if self.deinstallation_perforation_combo == 'Да':
            work_list.extend(self.deinstallation_perforation_work())

        if self.equipment_audit_combo == 'Да':
            work_list.extend([
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
                 f'Ревизия:{self.equipment_audit_text_line}',
                 None, None, None, None, None, None, None, None, None, None, None,
                 None, 'факт', None, 'час', 0.5, 1, 1, '=V480*W480*X480', '=Y480-AA480-AB480-AC480-AD480', None,
                 None, None, None, None]]
            )

        return work_list

    def deinstallation_perforation_work(self):
        work_list = [
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'ГИС', 'Прочие',
             f'{self.deinstallation_perforation_text_line} '
             f'{self.deinstallation_perforation_time_begin_date}-{self.deinstallation_perforation_time_end_date}', None,
             None, None, None, None, None, None, None, 'АКТ№', None, None, None, 'Факт', None, 'час',
             self.deinstallation_perforation_time_line,
             1, 1, '=V919*W919*X919', '=Y919-AA9(19-AB919-AC919-AD919', None, None, None, None, None]]
        self.date_work_line = self.deinstallation_perforation_time_begin_date.split(' ')[0]
        return work_list

    def initiation_perforator(self):
        work_list = [
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'Д/ж, м/ж спайдера', None, None, None, None, None,
             None, None, None, None, None, None, None, '§185разд.1', None, 'час', 1, 0.14, 1, '=V908*W908*X908',
             '=Y908-AA908-AB908-AC908-AD908', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'Д/ж, м/ж спайдера', None, None, None, None, None,
             None, None, None, None, None, None, None, '§185разд.1', None, 'час', 1, 0.14, 1, '=V909*W909*X909',
             '=Y909-AA909-AB909-AC909-AD909', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'ГИС', 'ПВР', 'ГИС - ПВР (инициация)', None, None, None, None, None, None,
             None, None, 'АКТ№', None, None, None, 'Факт', None, 'час', 1, 1, 1, '=V910*W910*X910',
             '=Y910-AA910-AB910-AC910-AD910', None, None, None, None, None]]
        return work_list


sand_list = [
    ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', 'Перо,воронка', 'ПЗР СПО перо, воронка', None, None, None, None, None,
     None, None, None, None, None, None, None, '§176разд.1', None, 'шт', 1, 0.5, 1, '=V1161*W1161*X1161',
     '=Y1161-AA1161-AB1161-AC1161-AD1161', None, None, None, None, None],
    ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', 'Перо,воронка', 'Спуск НКТ компановка', None, None, None, None, None,
     '73мм', 1000,
     '=IF(AND(M1162/V1162>=ЦИКЛ!$V$9,M1162/V1162<=ЦИКЛ!$W$9),ЦИКЛ!$U$9,IF(AND(M1162/V1162>=ЦИКЛ!$V$10,M1162/V1162<=ЦИКЛ!$W$10),ЦИКЛ!$U$10,IF(AND(M1162/V1162>=ЦИКЛ!$V$11,M1162/V1162<=ЦИКЛ!$W$11),ЦИКЛ!$U$11,IF(AND(M1162/V1162>=ЦИКЛ!$V$12,M1162/V1162<=ЦИКЛ!$W$12),ЦИКЛ!$U$12,IF(AND(M1162/V1162>=ЦИКЛ!$V$13,M1162/V1162<=ЦИКЛ!$W$13),ЦИКЛ!$U$13,IF(AND(M1162/V1162>=ЦИКЛ!$V$14,M1162/V1162<=ЦИКЛ!$W$14),ЦИКЛ!$U$14))))))',
     None, None, None, None,
     '=IF($AD$8=ЦИКЛ!$A$4,ЦИКЛ!$P$4,IF($AD$8=ЦИКЛ!$A$7,ЦИКЛ!$P$7,IF($AD$8=ЦИКЛ!$A$10,ЦИКЛ!$P$7,IF($AD$8=ЦИКЛ!$A$52,ЦИКЛ!$P$52,IF($AD$8=ЦИКЛ!$A$70,ЦИКЛ!$P$70,IF($AD$8=ЦИКЛ!$A$88,ЦИКЛ!$P$88,IF($AD$8=ЦИКЛ!$A$106,ЦИКЛ!$P$106,IF($AD$8=ЦИКЛ!$A$133,ЦИКЛ!$P$133,IF($AD$8=ЦИКЛ!$Q$4,ЦИКЛ!$P$4,IF($AD$8=ЦИКЛ!$R$4,ЦИКЛ!$P$4))))))))))',
     None, 'шт', 100,
     '=IF(AND($AD$8=ЦИКЛ!$A$4,ЦИКЛ!$D$3=N1162,ЦИКЛ!$B$37=АВР!L1162),ЦИКЛ!$D$37,IF(AND($AD$8=ЦИКЛ!$A$4,ЦИКЛ!$E$3=N1162,ЦИКЛ!$B$37=АВР!L1162),ЦИКЛ!$E$37,IF(AND($AD$8=ЦИКЛ!$A$4,ЦИКЛ!$F$3=N1162,ЦИКЛ!$B$37=АВР!L1162),ЦИКЛ!$F$37,IF(AND($AD$8=ЦИКЛ!$A$4,ЦИКЛ!$G$3=N1162,ЦИКЛ!$B$37=АВР!L1162),ЦИКЛ!$G$37,IF(AND($AD$8=ЦИКЛ!$A$4,ЦИКЛ!$H$3=N1162,ЦИКЛ!$B$37=АВР!L1162),ЦИКЛ!$H$37,IF(AND($AD$8=ЦИКЛ!$A$4,ЦИКЛ!$I$3=N1162,ЦИКЛ!$B$37=АВР!L1162),ЦИКЛ!$I$37,IF(AND($AD$8=ЦИКЛ!$Q$4,ЦИКЛ!$D$3=N1162,ЦИКЛ!$B$37=АВР!L1162),ЦИКЛ!$D$37,IF(AND($AD$8=ЦИКЛ!$Q$4,ЦИКЛ!$E$3=N1162,ЦИКЛ!$B$37=АВР!L1162),ЦИКЛ!$E$37,IF(AND($AD$8=ЦИКЛ!$Q$4,ЦИКЛ!$F$3=N1162,ЦИКЛ!$B$37=АВР!L1162),ЦИКЛ!$F$37,IF(AND($AD$8=ЦИКЛ!$Q$4,ЦИКЛ!$G$3=N1162,ЦИКЛ!$B$37=АВР!L1162),ЦИКЛ!$G$37,IF(AND($AD$8=ЦИКЛ!$Q$4,ЦИКЛ!$H$3=N1162,ЦИКЛ!$B$37=АВР!L1162),ЦИКЛ!$H$37,IF(AND($AD$8=ЦИКЛ!$Q$4,ЦИКЛ!$I$3=N1162,ЦИКЛ!$B$37=АВР!L1162),ЦИКЛ!$I$37,IF(AND($AD$8=ЦИКЛ!$R$4,ЦИКЛ!$D$3=N1162,ЦИКЛ!$B$37=АВР!L1162),ЦИКЛ!$D$37,IF(AND($AD$8=ЦИКЛ!$R$4,ЦИКЛ!$E$3=N1162,ЦИКЛ!$B$37=АВР!L1162),ЦИКЛ!$E$37,IF(AND($AD$8=ЦИКЛ!$R$4,ЦИКЛ!$F$3=N1162,ЦИКЛ!$B$37=АВР!L1162),ЦИКЛ!$F$37,IF(AND($AD$8=ЦИКЛ!$R$4,ЦИКЛ!$G$3=N1162,ЦИКЛ!$B$37=АВР!L1162),ЦИКЛ!$G$37,IF(AND($AD$8=ЦИКЛ!$R$4,ЦИКЛ!$H$3=N1162,ЦИКЛ!$B$37=АВР!L1162),ЦИКЛ!$H$37,IF(AND($AD$8=ЦИКЛ!$R$4,ЦИКЛ!$I$3=N1162,ЦИКЛ!$B$37=АВР!L1162),ЦИКЛ!$I$37,IF(AND($AD$8=ЦИКЛ!$A$7,ЦИКЛ!$D$3=N1162,ЦИКЛ!$B$37=АВР!L1162),ЦИКЛ!$D$37,IF(AND($AD$8=ЦИКЛ!$A$7,ЦИКЛ!$E$3=N1162,ЦИКЛ!$B$37=АВР!L1162),ЦИКЛ!$E$37,IF(AND($AD$8=ЦИКЛ!$A$7,ЦИКЛ!$F$3=N1162,ЦИКЛ!$B$37=АВР!L1162),ЦИКЛ!$F$37,IF(AND($AD$8=ЦИКЛ!$A$7,ЦИКЛ!$G$3=N1162,ЦИКЛ!$B$37=АВР!L1162),ЦИКЛ!$G$37,IF(AND($AD$8=ЦИКЛ!$A$7,ЦИКЛ!$H$3=N1162,ЦИКЛ!$B$37=АВР!L1162),ЦИКЛ!$H$37,IF(AND($AD$8=ЦИКЛ!$A$7,ЦИКЛ!$I$3=N1162,ЦИКЛ!$B$37=АВР!L1162),ЦИКЛ!$I$37,IF(AND($AD$8=ЦИКЛ!$A$10,ЦИКЛ!$D$3=N1162,ЦИКЛ!$B$37=АВР!L1162),ЦИКЛ!$D$37,IF(AND($AD$8=ЦИКЛ!$A$10,ЦИКЛ!$E$3=N1162,ЦИКЛ!$B$37=АВР!L1162),ЦИКЛ!$E$37,IF(AND($AD$8=ЦИКЛ!$A$10,ЦИКЛ!$F$3=N1162,ЦИКЛ!$B$37=АВР!L1162),ЦИКЛ!$F$37,IF(AND($AD$8=ЦИКЛ!$A$10,ЦИКЛ!$G$3=N1162,ЦИКЛ!$B$37=АВР!L1162),ЦИКЛ!$G$37,IF(AND($AD$8=ЦИКЛ!$A$10,ЦИКЛ!$H$3=N1162,ЦИКЛ!$B$37=АВР!L1162),ЦИКЛ!$H$37,IF(AND($AD$8=ЦИКЛ!$A$10,ЦИКЛ!$I$3=N1162,ЦИКЛ!$B$37=АВР!L1162),ЦИКЛ!$I$37,IF(AND($AD$8=ЦИКЛ!$A$52,ЦИКЛ!$D$3=N1162,ЦИКЛ!$B$37=АВР!L1162),ЦИКЛ!$D$63,IF(AND($AD$8=ЦИКЛ!$A$52,ЦИКЛ!$E$3=N1162,ЦИКЛ!$B$37=АВР!L1162),ЦИКЛ!$E$63,IF(AND($AD$8=ЦИКЛ!$A$52,ЦИКЛ!$F$3=N1162,ЦИКЛ!$B$37=АВР!L1162),ЦИКЛ!$F$63,IF(AND($AD$8=ЦИКЛ!$A$52,ЦИКЛ!$G$3=N1162,ЦИКЛ!$B$37=АВР!L1162),ЦИКЛ!$G$63,IF(AND($AD$8=ЦИКЛ!$A$52,ЦИКЛ!$H$3=N1162,ЦИКЛ!$B$37=АВР!L1162),ЦИКЛ!$H$63,IF(AND($AD$8=ЦИКЛ!$A$52,ЦИКЛ!$I$3=N1162,ЦИКЛ!$B$37=АВР!L1162),ЦИКЛ!$I$63,IF(AND($AD$8=ЦИКЛ!$A$70,ЦИКЛ!$D$3=N1162,ЦИКЛ!$B$37=АВР!L1162),ЦИКЛ!$D$81,IF(AND($AD$8=ЦИКЛ!$A$70,ЦИКЛ!$E$3=N1162,ЦИКЛ!$B$37=АВР!L1162),ЦИКЛ!$E$81,IF(AND($AD$8=ЦИКЛ!$A$70,ЦИКЛ!$F$3=N1162,ЦИКЛ!$B$37=АВР!L1162),ЦИКЛ!$F$81,IF(AND($AD$8=ЦИКЛ!$A$70,ЦИКЛ!$G$3=N1162,ЦИКЛ!$B$37=АВР!L1162),ЦИКЛ!$G$81,IF(AND($AD$8=ЦИКЛ!$A$70,ЦИКЛ!$H$3=N1162,ЦИКЛ!$B$37=АВР!L1162),ЦИКЛ!$H$81,IF(AND($AD$8=ЦИКЛ!$A$70,ЦИКЛ!$I$3=N1162,ЦИКЛ!$B$37=АВР!L1162),ЦИКЛ!$I$81,IF(AND($AD$8=ЦИКЛ!$A$88,ЦИКЛ!$D$3=N1162,ЦИКЛ!$B$37=АВР!L1162),ЦИКЛ!$D$99,IF(AND($AD$8=ЦИКЛ!$A$88,ЦИКЛ!$E$3=N1162,ЦИКЛ!$B$37=АВР!L1162),ЦИКЛ!$E$99,IF(AND($AD$8=ЦИКЛ!$A$88,ЦИКЛ!$F$3=N1162,ЦИКЛ!$B$37=АВР!L1162),ЦИКЛ!$F$99,IF(AND($AD$8=ЦИКЛ!$A$88,ЦИКЛ!$G$3=N1162,ЦИКЛ!$B$37=АВР!L1162),ЦИКЛ!$G$99,IF(AND($AD$8=ЦИКЛ!$A$88,ЦИКЛ!$H$3=N1162,ЦИКЛ!$B$37=АВР!L1162),ЦИКЛ!$H$99,IF(AND($AD$8=ЦИКЛ!$A$88,ЦИКЛ!$I$3=N1162,ЦИКЛ!$B$37=АВР!L1162),ЦИКЛ!$I$99,IF(AND($AD$8=ЦИКЛ!$A$106,ЦИКЛ!$D$3=N1162,ЦИКЛ!$B$37=АВР!L1162),ЦИКЛ!$D$120,IF(AND($AD$8=ЦИКЛ!$A$106,ЦИКЛ!$E$3=N1162,ЦИКЛ!$B$37=АВР!L1162),ЦИКЛ!$E$120,IF(AND($AD$8=ЦИКЛ!$A$106,ЦИКЛ!$F$3=N1162,ЦИКЛ!$B$37=АВР!L1162),ЦИКЛ!$F$120,IF(AND($AD$8=ЦИКЛ!$A$106,ЦИКЛ!$G$3=N1162,ЦИКЛ!$B$37=АВР!L1162),ЦИКЛ!$G$120,IF(AND($AD$8=ЦИКЛ!$A$106,ЦИКЛ!$H$3=N1162,ЦИКЛ!$B$37=АВР!L1162),ЦИКЛ!$H$120,IF(AND($AD$8=ЦИКЛ!$A$106,ЦИКЛ!$I$3=N1162,ЦИКЛ!$B$37=АВР!L1162),ЦИКЛ!$I$120,IF(AND($AD$8=ЦИКЛ!$A$128,ЦИКЛ!$D$3=N1162,ЦИКЛ!$B$37=АВР!L1162),ЦИКЛ!$D$142,IF(AND($AD$8=ЦИКЛ!$A$128,ЦИКЛ!$E$3=N1162,ЦИКЛ!$B$37=АВР!L1162),ЦИКЛ!$E$142,IF(AND($AD$8=ЦИКЛ!$A$128,ЦИКЛ!$F$3=N1162,ЦИКЛ!$B$37=АВР!L1162),ЦИКЛ!$F$142,IF(AND($AD$8=ЦИКЛ!$A$128,ЦИКЛ!$G$3=N1162,ЦИКЛ!$B$37=АВР!L1162),ЦИКЛ!$G$142,IF(AND($AD$8=ЦИКЛ!$A$128,ЦИКЛ!$H$3=N1162,ЦИКЛ!$B$37=АВР!L1162),ЦИКЛ!$H$142,IF(AND(АВР!$AD$8=ЦИКЛ!$A$128,ЦИКЛ!$I$3=N1162,ЦИКЛ!$B$37=АВР!L1162),ЦИКЛ!$I$142))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))',
     1, '=V1162*W1162*X1162', '=Y1162-AA1162-AB1162-AC1162-AD1162', None, None, None, None, None],
    ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', 'Перо,воронка', 'Навернуть/отвернуть предохранительное кольцо', None, None,
     None, None, None, None, None, None, None, None, None, None, '§300разд.1', None, 'шт', '=SUM(V1162)', 0.003, 1,
     '=V1163*W1163*X1163', '=Y1163-AA1163-AB1163-AC1163-AD1163', None, None, None, None, None],
    ['=ROW()-ROW($A$56)', None, None, 'спо', 'Перо,воронка', 'Замер НКТ ', None, None, None, None, None, None, None,
     None, None, None, None, None, '§47разд.1', None, 'шт', '=V1163', '=0.5/60', 1, '=V1164*W1164*X1164',
     '=Y1164-AA1164-AB1164-AC1164-AD1164', None, None, None, None, None],
    ['=ROW()-ROW($A$56)', 'спуск 73мм', None, 'спо', 'Перо,воронка', 'Подкатывание труб с 201 трубы ', None, None, None,
     None, None, None, None, None, None, None, None, None, '§40разд.1', None, 'шт', '=V1163-201', 0.008, 1,
     '=V1165*W1165*X1165', '=Y1165-AA1165-AB1165-AC1165-AD1165', None, None, None, None, None],
    ['=ROW()-ROW($A$56)', None, None, 'спо', 'Перо,воронка', 'Осложнение при спуске НКТ-вытеснение (ВРЕМЯ)', None, None,
     None, None, None, None, 'Объем', 0, 'АКТ№', None, None, None, 'факт', None, 'час', 0, 1, 1, '=V1166*W1166*X1166',
     '=Y1166-AA1166-AB1166-AC1166-AD1166', None, None, None, None, None],
    ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'кварцевый песок', 'ПЗР+Отсыпка песком в инт. в объеме 583л',
     None, None, None, None, None, 'Исполнитель', 'ПО ТКРС', None, 'АКТ№', 'ПЕСОК', 'Песок кварцевый фр.1-2', None,
     '§276разд.1', None, 'м', '=M1162', 51, 1,
     '=((1*W1167)+5+(((2.6/400)*0.75)*V1167)+2+1+(1.6*W1167)+(((2.6/400)*0.75)*V1167)+1+39+27)/60',
     '=Y1167-AA1167-AB1167-AC1167-AD1167', None, None, None, None, None],
    ['=ROW()-ROW($A$56)', None, None, 'Тех.операции', 'кварцевый песок', 'Ожидание оседание песка (', None, None, None,
     None, None, None, None, None, 'АКТ№', None, None, None, 'простои', 'Тех. ожидание', 'час', 4, 1, 1,
     '=V1168*W1168*X1168', '=Y1168-AA1168-AB1168-AC1168-AD1168', None, None, None, None, None],
    ['=ROW()-ROW($A$56)', None, None, 'Тех.операции', None, 'Определение кровли песчанного моста на гл. 1195м', None,
     None, None, None, None, None, None, None, 'АКТ№', None, None, None, '§289разд.1', None, 'раз', 1, 0.17, 1,
     '=V1169*W1169*X1169', '=Y1169-AA1169-AB1169-AC1169-AD1169', None, None, None, None, None],
    ['=ROW()-ROW($A$56)', None, None, 'Тех.операции', None, 'Опрессовка пес.м. на Р-100атм(+)', None, None, None, None,
     None, None, None, None, 'АКТ№', None, None, None, '§148разд.1', None, 'раз', 1, 0.58, 1, '=V1170*W1170*X1170',
     '=Y1170-AA1170-AB1170-AC1170-AD1170', None, None, None, None, None],
    ['=ROW()-ROW($A$56)', None, None, 'Тех.операции', 'Промывка', 'ПР  перед вымывом излишков пропанта', None, None,
     None, None, None, None, None, None, None, None, None, None, '§285разд.1', None, 'раз', 1, 0.15, 1,
     '=V1171*W1171*X1171', '=Y1171-AA1171-AB1171-AC1171-AD1171', None, None, None, None, None],
    ['=ROW()-ROW($A$56)', None, None, 'Тех.операции', 'Промывка', 'Промывка ', None, None, None, None, None, None, None,
     None, 'АКТ№', None, None, None, '§301разд.1', None, 'м3', 27, 0.033, 1, '=V1172*W1172*X1172',
     '=Y1172-AA1172-AB1172-AC1172-AD1172', None, None, None, None, None],
    ['=ROW()-ROW($A$56)', None, None, 'Тех.операции', 'Промывка', 'Разобрать промывочное оборудование', None, None,
     None, None, None, None, None, None, None, None, None, None, '§161разд.1', None, 'раз', 1, 0.23, 1,
     '=V1173*W1173*X1173', '=Y1173-AA1173-AB1173-AC1173-AD1173', None, None, None, None, None],
    ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', 'Перо,воронка', 'Подъем НКТ  3 скорость', None, None, None, None, '73мм',
     1000,
     '=IF(AND(L1174/V1174>=ЦИКЛ!$V$9,L1174/V1174<=ЦИКЛ!$W$9),ЦИКЛ!$U$9,IF(AND(L1174/V1174>=ЦИКЛ!$V$10,L1174/V1174<=ЦИКЛ!$W$10),ЦИКЛ!$U$10,IF(AND(L1174/V1174>=ЦИКЛ!$V$11,L1174/V1174<=ЦИКЛ!$W$11),ЦИКЛ!$U$11,IF(AND(L1174/V1174>=ЦИКЛ!$V$12,L1174/V1174<=ЦИКЛ!$W$12),ЦИКЛ!$U$12,IF(AND(L1174/V1174>=ЦИКЛ!$V$13,L1174/V1174<=ЦИКЛ!$W$13),ЦИКЛ!$U$13,IF(AND(L1174/V1174>=ЦИКЛ!$V$14,L1174/V1174<=ЦИКЛ!$W$14),ЦИКЛ!$U$14))))))',
     '=IF(AND(АВР!$AD$8=ЦИКЛ!$A$6,ЦИКЛ!$D$3=M1174),ЦИКЛ!$J$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$6,ЦИКЛ!$E$3=M1174),ЦИКЛ!$K$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$6,ЦИКЛ!$F$3=M1174),ЦИКЛ!$L$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$6,ЦИКЛ!$G$3=M1174),ЦИКЛ!$M$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$6,ЦИКЛ!$N$3=M1174),ЦИКЛ!$H$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$6,ЦИКЛ!$I$3=M1174),ЦИКЛ!$O$30,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$6,ЦИКЛ!$D$3=M1174),ЦИКЛ!$J$30,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$6,ЦИКЛ!$E$3=M1174),ЦИКЛ!$K$30,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$6,ЦИКЛ!$F$3=M1174),ЦИКЛ!$L$30,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$6,ЦИКЛ!$G$3=M1174),ЦИКЛ!$M$30,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$6,ЦИКЛ!$H$3=M1174),ЦИКЛ!$N$30,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$6,ЦИКЛ!$I$3=M1174),ЦИКЛ!$O$30,IF(AND(АВР!$AD$8=ЦИКЛ!$R$6,ЦИКЛ!$D$3=M1174),ЦИКЛ!$J$30,IF(AND(АВР!$AD$8=ЦИКЛ!$R$6,ЦИКЛ!$E$3=M1174),ЦИКЛ!$K$30,IF(AND(АВР!$AD$8=ЦИКЛ!$R$6,ЦИКЛ!$F$3=M1174),ЦИКЛ!$L$30,IF(AND(АВР!$AD$8=ЦИКЛ!$R$6,ЦИКЛ!$G$3=M1174),ЦИКЛ!$M$30,IF(AND(АВР!$AD$8=ЦИКЛ!$R$6,ЦИКЛ!$H$3=M1174),ЦИКЛ!$N$30,IF(AND(АВР!$AD$8=ЦИКЛ!$R$6,ЦИКЛ!$I$3=M1174),ЦИКЛ!$O$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$9,ЦИКЛ!$D$3=M1174),ЦИКЛ!$J$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$9,ЦИКЛ!$E$3=M1174),ЦИКЛ!$K$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$9,ЦИКЛ!$F$3=M1174),ЦИКЛ!$L$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$9,ЦИКЛ!$G$3=M1174),ЦИКЛ!$M$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$9,ЦИКЛ!$H$3=M1174),ЦИКЛ!$N$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$9,ЦИКЛ!$I$3=M1174),ЦИКЛ!$O$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$12,ЦИКЛ!$D$3=M1174),ЦИКЛ!$J$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$12,ЦИКЛ!$E$3=M1174),ЦИКЛ!$K$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$12,ЦИКЛ!$F$3=M1174),ЦИКЛ!$L$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$12,ЦИКЛ!$G$3=M1174),ЦИКЛ!$M$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$12,ЦИКЛ!$H$3=M1174),ЦИКЛ!$N$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$12,ЦИКЛ!$I$3=M1174),ЦИКЛ!$O$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$54,ЦИКЛ!$D$3=M1174),ЦИКЛ!$J$62,IF(AND(АВР!$AD$8=ЦИКЛ!$A$54,ЦИКЛ!$E$3=M1174),ЦИКЛ!$K$62,IF(AND(АВР!$AD$8=ЦИКЛ!$A$54,ЦИКЛ!$F$3=M1174),ЦИКЛ!$L$62,IF(AND(АВР!$AD$8=ЦИКЛ!$A$54,ЦИКЛ!$G$3=M1174),ЦИКЛ!$M$62,IF(AND(АВР!$AD$8=ЦИКЛ!$A$54,ЦИКЛ!$H$3=M1174),ЦИКЛ!$N$62,IF(AND(АВР!$AD$8=ЦИКЛ!$A$54,ЦИКЛ!$I$3=M1174),ЦИКЛ!$O$62,IF(AND(АВР!$AD$8=ЦИКЛ!$A$72,ЦИКЛ!$D$3=M1174),ЦИКЛ!$J$80,IF(AND(АВР!$AD$8=ЦИКЛ!$A$72,ЦИКЛ!$E$3=M1174),ЦИКЛ!$K$80,IF(AND(АВР!$AD$8=ЦИКЛ!$A$72,ЦИКЛ!$F$3=M1174),ЦИКЛ!$L$80,IF(AND(АВР!$AD$8=ЦИКЛ!$A$72,ЦИКЛ!$G$3=M1174),ЦИКЛ!$M$80,IF(AND(АВР!$AD$8=ЦИКЛ!$A$72,ЦИКЛ!$H$3=M1174),ЦИКЛ!$N$80,IF(AND(АВР!$AD$8=ЦИКЛ!$A$72,ЦИКЛ!$I$3=M1174),ЦИКЛ!$O$80,IF(AND(АВР!$AD$8=ЦИКЛ!$A$90,ЦИКЛ!$D$3=M1174),ЦИКЛ!$J$98,IF(AND(АВР!$AD$8=ЦИКЛ!$A$90,ЦИКЛ!$E$3=M1174),ЦИКЛ!$K$98,IF(AND(АВР!$AD$8=ЦИКЛ!$A$90,ЦИКЛ!$F$3=M1174),ЦИКЛ!$L$98,IF(AND(АВР!$AD$8=ЦИКЛ!$A$90,ЦИКЛ!$G$3=M1174),ЦИКЛ!$M$98,IF(AND(АВР!$AD$8=ЦИКЛ!$A$90,ЦИКЛ!$H$3=M1174),ЦИКЛ!$N$98,IF(AND(АВР!$AD$8=ЦИКЛ!$A$90,ЦИКЛ!$I$3=M1174),ЦИКЛ!$O$98,IF(AND(АВР!$AD$8=ЦИКЛ!$A$108,ЦИКЛ!$D$3=M1174),ЦИКЛ!$J$118,IF(AND(АВР!$AD$8=ЦИКЛ!$A$108,ЦИКЛ!$E$3=M1174),ЦИКЛ!$K$118,IF(AND(АВР!$AD$8=ЦИКЛ!$A$108,ЦИКЛ!$F$3=M1174),ЦИКЛ!$L$118,IF(AND(АВР!$AD$8=ЦИКЛ!$A$108,ЦИКЛ!$G$3=M1174),ЦИКЛ!$M$118,IF(AND(АВР!$AD$8=ЦИКЛ!$A$108,ЦИКЛ!$H$3=M1174),ЦИКЛ!$N$118,IF(AND(АВР!$AD$8=ЦИКЛ!$A$108,ЦИКЛ!$I$3=M1174),ЦИКЛ!$O$118,IF(AND(АВР!$AD$8=ЦИКЛ!$A$130,ЦИКЛ!$D$3=M1174),ЦИКЛ!$J$140,IF(AND(АВР!$AD$8=ЦИКЛ!$A$130,ЦИКЛ!$E$3=M1174),ЦИКЛ!$K$140,IF(AND(АВР!$AD$8=ЦИКЛ!$A$130,ЦИКЛ!$F$3=M1174),ЦИКЛ!$L$140,IF(AND(АВР!$AD$8=ЦИКЛ!$A$130,ЦИКЛ!$G$3=M1174),ЦИКЛ!$M$140,IF(AND(АВР!$AD$8=ЦИКЛ!$A$130,ЦИКЛ!$H$3=M1174),ЦИКЛ!$N$140,IF(AND(АВР!$AD$8=ЦИКЛ!$A$130,ЦИКЛ!$I$3=M1174),ЦИКЛ!$O$140))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))',
     None, None, None, None,
     '=IF($AD$8=ЦИКЛ!$A$4,ЦИКЛ!$P$4,IF($AD$8=ЦИКЛ!$A$7,ЦИКЛ!$P$7,IF($AD$8=ЦИКЛ!$A$10,ЦИКЛ!$P$7,IF($AD$8=ЦИКЛ!$A$52,ЦИКЛ!$P$52,IF($AD$8=ЦИКЛ!$A$70,ЦИКЛ!$P$70,IF($AD$8=ЦИКЛ!$A$88,ЦИКЛ!$P$88,IF($AD$8=ЦИКЛ!$A$106,ЦИКЛ!$P$106,IF($AD$8=ЦИКЛ!$A$133,ЦИКЛ!$P$133,IF($AD$8=ЦИКЛ!$Q$4,ЦИКЛ!$P$4,IF($AD$8=ЦИКЛ!$R$4,ЦИКЛ!$P$4))))))))))',
     None, 'шт', 100,
     '=IF(AND(АВР!$AD$8=ЦИКЛ!$A$6,ЦИКЛ!$D$3=M1174,ЦИКЛ!$B$37=АВР!K1174),ЦИКЛ!$D$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$6,ЦИКЛ!$E$3=M1174,ЦИКЛ!$B$37=АВР!K1174),ЦИКЛ!$E$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$6,ЦИКЛ!$F$3=M1174,ЦИКЛ!$B$37=АВР!K1174),ЦИКЛ!$F$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$6,ЦИКЛ!$G$3=M1174,ЦИКЛ!$B$37=АВР!K1174),ЦИКЛ!$G$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$6,ЦИКЛ!$H$3=M1174,ЦИКЛ!$B$37=АВР!K1174),ЦИКЛ!$H$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$6,ЦИКЛ!$I$3=M1174,ЦИКЛ!$B$37=АВР!K1174),ЦИКЛ!$I$30,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$6,ЦИКЛ!$D$3=M1174,ЦИКЛ!$B$37=АВР!K1174),ЦИКЛ!$D$30,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$6,ЦИКЛ!$E$3=M1174,ЦИКЛ!$B$37=АВР!K1174),ЦИКЛ!$E$30,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$6,ЦИКЛ!$F$3=M1174,ЦИКЛ!$B$37=АВР!K1174),ЦИКЛ!$F$30,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$6,ЦИКЛ!$G$3=M1174,ЦИКЛ!$B$37=АВР!K1174),ЦИКЛ!$G$30,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$6,ЦИКЛ!$H$3=M1174,ЦИКЛ!$B$37=АВР!K1174),ЦИКЛ!$H$30,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$6,ЦИКЛ!$I$3=M1174,ЦИКЛ!$B$37=АВР!K1174),ЦИКЛ!$I$30,IF(AND(АВР!$AD$8=ЦИКЛ!$R$6,ЦИКЛ!$D$3=M1174,ЦИКЛ!$B$37=АВР!K1174),ЦИКЛ!$D$30,IF(AND(АВР!$AD$8=ЦИКЛ!$R$6,ЦИКЛ!$E$3=M1174,ЦИКЛ!$B$37=АВР!K1174),ЦИКЛ!$E$30,IF(AND(АВР!$AD$8=ЦИКЛ!$R$6,ЦИКЛ!$F$3=M1174,ЦИКЛ!$B$37=АВР!K1174),ЦИКЛ!$F$30,IF(AND(АВР!$AD$8=ЦИКЛ!$R$6,ЦИКЛ!$G$3=M1174,ЦИКЛ!$B$37=АВР!K1174),ЦИКЛ!$G$30,IF(AND(АВР!$AD$8=ЦИКЛ!$R$6,ЦИКЛ!$H$3=M1174,ЦИКЛ!$B$37=АВР!K1174),ЦИКЛ!$H$30,IF(AND(АВР!$AD$8=ЦИКЛ!$R$6,ЦИКЛ!$I$3=M1174,ЦИКЛ!$B$37=АВР!K1174),ЦИКЛ!$I$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$9,ЦИКЛ!$D$3=M1174,ЦИКЛ!$B$37=АВР!K1174),ЦИКЛ!$D$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$9,ЦИКЛ!$E$3=M1174,ЦИКЛ!$B$37=АВР!K1174),ЦИКЛ!$E$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$9,ЦИКЛ!$F$3=M1174,ЦИКЛ!$B$37=АВР!K1174),ЦИКЛ!$F$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$21,ЦИКЛ!$G$3=M1174,ЦИКЛ!$B$37=АВР!K1174),ЦИКЛ!$G$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$9,ЦИКЛ!$H$3=M1174,ЦИКЛ!$B$37=АВР!K1174),ЦИКЛ!$H$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$9,ЦИКЛ!$I$3=M1174,ЦИКЛ!$B$37=АВР!K1174),ЦИКЛ!$I$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$12,ЦИКЛ!$D$3=M1174,ЦИКЛ!$B$37=АВР!K1174),ЦИКЛ!$D$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$12,ЦИКЛ!$E$3=M1174,ЦИКЛ!$B$37=АВР!K1174),ЦИКЛ!$E$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$12,ЦИКЛ!$F$3=M1174,ЦИКЛ!$B$37=АВР!K1174),ЦИКЛ!$F$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$12,ЦИКЛ!$G$3=M1174,ЦИКЛ!$B$37=АВР!K1174),ЦИКЛ!$G$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$12,ЦИКЛ!$H$3=M1174,ЦИКЛ!$B$37=АВР!K1174),ЦИКЛ!$H$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$12,ЦИКЛ!$I$3=M1174,ЦИКЛ!$B$37=АВР!K1174),ЦИКЛ!$I$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$54,ЦИКЛ!$D$3=M1174,ЦИКЛ!$B$37=АВР!K1174),ЦИКЛ!$D$62,IF(AND(АВР!$AD$8=ЦИКЛ!$A$54,ЦИКЛ!$E$3=M1174,ЦИКЛ!$B$37=АВР!K1174),ЦИКЛ!$E$62,IF(AND(АВР!$AD$8=ЦИКЛ!$A$54,ЦИКЛ!$F$3=M1174,ЦИКЛ!$B$37=АВР!K1174),ЦИКЛ!$F$62,IF(AND(АВР!$AD$8=ЦИКЛ!$A$54,ЦИКЛ!$G$3=M1174,ЦИКЛ!$B$37=АВР!K1174),ЦИКЛ!$G$62,IF(AND(АВР!$AD$8=ЦИКЛ!$A$54,ЦИКЛ!$H$3=M1174,ЦИКЛ!$B$37=АВР!K1174),ЦИКЛ!$H$62,IF(AND(АВР!$AD$8=ЦИКЛ!$A$54,ЦИКЛ!$I$3=M1174,ЦИКЛ!$B$37=АВР!K1174),ЦИКЛ!$I$62,IF(AND(АВР!$AD$8=ЦИКЛ!$A$72,ЦИКЛ!$D$3=M1174,ЦИКЛ!$B$37=АВР!K1174),ЦИКЛ!$D$80,IF(AND(АВР!$AD$8=ЦИКЛ!$A$72,ЦИКЛ!$E$3=M1174,ЦИКЛ!$B$37=АВР!K1174),ЦИКЛ!$E$80,IF(AND(АВР!$AD$8=ЦИКЛ!$A$72,ЦИКЛ!$F$3=M1174,ЦИКЛ!$B$37=АВР!K1174),ЦИКЛ!$F$80,IF(AND(АВР!$AD$8=ЦИКЛ!$A$72,ЦИКЛ!$G$3=M1174,ЦИКЛ!$B$37=АВР!K1174),ЦИКЛ!$G$80,IF(AND(АВР!$AD$8=ЦИКЛ!$A$72,ЦИКЛ!$H$3=M1174,ЦИКЛ!$B$37=АВР!K1174),ЦИКЛ!$H$80,IF(AND(АВР!$AD$8=ЦИКЛ!$A$72,ЦИКЛ!$I$3=M1174,ЦИКЛ!$B$37=АВР!K1174),ЦИКЛ!$I$80,IF(AND(АВР!$AD$8=ЦИКЛ!$A$90,ЦИКЛ!$D$3=M1174,ЦИКЛ!$B$37=АВР!K1174),ЦИКЛ!$D$98,IF(AND(АВР!$AD$8=ЦИКЛ!$A$90,ЦИКЛ!$E$3=M1174,ЦИКЛ!$B$37=АВР!K1174),ЦИКЛ!$E$98,IF(AND(АВР!$AD$8=ЦИКЛ!$A$90,ЦИКЛ!$F$3=M1174,ЦИКЛ!$B$37=АВР!K1174),ЦИКЛ!$F$98,IF(AND(АВР!$AD$8=ЦИКЛ!$A$90,ЦИКЛ!$G$3=M1174,ЦИКЛ!$B$37=АВР!K1174),ЦИКЛ!$G$98,IF(AND(АВР!$AD$8=ЦИКЛ!$A$90,ЦИКЛ!$H$3=M1174,ЦИКЛ!$B$37=АВР!K1174),ЦИКЛ!$H$98,IF(AND(АВР!$AD$8=ЦИКЛ!$A$90,ЦИКЛ!$I$3=M1174,ЦИКЛ!$B$37=АВР!K1174),ЦИКЛ!$I$98,IF(AND(АВР!$AD$8=ЦИКЛ!$A$113,ЦИКЛ!$D$3=M1174,ЦИКЛ!$B$37=АВР!K1174),ЦИКЛ!$D$118,IF(AND(АВР!$AD$8=ЦИКЛ!$A$108,ЦИКЛ!$E$3=M1174,ЦИКЛ!$B$37=АВР!K1174),ЦИКЛ!$E$118,IF(AND(АВР!$AD$8=ЦИКЛ!$A$113,ЦИКЛ!$F$3=M1174,ЦИКЛ!$B$37=АВР!K1174),ЦИКЛ!$F$118,IF(AND(АВР!$AD$8=ЦИКЛ!$A$108,ЦИКЛ!$G$3=M1174,ЦИКЛ!$B$37=АВР!K1174),ЦИКЛ!$G$118,IF(AND(АВР!$AD$8=ЦИКЛ!$A$113,ЦИКЛ!$H$3=M1174,ЦИКЛ!$B$37=АВР!K1174),ЦИКЛ!$H$118,IF(AND(АВР!$AD$8=ЦИКЛ!$A$108,ЦИКЛ!$I$3=M1174,ЦИКЛ!$B$37=АВР!K1174),ЦИКЛ!$I$118,IF(AND(АВР!$AD$8=ЦИКЛ!$A$135,ЦИКЛ!$D$3=M1174,ЦИКЛ!$B$37=АВР!K1174),ЦИКЛ!$D$140,IF(AND(АВР!$AD$8=ЦИКЛ!$A$130,ЦИКЛ!$E$3=M1174,ЦИКЛ!$B$37=АВР!K1174),ЦИКЛ!$E$140,IF(AND(АВР!$AD$8=ЦИКЛ!$A$135,ЦИКЛ!$F$3=M1174,ЦИКЛ!$B$37=АВР!K1174),ЦИКЛ!$F$140,IF(AND(АВР!$AD$8=ЦИКЛ!$A$130,ЦИКЛ!$G$3=M1174,ЦИКЛ!$B$37=АВР!K1174),ЦИКЛ!$G$140,IF(AND(АВР!$AD$8=ЦИКЛ!$A$135,ЦИКЛ!$H$3=M1174,ЦИКЛ!$B$37=АВР!K1174),ЦИКЛ!$H$140,IF(AND(АВР!$AD$8=ЦИКЛ!$A$130,ЦИКЛ!$I$3=M1174,ЦИКЛ!$B$37=АВР!K1174),ЦИКЛ!$I$140))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))',
     1, '=V1174*W1174*X1174', '=Y1174-AA1174-AB1174-AC1174-AD1174', None, None, None, None, None],
    ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'кварцевый песок', 'Ожидание оседание пропанта', None, None, None,
     None, None, None, None, None, None, None, None, None, 'простои', 'Тех. ожидание', 'час', 2, 1, 1,
     '=V1175*W1175*X1175', '=Y1175-AA1175-AB1175-AC1175-AD1175', None, None, None, None, None],
    ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', 'Перо,воронка', 'Спуск НКТ компоновка', None, None, None, None, None,
     '73мм', 1000,
     '=IF(AND(M1176/V1176>=ЦИКЛ!$V$9,M1176/V1176<=ЦИКЛ!$W$9),ЦИКЛ!$U$9,IF(AND(M1176/V1176>=ЦИКЛ!$V$10,M1176/V1176<=ЦИКЛ!$W$10),ЦИКЛ!$U$10,IF(AND(M1176/V1176>=ЦИКЛ!$V$11,M1176/V1176<=ЦИКЛ!$W$11),ЦИКЛ!$U$11,IF(AND(M1176/V1176>=ЦИКЛ!$V$12,M1176/V1176<=ЦИКЛ!$W$12),ЦИКЛ!$U$12,IF(AND(M1176/V1176>=ЦИКЛ!$V$13,M1176/V1176<=ЦИКЛ!$W$13),ЦИКЛ!$U$13,IF(AND(M1176/V1176>=ЦИКЛ!$V$14,M1176/V1176<=ЦИКЛ!$W$14),ЦИКЛ!$U$14))))))',
     None, None, None, None,
     '=IF($AD$8=ЦИКЛ!$A$4,ЦИКЛ!$P$4,IF($AD$8=ЦИКЛ!$A$7,ЦИКЛ!$P$7,IF($AD$8=ЦИКЛ!$A$10,ЦИКЛ!$P$7,IF($AD$8=ЦИКЛ!$A$52,ЦИКЛ!$P$52,IF($AD$8=ЦИКЛ!$A$70,ЦИКЛ!$P$70,IF($AD$8=ЦИКЛ!$A$88,ЦИКЛ!$P$88,IF($AD$8=ЦИКЛ!$A$106,ЦИКЛ!$P$106,IF($AD$8=ЦИКЛ!$A$133,ЦИКЛ!$P$133,IF($AD$8=ЦИКЛ!$Q$4,ЦИКЛ!$P$4,IF($AD$8=ЦИКЛ!$R$4,ЦИКЛ!$P$4))))))))))',
     None, 'шт', 100,
     '=IF(AND($AD$8=ЦИКЛ!$A$4,ЦИКЛ!$D$3=N1176,ЦИКЛ!$B$37=АВР!L1176),ЦИКЛ!$D$37,IF(AND($AD$8=ЦИКЛ!$A$4,ЦИКЛ!$E$3=N1176,ЦИКЛ!$B$37=АВР!L1176),ЦИКЛ!$E$37,IF(AND($AD$8=ЦИКЛ!$A$4,ЦИКЛ!$F$3=N1176,ЦИКЛ!$B$37=АВР!L1176),ЦИКЛ!$F$37,IF(AND($AD$8=ЦИКЛ!$A$4,ЦИКЛ!$G$3=N1176,ЦИКЛ!$B$37=АВР!L1176),ЦИКЛ!$G$37,IF(AND($AD$8=ЦИКЛ!$A$4,ЦИКЛ!$H$3=N1176,ЦИКЛ!$B$37=АВР!L1176),ЦИКЛ!$H$37,IF(AND($AD$8=ЦИКЛ!$A$4,ЦИКЛ!$I$3=N1176,ЦИКЛ!$B$37=АВР!L1176),ЦИКЛ!$I$37,IF(AND($AD$8=ЦИКЛ!$Q$4,ЦИКЛ!$D$3=N1176,ЦИКЛ!$B$37=АВР!L1176),ЦИКЛ!$D$37,IF(AND($AD$8=ЦИКЛ!$Q$4,ЦИКЛ!$E$3=N1176,ЦИКЛ!$B$37=АВР!L1176),ЦИКЛ!$E$37,IF(AND($AD$8=ЦИКЛ!$Q$4,ЦИКЛ!$F$3=N1176,ЦИКЛ!$B$37=АВР!L1176),ЦИКЛ!$F$37,IF(AND($AD$8=ЦИКЛ!$Q$4,ЦИКЛ!$G$3=N1176,ЦИКЛ!$B$37=АВР!L1176),ЦИКЛ!$G$37,IF(AND($AD$8=ЦИКЛ!$Q$4,ЦИКЛ!$H$3=N1176,ЦИКЛ!$B$37=АВР!L1176),ЦИКЛ!$H$37,IF(AND($AD$8=ЦИКЛ!$Q$4,ЦИКЛ!$I$3=N1176,ЦИКЛ!$B$37=АВР!L1176),ЦИКЛ!$I$37,IF(AND($AD$8=ЦИКЛ!$R$4,ЦИКЛ!$D$3=N1176,ЦИКЛ!$B$37=АВР!L1176),ЦИКЛ!$D$37,IF(AND($AD$8=ЦИКЛ!$R$4,ЦИКЛ!$E$3=N1176,ЦИКЛ!$B$37=АВР!L1176),ЦИКЛ!$E$37,IF(AND($AD$8=ЦИКЛ!$R$4,ЦИКЛ!$F$3=N1176,ЦИКЛ!$B$37=АВР!L1176),ЦИКЛ!$F$37,IF(AND($AD$8=ЦИКЛ!$R$4,ЦИКЛ!$G$3=N1176,ЦИКЛ!$B$37=АВР!L1176),ЦИКЛ!$G$37,IF(AND($AD$8=ЦИКЛ!$R$4,ЦИКЛ!$H$3=N1176,ЦИКЛ!$B$37=АВР!L1176),ЦИКЛ!$H$37,IF(AND($AD$8=ЦИКЛ!$R$4,ЦИКЛ!$I$3=N1176,ЦИКЛ!$B$37=АВР!L1176),ЦИКЛ!$I$37,IF(AND($AD$8=ЦИКЛ!$A$7,ЦИКЛ!$D$3=N1176,ЦИКЛ!$B$37=АВР!L1176),ЦИКЛ!$D$37,IF(AND($AD$8=ЦИКЛ!$A$7,ЦИКЛ!$E$3=N1176,ЦИКЛ!$B$37=АВР!L1176),ЦИКЛ!$E$37,IF(AND($AD$8=ЦИКЛ!$A$7,ЦИКЛ!$F$3=N1176,ЦИКЛ!$B$37=АВР!L1176),ЦИКЛ!$F$37,IF(AND($AD$8=ЦИКЛ!$A$7,ЦИКЛ!$G$3=N1176,ЦИКЛ!$B$37=АВР!L1176),ЦИКЛ!$G$37,IF(AND($AD$8=ЦИКЛ!$A$7,ЦИКЛ!$H$3=N1176,ЦИКЛ!$B$37=АВР!L1176),ЦИКЛ!$H$37,IF(AND($AD$8=ЦИКЛ!$A$7,ЦИКЛ!$I$3=N1176,ЦИКЛ!$B$37=АВР!L1176),ЦИКЛ!$I$37,IF(AND($AD$8=ЦИКЛ!$A$10,ЦИКЛ!$D$3=N1176,ЦИКЛ!$B$37=АВР!L1176),ЦИКЛ!$D$37,IF(AND($AD$8=ЦИКЛ!$A$10,ЦИКЛ!$E$3=N1176,ЦИКЛ!$B$37=АВР!L1176),ЦИКЛ!$E$37,IF(AND($AD$8=ЦИКЛ!$A$10,ЦИКЛ!$F$3=N1176,ЦИКЛ!$B$37=АВР!L1176),ЦИКЛ!$F$37,IF(AND($AD$8=ЦИКЛ!$A$10,ЦИКЛ!$G$3=N1176,ЦИКЛ!$B$37=АВР!L1176),ЦИКЛ!$G$37,IF(AND($AD$8=ЦИКЛ!$A$10,ЦИКЛ!$H$3=N1176,ЦИКЛ!$B$37=АВР!L1176),ЦИКЛ!$H$37,IF(AND($AD$8=ЦИКЛ!$A$10,ЦИКЛ!$I$3=N1176,ЦИКЛ!$B$37=АВР!L1176),ЦИКЛ!$I$37,IF(AND($AD$8=ЦИКЛ!$A$52,ЦИКЛ!$D$3=N1176,ЦИКЛ!$B$37=АВР!L1176),ЦИКЛ!$D$63,IF(AND($AD$8=ЦИКЛ!$A$52,ЦИКЛ!$E$3=N1176,ЦИКЛ!$B$37=АВР!L1176),ЦИКЛ!$E$63,IF(AND($AD$8=ЦИКЛ!$A$52,ЦИКЛ!$F$3=N1176,ЦИКЛ!$B$37=АВР!L1176),ЦИКЛ!$F$63,IF(AND($AD$8=ЦИКЛ!$A$52,ЦИКЛ!$G$3=N1176,ЦИКЛ!$B$37=АВР!L1176),ЦИКЛ!$G$63,IF(AND($AD$8=ЦИКЛ!$A$52,ЦИКЛ!$H$3=N1176,ЦИКЛ!$B$37=АВР!L1176),ЦИКЛ!$H$63,IF(AND($AD$8=ЦИКЛ!$A$52,ЦИКЛ!$I$3=N1176,ЦИКЛ!$B$37=АВР!L1176),ЦИКЛ!$I$63,IF(AND($AD$8=ЦИКЛ!$A$70,ЦИКЛ!$D$3=N1176,ЦИКЛ!$B$37=АВР!L1176),ЦИКЛ!$D$81,IF(AND($AD$8=ЦИКЛ!$A$70,ЦИКЛ!$E$3=N1176,ЦИКЛ!$B$37=АВР!L1176),ЦИКЛ!$E$81,IF(AND($AD$8=ЦИКЛ!$A$70,ЦИКЛ!$F$3=N1176,ЦИКЛ!$B$37=АВР!L1176),ЦИКЛ!$F$81,IF(AND($AD$8=ЦИКЛ!$A$70,ЦИКЛ!$G$3=N1176,ЦИКЛ!$B$37=АВР!L1176),ЦИКЛ!$G$81,IF(AND($AD$8=ЦИКЛ!$A$70,ЦИКЛ!$H$3=N1176,ЦИКЛ!$B$37=АВР!L1176),ЦИКЛ!$H$81,IF(AND($AD$8=ЦИКЛ!$A$70,ЦИКЛ!$I$3=N1176,ЦИКЛ!$B$37=АВР!L1176),ЦИКЛ!$I$81,IF(AND($AD$8=ЦИКЛ!$A$88,ЦИКЛ!$D$3=N1176,ЦИКЛ!$B$37=АВР!L1176),ЦИКЛ!$D$99,IF(AND($AD$8=ЦИКЛ!$A$88,ЦИКЛ!$E$3=N1176,ЦИКЛ!$B$37=АВР!L1176),ЦИКЛ!$E$99,IF(AND($AD$8=ЦИКЛ!$A$88,ЦИКЛ!$F$3=N1176,ЦИКЛ!$B$37=АВР!L1176),ЦИКЛ!$F$99,IF(AND($AD$8=ЦИКЛ!$A$88,ЦИКЛ!$G$3=N1176,ЦИКЛ!$B$37=АВР!L1176),ЦИКЛ!$G$99,IF(AND($AD$8=ЦИКЛ!$A$88,ЦИКЛ!$H$3=N1176,ЦИКЛ!$B$37=АВР!L1176),ЦИКЛ!$H$99,IF(AND($AD$8=ЦИКЛ!$A$88,ЦИКЛ!$I$3=N1176,ЦИКЛ!$B$37=АВР!L1176),ЦИКЛ!$I$99,IF(AND($AD$8=ЦИКЛ!$A$106,ЦИКЛ!$D$3=N1176,ЦИКЛ!$B$37=АВР!L1176),ЦИКЛ!$D$120,IF(AND($AD$8=ЦИКЛ!$A$106,ЦИКЛ!$E$3=N1176,ЦИКЛ!$B$37=АВР!L1176),ЦИКЛ!$E$120,IF(AND($AD$8=ЦИКЛ!$A$106,ЦИКЛ!$F$3=N1176,ЦИКЛ!$B$37=АВР!L1176),ЦИКЛ!$F$120,IF(AND($AD$8=ЦИКЛ!$A$106,ЦИКЛ!$G$3=N1176,ЦИКЛ!$B$37=АВР!L1176),ЦИКЛ!$G$120,IF(AND($AD$8=ЦИКЛ!$A$106,ЦИКЛ!$H$3=N1176,ЦИКЛ!$B$37=АВР!L1176),ЦИКЛ!$H$120,IF(AND($AD$8=ЦИКЛ!$A$106,ЦИКЛ!$I$3=N1176,ЦИКЛ!$B$37=АВР!L1176),ЦИКЛ!$I$120,IF(AND($AD$8=ЦИКЛ!$A$128,ЦИКЛ!$D$3=N1176,ЦИКЛ!$B$37=АВР!L1176),ЦИКЛ!$D$142,IF(AND($AD$8=ЦИКЛ!$A$128,ЦИКЛ!$E$3=N1176,ЦИКЛ!$B$37=АВР!L1176),ЦИКЛ!$E$142,IF(AND($AD$8=ЦИКЛ!$A$128,ЦИКЛ!$F$3=N1176,ЦИКЛ!$B$37=АВР!L1176),ЦИКЛ!$F$142,IF(AND($AD$8=ЦИКЛ!$A$128,ЦИКЛ!$G$3=N1176,ЦИКЛ!$B$37=АВР!L1176),ЦИКЛ!$G$142,IF(AND($AD$8=ЦИКЛ!$A$128,ЦИКЛ!$H$3=N1176,ЦИКЛ!$B$37=АВР!L1176),ЦИКЛ!$H$142,IF(AND(АВР!$AD$8=ЦИКЛ!$A$128,ЦИКЛ!$I$3=N1176,ЦИКЛ!$B$37=АВР!L1176),ЦИКЛ!$I$142))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))',
     1, '=V1176*W1176*X1176', '=Y1176-AA1176-AB1176-AC1176-AD1176', None, None, None, None, None],
    ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'Определение кровли песчанного моста на гл. 1195м', None,
     None, None, None, None, None, None, None, None, None, None, None, '§289разд.1', None, 'раз', 1, 0.17, 1,
     '=V1177*W1177*X1177', '=Y1177-AA1177-AB1177-AC1177-AD1177', None, None, None, None, None],
    ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'Опрессовка пес.м. на Р-100атм(+)', None, None, None, None,
     None, None, None, None, None, None, None, None, '§290разд.1', None, 'раз', 1, 0.58, 1, '=V1178*W1178*X1178',
     '=Y1178-AA1178-AB1178-AC1178-AD1178', None, None, None, None, None],
    ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'Промывка', 'ПР  перед вымывом излишков пропанта', None, None,
     None, None, None, None, None, None, None, None, None, None, '§285разд.1', None, 'раз', 1, 0.15, 1,
     '=V1179*W1179*X1179', '=Y1179-AA1179-AB1179-AC1179-AD1179', None, None, None, None, None],
    ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'Промывка', 'Промывка ', None, None, None, None, None, None, None,
     None, None, None, None, None, '§300разд.1', None, 'м3', 27, 0.033, 1, '=V1180*W1180*X1180',
     '=Y1180-AA1180-AB1180-AC1180-AD1180', None, None, None, None, None],
    ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'Промывка', 'Разобрать промывочное оборудование', None, None,
     None, None, None, None, None, None, None, None, None, None, '§161разд.1', None, 'раз', 1, 0.23, 1,
     '=V1181*W1181*X1181', '=Y1181-AA1181-AB1181-AC1181-AD1181', None, None, None, None, None],
    ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', 'Перо,воронка', 'Подъем НКТ  1 скорость ', None, None, None, None, '73мм',
     1000,
     '=IF(AND(L1182/V1182>=ЦИКЛ!$V$9,L1182/V1182<=ЦИКЛ!$W$9),ЦИКЛ!$U$9,IF(AND(L1182/V1182>=ЦИКЛ!$V$10,L1182/V1182<=ЦИКЛ!$W$10),ЦИКЛ!$U$10,IF(AND(L1182/V1182>=ЦИКЛ!$V$11,L1182/V1182<=ЦИКЛ!$W$11),ЦИКЛ!$U$11,IF(AND(L1182/V1182>=ЦИКЛ!$V$12,L1182/V1182<=ЦИКЛ!$W$12),ЦИКЛ!$U$12,IF(AND(L1182/V1182>=ЦИКЛ!$V$13,L1182/V1182<=ЦИКЛ!$W$13),ЦИКЛ!$U$13,IF(AND(L1182/V1182>=ЦИКЛ!$V$14,L1182/V1182<=ЦИКЛ!$W$14),ЦИКЛ!$U$14))))))',
     '=IF(AND(АВР!$AD$8=ЦИКЛ!$A$4,ЦИКЛ!$D$3=M1182),ЦИКЛ!$J$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$4,ЦИКЛ!$E$3=M1182),ЦИКЛ!$K$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$4,ЦИКЛ!$F$3=M1182),ЦИКЛ!$L$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$4,ЦИКЛ!$M$3=M1182),ЦИКЛ!$M$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$4,ЦИКЛ!$H$3=M1182),ЦИКЛ!$N$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$4,ЦИКЛ!$I$3=M1182),ЦИКЛ!$O$28,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$4,ЦИКЛ!$D$3=M1182),ЦИКЛ!$J$28,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$4,ЦИКЛ!$E$3=M1182),ЦИКЛ!$K$28,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$4,ЦИКЛ!$F$3=M1182),ЦИКЛ!$L$28,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$4,ЦИКЛ!$G$3=M1182),ЦИКЛ!$M$28,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$4,ЦИКЛ!$H$3=M1182),ЦИКЛ!$N$28,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$4,ЦИКЛ!$O$3=M1182),ЦИКЛ!$I$28,IF(AND(АВР!$AD$8=ЦИКЛ!$R$4,ЦИКЛ!$D$3=M1182),ЦИКЛ!$J$28,IF(AND(АВР!$AD$8=ЦИКЛ!$R$4,ЦИКЛ!$E$3=M1182),ЦИКЛ!$K$28,IF(AND(АВР!$AD$8=ЦИКЛ!$R$4,ЦИКЛ!$F$3=M1182),ЦИКЛ!$L$28,IF(AND(АВР!$AD$8=ЦИКЛ!$R$4,ЦИКЛ!$G$3=M1182),ЦИКЛ!$M$28,IF(AND(АВР!$AD$8=ЦИКЛ!$R$4,ЦИКЛ!$N$3=M1182),ЦИКЛ!$H$28,IF(AND(АВР!$AD$8=ЦИКЛ!$R$4,ЦИКЛ!$I$3=M1182),ЦИКЛ!$O$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$7,ЦИКЛ!$D$3=M1182),ЦИКЛ!$J$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$7,ЦИКЛ!$E$3=M1182),ЦИКЛ!$K$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$7,ЦИКЛ!$F$3=M1182),ЦИКЛ!$L$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$7,ЦИКЛ!$G$3=M1182),ЦИКЛ!$M$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$7,ЦИКЛ!$N$3=M1182),ЦИКЛ!$H$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$7,ЦИКЛ!$I$3=M1182),ЦИКЛ!$O$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$10,ЦИКЛ!$D$3=M1182),ЦИКЛ!$J$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$10,ЦИКЛ!$E$3=M1182),ЦИКЛ!$K$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$10,ЦИКЛ!$F$3=M1182),ЦИКЛ!$L$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$10,ЦИКЛ!$G$3=M1182),ЦИКЛ!$M$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$10,ЦИКЛ!$H$3=M1182),ЦИКЛ!$N$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$10,ЦИКЛ!$I$3=M1182),ЦИКЛ!$O$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$52,ЦИКЛ!$D$3=M1182),ЦИКЛ!$J$60,IF(AND(АВР!$AD$8=ЦИКЛ!$A$52,ЦИКЛ!$E$3=M1182),ЦИКЛ!$K$60,IF(AND(АВР!$AD$8=ЦИКЛ!$A$52,ЦИКЛ!$F$3=M1182),ЦИКЛ!$L$60,IF(AND(АВР!$AD$8=ЦИКЛ!$A$52,ЦИКЛ!$G$3=M1182),ЦИКЛ!$M$60,IF(AND(АВР!$AD$8=ЦИКЛ!$A$52,ЦИКЛ!$H$3=M1182),ЦИКЛ!$N$60,IF(AND(АВР!$AD$8=ЦИКЛ!$A$52,ЦИКЛ!$I$3=M1182),ЦИКЛ!$O$60,IF(AND(АВР!$AD$8=ЦИКЛ!$A$70,ЦИКЛ!$D$3=M1182),ЦИКЛ!$J$78,IF(AND(АВР!$AD$8=ЦИКЛ!$A$70,ЦИКЛ!$E$3=M1182),ЦИКЛ!$K$78,IF(AND(АВР!$AD$8=ЦИКЛ!$A$70,ЦИКЛ!$F$3=M1182),ЦИКЛ!$L$78,IF(AND(АВР!$AD$8=ЦИКЛ!$A$70,ЦИКЛ!$G$3=M1182),ЦИКЛ!$M$78,IF(AND(АВР!$AD$8=ЦИКЛ!$A$70,ЦИКЛ!$H$3=M1182),ЦИКЛ!$N$78,IF(AND(АВР!$AD$8=ЦИКЛ!$A$70,ЦИКЛ!$I$3=M1182),ЦИКЛ!$O$78,IF(AND(АВР!$AD$8=ЦИКЛ!$A$88,ЦИКЛ!$D$3=M1182),ЦИКЛ!$J$96,IF(AND(АВР!$AD$8=ЦИКЛ!$A$88,ЦИКЛ!$E$3=M1182),ЦИКЛ!$K$96,IF(AND(АВР!$AD$8=ЦИКЛ!$A$88,ЦИКЛ!$F$3=M1182),ЦИКЛ!$L$96,IF(AND(АВР!$AD$8=ЦИКЛ!$A$88,ЦИКЛ!$G$3=M1182),ЦИКЛ!$M$96,IF(AND(АВР!$AD$8=ЦИКЛ!$A$88,ЦИКЛ!$H$3=M1182),ЦИКЛ!$N$96,IF(AND(АВР!$AD$8=ЦИКЛ!$A$88,ЦИКЛ!$I$3=M1182),ЦИКЛ!$O$96,IF(AND(АВР!$AD$8=ЦИКЛ!$A$116,ЦИКЛ!$D$3=M1182),ЦИКЛ!$J$116,IF(AND(АВР!$AD$8=ЦИКЛ!$A$116,ЦИКЛ!$E$3=M1182),ЦИКЛ!$K$116,IF(AND(АВР!$AD$8=ЦИКЛ!$A$116,ЦИКЛ!$F$3=M1182),ЦИКЛ!$L$116,IF(AND(АВР!$AD$8=ЦИКЛ!$A$116,ЦИКЛ!$G$3=M1182),ЦИКЛ!$M$116,IF(AND(АВР!$AD$8=ЦИКЛ!$A$116,ЦИКЛ!$H$3=M1182),ЦИКЛ!$N$116,IF(AND(АВР!$AD$8=ЦИКЛ!$A$116,ЦИКЛ!$I$3=M1182),ЦИКЛ!$O$116,IF(AND(АВР!$AD$8=ЦИКЛ!$A$128,ЦИКЛ!$D$3=M1182),ЦИКЛ!$J$138,IF(AND(АВР!$AD$8=ЦИКЛ!$A$128,ЦИКЛ!$E$3=M1182),ЦИКЛ!$K$138,IF(AND(АВР!$AD$8=ЦИКЛ!$A$128,ЦИКЛ!$F$3=M1182),ЦИКЛ!$L$138,IF(AND(АВР!$AD$8=ЦИКЛ!$A$128,ЦИКЛ!$G$3=M1182),ЦИКЛ!$M$138,IF(AND(АВР!$AD$8=ЦИКЛ!$A$128,ЦИКЛ!$H$3=M1182),ЦИКЛ!$N$138,IF(AND(АВР!$AD$8=ЦИКЛ!$A$128,ЦИКЛ!$I$3=M1182),ЦИКЛ!$O$138))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))',
     None, None, None, None,
     '=IF($AD$8=ЦИКЛ!$A$4,ЦИКЛ!$P$4,IF($AD$8=ЦИКЛ!$A$7,ЦИКЛ!$P$7,IF($AD$8=ЦИКЛ!$A$10,ЦИКЛ!$P$7,IF($AD$8=ЦИКЛ!$A$52,ЦИКЛ!$P$52,IF($AD$8=ЦИКЛ!$A$70,ЦИКЛ!$P$70,IF($AD$8=ЦИКЛ!$A$88,ЦИКЛ!$P$88,IF($AD$8=ЦИКЛ!$A$106,ЦИКЛ!$P$106,IF($AD$8=ЦИКЛ!$A$133,ЦИКЛ!$P$133,IF($AD$8=ЦИКЛ!$Q$4,ЦИКЛ!$P$4,IF($AD$8=ЦИКЛ!$R$4,ЦИКЛ!$P$4))))))))))',
     None, 'шт', 100,
     '=IF(AND(АВР!$AD$8=ЦИКЛ!$A$4,ЦИКЛ!$D$3=M1182,ЦИКЛ!$B$37=АВР!K1182),ЦИКЛ!$D$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$4,ЦИКЛ!$E$3=M1182,ЦИКЛ!$B$37=АВР!K1182),ЦИКЛ!$E$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$4,ЦИКЛ!$F$3=M1182,ЦИКЛ!$B$37=АВР!K1182),ЦИКЛ!$F$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$4,ЦИКЛ!$G$3=M1182,ЦИКЛ!$B$37=АВР!K1182),ЦИКЛ!$G$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$4,ЦИКЛ!$H$3=M1182,ЦИКЛ!$B$37=АВР!K1182),ЦИКЛ!$H$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$4,ЦИКЛ!$I$3=M1182,ЦИКЛ!$B$37=АВР!K1182),ЦИКЛ!$I$28,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$4,ЦИКЛ!$D$3=M1182,ЦИКЛ!$B$37=АВР!K1182),ЦИКЛ!$D$28,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$4,ЦИКЛ!$E$3=M1182,ЦИКЛ!$B$37=АВР!K1182),ЦИКЛ!$E$28,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$4,ЦИКЛ!$F$3=M1182,ЦИКЛ!$B$37=АВР!K1182),ЦИКЛ!$F$28,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$4,ЦИКЛ!$G$3=M1182,ЦИКЛ!$B$37=АВР!K1182),ЦИКЛ!$G$28,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$4,ЦИКЛ!$H$3=M1182,ЦИКЛ!$B$37=АВР!K1182),ЦИКЛ!$H$28,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$4,ЦИКЛ!$I$3=M1182,ЦИКЛ!$B$37=АВР!K1182),ЦИКЛ!$I$28,IF(AND(АВР!$AD$8=ЦИКЛ!$R$4,ЦИКЛ!$D$3=M1182,ЦИКЛ!$B$37=АВР!K1182),ЦИКЛ!$D$28,IF(AND(АВР!$AD$8=ЦИКЛ!$R$4,ЦИКЛ!$E$3=M1182,ЦИКЛ!$B$37=АВР!K1182),ЦИКЛ!$E$28,IF(AND(АВР!$AD$8=ЦИКЛ!$R$4,ЦИКЛ!$F$3=M1182,ЦИКЛ!$B$37=АВР!K1182),ЦИКЛ!$F$28,IF(AND(АВР!$AD$8=ЦИКЛ!$R$4,ЦИКЛ!$G$3=M1182,ЦИКЛ!$B$37=АВР!K1182),ЦИКЛ!$G$28,IF(AND(АВР!$AD$8=ЦИКЛ!$R$4,ЦИКЛ!$H$3=M1182,ЦИКЛ!$B$37=АВР!K1182),ЦИКЛ!$H$28,IF(AND(АВР!$AD$8=ЦИКЛ!$R$4,ЦИКЛ!$I$3=M1182,ЦИКЛ!$B$37=АВР!K1182),ЦИКЛ!$I$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$7,ЦИКЛ!$D$3=M1182,ЦИКЛ!$B$37=АВР!K1182),ЦИКЛ!$D$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$7,ЦИКЛ!$E$3=M1182,ЦИКЛ!$B$37=АВР!K1182),ЦИКЛ!$E$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$7,ЦИКЛ!$F$3=M1182,ЦИКЛ!$B$37=АВР!K1182),ЦИКЛ!$F$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$7,ЦИКЛ!$G$3=M1182,ЦИКЛ!$B$37=АВР!K1182),ЦИКЛ!$G$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$7,ЦИКЛ!$H$3=M1182,ЦИКЛ!$B$37=АВР!K1182),ЦИКЛ!$H$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$7,ЦИКЛ!$I$3=M1182,ЦИКЛ!$B$37=АВР!K1182),ЦИКЛ!$I$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$10,ЦИКЛ!$D$3=M1182,ЦИКЛ!$B$37=АВР!K1182),ЦИКЛ!$D$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$10,ЦИКЛ!$E$3=M1182,ЦИКЛ!$B$37=АВР!K1182),ЦИКЛ!$E$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$10,ЦИКЛ!$F$3=M1182,ЦИКЛ!$B$37=АВР!K1182),ЦИКЛ!$F$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$10,ЦИКЛ!$G$3=M1182,ЦИКЛ!$B$37=АВР!K1182),ЦИКЛ!$G$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$10,ЦИКЛ!$H$3=M1182,ЦИКЛ!$B$37=АВР!K1182),ЦИКЛ!$H$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$10,ЦИКЛ!$I$3=M1182,ЦИКЛ!$B$37=АВР!K1182),ЦИКЛ!$I$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$52,ЦИКЛ!$D$3=M1182,ЦИКЛ!$B$37=АВР!K1182),ЦИКЛ!$D$60,IF(AND(АВР!$AD$8=ЦИКЛ!$A$52,ЦИКЛ!$E$3=M1182,ЦИКЛ!$B$37=АВР!K1182),ЦИКЛ!$E$60,IF(AND(АВР!$AD$8=ЦИКЛ!$A$52,ЦИКЛ!$F$3=M1182,ЦИКЛ!$B$37=АВР!K1182),ЦИКЛ!$F$60,IF(AND(АВР!$AD$8=ЦИКЛ!$A$52,ЦИКЛ!$G$3=M1182,ЦИКЛ!$B$37=АВР!K1182),ЦИКЛ!$G$60,IF(AND(АВР!$AD$8=ЦИКЛ!$A$52,ЦИКЛ!$H$3=M1182,ЦИКЛ!$B$37=АВР!K1182),ЦИКЛ!$H$60,IF(AND(АВР!$AD$8=ЦИКЛ!$A$52,ЦИКЛ!$I$3=M1182,ЦИКЛ!$B$37=АВР!K1182),ЦИКЛ!$I$60,IF(AND(АВР!$AD$8=ЦИКЛ!$A$70,ЦИКЛ!$D$3=M1182,ЦИКЛ!$B$37=АВР!K1182),ЦИКЛ!$D$78,IF(AND(АВР!$AD$8=ЦИКЛ!$A$70,ЦИКЛ!$E$3=M1182,ЦИКЛ!$B$37=АВР!K1182),ЦИКЛ!$E$78,IF(AND(АВР!$AD$8=ЦИКЛ!$A$70,ЦИКЛ!$F$3=M1182,ЦИКЛ!$B$37=АВР!K1182),ЦИКЛ!$F$78,IF(AND(АВР!$AD$8=ЦИКЛ!$A$70,ЦИКЛ!$G$3=M1182,ЦИКЛ!$B$37=АВР!K1182),ЦИКЛ!$G$78,IF(AND(АВР!$AD$8=ЦИКЛ!$A$70,ЦИКЛ!$H$3=M1182,ЦИКЛ!$B$37=АВР!K1182),ЦИКЛ!$H$78,IF(AND(АВР!$AD$8=ЦИКЛ!$A$70,ЦИКЛ!$I$3=M1182,ЦИКЛ!$B$37=АВР!K1182),ЦИКЛ!$I$78,IF(AND(АВР!$AD$8=ЦИКЛ!$A$88,ЦИКЛ!$D$3=M1182,ЦИКЛ!$B$37=АВР!K1182),ЦИКЛ!$D$96,IF(AND(АВР!$AD$8=ЦИКЛ!$A$88,ЦИКЛ!$E$3=M1182,ЦИКЛ!$B$37=АВР!K1182),ЦИКЛ!$E$96,IF(AND(АВР!$AD$8=ЦИКЛ!$A$88,ЦИКЛ!$F$3=M1182,ЦИКЛ!$B$37=АВР!K1182),ЦИКЛ!$F$96,IF(AND(АВР!$AD$8=ЦИКЛ!$A$88,ЦИКЛ!$G$3=M1182,ЦИКЛ!$B$37=АВР!K1182),ЦИКЛ!$G$96,IF(AND(АВР!$AD$8=ЦИКЛ!$A$88,ЦИКЛ!$H$3=M1182,ЦИКЛ!$B$37=АВР!K1182),ЦИКЛ!$H$96,IF(AND(АВР!$AD$8=ЦИКЛ!$A$88,ЦИКЛ!$I$3=M1182,ЦИКЛ!$B$37=АВР!K1182),ЦИКЛ!$I$96,IF(AND(АВР!$AD$8=ЦИКЛ!$A$106,ЦИКЛ!$D$3=M1182,ЦИКЛ!$B$37=АВР!K1182),ЦИКЛ!$D$116,IF(AND(АВР!$AD$8=ЦИКЛ!$A$106,ЦИКЛ!$E$3=M1182,ЦИКЛ!$B$37=АВР!K1182),ЦИКЛ!$E$116,IF(AND(АВР!$AD$8=ЦИКЛ!$A$106,ЦИКЛ!$F$3=M1182,ЦИКЛ!$B$37=АВР!K1182),ЦИКЛ!$F$116,IF(AND(АВР!$AD$8=ЦИКЛ!$A$106,ЦИКЛ!$G$3=M1182,ЦИКЛ!$B$37=АВР!K1182),ЦИКЛ!$G$116,IF(AND(АВР!$AD$8=ЦИКЛ!$A$106,ЦИКЛ!$H$3=M1182,ЦИКЛ!$B$37=АВР!K1182),ЦИКЛ!$H$116,IF(AND(АВР!$AD$8=ЦИКЛ!$A$106,ЦИКЛ!$I$3=M1182,ЦИКЛ!$B$37=АВР!K1182),ЦИКЛ!$I$116,IF(AND(АВР!$AD$8=ЦИКЛ!$A$128,ЦИКЛ!$D$3=M1182,ЦИКЛ!$B$37=АВР!K1182),ЦИКЛ!$D$138,IF(AND(АВР!$AD$8=ЦИКЛ!$A$128,ЦИКЛ!$E$3=M1182,ЦИКЛ!$B$37=АВР!K1182),ЦИКЛ!$E$138,IF(AND(АВР!$AD$8=ЦИКЛ!$A$128,ЦИКЛ!$F$3=M1182,ЦИКЛ!$B$37=АВР!K1182),ЦИКЛ!$F$138,IF(AND(АВР!$AD$8=ЦИКЛ!$A$128,ЦИКЛ!$G$3=M1182,ЦИКЛ!$B$37=АВР!K1182),ЦИКЛ!$G$138,IF(AND(АВР!$AD$8=ЦИКЛ!$A$128,ЦИКЛ!$H$3=M1182,ЦИКЛ!$B$37=АВР!K1182),ЦИКЛ!$H$138,IF(AND(АВР!$AD$8=ЦИКЛ!$A$128,ЦИКЛ!$I$3=M1182,ЦИКЛ!$B$37=АВР!K1182),ЦИКЛ!$I$138))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))',
     1.2, '=V1182*W1182*X1182', '=Y1182-AA1182-AB1182-AC1182-AD1182', None, None, None, None, None],
    ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', 'Перо,воронка', 'Подъем НКТ  2 скорость', None, None, None, None, '73мм',
     1000,
     '=IF(AND(L1183/V1183>=ЦИКЛ!$V$9,L1183/V1183<=ЦИКЛ!$W$9),ЦИКЛ!$U$9,IF(AND(L1183/V1183>=ЦИКЛ!$V$10,L1183/V1183<=ЦИКЛ!$W$10),ЦИКЛ!$U$10,IF(AND(L1183/V1183>=ЦИКЛ!$V$11,L1183/V1183<=ЦИКЛ!$W$11),ЦИКЛ!$U$11,IF(AND(L1183/V1183>=ЦИКЛ!$V$12,L1183/V1183<=ЦИКЛ!$W$12),ЦИКЛ!$U$12,IF(AND(L1183/V1183>=ЦИКЛ!$V$13,L1183/V1183<=ЦИКЛ!$W$13),ЦИКЛ!$U$13,IF(AND(L1183/V1183>=ЦИКЛ!$V$14,L1183/V1183<=ЦИКЛ!$W$14),ЦИКЛ!$U$14))))))',
     '=IF(AND(АВР!$AD$8=ЦИКЛ!$A$5,ЦИКЛ!$D$3=M1183),ЦИКЛ!$J$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$5,ЦИКЛ!$E$3=M1183),ЦИКЛ!$K$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$5,ЦИКЛ!$F$3=M1183),ЦИКЛ!$L$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$5,ЦИКЛ!$G$3=M1183),ЦИКЛ!$M$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$5,ЦИКЛ!$H$3=M1183),ЦИКЛ!$N$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$5,ЦИКЛ!$I$3=M1183),ЦИКЛ!$O$29,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$5,ЦИКЛ!$D$3=M1183),ЦИКЛ!$J$29,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$5,ЦИКЛ!$E$3=M1183),ЦИКЛ!$K$29,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$5,ЦИКЛ!$F$3=M1183),ЦИКЛ!$L$29,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$5,ЦИКЛ!$G$3=M1183),ЦИКЛ!$M$29,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$5,ЦИКЛ!$H$3=M1183),ЦИКЛ!$N$29,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$5,ЦИКЛ!$I$3=M1183),ЦИКЛ!$O$29,IF(AND(АВР!$AD$8=ЦИКЛ!$R$5,ЦИКЛ!$D$3=M1183),ЦИКЛ!$J$29,IF(AND(АВР!$AD$8=ЦИКЛ!$R$5,ЦИКЛ!$E$3=M1183),ЦИКЛ!$K$29,IF(AND(АВР!$AD$8=ЦИКЛ!$R$5,ЦИКЛ!$F$3=M1183),ЦИКЛ!$L$29,IF(AND(АВР!$AD$8=ЦИКЛ!$R$5,ЦИКЛ!$G$3=M1183),ЦИКЛ!$M$29,IF(AND(АВР!$AD$8=ЦИКЛ!$R$5,ЦИКЛ!$H$3=M1183),ЦИКЛ!$N$29,IF(AND(АВР!$AD$8=ЦИКЛ!$R$5,ЦИКЛ!$I$3=M1183),ЦИКЛ!$O$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$8,ЦИКЛ!$D$3=M1183),ЦИКЛ!$J$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$8,ЦИКЛ!$E$3=M1183),ЦИКЛ!$K$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$8,ЦИКЛ!$F$3=M1183),ЦИКЛ!$L$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$8,ЦИКЛ!$G$3=M1183),ЦИКЛ!$M$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$8,ЦИКЛ!$H$3=M1183),ЦИКЛ!$N$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$8,ЦИКЛ!$I$3=M1183),ЦИКЛ!$O$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$11,ЦИКЛ!$D$3=M1183),ЦИКЛ!$J$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$11,ЦИКЛ!$E$3=M1183),ЦИКЛ!$K$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$11,ЦИКЛ!$F$3=M1183),ЦИКЛ!$L$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$11,ЦИКЛ!$G$3=M1183),ЦИКЛ!$M$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$11,ЦИКЛ!$H$3=M1183),ЦИКЛ!$N$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$11,ЦИКЛ!$I$3=M1183),ЦИКЛ!$O$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$53,ЦИКЛ!$D$3=M1183),ЦИКЛ!#REF!,IF(AND(АВР!$AD$8=ЦИКЛ!$A$53,ЦИКЛ!$E$3=M1183),ЦИКЛ!$K$61,IF(AND(АВР!$AD$8=ЦИКЛ!$A$53,ЦИКЛ!$F$3=M1183),ЦИКЛ!$L$61,IF(AND(АВР!$AD$8=ЦИКЛ!$A$53,ЦИКЛ!$G$3=M1183),ЦИКЛ!$M$61,IF(AND(АВР!$AD$8=ЦИКЛ!$A$53,ЦИКЛ!$H$3=M1183),ЦИКЛ!$N$61,IF(AND(АВР!$AD$8=ЦИКЛ!$A$53,ЦИКЛ!$I$3=M1183),ЦИКЛ!$O$61,IF(AND(АВР!$AD$8=ЦИКЛ!$A$71,ЦИКЛ!$D$3=M1183),ЦИКЛ!$J$79,IF(AND(АВР!$AD$8=ЦИКЛ!$A$71,ЦИКЛ!$E$3=M1183),ЦИКЛ!$K$79,IF(AND(АВР!$AD$8=ЦИКЛ!$A$71,ЦИКЛ!$F$3=M1183),ЦИКЛ!$L$79,IF(AND(АВР!$AD$8=ЦИКЛ!$A$71,ЦИКЛ!$G$3=M1183),ЦИКЛ!$M$79,IF(AND(АВР!$AD$8=ЦИКЛ!$A$71,ЦИКЛ!$H$3=M1183),ЦИКЛ!$N$79,IF(AND(АВР!$AD$8=ЦИКЛ!$A$71,ЦИКЛ!$I$3=M1183),ЦИКЛ!$O$79,IF(AND(АВР!$AD$8=ЦИКЛ!$A$89,ЦИКЛ!$D$3=M1183),ЦИКЛ!$J$97,IF(AND(АВР!$AD$8=ЦИКЛ!$A$89,ЦИКЛ!$E$3=M1183),ЦИКЛ!$K$97,IF(AND(АВР!$AD$8=ЦИКЛ!$A$89,ЦИКЛ!$F$3=M1183),ЦИКЛ!$L$97,IF(AND(АВР!$AD$8=ЦИКЛ!$A$89,ЦИКЛ!$G$3=M1183),ЦИКЛ!$M$97,IF(AND(АВР!$AD$8=ЦИКЛ!$A$89,ЦИКЛ!$H$3=M1183),ЦИКЛ!$N$97,IF(AND(АВР!$AD$8=ЦИКЛ!$A$89,ЦИКЛ!$I$3=M1183),ЦИКЛ!$O$97,IF(AND(АВР!$AD$8=ЦИКЛ!$A$107,ЦИКЛ!$D$3=M1183),ЦИКЛ!$J$117,IF(AND(АВР!$AD$8=ЦИКЛ!$A$107,ЦИКЛ!$E$3=M1183),ЦИКЛ!$K$117,IF(AND(АВР!$AD$8=ЦИКЛ!$A$107,ЦИКЛ!$F$3=M1183),ЦИКЛ!$L$117,IF(AND(АВР!$AD$8=ЦИКЛ!$A$107,ЦИКЛ!$G$3=M1183),ЦИКЛ!$M$117,IF(AND(АВР!$AD$8=ЦИКЛ!$A$107,ЦИКЛ!$H$3=M1183),ЦИКЛ!$N$117,IF(AND(АВР!$AD$8=ЦИКЛ!$A$107,ЦИКЛ!$I$3=M1183),ЦИКЛ!$O$117,IF(AND(АВР!$AD$8=ЦИКЛ!$A$129,ЦИКЛ!$D$3=M1183),ЦИКЛ!$J$139,IF(AND(АВР!$AD$8=ЦИКЛ!$A$129,ЦИКЛ!$E$3=M1183),ЦИКЛ!$K$139,IF(AND(АВР!$AD$8=ЦИКЛ!$A$129,ЦИКЛ!$F$3=M1183),ЦИКЛ!$L$139,IF(AND(АВР!$AD$8=ЦИКЛ!$A$129,ЦИКЛ!$G$3=M1183),ЦИКЛ!$M$139,IF(AND(АВР!$AD$8=ЦИКЛ!$A$129,ЦИКЛ!$H$3=M1183),ЦИКЛ!$N$139,IF(AND(АВР!$AD$8=ЦИКЛ!$A$129,ЦИКЛ!$I$3=M1183),ЦИКЛ!$O$139))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))',
     None, None, None, None,
     '=IF($AD$8=ЦИКЛ!$A$4,ЦИКЛ!$P$4,IF($AD$8=ЦИКЛ!$A$7,ЦИКЛ!$P$7,IF($AD$8=ЦИКЛ!$A$10,ЦИКЛ!$P$7,IF($AD$8=ЦИКЛ!$A$52,ЦИКЛ!$P$52,IF($AD$8=ЦИКЛ!$A$70,ЦИКЛ!$P$70,IF($AD$8=ЦИКЛ!$A$88,ЦИКЛ!$P$88,IF($AD$8=ЦИКЛ!$A$106,ЦИКЛ!$P$106,IF($AD$8=ЦИКЛ!$A$133,ЦИКЛ!$P$133,IF($AD$8=ЦИКЛ!$Q$4,ЦИКЛ!$P$4,IF($AD$8=ЦИКЛ!$R$4,ЦИКЛ!$P$4))))))))))',
     None, 'шт', 100,
     '=IF(AND(АВР!$AD$8=ЦИКЛ!$A$5,ЦИКЛ!$D$3=M1183,ЦИКЛ!$B$37=АВР!K1183),ЦИКЛ!$D$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$5,ЦИКЛ!$E$3=M1183,ЦИКЛ!$B$37=АВР!K1183),ЦИКЛ!$E$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$5,ЦИКЛ!$F$3=M1183,ЦИКЛ!$B$37=АВР!K1183),ЦИКЛ!$F$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$5,ЦИКЛ!$G$3=M1183,ЦИКЛ!$B$37=АВР!K1183),ЦИКЛ!$G$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$5,ЦИКЛ!$H$3=M1183,ЦИКЛ!$B$37=АВР!K1183),ЦИКЛ!$H$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$5,ЦИКЛ!$I$3=M1183,ЦИКЛ!$B$37=K1183),ЦИКЛ!$I$29,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$5,ЦИКЛ!$D$3=M1183,ЦИКЛ!$B$37=K1183),ЦИКЛ!$D$29,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$5,ЦИКЛ!$E$3=M1183,ЦИКЛ!$B$37=K1183),ЦИКЛ!$E$29,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$5,ЦИКЛ!$F$3=M1183,ЦИКЛ!$B$37=K1183),ЦИКЛ!$F$29,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$5,ЦИКЛ!$G$3=M1183,ЦИКЛ!$B$37=K1183),ЦИКЛ!$G$29,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$5,ЦИКЛ!$H$3=M1183,ЦИКЛ!$B$37=K1183),ЦИКЛ!$H$29,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$5,ЦИКЛ!$I$3=M1183,ЦИКЛ!$B$37=K1183),ЦИКЛ!$I$29,IF(AND(АВР!$AD$8=ЦИКЛ!$R$5,ЦИКЛ!$D$3=M1183,ЦИКЛ!$B$37=K1183),ЦИКЛ!$D$29,IF(AND(АВР!$AD$8=ЦИКЛ!$R$5,ЦИКЛ!$E$3=M1183,ЦИКЛ!$B$37=K1183),ЦИКЛ!$E$29,IF(AND(АВР!$AD$8=ЦИКЛ!$R$5,ЦИКЛ!$F$3=M1183,ЦИКЛ!$B$37=K1183),ЦИКЛ!$F$29,IF(AND(АВР!$AD$8=ЦИКЛ!$R$5,ЦИКЛ!$G$3=M1183,ЦИКЛ!$B$37=K1183),ЦИКЛ!$G$29,IF(AND(АВР!$AD$8=ЦИКЛ!$R$5,ЦИКЛ!$H$3=M1183,ЦИКЛ!$B$37=K1183),ЦИКЛ!$H$29,IF(AND(АВР!$AD$8=ЦИКЛ!$R$5,ЦИКЛ!$I$3=M1183,ЦИКЛ!$B$37=K1183),ЦИКЛ!$I$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$8,ЦИКЛ!$D$3=M1183,ЦИКЛ!$B$37=K1183),ЦИКЛ!$D$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$8,ЦИКЛ!$E$3=M1183,ЦИКЛ!$B$37=K1183),ЦИКЛ!$E$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$8,ЦИКЛ!$F$3=M1183,ЦИКЛ!$B$37=K1183),ЦИКЛ!$F$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$8,ЦИКЛ!$G$3=M1183,ЦИКЛ!$B$37=K1183),ЦИКЛ!$G$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$8,ЦИКЛ!$H$3=M1183,ЦИКЛ!$B$37=K1183),ЦИКЛ!$H$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$8,ЦИКЛ!$I$3=M1183,ЦИКЛ!$B$37=K1183),ЦИКЛ!$I$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$11,ЦИКЛ!$D$3=M1183,,ЦИКЛ!$B$37=K1183),ЦИКЛ!$D$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$11,ЦИКЛ!$E$3=M1183,ЦИКЛ!$B$37=K1183),ЦИКЛ!$E$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$11,ЦИКЛ!$F$3=M1183,ЦИКЛ!$B$37=K1183),ЦИКЛ!$F$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$11,ЦИКЛ!$G$3=M1183,ЦИКЛ!$B$37=K1183),ЦИКЛ!$G$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$11,ЦИКЛ!$H$3=M1183,ЦИКЛ!$B$37=K1183),ЦИКЛ!$H$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$11,ЦИКЛ!$I$3=M1183,ЦИКЛ!$B$37=K1183),ЦИКЛ!$I$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$53,ЦИКЛ!$D$3=M1183,ЦИКЛ!$B$37=K1183),ЦИКЛ!$D$61,IF(AND(АВР!$AD$8=ЦИКЛ!$A$53,ЦИКЛ!$E$3=M1183,ЦИКЛ!$B$37=K1183),ЦИКЛ!$E$61,IF(AND(АВР!$AD$8=ЦИКЛ!$A$53,ЦИКЛ!$F$3=M1183,ЦИКЛ!$B$37=K1183),ЦИКЛ!$F$61,IF(AND(АВР!$AD$8=ЦИКЛ!$A$53,ЦИКЛ!$G$3=M1183,ЦИКЛ!$B$37=K1183),ЦИКЛ!$G$61,IF(AND(АВР!$AD$8=ЦИКЛ!$A$53,ЦИКЛ!$H$3=M1183,ЦИКЛ!$B$37=K1183),ЦИКЛ!$H$61,IF(AND(АВР!$AD$8=ЦИКЛ!$A$53,ЦИКЛ!$I$3=M1183,ЦИКЛ!$B$37=K1183),ЦИКЛ!$I$61,IF(AND(АВР!$AD$8=ЦИКЛ!$A$71,ЦИКЛ!$D$3=M1183,ЦИКЛ!$B$37=K1183),ЦИКЛ!$D$79,IF(AND(АВР!$AD$8=ЦИКЛ!$A$71,ЦИКЛ!$E$3=M1183,ЦИКЛ!$B$37=K1183),ЦИКЛ!$E$79,IF(AND(АВР!$AD$8=ЦИКЛ!$A$71,ЦИКЛ!$F$3=M1183,ЦИКЛ!$B$37=K1183),ЦИКЛ!$F$79,IF(AND(АВР!$AD$8=ЦИКЛ!$A$71,ЦИКЛ!$G$3=M1183,ЦИКЛ!$B$37=K1183),ЦИКЛ!$G$79,IF(AND(АВР!$AD$8=ЦИКЛ!$A$71,ЦИКЛ!$H$3=M1183,ЦИКЛ!$B$37=K1183),ЦИКЛ!$H$79,IF(AND(АВР!$AD$8=ЦИКЛ!$A$71,ЦИКЛ!$I$3=M1183,ЦИКЛ!$B$37=K1183),ЦИКЛ!$I$79,IF(AND(АВР!$AD$8=ЦИКЛ!$A$89,ЦИКЛ!$D$3=M1183,ЦИКЛ!$B$37=K1183),ЦИКЛ!$D$97,IF(AND(АВР!$AD$8=ЦИКЛ!$A$89,ЦИКЛ!$E$3=M1183,ЦИКЛ!$B$37=K1183),ЦИКЛ!$E$97,IF(AND(АВР!$AD$8=ЦИКЛ!$A$89,ЦИКЛ!$F$3=M1183,ЦИКЛ!$B$37=K1183),ЦИКЛ!$F$97,IF(AND(АВР!$AD$8=ЦИКЛ!$A$89,ЦИКЛ!$G$3=M1183,ЦИКЛ!$B$37=K1183),ЦИКЛ!$G$97,IF(AND(АВР!$AD$8=ЦИКЛ!$A$89,ЦИКЛ!$H$3=M1183,ЦИКЛ!$B$37=K1183),ЦИКЛ!$H$97,IF(AND(АВР!$AD$8=ЦИКЛ!$A$89,ЦИКЛ!$I$3=M1183,ЦИКЛ!$B$37=K1183),ЦИКЛ!$I$97,IF(AND(АВР!$AD$8=ЦИКЛ!$A$107,ЦИКЛ!$D$3=M1183,ЦИКЛ!$B$37=K1183),ЦИКЛ!$D$117,IF(AND(АВР!$AD$8=ЦИКЛ!$A$107,ЦИКЛ!$E$3=M1183,ЦИКЛ!$B$37=K1183),ЦИКЛ!$E$117,IF(AND(АВР!$AD$8=ЦИКЛ!$A$107,ЦИКЛ!$F$3=M1183,ЦИКЛ!$B$37=K1183),ЦИКЛ!$F$117,IF(AND(АВР!$AD$8=ЦИКЛ!$A$107,ЦИКЛ!$G$3=M1183,ЦИКЛ!$B$37=K1183),ЦИКЛ!$G$117,IF(AND(АВР!$AD$8=ЦИКЛ!$A$107,ЦИКЛ!$H$3=M1183,ЦИКЛ!$B$37=K1183),ЦИКЛ!$H$117,IF(AND(АВР!$AD$8=ЦИКЛ!$A$107,ЦИКЛ!$I$3=M1183,ЦИКЛ!$B$37=K1183),ЦИКЛ!$I$117,IF(AND(АВР!$AD$8=ЦИКЛ!$A$129,ЦИКЛ!$D$3=M1183,ЦИКЛ!$B$37=K1183),ЦИКЛ!$D$139,IF(AND(АВР!$AD$8=ЦИКЛ!$A$129,ЦИКЛ!$E$3=M1183,ЦИКЛ!$B$37=K1183),ЦИКЛ!$E$139,IF(AND(АВР!$AD$8=ЦИКЛ!$A$129,ЦИКЛ!$F$3=M1183,ЦИКЛ!$B$37=K1183),ЦИКЛ!$F$139,IF(AND(АВР!$AD$8=ЦИКЛ!$A$129,ЦИКЛ!$G$3=M1183,ЦИКЛ!$B$37=K1183),ЦИКЛ!$G$139,IF(AND(АВР!$AD$8=ЦИКЛ!$A$129,ЦИКЛ!$H$3=M1183,ЦИКЛ!$B$37=K1183),ЦИКЛ!$H$139,IF(AND(АВР!$AD$8=ЦИКЛ!$A$129,ЦИКЛ!$I$3=M1183,ЦИКЛ!$B$37=K1183),ЦИКЛ!$I$139))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))',
     1.2, '=V1183*W1183*X1183', '=Y1183-AA1183-AB1183-AC1183-AD1183', None, None, None, None, None],
    ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', 'Перо,воронка', 'Подъем НКТ  3 скорость', None, None, None, None, '73мм',
     1000,
     '=IF(AND(L1184/V1184>=ЦИКЛ!$V$9,L1184/V1184<=ЦИКЛ!$W$9),ЦИКЛ!$U$9,IF(AND(L1184/V1184>=ЦИКЛ!$V$10,L1184/V1184<=ЦИКЛ!$W$10),ЦИКЛ!$U$10,IF(AND(L1184/V1184>=ЦИКЛ!$V$11,L1184/V1184<=ЦИКЛ!$W$11),ЦИКЛ!$U$11,IF(AND(L1184/V1184>=ЦИКЛ!$V$12,L1184/V1184<=ЦИКЛ!$W$12),ЦИКЛ!$U$12,IF(AND(L1184/V1184>=ЦИКЛ!$V$13,L1184/V1184<=ЦИКЛ!$W$13),ЦИКЛ!$U$13,IF(AND(L1184/V1184>=ЦИКЛ!$V$14,L1184/V1184<=ЦИКЛ!$W$14),ЦИКЛ!$U$14))))))',
     '=IF(AND(АВР!$AD$8=ЦИКЛ!$A$6,ЦИКЛ!$D$3=M1184),ЦИКЛ!$J$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$6,ЦИКЛ!$E$3=M1184),ЦИКЛ!$K$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$6,ЦИКЛ!$F$3=M1184),ЦИКЛ!$L$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$6,ЦИКЛ!$G$3=M1184),ЦИКЛ!$M$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$6,ЦИКЛ!$N$3=M1184),ЦИКЛ!$H$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$6,ЦИКЛ!$I$3=M1184),ЦИКЛ!$O$30,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$6,ЦИКЛ!$D$3=M1184),ЦИКЛ!$J$30,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$6,ЦИКЛ!$E$3=M1184),ЦИКЛ!$K$30,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$6,ЦИКЛ!$F$3=M1184),ЦИКЛ!$L$30,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$6,ЦИКЛ!$G$3=M1184),ЦИКЛ!$M$30,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$6,ЦИКЛ!$H$3=M1184),ЦИКЛ!$N$30,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$6,ЦИКЛ!$I$3=M1184),ЦИКЛ!$O$30,IF(AND(АВР!$AD$8=ЦИКЛ!$R$6,ЦИКЛ!$D$3=M1184),ЦИКЛ!$J$30,IF(AND(АВР!$AD$8=ЦИКЛ!$R$6,ЦИКЛ!$E$3=M1184),ЦИКЛ!$K$30,IF(AND(АВР!$AD$8=ЦИКЛ!$R$6,ЦИКЛ!$F$3=M1184),ЦИКЛ!$L$30,IF(AND(АВР!$AD$8=ЦИКЛ!$R$6,ЦИКЛ!$G$3=M1184),ЦИКЛ!$M$30,IF(AND(АВР!$AD$8=ЦИКЛ!$R$6,ЦИКЛ!$H$3=M1184),ЦИКЛ!$N$30,IF(AND(АВР!$AD$8=ЦИКЛ!$R$6,ЦИКЛ!$I$3=M1184),ЦИКЛ!$O$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$9,ЦИКЛ!$D$3=M1184),ЦИКЛ!$J$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$9,ЦИКЛ!$E$3=M1184),ЦИКЛ!$K$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$9,ЦИКЛ!$F$3=M1184),ЦИКЛ!$L$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$9,ЦИКЛ!$G$3=M1184),ЦИКЛ!$M$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$9,ЦИКЛ!$H$3=M1184),ЦИКЛ!$N$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$9,ЦИКЛ!$I$3=M1184),ЦИКЛ!$O$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$12,ЦИКЛ!$D$3=M1184),ЦИКЛ!$J$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$12,ЦИКЛ!$E$3=M1184),ЦИКЛ!$K$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$12,ЦИКЛ!$F$3=M1184),ЦИКЛ!$L$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$12,ЦИКЛ!$G$3=M1184),ЦИКЛ!$M$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$12,ЦИКЛ!$H$3=M1184),ЦИКЛ!$N$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$12,ЦИКЛ!$I$3=M1184),ЦИКЛ!$O$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$54,ЦИКЛ!$D$3=M1184),ЦИКЛ!$J$62,IF(AND(АВР!$AD$8=ЦИКЛ!$A$54,ЦИКЛ!$E$3=M1184),ЦИКЛ!$K$62,IF(AND(АВР!$AD$8=ЦИКЛ!$A$54,ЦИКЛ!$F$3=M1184),ЦИКЛ!$L$62,IF(AND(АВР!$AD$8=ЦИКЛ!$A$54,ЦИКЛ!$G$3=M1184),ЦИКЛ!$M$62,IF(AND(АВР!$AD$8=ЦИКЛ!$A$54,ЦИКЛ!$H$3=M1184),ЦИКЛ!$N$62,IF(AND(АВР!$AD$8=ЦИКЛ!$A$54,ЦИКЛ!$I$3=M1184),ЦИКЛ!$O$62,IF(AND(АВР!$AD$8=ЦИКЛ!$A$72,ЦИКЛ!$D$3=M1184),ЦИКЛ!$J$80,IF(AND(АВР!$AD$8=ЦИКЛ!$A$72,ЦИКЛ!$E$3=M1184),ЦИКЛ!$K$80,IF(AND(АВР!$AD$8=ЦИКЛ!$A$72,ЦИКЛ!$F$3=M1184),ЦИКЛ!$L$80,IF(AND(АВР!$AD$8=ЦИКЛ!$A$72,ЦИКЛ!$G$3=M1184),ЦИКЛ!$M$80,IF(AND(АВР!$AD$8=ЦИКЛ!$A$72,ЦИКЛ!$H$3=M1184),ЦИКЛ!$N$80,IF(AND(АВР!$AD$8=ЦИКЛ!$A$72,ЦИКЛ!$I$3=M1184),ЦИКЛ!$O$80,IF(AND(АВР!$AD$8=ЦИКЛ!$A$90,ЦИКЛ!$D$3=M1184),ЦИКЛ!$J$98,IF(AND(АВР!$AD$8=ЦИКЛ!$A$90,ЦИКЛ!$E$3=M1184),ЦИКЛ!$K$98,IF(AND(АВР!$AD$8=ЦИКЛ!$A$90,ЦИКЛ!$F$3=M1184),ЦИКЛ!$L$98,IF(AND(АВР!$AD$8=ЦИКЛ!$A$90,ЦИКЛ!$G$3=M1184),ЦИКЛ!$M$98,IF(AND(АВР!$AD$8=ЦИКЛ!$A$90,ЦИКЛ!$H$3=M1184),ЦИКЛ!$N$98,IF(AND(АВР!$AD$8=ЦИКЛ!$A$90,ЦИКЛ!$I$3=M1184),ЦИКЛ!$O$98,IF(AND(АВР!$AD$8=ЦИКЛ!$A$108,ЦИКЛ!$D$3=M1184),ЦИКЛ!$J$118,IF(AND(АВР!$AD$8=ЦИКЛ!$A$108,ЦИКЛ!$E$3=M1184),ЦИКЛ!$K$118,IF(AND(АВР!$AD$8=ЦИКЛ!$A$108,ЦИКЛ!$F$3=M1184),ЦИКЛ!$L$118,IF(AND(АВР!$AD$8=ЦИКЛ!$A$108,ЦИКЛ!$G$3=M1184),ЦИКЛ!$M$118,IF(AND(АВР!$AD$8=ЦИКЛ!$A$108,ЦИКЛ!$H$3=M1184),ЦИКЛ!$N$118,IF(AND(АВР!$AD$8=ЦИКЛ!$A$108,ЦИКЛ!$I$3=M1184),ЦИКЛ!$O$118,IF(AND(АВР!$AD$8=ЦИКЛ!$A$130,ЦИКЛ!$D$3=M1184),ЦИКЛ!$J$140,IF(AND(АВР!$AD$8=ЦИКЛ!$A$130,ЦИКЛ!$E$3=M1184),ЦИКЛ!$K$140,IF(AND(АВР!$AD$8=ЦИКЛ!$A$130,ЦИКЛ!$F$3=M1184),ЦИКЛ!$L$140,IF(AND(АВР!$AD$8=ЦИКЛ!$A$130,ЦИКЛ!$G$3=M1184),ЦИКЛ!$M$140,IF(AND(АВР!$AD$8=ЦИКЛ!$A$130,ЦИКЛ!$H$3=M1184),ЦИКЛ!$N$140,IF(AND(АВР!$AD$8=ЦИКЛ!$A$130,ЦИКЛ!$I$3=M1184),ЦИКЛ!$O$140))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))',
     None, None, None, None,
     '=IF($AD$8=ЦИКЛ!$A$4,ЦИКЛ!$P$4,IF($AD$8=ЦИКЛ!$A$7,ЦИКЛ!$P$7,IF($AD$8=ЦИКЛ!$A$10,ЦИКЛ!$P$7,IF($AD$8=ЦИКЛ!$A$52,ЦИКЛ!$P$52,IF($AD$8=ЦИКЛ!$A$70,ЦИКЛ!$P$70,IF($AD$8=ЦИКЛ!$A$88,ЦИКЛ!$P$88,IF($AD$8=ЦИКЛ!$A$106,ЦИКЛ!$P$106,IF($AD$8=ЦИКЛ!$A$133,ЦИКЛ!$P$133,IF($AD$8=ЦИКЛ!$Q$4,ЦИКЛ!$P$4,IF($AD$8=ЦИКЛ!$R$4,ЦИКЛ!$P$4))))))))))',
     None, 'шт', 100,
     '=IF(AND(АВР!$AD$8=ЦИКЛ!$A$6,ЦИКЛ!$D$3=M1184,ЦИКЛ!$B$37=АВР!K1184),ЦИКЛ!$D$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$6,ЦИКЛ!$E$3=M1184,ЦИКЛ!$B$37=АВР!K1184),ЦИКЛ!$E$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$6,ЦИКЛ!$F$3=M1184,ЦИКЛ!$B$37=АВР!K1184),ЦИКЛ!$F$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$6,ЦИКЛ!$G$3=M1184,ЦИКЛ!$B$37=АВР!K1184),ЦИКЛ!$G$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$6,ЦИКЛ!$H$3=M1184,ЦИКЛ!$B$37=АВР!K1184),ЦИКЛ!$H$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$6,ЦИКЛ!$I$3=M1184,ЦИКЛ!$B$37=АВР!K1184),ЦИКЛ!$I$30,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$6,ЦИКЛ!$D$3=M1184,ЦИКЛ!$B$37=АВР!K1184),ЦИКЛ!$D$30,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$6,ЦИКЛ!$E$3=M1184,ЦИКЛ!$B$37=АВР!K1184),ЦИКЛ!$E$30,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$6,ЦИКЛ!$F$3=M1184,ЦИКЛ!$B$37=АВР!K1184),ЦИКЛ!$F$30,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$6,ЦИКЛ!$G$3=M1184,ЦИКЛ!$B$37=АВР!K1184),ЦИКЛ!$G$30,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$6,ЦИКЛ!$H$3=M1184,ЦИКЛ!$B$37=АВР!K1184),ЦИКЛ!$H$30,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$6,ЦИКЛ!$I$3=M1184,ЦИКЛ!$B$37=АВР!K1184),ЦИКЛ!$I$30,IF(AND(АВР!$AD$8=ЦИКЛ!$R$6,ЦИКЛ!$D$3=M1184,ЦИКЛ!$B$37=АВР!K1184),ЦИКЛ!$D$30,IF(AND(АВР!$AD$8=ЦИКЛ!$R$6,ЦИКЛ!$E$3=M1184,ЦИКЛ!$B$37=АВР!K1184),ЦИКЛ!$E$30,IF(AND(АВР!$AD$8=ЦИКЛ!$R$6,ЦИКЛ!$F$3=M1184,ЦИКЛ!$B$37=АВР!K1184),ЦИКЛ!$F$30,IF(AND(АВР!$AD$8=ЦИКЛ!$R$6,ЦИКЛ!$G$3=M1184,ЦИКЛ!$B$37=АВР!K1184),ЦИКЛ!$G$30,IF(AND(АВР!$AD$8=ЦИКЛ!$R$6,ЦИКЛ!$H$3=M1184,ЦИКЛ!$B$37=АВР!K1184),ЦИКЛ!$H$30,IF(AND(АВР!$AD$8=ЦИКЛ!$R$6,ЦИКЛ!$I$3=M1184,ЦИКЛ!$B$37=АВР!K1184),ЦИКЛ!$I$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$9,ЦИКЛ!$D$3=M1184,ЦИКЛ!$B$37=АВР!K1184),ЦИКЛ!$D$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$9,ЦИКЛ!$E$3=M1184,ЦИКЛ!$B$37=АВР!K1184),ЦИКЛ!$E$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$9,ЦИКЛ!$F$3=M1184,ЦИКЛ!$B$37=АВР!K1184),ЦИКЛ!$F$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$21,ЦИКЛ!$G$3=M1184,ЦИКЛ!$B$37=АВР!K1184),ЦИКЛ!$G$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$9,ЦИКЛ!$H$3=M1184,ЦИКЛ!$B$37=АВР!K1184),ЦИКЛ!$H$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$9,ЦИКЛ!$I$3=M1184,ЦИКЛ!$B$37=АВР!K1184),ЦИКЛ!$I$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$12,ЦИКЛ!$D$3=M1184,ЦИКЛ!$B$37=АВР!K1184),ЦИКЛ!$D$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$12,ЦИКЛ!$E$3=M1184,ЦИКЛ!$B$37=АВР!K1184),ЦИКЛ!$E$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$12,ЦИКЛ!$F$3=M1184,ЦИКЛ!$B$37=АВР!K1184),ЦИКЛ!$F$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$12,ЦИКЛ!$G$3=M1184,ЦИКЛ!$B$37=АВР!K1184),ЦИКЛ!$G$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$12,ЦИКЛ!$H$3=M1184,ЦИКЛ!$B$37=АВР!K1184),ЦИКЛ!$H$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$12,ЦИКЛ!$I$3=M1184,ЦИКЛ!$B$37=АВР!K1184),ЦИКЛ!$I$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$54,ЦИКЛ!$D$3=M1184,ЦИКЛ!$B$37=АВР!K1184),ЦИКЛ!$D$62,IF(AND(АВР!$AD$8=ЦИКЛ!$A$54,ЦИКЛ!$E$3=M1184,ЦИКЛ!$B$37=АВР!K1184),ЦИКЛ!$E$62,IF(AND(АВР!$AD$8=ЦИКЛ!$A$54,ЦИКЛ!$F$3=M1184,ЦИКЛ!$B$37=АВР!K1184),ЦИКЛ!$F$62,IF(AND(АВР!$AD$8=ЦИКЛ!$A$54,ЦИКЛ!$G$3=M1184,ЦИКЛ!$B$37=АВР!K1184),ЦИКЛ!$G$62,IF(AND(АВР!$AD$8=ЦИКЛ!$A$54,ЦИКЛ!$H$3=M1184,ЦИКЛ!$B$37=АВР!K1184),ЦИКЛ!$H$62,IF(AND(АВР!$AD$8=ЦИКЛ!$A$54,ЦИКЛ!$I$3=M1184,ЦИКЛ!$B$37=АВР!K1184),ЦИКЛ!$I$62,IF(AND(АВР!$AD$8=ЦИКЛ!$A$72,ЦИКЛ!$D$3=M1184,ЦИКЛ!$B$37=АВР!K1184),ЦИКЛ!$D$80,IF(AND(АВР!$AD$8=ЦИКЛ!$A$72,ЦИКЛ!$E$3=M1184,ЦИКЛ!$B$37=АВР!K1184),ЦИКЛ!$E$80,IF(AND(АВР!$AD$8=ЦИКЛ!$A$72,ЦИКЛ!$F$3=M1184,ЦИКЛ!$B$37=АВР!K1184),ЦИКЛ!$F$80,IF(AND(АВР!$AD$8=ЦИКЛ!$A$72,ЦИКЛ!$G$3=M1184,ЦИКЛ!$B$37=АВР!K1184),ЦИКЛ!$G$80,IF(AND(АВР!$AD$8=ЦИКЛ!$A$72,ЦИКЛ!$H$3=M1184,ЦИКЛ!$B$37=АВР!K1184),ЦИКЛ!$H$80,IF(AND(АВР!$AD$8=ЦИКЛ!$A$72,ЦИКЛ!$I$3=M1184,ЦИКЛ!$B$37=АВР!K1184),ЦИКЛ!$I$80,IF(AND(АВР!$AD$8=ЦИКЛ!$A$90,ЦИКЛ!$D$3=M1184,ЦИКЛ!$B$37=АВР!K1184),ЦИКЛ!$D$98,IF(AND(АВР!$AD$8=ЦИКЛ!$A$90,ЦИКЛ!$E$3=M1184,ЦИКЛ!$B$37=АВР!K1184),ЦИКЛ!$E$98,IF(AND(АВР!$AD$8=ЦИКЛ!$A$90,ЦИКЛ!$F$3=M1184,ЦИКЛ!$B$37=АВР!K1184),ЦИКЛ!$F$98,IF(AND(АВР!$AD$8=ЦИКЛ!$A$90,ЦИКЛ!$G$3=M1184,ЦИКЛ!$B$37=АВР!K1184),ЦИКЛ!$G$98,IF(AND(АВР!$AD$8=ЦИКЛ!$A$90,ЦИКЛ!$H$3=M1184,ЦИКЛ!$B$37=АВР!K1184),ЦИКЛ!$H$98,IF(AND(АВР!$AD$8=ЦИКЛ!$A$90,ЦИКЛ!$I$3=M1184,ЦИКЛ!$B$37=АВР!K1184),ЦИКЛ!$I$98,IF(AND(АВР!$AD$8=ЦИКЛ!$A$113,ЦИКЛ!$D$3=M1184,ЦИКЛ!$B$37=АВР!K1184),ЦИКЛ!$D$118,IF(AND(АВР!$AD$8=ЦИКЛ!$A$108,ЦИКЛ!$E$3=M1184,ЦИКЛ!$B$37=АВР!K1184),ЦИКЛ!$E$118,IF(AND(АВР!$AD$8=ЦИКЛ!$A$113,ЦИКЛ!$F$3=M1184,ЦИКЛ!$B$37=АВР!K1184),ЦИКЛ!$F$118,IF(AND(АВР!$AD$8=ЦИКЛ!$A$108,ЦИКЛ!$G$3=M1184,ЦИКЛ!$B$37=АВР!K1184),ЦИКЛ!$G$118,IF(AND(АВР!$AD$8=ЦИКЛ!$A$113,ЦИКЛ!$H$3=M1184,ЦИКЛ!$B$37=АВР!K1184),ЦИКЛ!$H$118,IF(AND(АВР!$AD$8=ЦИКЛ!$A$108,ЦИКЛ!$I$3=M1184,ЦИКЛ!$B$37=АВР!K1184),ЦИКЛ!$I$118,IF(AND(АВР!$AD$8=ЦИКЛ!$A$135,ЦИКЛ!$D$3=M1184,ЦИКЛ!$B$37=АВР!K1184),ЦИКЛ!$D$140,IF(AND(АВР!$AD$8=ЦИКЛ!$A$130,ЦИКЛ!$E$3=M1184,ЦИКЛ!$B$37=АВР!K1184),ЦИКЛ!$E$140,IF(AND(АВР!$AD$8=ЦИКЛ!$A$135,ЦИКЛ!$F$3=M1184,ЦИКЛ!$B$37=АВР!K1184),ЦИКЛ!$F$140,IF(AND(АВР!$AD$8=ЦИКЛ!$A$130,ЦИКЛ!$G$3=M1184,ЦИКЛ!$B$37=АВР!K1184),ЦИКЛ!$G$140,IF(AND(АВР!$AD$8=ЦИКЛ!$A$135,ЦИКЛ!$H$3=M1184,ЦИКЛ!$B$37=АВР!K1184),ЦИКЛ!$H$140,IF(AND(АВР!$AD$8=ЦИКЛ!$A$130,ЦИКЛ!$I$3=M1184,ЦИКЛ!$B$37=АВР!K1184),ЦИКЛ!$I$140))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))',
     1.2, '=V1184*W1184*X1184', '=Y1184-AA1184-AB1184-AC1184-AD1184', None, None, None, None, None],
    ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', 'Перо,воронка', 'Подъем НКТ  4 скорость', None, None, None, None, '73мм',
     1000,
     '=IF(AND(L1185/V1185>=ЦИКЛ!$V$9,L1185/V1185<=ЦИКЛ!$W$9),ЦИКЛ!$U$9,IF(AND(L1185/V1185>=ЦИКЛ!$V$10,L1185/V1185<=ЦИКЛ!$W$10),ЦИКЛ!$U$10,IF(AND(L1185/V1185>=ЦИКЛ!$V$11,L1185/V1185<=ЦИКЛ!$W$11),ЦИКЛ!$U$11,IF(AND(L1185/V1185>=ЦИКЛ!$V$12,L1185/V1185<=ЦИКЛ!$W$12),ЦИКЛ!$U$12,IF(AND(L1185/V1185>=ЦИКЛ!$V$13,L1185/V1185<=ЦИКЛ!$W$13),ЦИКЛ!$U$13,IF(AND(L1185/V1185>=ЦИКЛ!$V$14,L1185/V1185<=ЦИКЛ!$W$14),ЦИКЛ!$U$14))))))',
     '=IF(AND(АВР!$AD$8=ЦИКЛ!$A$109,ЦИКЛ!$D$3=M1185),ЦИКЛ!$J$119,IF(AND(АВР!$AD$8=ЦИКЛ!$A$109,ЦИКЛ!$E$3=M1185),ЦИКЛ!$K$119,IF(AND(АВР!$AD$8=ЦИКЛ!$A$109,ЦИКЛ!$F$3=M1185),ЦИКЛ!$L$119,IF(AND(АВР!$AD$8=ЦИКЛ!$A$109,ЦИКЛ!$G$3=M1185),ЦИКЛ!$M$119,IF(AND(АВР!$AD$8=ЦИКЛ!$A$109,ЦИКЛ!$H$3=M1185),ЦИКЛ!$N$119,IF(AND(АВР!$AD$8=ЦИКЛ!$A$109,ЦИКЛ!$I$3=M1185),ЦИКЛ!$O$119,IF(AND(АВР!$AD$8=ЦИКЛ!$A$131,ЦИКЛ!$D$3=M1185),ЦИКЛ!$J$141,IF(AND(АВР!$AD$8=ЦИКЛ!$A$131,ЦИКЛ!$E$3=M1185),ЦИКЛ!$K$141,IF(AND(АВР!$AD$8=ЦИКЛ!$A$131,ЦИКЛ!$F$3=M1185),ЦИКЛ!$L$141,IF(AND(АВР!$AD$8=ЦИКЛ!$A$131,ЦИКЛ!$G$3=M1185),ЦИКЛ!$M$141,IF(AND(АВР!$AD$8=ЦИКЛ!$A$131,ЦИКЛ!$H$3=M1185),ЦИКЛ!$N$141,IF(AND(АВР!$AD$8=ЦИКЛ!$A$131,ЦИКЛ!$I$3=M1185),ЦИКЛ!$O$141))))))))))))',
     None, None, None, None,
     '=IF($AD$8=ЦИКЛ!$A$4,ЦИКЛ!$P$4,IF($AD$8=ЦИКЛ!$A$7,ЦИКЛ!$P$7,IF($AD$8=ЦИКЛ!$A$10,ЦИКЛ!$P$7,IF($AD$8=ЦИКЛ!$A$52,ЦИКЛ!$P$52,IF($AD$8=ЦИКЛ!$A$70,ЦИКЛ!$P$70,IF($AD$8=ЦИКЛ!$A$88,ЦИКЛ!$P$88,IF($AD$8=ЦИКЛ!$A$106,ЦИКЛ!$P$106,IF($AD$8=ЦИКЛ!$A$133,ЦИКЛ!$P$133,IF($AD$8=ЦИКЛ!$Q$4,ЦИКЛ!$P$4,IF($AD$8=ЦИКЛ!$R$4,ЦИКЛ!$P$4))))))))))',
     None, 'шт', 100,
     '=IF(AND(АВР!$AD$8=ЦИКЛ!$A$109,ЦИКЛ!$D$3=M1185,ЦИКЛ!$B$37=АВР!K1185),ЦИКЛ!$D$119,IF(AND(АВР!$AD$8=ЦИКЛ!$A$109,ЦИКЛ!$E$3=M1185,ЦИКЛ!$B$37=АВР!K1185),ЦИКЛ!$E$119,IF(AND(АВР!$AD$8=ЦИКЛ!$A$109,ЦИКЛ!$F$3=M1185,ЦИКЛ!$B$37=АВР!K1185),ЦИКЛ!$F$119,IF(AND(АВР!$AD$8=ЦИКЛ!$A$109,ЦИКЛ!$G$3=M1185,ЦИКЛ!$B$37=АВР!K1185),ЦИКЛ!$G$119,IF(AND(АВР!$AD$8=ЦИКЛ!$A$109,ЦИКЛ!$H$3=M1185,ЦИКЛ!$B$37=АВР!K1185),ЦИКЛ!$H$119,IF(AND(АВР!$AD$8=ЦИКЛ!$A$109,ЦИКЛ!$I$3=M1185,ЦИКЛ!$B$37=АВР!K1185),ЦИКЛ!$I$119,IF(AND(АВР!$AD$8=ЦИКЛ!$A$131,ЦИКЛ!$D$3=M1185,ЦИКЛ!$B$37=АВР!K1185),ЦИКЛ!$D$141,IF(AND(АВР!$AD$8=ЦИКЛ!$A$131,ЦИКЛ!$E$3=M1185,ЦИКЛ!$B$37=АВР!K1185),ЦИКЛ!$E$141,IF(AND(АВР!$AD$8=ЦИКЛ!$A$131,ЦИКЛ!$F$3=M1185,ЦИКЛ!$B$37=АВР!K1185),ЦИКЛ!$F$141,IF(AND(АВР!$AD$8=ЦИКЛ!$A$131,ЦИКЛ!$G$3=M1185,ЦИКЛ!$B$37=АВР!K1185),ЦИКЛ!$G$141,IF(AND(АВР!$AD$8=ЦИКЛ!$A$131,ЦИКЛ!$H$3=M1185,ЦИКЛ!$B$37=АВР!K1185),ЦИКЛ!$H$141,IF(AND(АВР!$AD$8=ЦИКЛ!$A$131,ЦИКЛ!$I$3=M1185,ЦИКЛ!$B$37=АВР!K1185),ЦИКЛ!$I$141))))))))))))',
     1.2, '=V1185*W1185*X1185', '=Y1185-AA1185-AB1185-AC1185-AD1185', None, None, None, None, None],
    ['=ROW()-ROW($A$56)', None, None, 'спо', 'Перо,воронка', 'Долив скважины', None, None, None, None, None, None, None,
     None, None, None, None, None, '§168разд.1', None, 'шт', '=((SUM(V1182:V1185))/10)', 0.003, 1, '=V1186*W1186*X1186',
     '=Y1186-AA1186-AB1186-AC1186-AD1186', None, None, None, None, None],
    ['=ROW()-ROW($A$56)', 'подъем 73мм', None, 'спо', 'Перо,воронка', 'Откатывание труб с 201 трубы ', None, None, None,
     None, None, None, None, None, None, None, None, None, '§40разд.1', None, 'шт', '=((SUM(V1182:V1185))-201)', 0.008,
     1, '=V1187*W1187*X1187', '=Y1187-AA1187-AB1187-AC1187-AD1187', None, None, None, None, None],
    ['=ROW()-ROW($A$56)', None, None, 'спо', 'Перо,воронка', 'Осложнение при подъеме НКТ', None, None, None, None, None,
     None, 'Объем', 0, None, None, None, None, 'факт', None, 'час', 0, 1, 1, '=V1188*W1188*X1188',
     '=Y1188-AA1188-AB1188-AC1188-AD1188', None, None, None, None, None]]

if __name__ == "__main__":
    # app3 = QApplication(sys.argv)

    app = QApplication(sys.argv)
    window = PipePerforator(22, 22)
    window.show()
    sys.exit(app.exec_())
