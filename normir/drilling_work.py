import sys
from datetime import datetime, timedelta

import well_data

from collections import namedtuple
from normir.files_with_list import cause_presence_of_jamming, drilling_ek_list

from normir.norms import LIFTING_NORM_SBT, DESCENT_NORM_SBT

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
        self.select_type_combo.addItems(['', 'НКТ', 'СБТ'])

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
        self.solvent_injection_label = QLabel('Закачка растворителя')
        self.nkt_is_same_label = QLabel('Кол-во НКТ на подъем совпадает со спуском')

        self.raid_work_text_label = QLabel('Интервалы бурения')
        self.count_of_nkt_extensions_label = QLabel('Кол-во метров бурения')
        self.drilling_ek_combo_label = QLabel('Что бурили')
        self.select_type_drill_combo_label = QLabel('Фрез или долото')
        self.raid_work_time_begin_label = QLabel('начало райбирования')

        self.raid_work_time_end_label = QLabel('Окончание осложнения райбирования')
        self.raid_work_time_label = QLabel('затраченное время')

    def update_select_type_combo(self, index):

        self.type_rotor_label = QLabel('Тип ротора')
        self.type_rotor_combo = QComboBox(self)
        self.type_rotor_combo.addItems(['Мех ротор', 'Гидроротор'])

        self.count_spo_sbt_label = QLabel('Первое спо СБТ')
        self.count_spo_sbt_combo = QComboBox(self)
        self.count_spo_sbt_combo.addItems(['Нет', 'Да'])

        if well_data.count_SBT != 0:
            self.count_spo_sbt_combo.setCurrentIndex(1)

        self.type_key_label = QLabel('монтаж мех ключей при подьеме')
        self.type_key_combo = QComboBox(self)
        self.type_key_combo.addItems(['Нет', 'Да'])

        if index == 'СБТ':
            self.nkt_48_lenght_label = QLabel('Длина на спуск СБТ48')
            self.nkt_48_count_label = QLabel('Кол-во на спуск СБТ48')
            self.nkt_60_lenght_label = QLabel('Длина на спуск СБТ60')
            self.nkt_60_lenght_label = QLabel('Длина на спуск СБТ60')
            self.technological_crap_question_label = QLabel('Был ли тех. отстой')
            self.nkt_60_count_label = QLabel('Кол-во на спуск СБТ60')
            self.nkt_73_lenght_label = QLabel('Длина СБТ73')
            self.nkt_73_count_label = QLabel('Кол-во СБТ73')
            self.nkt_89_lenght_label = QLabel('Длина СБТ89-102')
            self.nkt_89_count_label = QLabel('Кол-во СБТ89-102')

            self.grid.addWidget(self.type_rotor_label, 10, 1)
            self.grid.addWidget(self.type_rotor_combo, 11, 1)
            self.grid.addWidget(self.count_spo_sbt_label, 10, 2)
            self.grid.addWidget(self.count_spo_sbt_combo, 11, 2)
            self.grid.addWidget(self.type_key_label, 10, 3)
            self.grid.addWidget(self.type_key_combo, 11, 3)

        else:
            self.type_rotor_label.setParent(None)
            self.type_rotor_combo.setParent(None)
            self.count_spo_sbt_label.setParent(None)
            self.count_spo_sbt_combo.setParent(None)
            self.type_key_label.setParent(None)
            self.type_key_combo.setParent(None)

        self.complications_during_tubing_running_combo = QComboBox(self)
        self.complications_during_tubing_running_combo.addItems(['Нет', 'Да'])

        self.complications_of_failure_combo = QComboBox(self)
        self.complications_of_failure_combo.addItems(['Нет', 'Да'])

        self.complications_when_lifting_combo = QComboBox(self)
        self.complications_when_lifting_combo.addItems(['Нет', 'Да'])

        # self.grid.addWidget(self.complications_of_failure_label, 10, 1)
        # self.grid.addWidget(self.complications_of_failure_combo, 11, 1)

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

        self.volume_well_flush_line = QLineEdit(self)
        self.volume_well_flush_line.setValidator(self.validator_float)

        self.grid.addWidget(self.volume_well_flush_label, 30, 4)
        self.grid.addWidget(self.volume_well_flush_line, 31, 4)

        self.grid.addWidget(self.complications_when_lifting_label, 46, 1)
        self.grid.addWidget(self.complications_when_lifting_combo, 47, 1)

        self.solvent_injection_combo = QComboBox(self)
        self.solvent_injection_combo.addItems(['Нет', 'Да'])

        self.grid.addWidget(self.solvent_injection_label, 32, 1)
        self.grid.addWidget(self.solvent_injection_combo, 33, 1)

        self.nkt_is_same_combo = QComboBox(self)
        self.nkt_is_same_combo.addItems(['Да', 'Нет'])

        self.grid.addWidget(self.nkt_is_same_label, 34, 1)
        self.grid.addWidget(self.nkt_is_same_combo, 35, 1)

        # self.normalization_question_combo = QComboBox(self)
        # self.normalization_question_combo.addItems(['Нет', 'Да'])
        #
        # self.grid.addWidget(self.normalization_question_label, 50, 1)
        # self.grid.addWidget(self.normalization_question_combo, 51, 1)

        self.technological_crap_question_combo = QComboBox(self)
        self.technological_crap_question_combo.addItems(['Нет', 'Да'])

        self.grid.addWidget(self.technological_crap_question_label, 52, 1)
        self.grid.addWidget(self.technological_crap_question_combo, 53, 1)

        self.equipment_audit_label = QLabel('Была ли ревизия')
        self.equipment_audit_combo = QComboBox(self)
        self.equipment_audit_combo.addItems(['Нет', 'Да'])

        self.grid.addWidget(self.equipment_audit_label, 54, 1)
        self.grid.addWidget(self.equipment_audit_combo, 55, 1)

        self.equipment_audit_combo.currentTextChanged.connect(self.update_equipment_audit_combo)
        # self.pressuar_gno_combo.currentTextChanged.connect(self.update_pressuar_gno_combo)
        self.technological_crap_question_combo.currentTextChanged.connect(self.update_technological_crap_question_combo)
        self.solvent_injection_combo.currentTextChanged.connect(self.update_solvent_injection_combo)
        # self.pressuar_gno_combo.currentTextChanged.connect(self.update_pressuar_gno_combo)
        # self.normalization_question_combo.currentTextChanged.connect(self.update_normalization_question_combo)
        self.complications_of_failure_combo.currentTextChanged.connect(self.update_complications_of_failure)
        self.complications_when_lifting_combo.currentTextChanged.connect(self.update_complications_when_lifting)

        self.complications_during_tubing_running_combo.currentTextChanged.connect(
            self.update_complications_during_tubing_running_combo)
        self.nkt_is_same_combo.currentTextChanged.connect(self.update_nkt_is_same_combo)

        self.raid_work_text_edit = QLineEdit(self)

        self.count_of_nkt_extensions_line = QLineEdit(self)
        self.count_of_nkt_extensions_line.setValidator(self.validator_float)

        self.grid.addWidget(self.raid_work_text_label, 30, 1)
        self.grid.addWidget(self.raid_work_text_edit, 31, 1)

        self.drilling_ek_combo = QComboBox(self)
        self.drilling_ek_combo.addItems(drilling_ek_list)

        self.grid.addWidget(self.drilling_ek_combo_label, 30, 2)
        self.grid.addWidget(self.drilling_ek_combo, 31, 2)

        self.select_type_drill_combo = QComboBox(self)
        self.select_type_drill_combo.addItems(['', 'фрез', 'долото'])

        self.grid.addWidget(self.select_type_drill_combo_label, 30, 3)
        self.grid.addWidget(self.select_type_drill_combo, 31, 3)

        self.grid.addWidget(self.count_of_nkt_extensions_label, 30, 5)
        self.grid.addWidget(self.count_of_nkt_extensions_line, 31, 5)

        self.raid_work_time_begin_date = QDateTimeEdit(self)
        self.raid_work_time_begin_date.setDisplayFormat("dd.MM.yyyy HH:mm")
        self.raid_work_time_begin_date.setDateTime(self.date_work_str)

        self.raid_work_time_end_date = QDateTimeEdit(self)
        self.raid_work_time_end_date.setDisplayFormat("dd.MM.yyyy HH:mm")
        self.raid_work_time_end_date.setDateTime(self.date_work_str)

        self.raid_work_time_line = QLineEdit(self)
        self.raid_work_time_line.setValidator(self.validator_float)

        self.grid.addWidget(self.raid_work_time_begin_label, 30, 6)
        self.grid.addWidget(self.raid_work_time_begin_date, 31, 6)
        self.grid.addWidget(self.raid_work_time_end_label, 30, 7)
        self.grid.addWidget(self.raid_work_time_end_date, 31, 7)
        self.grid.addWidget(self.raid_work_time_label, 30, 8)
        self.grid.addWidget(self.raid_work_time_line, 31, 8)

        self.raid_work_time_end_date.dateTimeChanged.connect(self.update_date_of_raid)
        self.raid_work_time_begin_date.dateTimeChanged.connect(self.update_date_of_raid)

        self.raid_work_text_edit.editingFinished.connect(self.update_raid_work)

    def update_equipment_audit_combo(self, index):
        if index == 'Нет':
            self.equipment_audit_text_label.setParent(None)
            self.equipment_audit_text_line.setParent(None)
        else:

            self.equipment_audit_text_label = QLabel('Текст ревизии')
            self.equipment_audit_text_line = QLineEdit(self)

            self.grid.addWidget(self.equipment_audit_text_label, 54, 3)
            self.grid.addWidget(self.equipment_audit_text_line, 55, 3)

    def update_raid_work(self):
        text = self.raid_work_text_edit.text()
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

        self.count_of_nkt_extensions_line.setText(str(count_skm))

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

    def update_normalization_question_combo(self, index):

        if index == 'Нет':
            self.normalization_question_text_label.setParent(None)
            self.normalization_question_text_line.setParent(None)
            self.normalization_question_time_label.setParent(None)
            self.normalization_question_time_line.setParent(None)
            self.normalization_question_time_end_label.setParent(None)
            self.normalization_question_time_end_date.setParent(None)
            self.normalization_question_time_begin_label.setParent(None)
            self.normalization_question_time_begin_date.setParent(None)
        else:
            self.normalization_question_text_label = QLabel('Текст осложнения')
            self.normalization_question_text_line = QLineEdit(self)

            self.normalization_question_time_begin_label = QLabel('начало осложнения')
            self.normalization_question_time_begin_date = QDateTimeEdit(self)
            self.normalization_question_time_begin_date.setDisplayFormat("dd.MM.yyyy HH:mm")
            self.normalization_question_time_begin_date.setDateTime(self.date_work_str)

            self.normalization_question_time_end_label = QLabel('Окончание осложнения')
            self.normalization_question_time_end_date = QDateTimeEdit(self)
            self.normalization_question_time_end_date.setDisplayFormat("dd.MM.yyyy HH:mm")
            self.normalization_question_time_end_date.setDateTime(self.date_work_str)

            self.normalization_question_time_label = QLabel('затраченное время')
            self.normalization_question_time_line = QLineEdit(self)
            self.normalization_question_time_line.setValidator(self.validator_float)

            self.grid.addWidget(self.normalization_question_text_label, 50, 2)
            self.grid.addWidget(self.normalization_question_text_line, 51, 2)
            self.grid.addWidget(self.normalization_question_time_begin_label, 50, 3)
            self.grid.addWidget(self.normalization_question_time_begin_date, 51, 3)
            self.grid.addWidget(self.normalization_question_time_end_label, 50, 4)
            self.grid.addWidget(self.normalization_question_time_end_date, 51, 4)
            self.grid.addWidget(self.normalization_question_time_label, 50, 5)
            self.grid.addWidget(self.normalization_question_time_line, 51, 5)

            self.normalization_question_time_end_date.dateTimeChanged.connect(self.update_date_of_normalization)
            self.normalization_question_time_begin_date.dateTimeChanged.connect(self.update_date_of_normalization)

    def update_solvent_injection_combo(self, index):

        if index == 'Нет':
            self.solvent_volume_text_label.setParent(None)
            self.solvent_volume_text_line.setParent(None)
            self.solvent_volume_time_label.setParent(None)
            self.solvent_volume_time_line.setParent(None)
            self.solvent_volume_time_end_label.setParent(None)
            self.solvent_volume_time_end_date.setParent(None)
            self.solvent_volume_time_begin_label.setParent(None)
            self.solvent_volume_time_begin_date.setParent(None)
            self.volume_of_finishing_label.setParent(None)
            self.volume_of_finishing_line.setParent(None)
            self.volume_flush_line.setParent(None)

            self.volume_flush_label.setParent(None)

        else:
            self.solvent_volume_text_label = QLabel('Объем раствооителя')
            self.solvent_volume_text_line = QLineEdit(self)
            self.solvent_volume_text_line.setValidator(self.validator_float)
            self.solvent_volume_text_line.setText('2')

            self.volume_of_finishing_label = QLabel('Объем доводки тех водой')
            self.volume_of_finishing_line = QLineEdit(self)
            self.volume_of_finishing_line.setValidator(self.validator_float)

            self.volume_flush_label = QLabel('Объем промывки')
            self.volume_flush_line = QLineEdit(self)
            self.volume_flush_line.setValidator(self.validator_float)

            self.solvent_volume_time_begin_label = QLabel('начало реагирования')
            self.solvent_volume_time_begin_date = QDateTimeEdit(self)
            self.solvent_volume_time_begin_date.setDisplayFormat("dd.MM.yyyy HH:mm")
            self.solvent_volume_time_begin_date.setDateTime(self.date_work_str)

            self.solvent_volume_time_end_label = QLabel('Окончание реагирования')
            self.solvent_volume_time_end_date = QDateTimeEdit(self)
            self.solvent_volume_time_end_date.setDisplayFormat("dd.MM.yyyy HH:mm")
            self.solvent_volume_time_end_date.setDateTime(self.date_work_str)

            self.solvent_volume_time_label = QLabel('затраченное время реагирования')
            self.solvent_volume_time_line = QLineEdit(self)
            self.solvent_volume_time_line.setValidator(self.validator_float)

            self.grid.addWidget(self.solvent_volume_text_label, 32, 2)
            self.grid.addWidget(self.solvent_volume_text_line, 33, 2)
            self.grid.addWidget(self.volume_of_finishing_label, 32, 3)
            self.grid.addWidget(self.volume_of_finishing_line, 33, 3)
            self.grid.addWidget(self.volume_flush_label, 32, 4)
            self.grid.addWidget(self.volume_flush_line, 33, 4)
            self.grid.addWidget(self.solvent_volume_time_begin_label, 32, 5)
            self.grid.addWidget(self.solvent_volume_time_begin_date, 33, 5)
            self.grid.addWidget(self.solvent_volume_time_end_label, 32, 6)
            self.grid.addWidget(self.solvent_volume_time_end_date, 33, 6)
            self.grid.addWidget(self.solvent_volume_time_label, 32, 7)
            self.grid.addWidget(self.solvent_volume_time_line, 33, 7)

            self.solvent_volume_time_end_date.dateTimeChanged.connect(
                self.update_date_solvent_volume)
            self.solvent_volume_time_begin_date.dateTimeChanged.connect(
                self.update_date_solvent_volume)

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

    def update_date_of_raid(self):
        time_begin = self.raid_work_time_begin_date.dateTime()
        time_end = self.raid_work_time_end_date.dateTime()

        time_difference = self.calculate_date(time_begin, time_end)
        self.raid_work_time_line.setText(str(time_difference))

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
        self.addTab(TabPage_SO_Timplate(self), 'Райбер')


