import sys
from datetime import datetime, timedelta

import well_data

from collections import namedtuple
from normir.files_with_list import cause_presence_of_jamming, drilling_ek_list

from PyQt5.QtGui import QIntValidator, QDoubleValidator
from PyQt5.QtWidgets import QWidget, QLabel, QComboBox, QLineEdit, QGridLayout, QTabWidget, QMainWindow, QPushButton, \
    QMessageBox, QApplication, QHeaderView, QTableWidget, QTableWidgetItem, QTextEdit, QDateEdit, QDateTimeEdit
from normir.template_without_skm import TemplateWithoutSKM
from PyQt5.QtCore import Qt

from normir.relocation_brigade import TextEditTableWidgetItem


class TabPage_SO_Timplate(QWidget):
    def __init__(self, parent=None):
        super().__init__()

        self.validator_int = QIntValidator(0, 6000)
        self.validator_float = QDoubleValidator(0, 6000, 1)

        self.date_work_label = QLabel('Дата работы')
        self.date_work_line = QLineEdit(self)
        self.date_work_line.setText(f'{well_data.date_work}')

        self.date_work_str = datetime.strptime(self.date_work_line.text(), '%d.%m.%Y')

        self.select_type_combo_label = QLabel('Выбор компоновки спуска')
        self.select_type_combo = QComboBox(self)
        self.select_type_combo.addItems(['', 'НКТ'])

        self.grid = QGridLayout(self)

        self.grid.addWidget(self.date_work_label, 4, 2)
        self.grid.addWidget(self.date_work_line, 5, 2)

        self.grid.addWidget(self.select_type_combo_label, 4, 3)
        self.grid.addWidget(self.select_type_combo, 5, 3)

        self.select_type_combo.currentTextChanged.connect(self.update_select_type_combo)

        if well_data.date_work != '':
            self.date_work_line.setText(well_data.date_work)

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
            self.nkt_48_lenght_edit = QLineEdit(self)
            self.nkt_48_lenght_edit.setValidator(self.validator_int)

            self.nkt_48_count_edit = QLineEdit(self)
            self.nkt_48_count_edit.setValidator(self.validator_int)

            self.nkt_60_lenght_edit = QLineEdit(self)
            self.nkt_60_lenght_edit.setValidator(self.validator_int)

            self.nkt_60_count_edit = QLineEdit(self)
            self.nkt_60_count_edit.setValidator(self.validator_int)

            self.nkt_73_lenght_edit = QLineEdit(self)
            self.nkt_73_lenght_edit.setValidator(self.validator_int)

            self.nkt_73_count_edit = QLineEdit(self)
            self.nkt_73_count_edit.setValidator(self.validator_int)

            self.nkt_89_lenght_edit = QLineEdit(self)
            self.nkt_89_lenght_edit.setValidator(self.validator_int)

            self.nkt_89_count_edit = QLineEdit(self)
            self.nkt_89_count_edit.setValidator(self.validator_int)

            self.grid.addWidget(self.nkt_48_lenght_label, 22, 1)
            self.grid.addWidget(self.nkt_48_lenght_edit, 23, 1)

            self.grid.addWidget(self.nkt_48_count_label, 24, 1)
            self.grid.addWidget(self.nkt_48_count_edit, 25, 1)

            self.grid.addWidget(self.nkt_60_lenght_label, 22, 2)
            self.grid.addWidget(self.nkt_60_lenght_edit, 23, 2)

            self.grid.addWidget(self.nkt_60_count_label, 24, 2)
            self.grid.addWidget(self.nkt_60_count_edit, 25, 2)

            self.grid.addWidget(self.nkt_73_lenght_label, 22, 3)
            self.grid.addWidget(self.nkt_73_lenght_edit, 23, 3)

            self.grid.addWidget(self.nkt_73_count_label, 24, 3)
            self.grid.addWidget(self.nkt_73_count_edit, 25, 3)

            self.grid.addWidget(self.nkt_89_lenght_label, 22, 4)
            self.grid.addWidget(self.nkt_89_lenght_edit, 23, 4)

            self.grid.addWidget(self.nkt_89_count_label, 24, 4)
            self.grid.addWidget(self.nkt_89_count_edit, 25, 4)

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
        #
        # self.technological_crap_question_combo = QComboBox(self)
        # self.technological_crap_question_combo.addItems(['Нет', 'Да'])
        #
        # self.grid.addWidget(self.technological_crap_question_label, 52, 1)
        # self.grid.addWidget(self.technological_crap_question_combo, 53, 1)

        self.equipment_audit_label = QLabel('Была ли ревизия')
        self.equipment_audit_combo = QComboBox(self)
        self.equipment_audit_combo.addItems(['Нет', 'Да'])

        self.grid.addWidget(self.equipment_audit_label, 54, 1)
        self.grid.addWidget(self.equipment_audit_combo, 55, 1)

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

    def update_equipment_audit_combo(self, index):
        if index == 'Нет':
            self.equipment_audit_text_label.setParent(None)
            self.equipment_audit_text_line.setParent(None)
        else:

            self.equipment_audit_text_label = QLabel('Текст ревизии')
            self.equipment_audit_text_line = QLineEdit(self)

            self.grid.addWidget(self.equipment_audit_text_label, 54, 3)
            self.grid.addWidget(self.equipment_audit_text_line, 55, 3)

    def update_nkt_is_same_combo(self, index):
        if index == 'Да':
            self.nkt_48_lenght_up_label.setParent(None)
            self.nkt_48_lenght_up_edit.setParent(None)

            self.nkt_48_count_up_label.setParent(None)
            self.nkt_48_count_up_edit.setParent(None)

            self.nkt_60_lenght_up_label.setParent(None)
            self.nkt_60_lenght_up_edit.setParent(None)

            self.nkt_60_count_up_label.setParent(None)
            self.nkt_60_count_up_edit.setParent(None)

            self.nkt_73_lenght_up_label.setParent(None)
            self.nkt_73_lenght_up_edit.setParent(None)

            self.nkt_73_count_up_label.setParent(None)
            self.nkt_73_count_up_edit.setParent(None)

            self.nkt_89_lenght_up_label.setParent(None)
            self.nkt_89_lenght_up_edit.setParent(None)

            self.nkt_89_count_up_label.setParent(None)
            self.nkt_89_count_up_edit.setParent(None)

        else:
            self.nkt_48_lenght_up_label = QLabel('Длина на подьем НКТ48')
            self.nkt_48_lenght_up_edit = QLineEdit(self)
            self.nkt_48_lenght_up_edit.setValidator(self.validator_int)

            self.nkt_48_count_up_label = QLabel('Кол-во на подьем НКТ48')
            self.nkt_48_count_up_edit = QLineEdit(self)
            self.nkt_48_count_up_edit.setValidator(self.validator_int)

            self.nkt_60_lenght_up_label = QLabel('Длина на подьем НКТ60')
            self.nkt_60_lenght_up_edit = QLineEdit(self)
            self.nkt_60_lenght_up_edit.setValidator(self.validator_int)

            self.nkt_60_count_up_label = QLabel('Кол-во на подьем НКТ60')
            self.nkt_60_count_up_edit = QLineEdit(self)
            self.nkt_60_count_up_edit.setValidator(self.validator_int)

            self.nkt_73_lenght_up_label = QLabel('Длина НКТ73')
            self.nkt_73_lenght_up_edit = QLineEdit(self)
            self.nkt_73_lenght_up_edit.setValidator(self.validator_int)

            self.nkt_73_count_up_label = QLabel('Кол-во НКТ73')
            self.nkt_73_count_up_edit = QLineEdit(self)
            self.nkt_73_count_up_edit.setValidator(self.validator_int)

            self.nkt_89_lenght_up_label = QLabel('Длина НКТ89-102')
            self.nkt_89_lenght_up_edit = QLineEdit(self)
            self.nkt_89_lenght_up_edit.setValidator(self.validator_int)

            self.nkt_89_count_up_label = QLabel('Кол-во НКТ89-102')
            self.nkt_89_count_up_edit = QLineEdit(self)
            self.nkt_89_count_up_edit.setValidator(self.validator_int)

            self.grid.addWidget(self.nkt_48_lenght_up_label, 36, 1)
            self.grid.addWidget(self.nkt_48_lenght_up_edit, 37, 1)

            self.grid.addWidget(self.nkt_48_count_up_label, 38, 1)
            self.grid.addWidget(self.nkt_48_count_up_edit, 39, 1)

            self.grid.addWidget(self.nkt_60_lenght_up_label, 36, 2)
            self.grid.addWidget(self.nkt_60_lenght_up_edit, 37, 2)

            self.grid.addWidget(self.nkt_60_count_up_label, 38, 2)
            self.grid.addWidget(self.nkt_60_count_up_edit, 39, 2)

            self.grid.addWidget(self.nkt_73_lenght_up_label, 36, 3)
            self.grid.addWidget(self.nkt_73_lenght_up_edit, 37, 3)

            self.grid.addWidget(self.nkt_73_count_up_label, 38, 3)
            self.grid.addWidget(self.nkt_73_count_up_edit, 39, 3)

            self.grid.addWidget(self.nkt_89_lenght_up_label, 36, 4)
            self.grid.addWidget(self.nkt_89_lenght_up_edit, 37, 4)

            self.grid.addWidget(self.nkt_89_count_up_label, 38, 4)
            self.grid.addWidget(self.nkt_89_count_up_edit, 39, 4)

    def update_complications_of_failure(self, index):

        if index == 'Нет':
            self.complications_of_failure_text_label.setParent(None)
            self.complications_of_failure_text_line.setParent(None)
            self.complications_of_failure_time_label.setParent(None)
            self.complications_of_failure_time_line.setParent(None)
            self.complications_of_failure_time_end_label.setParent(None)
            self.complications_of_failure_time_end_date.setParent(None)
            self.complications_of_failure_time_begin_label.setParent(None)
            self.complications_of_failure_time_begin_date.setParent(None)
        else:
            self.complications_of_failure_text_label = QLabel('Текст осложнения')
            self.complications_of_failure_text_line = QLineEdit(self)

            self.complications_of_failure_time_begin_label = QLabel('начало осложнения')
            self.complications_of_failure_time_begin_date = QDateTimeEdit(self)
            self.complications_of_failure_time_begin_date.setDisplayFormat("dd.MM.yyyy HH:mm")
            self.complications_of_failure_time_begin_date.setDateTime(self.date_work_str)

            self.complications_of_failure_time_end_label = QLabel('Окончание осложнения')
            self.complications_of_failure_time_end_date = QDateTimeEdit(self)
            self.complications_of_failure_time_end_date.setDisplayFormat("dd.MM.yyyy HH:mm")
            self.complications_of_failure_time_end_date.setDateTime(self.date_work_str)

            self.complications_of_failure_time_label = QLabel('затраченное время')
            self.complications_of_failure_time_line = QLineEdit(self)
            self.complications_of_failure_time_line.setValidator(self.validator_float)

            self.grid.addWidget(self.complications_of_failure_text_label, 28, 2)
            self.grid.addWidget(self.complications_of_failure_text_line, 29, 2)
            self.grid.addWidget(self.complications_of_failure_time_begin_label, 28, 3)
            self.grid.addWidget(self.complications_of_failure_time_begin_date, 29, 3)
            self.grid.addWidget(self.complications_of_failure_time_end_label, 28, 4)
            self.grid.addWidget(self.complications_of_failure_time_end_date, 29, 4)
            self.grid.addWidget(self.complications_of_failure_time_label, 28, 5)
            self.grid.addWidget(self.complications_of_failure_time_line, 29, 5)

            self.complications_of_failure_time_end_date.dateTimeChanged.connect(self.update_date_of_failure)
            self.complications_of_failure_time_begin_date.dateTimeChanged.connect(self.update_date_of_failure)


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

            self.installation_pipe_perforator_time_begin_label = QLabel('начало реагирования')
            self.installation_pipe_perforator_time_begin_date = QDateTimeEdit(self)
            self.installation_pipe_perforator_time_begin_date.setDisplayFormat("dd.MM.yyyy HH:mm")
            self.installation_pipe_perforator_time_begin_date.setDateTime(self.date_work_str)

            self.installation_pipe_perforator_time_end_label = QLabel('Окончание реагирования')
            self.installation_pipe_perforator_time_end_date = QDateTimeEdit(self)
            self.installation_pipe_perforator_time_end_date.setDisplayFormat("dd.MM.yyyy HH:mm")
            self.installation_pipe_perforator_time_end_date.setDateTime(self.date_work_str)

            self.installation_pipe_perforator_time_label = QLabel('затраченное время реагирования')
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

    def update_technological_crap_question_combo(self, index):

        if index == 'Нет':
            self.technological_crap_question_text_label.setParent(None)
            self.technological_crap_question_text_line.setParent(None)
            self.technological_crap_question_time_label.setParent(None)
            self.technological_crap_question_time_line.setParent(None)
            self.technological_crap_question_time_end_label.setParent(None)
            self.technological_crap_question_time_end_date.setParent(None)
            self.technological_crap_question_time_begin_label.setParent(None)
            self.technological_crap_question_time_begin_date.setParent(None)
            self.roof_definition_depth_label.setParent(None)
            self.roof_definition_depth_line.setParent(None)
            self.count_nkt_label.setParent(None)
            self.count_nkt_line.setParent(None)

        else:
            self.technological_crap_question_text_label = QLabel('Текст осложнения')
            self.technological_crap_question_text_line = QLineEdit(self)
            self.technological_crap_question_text_line.setText('Тех отстой')

            self.technological_crap_question_time_begin_label = QLabel('начало осложнения')
            self.technological_crap_question_time_begin_date = QDateTimeEdit(self)
            self.technological_crap_question_time_begin_date.setDisplayFormat("dd.MM.yyyy HH:mm")
            self.technological_crap_question_time_begin_date.setDateTime(self.date_work_str)

            self.technological_crap_question_time_end_label = QLabel('Окончание осложнения')
            self.technological_crap_question_time_end_date = QDateTimeEdit(self)
            self.technological_crap_question_time_end_date.setDisplayFormat("dd.MM.yyyy HH:mm")
            self.technological_crap_question_time_end_date.setDateTime(self.date_work_str)

            self.technological_crap_question_time_label = QLabel('затраченное время')
            self.technological_crap_question_time_line = QLineEdit(self)
            self.technological_crap_question_time_line.setValidator(self.validator_float)

            self.count_nkt_label = QLabel('Количество НКТ')
            self.count_nkt_line = QLineEdit(self)
            self.count_nkt_line.setValidator(self.validator_int)
            self.count_nkt_line.setText('3')

            self.roof_definition_depth_label = QLabel('Глубина определения кровля')
            self.roof_definition_depth_line = QLineEdit(self)
            self.roof_definition_depth_line.setValidator(self.validator_float)

            self.grid.addWidget(self.technological_crap_question_text_label, 52, 2)
            self.grid.addWidget(self.technological_crap_question_text_line, 53, 2)
            self.grid.addWidget(self.technological_crap_question_time_begin_label, 52, 3)
            self.grid.addWidget(self.technological_crap_question_time_begin_date, 53, 3)
            self.grid.addWidget(self.technological_crap_question_time_end_label, 52, 4)
            self.grid.addWidget(self.technological_crap_question_time_end_date, 53, 4)
            self.grid.addWidget(self.technological_crap_question_time_label, 52, 5)
            self.grid.addWidget(self.technological_crap_question_time_line, 53, 5)
            self.grid.addWidget(self.count_nkt_label, 52, 6)
            self.grid.addWidget(self.count_nkt_line, 53, 6)
            self.grid.addWidget(self.roof_definition_depth_label, 52, 7)
            self.grid.addWidget(self.roof_definition_depth_line, 53, 7)

            self.technological_crap_question_time_end_date.dateTimeChanged.connect(self.update_date_technological_crap)
            self.technological_crap_question_time_begin_date.dateTimeChanged.connect(
                self.update_date_technological_crap)

    def update_complications_during_tubing_running_combo(self, index):

        if index == 'Нет':
            self.complications_during_tubing_running_text_label.setParent(None)
            self.complications_during_tubing_running_text_line.setParent(None)
            self.complications_during_tubing_running_time_label.setParent(None)
            self.complications_during_tubing_running_time_line.setParent(None)
            self.complications_during_tubing_running_time_end_label.setParent(None)
            self.complications_during_tubing_running_time_end_date.setParent(None)
            self.complications_during_tubing_running_time_begin_label.setParent(None)
            self.complications_during_tubing_running_time_begin_date.setParent(None)
        else:
            self.complications_during_tubing_running_text_label = QLabel('Текст осложнения')
            self.complications_during_tubing_running_text_line = QLineEdit(self)
            self.complications_during_tubing_running_text_line.setText('Осложнение при спуске НКТ-вытеснение ')

            self.complications_during_tubing_running_time_begin_label = QLabel('начало осложнения')
            self.complications_during_tubing_running_time_begin_date = QDateTimeEdit(self)
            self.complications_during_tubing_running_time_begin_date.setDisplayFormat("dd.MM.yyyy HH:mm")
            self.complications_during_tubing_running_time_begin_date.setDateTime(self.date_work_str)

            self.complications_during_tubing_running_time_end_label = QLabel('Окончание осложнения')
            self.complications_during_tubing_running_time_end_date = QDateTimeEdit(self)
            self.complications_during_tubing_running_time_end_date.setDisplayFormat("dd.MM.yyyy HH:mm")
            self.complications_during_tubing_running_time_end_date.setDateTime(self.date_work_str)

            self.complications_during_tubing_running_time_label = QLabel('затраченное время')
            self.complications_during_tubing_running_time_line = QLineEdit(self)
            self.complications_during_tubing_running_time_line.setValidator(self.validator_float)

            self.grid.addWidget(self.complications_during_tubing_running_text_label, 26, 2)
            self.grid.addWidget(self.complications_during_tubing_running_text_line, 27, 2)
            self.grid.addWidget(self.complications_during_tubing_running_time_begin_label, 26, 3)
            self.grid.addWidget(self.complications_during_tubing_running_time_begin_date, 27, 3)
            self.grid.addWidget(self.complications_during_tubing_running_time_end_label, 26, 4)
            self.grid.addWidget(self.complications_during_tubing_running_time_end_date, 27, 4)
            self.grid.addWidget(self.complications_during_tubing_running_time_label, 26, 5)
            self.grid.addWidget(self.complications_during_tubing_running_time_line, 27, 5)

            self.complications_during_tubing_running_time_end_date.dateTimeChanged.connect(
                self.update_date_tubing_running)
            self.complications_during_tubing_running_time_begin_date.dateTimeChanged.connect(
                self.update_date_tubing_running)

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

    @staticmethod
    def calculate_date(time_begin, time_end):
        # Вычисляем разницу в секундах
        difference_in_seconds = time_begin.secsTo(time_end)

        # Преобразуем в часы
        difference_in_hours = round(difference_in_seconds / 3600, 1)
        return difference_in_hours

    def update_complications_when_lifting(self, index):
        if index == 'Нет':
            self.complications_when_lifting_text_label.setParent(None)
            self.complications_when_lifting_text_line.setParent(None)
            self.complications_when_lifting_time_label.setParent(None)
            self.complications_when_lifting_time_line.setParent(None)
            self.complications_when_lifting_time_begin_label.setParent(None)
            self.complications_when_lifting_time_begin_date.setParent(None)
            self.complications_when_lifting_time_end_label.setParent(None)
            self.complications_when_lifting_time_end_date.setParent(None)
        else:
            self.complications_when_lifting_text_label = QLabel('Текст осложнения')
            self.complications_when_lifting_text_line = QLineEdit(self)

            self.complications_when_lifting_time_begin_label = QLabel('начало осложнения')
            self.complications_when_lifting_time_begin_date = QDateTimeEdit(self)
            self.complications_when_lifting_time_begin_date.setDisplayFormat("dd.MM.yyyy HH:mm")
            self.complications_when_lifting_time_begin_date.setDateTime(self.date_work_str)

            self.complications_when_lifting_time_end_label = QLabel('Окончание осложнения')
            self.complications_when_lifting_time_end_date = QDateTimeEdit(self)
            self.complications_when_lifting_time_end_date.setDisplayFormat("dd.MM.yyyy HH:mm")
            self.complications_when_lifting_time_end_date.setDateTime(self.date_work_str)

            self.complications_when_lifting_time_label = QLabel('затраченное время О')
            self.complications_when_lifting_time_line = QLineEdit(self)

            self.complications_when_lifting_time_line.setValidator(self.validator_float)
            self.grid.addWidget(self.complications_when_lifting_text_label, 46, 2)
            self.grid.addWidget(self.complications_when_lifting_text_line, 47, 2)

            self.grid.addWidget(self.complications_when_lifting_time_begin_label, 46, 3)
            self.grid.addWidget(self.complications_when_lifting_time_begin_date, 47, 3)

            self.grid.addWidget(self.complications_when_lifting_time_end_label, 46, 4)
            self.grid.addWidget(self.complications_when_lifting_time_end_date, 47, 4)

            self.grid.addWidget(self.complications_when_lifting_time_label, 46, 5)
            self.grid.addWidget(self.complications_when_lifting_time_line, 47, 5)

            self.complications_when_lifting_time_end_date.dateTimeChanged.connect(self.update_date_when_lifting)
            self.complications_when_lifting_time_begin_date.dateTimeChanged.connect(self.update_date_when_lifting)