class DrillingWork(QMainWindow):
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
        elif self.select_type_combo in ['НКТ', 'СБТ']:
            self.type_equipment = 'Долото'
            self.coefficient_lifting = 1.2

            self.raid_work_text_edit = current_widget.raid_work_text_edit.text()

            self.count_of_nkt_extensions_line = current_widget.count_of_nkt_extensions_line.text()
            if self.count_of_nkt_extensions_line != '':
                self.count_of_nkt_extensions_line = int(self.count_of_nkt_extensions_line)
            else:
                question = QMessageBox.question(self, 'Бурение', 'Нормализации не было?')
                if question == QMessageBox.StandardButton.No:
                    return

            if self.select_type_combo == 'СБТ':
                self.type_rotor_combo = current_widget.type_rotor_combo.currentText()
                self.count_spo_sbt_combo = current_widget.count_spo_sbt_combo.currentText()
                self.type_key_combo = current_widget.type_key_combo.currentText()

        self.nkt_is_same_combo = current_widget.nkt_is_same_combo.currentText()
        self.equipment_audit_combo = current_widget.equipment_audit_combo.currentText()
        if self.equipment_audit_combo == 'Да':
            self.equipment_audit_text_line = current_widget.equipment_audit_text_line.text()

        self.volume_well_flush_line = current_widget.volume_well_flush_line.text()
        if self.volume_well_flush_line != ['', None]:
            self.volume_well_flush_line = int(self.volume_well_flush_line)
        else:
            question = QMessageBox.question(self, 'Промывка', 'Промывки не было?')
            if question == QMessageBox.StandardButton.No:
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
        # self.normalization_question_combo = current_widget.normalization_question_combo.currentText()
        self.solvent_injection_combo = current_widget.solvent_injection_combo.currentText()
        self.technological_crap_question_combo = current_widget.technological_crap_question_combo.currentText()
        self.complications_when_lifting_combo = current_widget.complications_when_lifting_combo.currentText()
        self.drilling_ek_combo = current_widget.drilling_ek_combo.currentText()
        if self.drilling_ek_combo == '':
            QMessageBox.warning(self, 'Нужно выбрать что бурили')
            return
        self.select_type_drill_combo = current_widget.select_type_drill_combo.currentText()
        if self.select_type_drill_combo == '':
            QMessageBox.warning(self, 'Нужно выбрать тип долото')
            return

        # self.pressuar_gno_combo = current_widget.pressuar_gno_combo.currentText()

        self.raid_work_time_begin_date = \
            current_widget.raid_work_time_begin_date.dateTime().toPyDateTime()
        self.raid_work_time_begin_date = \
            self.change_string_in_date(self.raid_work_time_begin_date)

        self.raid_work_time_end_date = \
            current_widget.raid_work_time_end_date.dateTime().toPyDateTime()
        self.raid_work_time_end_date = \
            self.change_string_in_date(self.raid_work_time_end_date)

        if self.raid_work_time_end_date == self.raid_work_time_begin_date:
            QMessageBox.warning(self, 'Даты совпадают', 'Даты совпадают')
            return

        self.raid_work_time_line = current_widget.raid_work_time_line.text()
        if self.raid_work_time_line != '':
            self.raid_work_time_line = round(float(self.raid_work_time_line), 1)

        else:
            QMessageBox.warning(self, 'Ошибка', f'Не введены время осложнения при срыве ПШ')
            return

        if self.raid_work_time_line <= 0:
            QMessageBox.warning(self, 'Ошибка', f'Затраченное время при срыве ПШ не может быть отрицательным')
            return

        if self.solvent_injection_combo == 'Да':

            self.solvent_volume_text_line = current_widget.solvent_volume_text_line.text()
            self.solvent_volume_time_begin_date = \
                current_widget.solvent_volume_time_begin_date.dateTime().toPyDateTime()
            self.solvent_volume_time_begin_date = \
                self.change_string_in_date(self.solvent_volume_time_begin_date)

            self.solvent_volume_time_end_date = \
                current_widget.solvent_volume_time_end_date.dateTime().toPyDateTime()
            self.solvent_volume_time_end_date = \
                self.change_string_in_date(self.solvent_volume_time_end_date)

            if current_widget.solvent_volume_text_line.text() == self.solvent_volume_time_begin_date:
                QMessageBox.warning(self, 'Даты совпадают', 'Даты совпадают')
                return

            if self.solvent_volume_text_line == '':
                QMessageBox.warning(self, 'Ошибка', f'Не введены обьем растворителя')
                return
            else:
                self.solvent_volume_text_line = round(float(self.solvent_volume_text_line), 1)

            self.solvent_volume_time_line = current_widget.solvent_volume_time_line.text()
            if self.solvent_volume_time_line != '':
                self.solvent_volume_time_line = round(float(self.solvent_volume_time_line), 1)

            else:
                QMessageBox.warning(self, 'Ошибка', f'Не введены время реагирования')
                return
            self.volume_of_finishing_line = current_widget.volume_of_finishing_line.text()
            self.volume_flush_line = current_widget.volume_flush_line.text()

            if self.volume_of_finishing_line != '':
                self.volume_of_finishing_line = round(float(self.volume_of_finishing_line), 1)

            else:
                QMessageBox.warning(self, 'Ошибка', f'Не введены обьем доводки техводой растворителя')
                return

            if self.volume_flush_line != '':
                self.volume_flush_line = round(float(self.volume_flush_line), 1)
            else:
                QMessageBox.warning(self, 'Ошибка', f'Не обьем промывки скважины после реагирования')
                return

            if self.solvent_volume_time_line <= 0:
                QMessageBox.warning(self, 'Ошибка', f'Затраченное время при срыве ПШ не может быть отрицательным')
                return

        if self.technological_crap_question_combo == 'Да':
            self.count_nkt_line = current_widget.count_nkt_line.text()
            self.roof_definition_depth_line = current_widget.roof_definition_depth_line.text()
            if self.count_nkt_line not in [None, '']:
                self.count_nkt_line = int(float(self.count_nkt_line))
            else:
                QMessageBox.warning(self, 'количество НКТ', 'Не указано количество НКТ при подьеме на техотстой')
                return
            if self.roof_definition_depth_line != '':
                self.roof_definition_depth_line = int(float(self.roof_definition_depth_line))
            else:
                QMessageBox.warning(self, 'количество НКТ', 'Не указано глубина определения забоя')
                return

            self.technological_crap_question_text_line = current_widget.technological_crap_question_text_line.text()
            self.technological_crap_question_time_begin_date = \
                current_widget.technological_crap_question_time_begin_date.dateTime().toPyDateTime()
            self.technological_crap_question_time_begin_date = \
                self.change_string_in_date(self.technological_crap_question_time_begin_date)

            self.technological_crap_question_time_end_date = \
                current_widget.technological_crap_question_time_end_date.dateTime().toPyDateTime()
            self.technological_crap_question_time_end_date = \
                self.change_string_in_date(self.technological_crap_question_time_end_date)

            if current_widget.technological_crap_question_text_line.text() == self.technological_crap_question_time_begin_date:
                QMessageBox.warning(self, 'Даты совпадают', 'Даты совпадают')
                return

            if self.technological_crap_question_text_line == '':
                QMessageBox.warning(self, 'Ошибка', f'Не введены текст осложнения при срыве ПШ')
                return

            self.technological_crap_question_time_line = current_widget.technological_crap_question_time_line.text()
            if self.technological_crap_question_time_line != '':
                self.technological_crap_question_time_line = round(float(self.technological_crap_question_time_line), 1)

            else:
                QMessageBox.warning(self, 'Ошибка', f'Не введены время осложнения при срыве ПШ')
                return

            if self.technological_crap_question_time_line <= 0:
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
            drilling_list = [
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'Вызов циркуляции (+)', None,
                 None, None, None,
                 None, None, None, None, None, None, None, None, '§301разд.1 п.72', None, 'раз', 1, '=5/60',
                 1, '=V774*W774*X774', '=Y774-AA774-AB774-AC774-AD774', None, None, None, None, None],
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции',
                 'бурение', 'ПЗР при разбуривании, проработке, райберовании', None, None, None, None, None, None,
                 None, None, None, None, None, None, '§156,160р.1', None, 'шт', 1, 1, 1, '=V775*W775*X775',
                 '=Y775-AA775-AB775-AC775-AD775', None, None, None, None, None]]

            if self.select_type_drill_combo == 'фрез':
                drilling_list.extend([['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'фрезерование',
                                       f'Фрезерование в инт. {self.raid_work_text_edit}м '
                                       f'{self.raid_work_time_begin_date}-{self.raid_work_time_end_date}', None, None,
                                       None, None, None,
                                       None, 'что бурили:', self.drilling_ek_combo, 'АКТ№', None, None, None, 'факт',
                                       None, 'час',
                                       self.raid_work_time_line, 1, 1, '=V777*W777*X777',
                                       '=Y777-AA777-AB777-AC777-AD777', None,
                                       None, None, None, None]])
            else:
                drilling_list.extend([['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'бурение',
                                       f'Разбуривание в инт.  {self.raid_work_text_edit}м '
                                       f'{self.raid_work_time_begin_date}-{self.raid_work_time_end_date}',
                                       None, None, None, None, None, None, 'что бурили:', self.drilling_ek_combo,
                                       'АКТ№', None, None, None,
                                       'факт', None,
                                       'час', self.raid_work_time_line, 1, 1, '=V776*W776*X776',
                                       '=Y776-AA776-AB776-AC776-AD776', None,
                                       None, None, None, None]])

            drilling_list.extend([
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'Наращивание', None, None, None,
                 None, None,
                 None, None, None, None, None, None, None, '§300разд.1', None, 'шт',
                 int(self.count_of_nkt_extensions_line/10), 0.17, 1, '=V778*W778*X778',
                 '=Y778-AA778-AB778-AC778-AD778', None, None, None, None, None]])

            work_list.extend(drilling_list)

        return work_list

    def lifting_SBT(self):

        middle_nkt = '9.6-10.5'
        count_nkt = 0
        for nkt_key, nkt_value in self.dict_nkt_up.items():
            nkt_key = '73мм СБТ'
            if count_nkt > 1:
                work_list.extend([
                    ['=ROW()-ROW($A$46)', '73мм-60мм', None, 'Тех.операции', None, 'Смена захвата ЭТА', None, None,
                     None, None, None, None, None, None, None, None, None, None, '§301разд.1 п.141', None, 'раз',
                     1, 0.07, 1, '=V361*W361*X361', '=Y361-AA361-AB361-AC361-AD361', None, None, None, None, None]])
            middle_nkt_value = nkt_value[0] / nkt_value[1]
            nkt_lenght = nkt_value[0]
            nkt_count = nkt_value[1]

            if 6.5 <= middle_nkt_value <= 7.6:
                middle_nkt = '6.5-7.5'
            elif 7.6 <= middle_nkt_value <= 8.6:
                middle_nkt = '7.6-8.5'
            elif 8.6 <= middle_nkt_value <= 9.6:
                middle_nkt = '8.6-9.5'
            elif 9.6 <= middle_nkt_value <= 10.6:
                middle_nkt = '9.6-10.5'
            elif 10.6 <= middle_nkt_value <= 11.6:
                middle_nkt = '10.6-11.5'
            elif 11.6 <= middle_nkt_value <= 12.6:
                middle_nkt = '11.6-12.5'

            max_count_3 = LIFTING_NORM_SBT[well_data.lifting_unit_combo][nkt_key]['III'][middle_nkt][1]
            koef_norm_3 = LIFTING_NORM_SBT[well_data.lifting_unit_combo][nkt_key]['III'][middle_nkt][0]
            razdel_3 = LIFTING_NORM_SBT[well_data.lifting_unit_combo][nkt_key]['III']['раздел']

            if max_count_3 > nkt_lenght:
                nkt_count_3 = nkt_count
            else:
                nkt_count_3 = max_count_3

            lenght_nkt_3 = int(middle_nkt_value * nkt_count_3)

            work_list = [
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', self.type_equipment,
                 'ПЗР СПО перед подъемом труб из скважины',
                 None, None, None,
                 None, None, None, None, None, None, None, None, None, '§207разд.1', None, 'шт', 1, 0.07, 1,
                 '=V199*W199*X199', '=Y199-AA199-AB199-AC199-AD199', None, None, None, None, None]]

            podien_3_list = ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', self.type_equipment,
                             'Подъем БТ 3 скорость',
                             None, None, None, None, nkt_key, lenght_nkt_3, middle_nkt, max_count_3,
                             None, None, None, None, razdel_3, None, 'шт', nkt_count_3, koef_norm_3,
                             self.coefficient_lifting, '=V202*W202*X202', '=Y202-AA202-AB202-AC202-AD202',
                             None, None, None, None, None]

            work_list.append(podien_3_list)

            nkt_count -= max_count_3

            if nkt_count > 0:
                max_count_2 = LIFTING_NORM_SBT[well_data.lifting_unit_combo][nkt_key]['II'][middle_nkt][1]
                koef_norm_2 = LIFTING_NORM_SBT[well_data.lifting_unit_combo][nkt_key]['II'][middle_nkt][0]
                razdel_2 = LIFTING_NORM_SBT[well_data.lifting_unit_combo][nkt_key]['II']['раздел']
                if max_count_2 > nkt_count:
                    nkt_count_2 = nkt_count
                else:
                    nkt_count_2 = max_count_2
                lenght_nkt_2 = int(middle_nkt_value * nkt_count_2)
                podiem_list_2 = ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', self.type_equipment,
                                 'Подъем БТ 2 скорость',
                                 None, None, None, None, nkt_key, lenght_nkt_2, middle_nkt, max_count_2,
                                 None, None, None, None, razdel_2, None, 'шт', nkt_count_2, koef_norm_2,
                                 self.coefficient_lifting, '=V202*W202*X202', '=Y202-AA202-AB202-AC202-AD202', None,
                                 None, None, None, None]
                nkt_count -= max_count_2
                work_list.insert(1, podiem_list_2)

            if nkt_count > 0:
                max_count_1 = LIFTING_NORM_SBT[well_data.lifting_unit_combo][nkt_key]['I'][middle_nkt][1]
                koef_norm_1 = LIFTING_NORM_SBT[well_data.lifting_unit_combo][nkt_key]['I'][middle_nkt][0]
                razdel_1 = LIFTING_NORM_SBT[well_data.lifting_unit_combo][nkt_key]['I']['раздел']

                lenght_nkt_1 = int(middle_nkt_value * nkt_count)
                podiem_list_1 = [
                    '=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', self.type_equipment,
                    'Подъем БТ  1 скорость',
                    None, None, None, None, nkt_key, lenght_nkt_1, middle_nkt, max_count_1,
                    None, None, None, None, razdel_1, None, 'шт', nkt_count, koef_norm_1,
                    self.coefficient_lifting, '=V202*W202*X202', '=Y202-AA202-AB202-AC202-AD202', None, None, None,
                    None, None]
                nkt_count -= max_count_1
                work_list.insert(1, podiem_list_1)

        nkt_sum = sum(list(map(lambda x: x[1], self.dict_nkt_up.values())))

        work_list.extend([
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', self.type_equipment, 'Долив скважины', None, None,
             None, None,
             None, None, None,
             None, None, None, None, None, '§168разд.1', None, 'шт', nkt_sum / 10, 0.003, 1, '=V204*W204*X204',
             '=Y204-AA204-AB204-AC204-AD204', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', self.type_equipment,
             'Навернуть/отвернуть предохранительное кольцо', None, None,
             None, None, None, None, None, None, None, None, None, None, '§300разд.1', None, 'шт',
             nkt_sum,
             0.003, 1, '=V205*W205*X205', '=Y205-AA205-AB205-AC205-AD205', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', self.type_equipment, 'Замер НКТ ', None, None, None,
             None, None,
             None, None, None,
             None, None, None, None, '§47разд.1', None, 'шт', nkt_sum, 0.008, 1,
             '=V207*W207*X207',
             '=Y207-AA207-AB207-AC207-AD207', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'д/ж спайдера',
             None, None, None, None,
             None, None, None, None, None, None, None, None, '§185разд.1', None, 'шт', 1, 0.07, 1, '=V209*W209*X209',
             '=Y209-AA209-AB209-AC209-AD209', None, None, None, None, None],
        ])

        if self.complications_when_lifting_combo == 'Да':
            work_list.insert(-4, ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', self.type_equipment,
                                  f'{self.complications_when_lifting_text_line} '
                                  f'{self.complications_when_lifting_time_begin_date}'
                                  f'{self.complications_when_lifting_time_end_date}',
                                  None, None,
                                  None, None, None,
                                  None, 'Объем', 0, None, None, None, None, 'факт', None,
                                  'час', self.complications_when_lifting_time_end_date, 1, 1, '=V206*W206*X206',
                                  '=Y206-AA206-AB206-AC206-AD206', None, None, None, None, None])
        if nkt_sum > 201:
            work_list.insert(-3, ['=ROW()-ROW($A$46)', 'подъем НКТ', None, 'спо', self.type_equipment,
                                  'Откатывание труб с 201 трубы ',
                                  None, None, None,
                                  None, None, None, None, None, None, None, None, None, '§40разд.1', None, 'шт',
                                  nkt_sum - 201, 0.008, 1,
                                  '=V208*W208*X208', '=Y208-AA208-AB208-AC208-AD208', None, None, None, None, None])

        return work_list
        pass

    def descent_SBT(self):
        sum_nkt = sum(list(map(lambda x: x[1], list(self.dict_nkt.values()))))
        work_list = []

        middle_nkt = '9.6-10.5'
        for nkt_key, nkt_value in self.dict_nkt.items():
            nkt_key = 'БТ'
            middle_nkt_value = nkt_value[0] / nkt_value[1]
            nkt_lenght = nkt_value[0]
            nkt_count = nkt_value[1]
            if 6.5 <= middle_nkt_value <= 7.6:
                middle_nkt = '6.5-7.5'
            elif 7.6 < middle_nkt_value <= 8.6:
                middle_nkt = '7.6-8.5'
            elif 8.6 < middle_nkt_value <= 9.6:
                middle_nkt = '8.6-9.5'
            elif 9.6 < middle_nkt_value <= 10.6:
                middle_nkt = '9.6-10.5'
            elif 10.6 < middle_nkt_value <= 11.6:
                middle_nkt = '10.6-11.5'
            elif 11.6 < middle_nkt_value <= 12.5:
                middle_nkt = '11.6-12.5'

            aaaa = DESCENT_NORM_SBT[well_data.lifting_unit_combo]
            koef_norm_down = DESCENT_NORM_SBT[well_data.lifting_unit_combo][nkt_key][middle_nkt]
            razdel_2_down = DESCENT_NORM_SBT[well_data.lifting_unit_combo][nkt_key]['раздел']

            work_list.extend([
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', self.type_equipment,
                 f'Спуск компоновка {nkt_key}', None,
                 None, None, None,
                 None, nkt_key, nkt_lenght,
                 middle_nkt, None, None, None, None,
                 razdel_2_down, None, 'шт', nkt_count,
                 koef_norm_down, self.coefficient_lifting, '=V448*W448*X448', '=Y448-AA448-AB448-AC448-AD448', None,
                 None,
                 None, None, None]])

            work_list.extend([
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', self.type_equipment,
                 'Навернуть/отвернуть предохранительное кольцо',
                 None, None, None, None, None, None, None, None, None, None, None, None, '§300разд.1',
                 None, 'шт',
                 sum_nkt, 0.003, 1, '=V449*W449*X449', '=Y449-AA449-AB449-AC449-AD449', None,
                 None, None,
                 None, None],
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', self.type_equipment, 'Замер НКТ ', None,
                 None,
                 None, None, None, None,
                 None, None, None, None, None, None, '§47разд.1', None, 'шт', sum_nkt, 0.008, 1,
                 '=V450*W450*X450',
                 '=Y450-AA450-AB450-AC450-AD450', None, None, None, None, None]])
            if sum_nkt > 201:
                work_list.append([
                    '=ROW()-ROW($A$46)', 'спуск 73мм', None, 'спо', self.type_equipment,
                    'Подкатывание труб с 201 трубы ', None,
                    None, None, None, None, None, None, None, None, None, None, None, '§40разд.1', None, 'шт',
                    sum_nkt - 201, 0.008, 1, '=V451*W451*X451', '=Y451-AA451-AB451-AC451-AD451', None, None, None,
                    None,
                    None])

        return work_list

    def raid_work(self):
        complications_of_failure_list = []
        complications_during_disassembly_list = []
        if self.select_type_combo != 'СБТ':
            work_list = [
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'Монтаж и демонтаж автокрана',
                 None,
                 None,
                 None, None, None, None, None, None, None, None, None, None, '§32разд.1', None, 'шт', 1, 0.27, 1,
                 '=V728*W728*X728', '=Y728-AA728-AB728-AC728-AD728', None, None, None, None, None],
                ['=ROW()-ROW($A$46)', 'кроме СБТ', None, 'Тех.операции', None, 'Разгрузить ВЗД + долото', None, None,
                 None, None, None, None, None, None, None, None, None, None, '§299разд.1 ', None, 'шт', 2, 0.12, 1,
                 '=V729*W729*X729', '=Y729-AA729-AB729-AC729', None, None, None, None, None]]
        else:
            work_list = []

        work_spo_list = [

            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', self.type_equipment, 'ПЗР СПО фрез(долото)', None,
             None, None,
             None, None, None,
             None, None, None, None, None, None, '§260,262разд.1', None, 'шт', 1, 0.4, 1, '=V730*W730*X730',
             '=Y730-AA730-AB730-AC730-AD730', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'М/ж спайдера', None, None, None,
             None, None, None,
             None, None, None, None, None, None, '§185разд.1', None, 'час', 1, 0.07, 1, '=V731*W731*X731',
             '=Y731-AA731-AB731-AC731-AD731', None, None, None, None, None],
            # ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', 'Райбер', 'ПЗР СПО шламоуловитель', None, None, None, None, None,
            #  None, None, None, None, None, None, None, ' §174,175 разд.1', None, 'раз', 1, '=0.13+0.17', 1,
            #  '=V732*W732*X732', '=Y732-AA732-AB732-AC732', None, None, None, None, None],
        ]
        if self.select_type_combo != 'СБТ':
            work_list.extend([['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', self.type_equipment, 'ПЗР СПО ЗД', None, None, None,
             None, None,
             None, None, None, None, None, None, None, '§263разд.1', None, 'шт', 1, 0.38, 1, '=V733*W733*X733',
             '=Y733-AA733-AB733-AC733-AD733', None, None, None, None, None]])

        work_list.extend(work_spo_list)

        if len(self.dict_nkt) != 0:
            if self.select_type_combo == 'НКТ':
                work_list.extend(TemplateWithoutSKM.descent_nkt_work(self))
            else:
                work_list.extend(self.descent_SBT())

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

        if self.select_type_combo == 'СБТ':
            work_list.extend(self.drilling_with_sbt_work())

        if self.count_of_nkt_extensions_line != 0:
            work_list.extend(self.skm_work())

        if self.select_type_combo == 'СБТ':
            work_list.extend(self.drilling_with_sbt_work_up())

        if self.solvent_injection_combo == 'Да':
            work_list.extend(self.solvent_injection_work())

        if self.technological_crap_question_combo == 'Да':
            technological_crap_question_list = TemplateWithoutSKM.descent_nkt_work(self)

            for row in technological_crap_question_list:
                technological_crap_question_list[row][13] = self.count_nkt_line * 10
                technological_crap_question_list[row][21] = self.count_nkt_line

            technological_crap_question_list.extend([
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
                 f'{self.technological_crap_question_text_line} {self.technological_crap_question_time_begin_date}-'
                 f'{self.technological_crap_question_time_end_date}', None, None, None,
                 None, None, None,
                 None, None, 'АКТ№', None, None, None, 'простои', 'Тех. ожидание',
                 'час', self.technological_crap_question_time_line, 1, 1,
                 '=V467*W467*X467',
                 '=Y467-AA467-AB467-AC467-AD467', None, None, None, None, None],
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
                 f'Определение кровли на гл. {self.roof_definition_depth_line}м', None, None,
                 None, None, None, None, None, None, 'АКТ№', None, None, None,
                 '§289разд.1', None, 'шт', 1, 0.17, 1,
                 '=V468*W468*X468', '=Y468-AA468-AB468-AC468-AD468', None, None, None,
                 None, None]])

            work_list.extend(technological_crap_question_list)
            self.date_work_line = self.technological_crap_question_time_end_date.split(' ')[0]

        work_list.extend(TemplateWithoutSKM.deinstallation_of_washing_equipment(self))
        if self.select_type_combo == 'НКТ':
            work_list.extend(TemplateWithoutSKM.lifting_nkt(self))
        else:
            work_list.extend(self.lifting_SBT())
            well_data.count_SBT += 1

            if self.type_key_combo == 'Да':
                work_list.extend(self.deinstallation_key())

        if self.equipment_audit_combo == 'Да':
            work_list.extend([
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
                 f'Ревизия:{self.equipment_audit_text_line}',
                 None, None, None, None, None, None, None, None, None, None, None,
                 None, 'факт', None, 'час', 0.5, 1, 1, '=V480*W480*X480', '=Y480-AA480-AB480-AC480-AD480', None,
                 None, None, None, None]]
            )

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

    def drilling_with_sbt_work_up(self):
        work_list = [

            ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None, 'Демонтаж спецтрубы', None, None, None, None,
             None,
             None, None, None, None, None, None, None, '§300разд.1 п.148', None, 'шт', 1, 0.27, 1,
             '=V932*W932*X932',
             '=Y932-AA932-AB932-AC932-AD932', None, None, None, None, None]]
        if self.type_rotor_combo == 'Гидроротор':
            work_list.extend([
                ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None, 'Демонтаж гидроротора ', None, None, None, None,
                 None, None, None, None, None, None, None, None, '§245разд.1', None, 'шт', 1, 0.38, 1,
                 '=V933*W933*X933',
                 '=Y933-AA933-AB933-AC933-AD933', None, None, None, None, None]])
        else:
            work_list.extend([
                ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None, 'Демонтаж мех. ротора', None, None, None, None,
                 None, None, None, None, None, None, None, None, '§247разд.1', None, 'шт', 1, 0.68, 1,
                 '=V934*W934*X934',
                 '=Y934-AA934-AB934-AC934-AD934', None, None, None, None, None]])

        if self.type_key_combo == 'Да':
            if self.count_spo_sbt_combo == 'Да':
                work_list.extend([
                    ['=ROW()-ROW($A$46)', 'подъем СБТ с УМК', None, 'Тех.операции', None,
                     'М/ж машинных ключей (первый монтаж)',
                     None, None, None, None, None, None, None, None, None, None, None, None, '§256разд.1', None, 'час',
                     1,
                     1, 1,
                     '=V936*W936*X936', '=Y936-AA936-AB936-AC936-AD936', None, None, None, None, None]])
            else:
                work_list.extend(
                    [['=ROW()-ROW($A$46)', 'подъем СБТ', None, 'Тех.операции', None,
                      'М/ж машинных ключей (след.монтаж)',
                      None, None, None, None, None, None, None, None, None, None, None, None, '§256разд.1', None, 'час',
                      0.25,
                      1, 1, '=V937*W937*X937', '=Y937-AA937-AB937-AC937-AD937', None, None, None, None, None]])

        return work_list

    def deinstallation_key(self):
        if self.count_spo_sbt_combo == 'Да':
            work_list = [
                ['=ROW()-ROW($A$46)', 'подъем СБТ', None, 'Тех.операции', None, 'Д/ж машинных ключей (первый раз)',
                 None, None, None, None, None, None, None, None, None, None, None, None, '§257разд.1', None, 'час',
                 0.12, 1, 1, '=V938*W938*X938', '=Y938-AA938-AB938-AC938-AD938', None, None, None, None, None]]
        else:
            work_list = [
                ['=ROW()-ROW($A$46)', 'подъем СБТ', None, 'Тех.операции', None, 'Д/ж машинных ключей (в конце)',
                 None,
                 None,
                 None, None, None, None, None, None, None, None, None, None, '§257разд.1', None, 'час', 0.47, 1, 1,
                 '=V939*W939*X939', '=Y939-AA939-AB939-AC939-AD939', None, None, None, None, None]]
        return work_list

    def drilling_with_sbt_work(self):
        work_list = [
            ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None, 'Демонтаж спайдера СПГ', None, None, None, None,
             None, None, None, None, None, None, None, None, '§185разд.1', None, 'шт', 1, 0.07, 1,
             '=V922*W922*X922',
             '=Y922-AA922-AB922-AC922-AD922', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None,
             'Демонтаж гидравлических ключей трубных(ГШК-1200, ГШК-1500 )', None, None, None, None, None, None,
             None,
             None, None, None, None, None, '§184разд.1', None, 'шт', 1, 0.12, 1, '=V923*W923*X923',
             '=Y923-AA923-AB923-AC923-AD923', None, None, None, None, None]]
        if self.type_rotor_combo == 'Гидротор':
            work_list.extend([
                ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None, 'Монтаж гидроротора', None, None, None,
                 None, None,
                 None, None, None, None, None, None, None, '§244разд.1', None, 'шт', 1, 0.45, 1, '=V924*W924*X924',
                 '=Y924-AA924-AB924-AC924-AD924', None, None, None, None, None]])
        else:
            if self.count_spo_sbt_combo == 'Да':
                work_list.extend([
                    ['=ROW()-ROW($A$46)', '1 монтаж', None, 'Тех.операции', 'Ротор', 'Монтаж мех. ротора', None,
                     None, None,
                     None, None, None, None, None, None, None, None, None, '§246разд.1', None, 'шт', 1, 2.53, 1,
                     '=V925*W925*X925', '=Y925-AA925-AB925-AC925-AD925', None, None, None, None, None]])
            else:
                work_list.extend([
                    ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None, 'Монтаж мех. ротора', None, None, None,
                     None, None,
                     None, None, None, None, None, None, None, '§246разд.1', None, 'шт', 1, 1.02, 1,
                     '=V926*W926*X926',
                     '=Y926-AA926-AB926-AC926-AD926', None, None, None, None, None]])

            work_list.extend([
                ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None, 'Монтаж  ведущий трубы', None, None, None,
                 None,
                 None, None, None, None, None, None, None, None, '§300разд.1 п.148', None, 'шт', 1, 0.27, 1,
                 '=V927*W927*X927', '=Y927-AA927-AB927-AC927-AD927', None, None, None, None, None]])

        return work_list

    def solvent_injection_work(self):
        work_list = [
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'ОПЗ',
             'Подготовительные работы, выполняемые ', None,
             None, None, 'ПО ТКРС', None, None, 'перед началом работ на скважине', None, None, 'РАСТВОРИТЕЛЬ',
             'Растворитель АСПО Реком 7125 серия 4, КР-4Р', None, '§227,229разд.1', None, 'шт', 1, 0.96, 1,
             '=V589*W589*X589', '=Y589-AA589-AB589-AC589-AD589', None, None, None, None, None]]
        if self.solvent_volume_text_line > 1:
            solvent_volume_list = [
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'ОПЗ',
                 f'Закачка растворителя первого 1м3',
                 None, None, None, None, None, None, None, None, 'АКТ№', None, None, None, '§228разд.1', None, 'м3',
                 1,
                 0.2,
                 1, '=V590*W590*X590', '=Y590-AA590-AB590-AC590-AD590', None, None, None, None, None],
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'ОПЗ',
                 f'Закачка растворителя следующего {self.solvent_volume_text_line - 1}м3', None, None,
                 None, None, None, None, None, None, 'АКТ№', None, None, None, '§228разд.1', None, 'м3', 1, 0.1,
                 1, '=V591*W591*X591', '=Y591-AA591-AB591-AC591-AD591', None, None, None, None, None]]
        else:
            solvent_volume_list = [
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'ОПЗ',
                 f'Закачка растворителя первого {self.solvent_volume_text_line}м3', None,
                 None, None, None, None, None, None, None, 'АКТ№', None, None, None, '§228разд.1', None, 'м3', 1,
                 0.2,
                 1, '=V590*W590*X590', '=Y590-AA590-AB590-AC590-AD590', None, None, None, None, None],
            ]
        work_list.extend(solvent_volume_list)
        volume_list = [
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'ОПЗ',
             f'Доводка растворителя в объеме {self.volume_of_finishing_line}', None, None, None, None,
             None, None, None, None, None, None, None, None, '§228разд.1', None, 'м3',
             self.volume_of_finishing_line,
             0.033, 1, '=V592*W592*X592',
             '=Y592-AA592-AB592-AC592-AD592', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'ОПЗ',
             f'Реагирование {self.solvent_volume_time_begin_date}-{self.solvent_volume_time_end_date}', None, None,
             None,
             None,
             None, None, None, None, 'АКТ№', None, None, None, 'простои', 'Тех. ожидание', 'час',
             self.solvent_volume_time_line, 1, 1,
             '=V593*W593*X593', '=Y593-AA593-AB593-AC593-AD593', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'Промывка', 'Переход на труб.простр.',
             None, None,
             None,
             None, None, None, None, None, None, None, None, None, '§162разд.1', None, 'раз', 1, 0.15, 1,
             '=V594*W594*X594', '=Y594-AA594-AB594-AC594-AD594', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'Промывка',
             f'Промывка в объеме {self.volume_flush_line}',
             None, None, None, None, None, None, None, None, 'АКТ№', None, None, None, '§301разд.1', None, 'м3',
             {self.volume_flush_line}, 0.033, 1, '=V595*W595*X595',
             '=Y595-AA595-AB595-AC595-AD595', None, None, None, None, None]]
        work_list.extend(volume_list)
        return work_list

if __name__ == "__main__":
    # app3 = QApplication(sys.argv)

    app = QApplication(sys.argv)
    window = DrillingWork(22, 22)
    window.show()
    sys.exit(app.exec_())