class TabWidget(QTabWidget):
    def __init__(self):
        super().__init__()
        self.addTab(TabPage_SO_Timplate(self), 'Трубный перфоратор')


class PipePerforator(QMainWindow):
    def __init__(self, ins_ind, table_widget, parent=None):
        super(QMainWindow, self).__init__(parent)
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

        # Заполнение QTableWidget данными из списка
        for datа in well_data.work_list_in_ois:
            row_position = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_position)
            self.tableWidget.setItem(row_position, 0, QTableWidgetItem(datа[0]))

            # Создание QTextEdit для переноса текста в ячейке
            text_edit = QTextEdit()
            text_edit.setText(datа[1])
            text_edit.setReadOnly(True)  # Сделаем текст редактируемым только для чтения

            self.tableWidget.setCellWidget(row_position, 1, text_edit)

            # Устанавливаем высоту строки в зависимости от текста
            self.adjustRowHeight(row_position, text_edit.toPlainText())
            # Устанавливаем высоту строки в зависимости от текста
            self.adjustRowHeight(row_position, datа[1])

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

    def adjustRowHeight(self, row, text):
        font_metrics = self.tableWidget.fontMetrics()  # Получаем метрики шрифта
        text_height = font_metrics.height()  # Высота строки на основе шрифта
        text_length = len(text)

        # Предположим, что мы используем фиксированную ширину для текстовой ячейки
        width = self.tableWidget.columnWidth(1)
        # Оцениваем количество необходимых строк для текста
        number_of_lines = (text_length // (width // font_metrics.averageCharWidth())) + 1
        self.tableWidget.setRowHeight(row, int((text_height * number_of_lines) / 2))  # Устанавливаем высоту

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
        self.equipment_audit_combo = current_widget.equipment_audit_combo.currentText()
        if self.equipment_audit_combo == 'Да':
            self.equipment_audit_text_line = current_widget.equipment_audit_text_line.text()
            if self.equipment_audit_text_line == '':
                QMessageBox.warning(self, 'Ошибка', 'Нужно внести текст ревизии')
                return

        try:
            self.nkt_48_lenght_edit = current_widget.nkt_48_lenght_edit.text()
            self.nkt_48_count_edit = current_widget.nkt_48_count_edit.text()
            self.nkt_60_lenght_edit = current_widget.nkt_60_lenght_edit.text()
            self.nkt_60_count_edit = current_widget.nkt_60_count_edit.text()
            self.nkt_73_lenght_edit = current_widget.nkt_73_lenght_edit.text()
            self.nkt_73_count_edit = current_widget.nkt_73_count_edit.text()
            self.nkt_89_lenght_edit = current_widget.nkt_89_lenght_edit.text()
            self.nkt_89_count_edit = current_widget.nkt_89_count_edit.text()

            if self.nkt_48_lenght_edit != '' and self.nkt_48_count_edit != '':
                if 6.5 < int(float(self.nkt_48_lenght_edit)) / int(float(self.nkt_48_count_edit)) < 12.5 == False:
                    QMessageBox.warning(self, 'Ошибка в средней длине НКТ', 'Ошибка в средней длине НКТ')
                    return
                self.dict_nkt.setdefault('48мм',
                                         (int(float(self.nkt_48_lenght_edit)), int(float(self.nkt_48_count_edit))))
            if self.nkt_60_lenght_edit != '' and self.nkt_60_count_edit != '':
                if 6.5 < int(float(self.nkt_60_lenght_edit)) / int(float(self.nkt_60_count_edit)) < 12.5 == False:
                    QMessageBox.warning(self, 'Ошибка в средней длине НКТ', 'Ошибка в средней длине НКТ')
                    return
                self.dict_nkt.setdefault('60мм',
                                         (int(float(self.nkt_60_lenght_edit)), int(float(self.nkt_60_count_edit))))
            if self.nkt_73_lenght_edit != '' and self.nkt_73_count_edit != '':
                if 6.5 < int(float(self.nkt_73_lenght_edit)) / int(float(self.nkt_73_count_edit)) < 12.5 == False:
                    QMessageBox.warning(self, 'Ошибка в средней длине НКТ', 'Ошибка в средней длине НКТ')
                    return
                self.dict_nkt.setdefault('73мм',
                                         (int(float(self.nkt_73_lenght_edit)), int(float(self.nkt_73_count_edit))))
            if self.nkt_89_lenght_edit != '' and self.nkt_89_count_edit != '':
                if 6.5 < int(float(self.nkt_89_lenght_edit)) / int(float(self.nkt_89_count_edit)) < 12.5 == False:
                    QMessageBox.warning(self, 'Ошибка в средней длине НКТ', 'Ошибка в средней длине НКТ')
                    return
                self.dict_nkt.setdefault('89мм',
                                         (int(float(self.nkt_89_lenght_edit)), int(float(self.nkt_89_count_edit))))
        except Exception as e:
            QMessageBox.warning(self, 'Ошибка', f'Введены не все значения {e}')
            return

        if self.nkt_is_same_combo == 'Нет':
            try:
                self.nkt_48_lenght_up_edit = current_widget.nkt_48_lenght_up_edit.text()
                self.nkt_48_count_up_edit = current_widget.nkt_48_count_up_edit.text()
                self.nkt_60_lenght_up_edit = current_widget.nkt_60_lenght_up_edit.text()
                self.nkt_60_count_up_edit = current_widget.nkt_60_count_up_edit.text()
                self.nkt_73_lenght_up_edit = current_widget.nkt_73_lenght_up_edit.text()
                self.nkt_73_count_up_edit = current_widget.nkt_73_count_up_edit.text()
                self.nkt_89_lenght_up_edit = current_widget.nkt_89_lenght_up_edit.text()
                self.nkt_89_count_up_edit = current_widget.nkt_89_count_up_edit.text()

                if self.nkt_48_lenght_up_edit != '' and self.nkt_48_count_up_edit != '':
                    self.dict_nkt_up.setdefault('48мм',
                                                (int(float(self.nkt_48_lenght_up_edit)),
                                                 int(float(self.nkt_48_count_up_edit))))
                if self.nkt_60_lenght_up_edit != '' and self.nkt_60_count_up_edit != '':
                    self.dict_nkt_up.setdefault('60мм',
                                                (int(float(self.nkt_60_lenght_up_edit)),
                                                 int(float(self.nkt_60_count_up_edit))))
                if self.nkt_73_lenght_up_edit != '' and self.nkt_73_count_up_edit != '':
                    self.dict_nkt_up.setdefault('73мм',
                                                (int(float(self.nkt_73_lenght_up_edit)),
                                                 int(float(self.nkt_73_count_up_edit))))
                if self.nkt_89_lenght_up_edit != '' and self.nkt_89_count_up_edit != '':
                    self.dict_nkt_up.setdefault('89мм',
                                                (int(float(self.nkt_89_lenght_up_edit)),
                                                 int(float(self.nkt_89_count_up_edit))))
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
            self.complications_of_failure_text_line = current_widget.complications_of_failure_text_line.text()
            self.complications_of_failure_time_begin_date = \
                current_widget.complications_of_failure_time_begin_date.dateTime().toPyDateTime()
            self.complications_of_failure_time_begin_date = \
                self.change_string_in_date(self.complications_of_failure_time_begin_date)

            self.complications_of_failure_time_end_date = \
                current_widget.complications_of_failure_time_end_date.dateTime().toPyDateTime()
            self.complications_of_failure_time_end_date = \
                self.change_string_in_date(self.complications_of_failure_time_end_date)

            if current_widget.complications_of_failure_text_line.text() == self.complications_of_failure_time_begin_date:
                QMessageBox.warning(self, 'Даты совпадают', 'Даты совпадают')
                return

            if self.complications_of_failure_text_line == '':
                QMessageBox.warning(self, 'Ошибка', f'Не введены текст осложнения при срыве ПШ')
                return

            self.complications_of_failure_time_line = current_widget.complications_of_failure_time_line.text()
            if self.complications_of_failure_time_line != '':
                self.complications_of_failure_time_line = round(float(self.complications_of_failure_time_line), 1)

            else:
                QMessageBox.warning(self, 'Ошибка', f'Не введены время осложнения при срыве ПШ')
                return

            if self.complications_of_failure_time_line <= 0:
                QMessageBox.warning(self, 'Ошибка', f'Затраченное время при срыве ПШ не может быть отрицательным')
                return

        if self.complications_during_tubing_running_combo == 'Да':
            self.complications_during_tubing_running_text_line = current_widget.complications_during_tubing_running_text_line.text()
            self.complications_during_tubing_running_time_begin_date = \
                current_widget.complications_during_tubing_running_time_begin_date.dateTime().toPyDateTime()
            self.complications_during_tubing_running_time_begin_date = \
                self.change_string_in_date(self.complications_during_tubing_running_time_begin_date)

            self.complications_during_tubing_running_time_end_date = \
                current_widget.complications_during_tubing_running_time_end_date.dateTime().toPyDateTime()
            self.complications_during_tubing_running_time_end_date = \
                self.change_string_in_date(self.complications_during_tubing_running_time_end_date)

            if current_widget.complications_during_tubing_running_text_line.text() == self.complications_during_tubing_running_time_begin_date:
                QMessageBox.warning(self, 'Даты совпадают', 'Даты совпадают')
                return

            if self.complications_during_tubing_running_text_line == '':
                QMessageBox.warning(self, 'Ошибка', f'Не введены текст осложнения демонтаже арматуры')
                return

            self.complications_during_tubing_running_time_line = current_widget.complications_during_tubing_running_time_line.text()
            if self.complications_during_tubing_running_time_line != '':
                self.complications_during_tubing_running_time_line = round(
                    float(self.complications_during_tubing_running_time_line), 1)

            else:
                QMessageBox.warning(self, 'Ошибка', f'Не введены время осложнения при демонтаже арматуры')
                return

            if self.complications_during_tubing_running_time_line <= 0:
                QMessageBox.warning(self, 'Ошибка',
                                    f'Затраченное время при срыве демонтаже арматуры не может быть отрицательным')
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
            try:
                self.complications_when_lifting_text_line = current_widget.complications_when_lifting_text_line.text()

                self.complications_when_lifting_time_begin_date = \
                    current_widget.complications_when_lifting_time_begin_date.dateTime().toPyDateTime()
                self.complications_when_lifting_time_begin_date = \
                    self.change_string_in_date(self.complications_when_lifting_time_begin_date)

                self.complications_when_lifting_time_end_date = \
                    current_widget.complications_when_lifting_time_end_date.dateTime().toPyDateTime()
                self.complications_when_lifting_time_end_date = \
                    self.change_string_in_date(self.complications_when_lifting_time_end_date)

                self.complications_when_lifting_time_line = current_widget.complications_when_lifting_time_line.text()

                if self.complications_when_lifting_time_end_date == self.complications_when_lifting_time_begin_date:
                    QMessageBox.warning(self, 'Даты совпадают', 'Даты совпадают')
                    return

                if self.complications_when_lifting_text_line == '':
                    QMessageBox.warning(self, 'Ошибка', f'Не введены текст осложнения при подьеме')
                    return
                else:
                    aaaaa = self.complications_when_lifting_time_line
                    self.complications_when_lifting_time_line = round(float(self.complications_when_lifting_time_line),
                                                                      1)

                if self.complications_when_lifting_time_line <= 0:
                    QMessageBox.warning(self, 'Ошибка',
                                        f'Затраченное время при подьеме не может быть отрицательным')
                    return

            except Exception as e:
                QMessageBox.warning(self, 'Ошибка', f'ВВедены не все значения {e}')
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

        MyWindow.populate_row(self, self.ins_ind, work_list, self.table_widget)
        well_data.pause = False
        self.close()

    @staticmethod
    def change_string_in_date(date_str):
        # Преобразуем строку в объект datetime

        formatted_date = date_str.strftime("%d.%m.%Y %H:%M")
        return formatted_date

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
            ['=ROW()-ROW($A$46)', None, None, 'ГИС', 'Прочие',
             f'{self.installation_pipe_perforator_text_line} '
             f'{self.installation_pipe_perforator_time_begin_date}-{self.installation_pipe_perforator_time_end_date}',
             None, None, None, None,
             None, None, None, None, 'АКТ№', None, None, None, 'Факт', None, 'час',
             self.installation_pipe_perforator_text_line, 1, 1, '=V901*W901*X901',
             '=Y901-AA901-AB901-AC901-AD901', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', None, None, 'спо', 'Перфоратор', 'ПЗР СПО трубного перфоратора', None, None, None,
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
                ['=ROW()-ROW($A$46)', None, None, 'ГИС', 'Прочие',
                 f'{self.deinstallation_perforation_text_line} '
                 f'{self.deinstallation_perforation_time_begin_date}-{self.deinstallation_perforation_time_end_date}', None,
                 None, None, None, None, None, None, None, 'АКТ№', None, None, None, 'Факт', None, 'час',
                 self.deinstallation_perforation_time_line,
                 1, 1, '=V919*W919*X919', '=Y919-AA9(19-AB919-AC919-AD919', None, None, None, None, None]]
        self.date_work_line = self.deinstallation_perforation_time_begin_date.split(' ')[0]
        return work_list

    def initiation_perforator(self):
        work_list = [
            ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None, 'Д/ж, м/ж спайдера', None, None, None, None, None,
             None, None, None, None, None, None, None, '§185разд.1', None, 'час', 1, 0.14, 1, '=V908*W908*X908',
             '=Y908-AA908-AB908-AC908-AD908', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None, 'Д/ж, м/ж спайдера', None, None, None, None, None,
             None, None, None, None, None, None, None, '§185разд.1', None, 'час', 1, 0.14, 1, '=V909*W909*X909',
             '=Y909-AA909-AB909-AC909-AD909', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', None, None, 'ГИС', 'ПВР', 'ГИС - ПВР (инициация)', None, None, None, None, None, None,
             None, None, 'АКТ№', None, None, None, 'Факт', None, 'час', 1, 1, 1, '=V910*W910*X910',
             '=Y910-AA910-AB910-AC910-AD910', None, None, None, None, None]]
        return work_list

    def volume_well_work(self):

        work_list = []
        volume_list = [
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'Промывка',
             'ПЗР при промывке скважины ',
             None, None, None, None, None, None, None, None, None, None, None, None, '§156,160р.1', None, 'шт',
             1, 1, 1, '=V462*W462*X462', '=Y462-AA462-AB462-AC462-AD462', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'Промывка',
             'Переход на обратную промывку',
             None, None, None, None, None, None, None, None, None, None, None, None, '§162разд.1', None, 'раз',
             1, 0.15, 1, '=V463*W463*X463', '=Y463-AA463-AB463-AC463-AD463', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'Промывка', 'Промывка ',
             None, None, None, None, None, None, None, None, None, None, None, None, '§300разд.1', None, 'м3',
             self.volume_well_flush_line, 0.033, 1,
             '=V464*W464*X464', '=Y464-AA464-AB464-AC464-AD464', None, None, None, None, None]
        ]
        work_list.extend(volume_list)
        return work_list


if __name__ == "__main__":
    # app3 = QApplication(sys.argv)

    app = QApplication(sys.argv)
    window = PipePerforator(22, 22)
    window.show()
    sys.exit(app.exec_())
