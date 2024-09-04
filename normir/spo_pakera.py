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


class TabPage_SO_Timplate(QWidget):
    def __init__(self, parent=None):
        super().__init__()

        self.validator_int = QIntValidator(0, 6000)
        self.validator_float = QDoubleValidator(0, 6000, 1)

        self.date_work_label = QLabel('Дата работы')
        self.date_work_line = QLineEdit(self)
        self.date_work_line.setText(f'{well_data.date_work}')

        self.date_work_str = datetime.strptime(self.date_work_line.text(), '%d.%m.%Y')

        self.select_paker_combo_label = QLabel('Выбор компоновки спуска')
        self.select_paker_combo = QComboBox(self)
        self.select_paker_combo.addItems(['', 'пакер', 'два пакера', 'пакер с заглушкой'])

        self.grid = QGridLayout(self)

        self.grid.addWidget(self.date_work_label, 4, 2)
        self.grid.addWidget(self.date_work_line, 5, 2)

        self.grid.addWidget(self.select_paker_combo_label, 4, 3)
        self.grid.addWidget(self.select_paker_combo, 5, 3)

        self.select_paker_combo.currentTextChanged.connect(self.update_select_paker_combo)

        if well_data.date_work != '':
            self.date_work_line.setText(well_data.date_work)

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
        self.rezult_zumpf_pressuar_combo_label = QLabel('Результат опрессовки')
        self.determination_of_pickup_combo_label = QLabel('Было ли определение Q?')
        self.determination_of_pickup_combo_zumpf_label = QLabel('Было ли определение Q?')
        self.saturation_volume_label = QLabel('Насыщение')
        self.determination_of_pickup_text_label = QLabel('Текст определение Q')
        self.saturation_volume_zumpf_label = QLabel('Насыщение')
        self.determination_of_pickup_zumpf_text_label = QLabel('Текст определение Q')

    def update_select_paker_combo(self, index):
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

        self.determination_of_pickup_combo = QComboBox(self)
        self.determination_of_pickup_combo.addItems(['Нет', 'Да'])

        self.grid.addWidget(self.determination_of_pickup_combo_label, 30, 4)
        self.grid.addWidget(self.determination_of_pickup_combo, 31, 4)

        self.depth_zumpf_paker_combo = QComboBox(self)
        self.depth_zumpf_paker_combo.addItems(['Нет', 'Да'])

        self.grid.addWidget(self.depth_zumpf_paker_combo_label, 30, 8)
        self.grid.addWidget(self.depth_zumpf_paker_combo, 31, 8)

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

        self.pressuar_tnkt_combo = QComboBox(self)
        self.pressuar_tnkt_combo.addItems(['Нет', 'Да'])

        self.grid.addWidget(self.pressuar_tnkt_label, 50, 1)
        self.grid.addWidget(self.pressuar_tnkt_combo, 51, 1)

        self.extra_work_question_combo = QComboBox(self)
        self.extra_work_question_combo.addItems(['Нет', 'Да'])

        self.grid.addWidget(self.extra_work_question_label, 52, 1)
        self.grid.addWidget(self.extra_work_question_combo, 53, 1)

        self.depth_paker_text_edit = QLineEdit(self)

        self.rezult_pressuar_combo = QComboBox(self)
        self.rezult_pressuar_combo.addItems(['+', '-'])

        self.pressuar_ek_line = QLineEdit(self)
        self.pressuar_ek_line.setValidator(self.validator_float)

        self.grid.addWidget(self.depth_paker_text_label, 30, 1)
        self.grid.addWidget(self.depth_paker_text_edit, 31, 1)

        self.grid.addWidget(self.pressuar_ek_label, 30, 2)
        self.grid.addWidget(self.pressuar_ek_line, 31, 2)
        self.grid.addWidget(self.rezult_pressuar_combo_label, 30, 3)
        self.grid.addWidget(self.rezult_pressuar_combo, 31, 3)

        self.depth_zumpf_paker_combo.currentTextChanged.connect(self.update_depth_zumpf_paker)

        self.determination_of_pickup_combo.currentTextChanged.connect(self.update_determination_of_pickup_combo)
        # self.pressuar_gno_combo.currentTextChanged.connect(self.update_pressuar_gno_combo)
        self.extra_work_question_combo.currentTextChanged.connect(self.update_extra_work_question_combo)
        self.solvent_injection_combo.currentTextChanged.connect(self.update_solvent_injection_combo)
        # self.pressuar_gno_combo.currentTextChanged.connect(self.update_pressuar_gno_combo)
        self.pressuar_tnkt_combo.currentTextChanged.connect(self.update_pressuar_tnkt_combo)
        self.complications_of_failure_combo.currentTextChanged.connect(self.update_complications_of_failure)
        self.complications_when_lifting_combo.currentTextChanged.connect(self.update_complications_when_lifting)

        self.complications_during_tubing_running_combo.currentTextChanged.connect(
            self.update_complications_during_tubing_running_combo)
        self.nkt_is_same_combo.currentTextChanged.connect(self.update_nkt_is_same_combo)

    def update_determination_of_pickup_combo(self, index):
        if index == 'Нет':
            self.saturation_volume_label.setParent(None)
            self.determination_of_pickup_text_label.setParent(None)
            self.saturation_volume_line.setParent(None)
            self.determination_of_pickup_text.setParent(None)
        else:
            self.saturation_volume_line = QLineEdit(self)
            self.saturation_volume_line.setValidator(self.validator_float)

            self.determination_of_pickup_text = QLineEdit(self)

            self.grid.addWidget(self.saturation_volume_label, 30, 5)
            self.grid.addWidget(self.saturation_volume_line, 31, 5)
            self.grid.addWidget(self.determination_of_pickup_text_label, 30, 6)
            self.grid.addWidget(self.determination_of_pickup_text, 31, 6)

    def update_determination_of_pickup_zumpf_combo(self, index):
        if index == 'Нет':
            self.saturation_volume_zumpf_line.setParent(None)
            self.determination_of_pickup_zumpf_text.setParent(None)
            self.saturation_volume_zumpf_label.setParent(None)
            self.determination_of_pickup_zumpf_text_label.setParent(None)
        else:
            self.saturation_volume_zumpf_line = QLineEdit(self)
            self.saturation_volume_zumpf_line.setValidator(self.validator_float)

            self.determination_of_pickup_zumpf_text = QLineEdit(self)

            self.grid.addWidget(self.saturation_volume_zumpf_label, 30, 12)
            self.grid.addWidget(self.saturation_volume_zumpf_line, 31, 12)
            self.grid.addWidget(self.determination_of_pickup_zumpf_text_label, 30, 13)
            self.grid.addWidget(self.determination_of_pickup_zumpf_text, 31, 13)

    def update_depth_zumpf_paker(self, index):
        if index == 'Нет':
            self.depth_zumpf_paker_line.setParent(None)
            self.rezult_zumpf_pressuar_combo.setParent(None)
            self.determination_of_pickup_zumpf_combo.setParent(None)
            self.depth_zumpf_paker_label.setParent(None)
            self.rezult_zumpf_pressuar_combo_label.setParent(None)
            self.determination_of_pickup_combo_zumpf_label.setParent(None)
            try:
                self.saturation_volume_zumpf_line.setParent(None)
                self.determination_of_pickup_zumpf_text.setParent(None)
                self.saturation_volume_zumpf_label.setParent(None)
                self.determination_of_pickup_zumpf_text_label.setParent(None)
            except:
                pass
        else:
            self.depth_zumpf_paker_line = QLineEdit(self)
            self.depth_zumpf_paker_line.setValidator(self.validator_float)
            self.rezult_zumpf_pressuar_combo = QComboBox(self)
            self.rezult_zumpf_pressuar_combo.addItems(['+', '-'])
            self.determination_of_pickup_zumpf_combo = QComboBox(self)
            self.determination_of_pickup_zumpf_combo.addItems(['Нет', 'Да'])

            self.grid.addWidget(self.depth_zumpf_paker_label, 30, 9)
            self.grid.addWidget(self.depth_zumpf_paker_line, 31, 9)
            self.grid.addWidget(self.rezult_zumpf_pressuar_combo_label, 30, 10)
            self.grid.addWidget(self.rezult_zumpf_pressuar_combo, 31, 10)
            self.grid.addWidget(self.determination_of_pickup_combo_zumpf_label, 30, 11)
            self.grid.addWidget(self.determination_of_pickup_zumpf_combo, 31, 11)

            self.determination_of_pickup_zumpf_combo.currentTextChanged.connect(
                self.update_determination_of_pickup_zumpf_combo)

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

    def update_pressuar_tnkt_combo(self, index):

        if index == 'Нет':
            self.pressuar_tnkt_text_label.setParent(None)
            self.pressuar_tnkt_text_line.setParent(None)
        else:
            self.pressuar_tnkt_text_label = QLabel('Текст опрессовки')
            self.pressuar_tnkt_text_line = QLineEdit(self)

            self.grid.addWidget(self.pressuar_tnkt_text_label, 50, 2)
            self.grid.addWidget(self.pressuar_tnkt_text_line, 51, 2)

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
            self.solvent_volume_text_label = QLabel('Объем раствроителя')
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

    def update_extra_work_question_combo(self, index):

        if index == 'Нет':
            self.extra_work_text_label.setParent(None)
            self.extra_work_text_line.setParent(None)
            self.extra_work_time_label.setParent(None)
            self.extra_work_time_line.setParent(None)
            self.extra_work_time_end_label.setParent(None)
            self.extra_work_time_end_date.setParent(None)
            self.extra_work_time_begin_label.setParent(None)
            self.extra_work_time_begin_date.setParent(None)
            self.roof_definition_depth_label.setParent(None)
            self.roof_definition_depth_line.setParent(None)

        else:
            self.type_combo_work_label = QLabel('Вид работ')
            self.type_combo_work = QComboBox(self)
            self.type_combo_work.addItems(['', 'Крезол', 'Сваб', 'Кислота силами подрядчика',
                                           'РИР 2С', 'ГРП', 'Огневые, земляные работы'])

            self.grid.addWidget(self.type_combo_work_label, 52, 2)
            self.grid.addWidget(self.type_combo_work, 53, 2)

            self.type_combo_work.currentTextChanged.connect(self.update_type_combo_work)

    def update_type_combo_work(self, index):
        # 'Крезол', 'Сваб', 'Кислота силами подрядчика',
        # 'РИР 2С', 'ГРП', 'Огневые, земляные работы'

        self.extra_work_text_label = QLabel('Текст проведения работ')
        self.extra_work_text_line = QLineEdit(self)

        self.extra_work_time_begin_label = QLabel('начало проведения работ')
        self.extra_work_time_begin_date = QDateTimeEdit(self)
        self.extra_work_time_begin_date.setDisplayFormat("dd.MM.yyyy HH:mm")
        self.extra_work_time_begin_date.setDateTime(self.date_work_str)

        self.extra_work_time_end_label = QLabel('Окончание проведения работ')
        self.extra_work_time_end_date = QDateTimeEdit(self)
        self.extra_work_time_end_date.setDisplayFormat("dd.MM.yyyy HH:mm")
        self.extra_work_time_end_date.setDateTime(self.date_work_str)

        self.extra_work_time_label = QLabel('затраченное время')
        self.extra_work_time_line = QLineEdit(self)
        self.extra_work_time_line.setValidator(self.validator_float)

        # self.grid.addWidget(self.extra_work_text_label, 52, 2)
        # self.grid.addWidget(self.extra_work_text_line, 53, 2)
        self.grid.addWidget(self.extra_work_time_begin_label, 52, 3)
        self.grid.addWidget(self.extra_work_time_begin_date, 53, 3)
        self.grid.addWidget(self.extra_work_time_end_label, 52, 4)
        self.grid.addWidget(self.extra_work_time_end_date, 53, 4)
        self.grid.addWidget(self.extra_work_time_label, 52, 5)
        self.grid.addWidget(self.extra_work_time_line, 53, 5)

        self.extra_work_time_end_date.dateTimeChanged.connect(self.update_date_technological_crap)
        self.extra_work_time_begin_date.dateTimeChanged.connect(
            self.update_date_technological_crap)

        if index in ['Крезол', 'Кислота силами подрядчика']:

            self.response_text_label = QLabel('Текст реагирование')
            self.response_text_line = QLineEdit(self)
            self.response_text_line.setText('Реагирование')

            self.response_time_begin_label = QLabel('начало реагирования')
            self.response_time_begin_date = QDateTimeEdit(self)
            self.response_time_begin_date.setDisplayFormat("dd.MM.yyyy HH:mm")
            self.response_time_begin_date.setDateTime(self.date_work_str)

            self.response_time_end_label = QLabel('Окончание реагирования')
            self.response_time_end_date = QDateTimeEdit(self)
            self.response_time_end_date.setDisplayFormat("dd.MM.yyyy HH:mm")
            self.response_time_end_date.setDateTime(self.date_work_str)

            self.response_time_line_label = QLabel('Затраченное время')
            self.response_time_line = QLineEdit(self)

            self.count_nkt_label = QLabel('Количество НКТ на допуск')
            self.count_nkt_line = QLineEdit(self)
            self.count_nkt_line.setValidator(self.validator_int)
            self.count_nkt_line.setText('3')

            self.roof_definition_depth_label = QLabel('Глубина воронки')
            self.roof_definition_depth_line = QLineEdit(self)
            self.roof_definition_depth_line.setValidator(self.validator_float)

            self.volume_flush_line_sko_label = QLabel('Объем промывки после СКО')
            self.volume_flush_line_sko_line = QLineEdit(self)
            self.volume_flush_line_sko_line.setValidator(self.validator_float)

            self.saturation_volume_sko_label = QLabel('Насыщение')
            self.saturation_volume_sko_line = QLineEdit(self)
            self.saturation_volume_sko_line.setValidator(self.validator_float)

            self.determination_of_pickup_sko_text_label = QLabel('Текст определение Q')
            self.determination_of_pickup_sko_text_line = QLineEdit(self)

            self.grid.addWidget(self.response_text_label, 62, 1)
            self.grid.addWidget(self.response_text_line, 63, 1)

            self.grid.addWidget(self.response_time_begin_label, 62, 2)
            self.grid.addWidget(self.response_time_begin_date, 63, 2)

            self.grid.addWidget(self.response_time_end_label, 62, 3)
            self.grid.addWidget(self.response_time_end_date, 63, 3)

            self.grid.addWidget(self.response_time_line_label, 62, 4)
            self.grid.addWidget(self.response_time_line, 63, 4)

            self.grid.addWidget(self.count_nkt_label, 64, 2)
            self.grid.addWidget(self.count_nkt_line, 65, 2)
            self.grid.addWidget(self.roof_definition_depth_label, 64, 3)
            self.grid.addWidget(self.roof_definition_depth_line, 65, 3)
            self.grid.addWidget(self.volume_flush_line_sko_label, 64, 4)
            self.grid.addWidget(self.volume_flush_line_sko_line, 65, 4)

            self.grid.addWidget(self.saturation_volume_sko_label, 66, 2)
            self.grid.addWidget(self.saturation_volume_sko_line, 67, 2)
            self.grid.addWidget(self.determination_of_pickup_sko_text_label, 66, 3)
            self.grid.addWidget(self.determination_of_pickup_sko_text_line, 67, 3)

            self.response_time_end_date.dateTimeChanged.connect(self.update_date_response)
            self.response_time_begin_date.dateTimeChanged.connect(
                self.update_date_response)

            if index in ['Крезол']:
                self.extra_work_text_line.setText('Работа фирмы ООО "Крезол"')

            if index in ['Кислота силами подрядчика']:
                self.skv_combo_label = QLabel(self)
                self.skv_combo = QComboBox(self)
                self.skv_combo.addItems(['Нет', 'Да'])

                self.response_skv_text_label = QLabel('Текст реагирование')
                self.response_skv_text_line = QLineEdit(self)
                self.response_skv_text_line.setText('Тех отстой')

                self.response_skv_time_begin_label = QLabel('начало реагирования')
                self.response_skv_time_begin_date = QDateTimeEdit(self)
                self.response_skv_time_begin_date.setDisplayFormat("dd.MM.yyyy HH:mm")
                self.response_skv_time_begin_date.setDateTime(self.date_work_str)

                self.response_skv_time_end_label = QLabel('Окончание реагирования')
                self.response_skv_time_end_date = QDateTimeEdit(self)
                self.response_skv_time_end_date.setDisplayFormat("dd.MM.yyyy HH:mm")
                self.response_skv_time_end_date.setDateTime(self.date_work_str)

                self.grid.addWidget(self.skv_combo_label, 54, 2)
                self.grid.addWidget(self.skv_combo_label, 55, 2)
                self.skv_combo.currentTextChanged.connect(self.update_skv_combo)

    def update_skv_combo(self, index):
        if index == 'Нет':
            pass
        else:
            self.volume_skv_label = QLabel(self)
            self.volume_skv_line = QLineEdit(self)
            self.volume_skv_line.setValidator(self.validator_float)

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

    def update_date_technological_crap(self):
        time_begin = self.extra_work_time_begin_date.dateTime()
        time_end = self.extra_work_time_end_date.dateTime()

        time_difference = self.calculate_date(time_begin, time_end)

        self.extra_work_time_line.setText(str(time_difference))

    def update_date_response(self):
        time_begin = self.response_time_begin_date.dateTime()
        time_end = self.response_time_end_date.dateTime()

        time_difference = self.calculate_date(time_begin, time_end)

        self.response_time_line.setText(str(time_difference))

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
        self.addTab(TabPage_SO_Timplate(self), 'пакер')


class SpoPakerAction(QMainWindow):
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
        self.pressuar_ek_line = None
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
        self.select_paker_combo = current_widget.select_paker_combo.currentText()
        self.rezult_pressuar_combo = current_widget.rezult_pressuar_combo.currentText()
        self.depth_zumpf_paker_combo = current_widget.depth_zumpf_paker_combo.currentText()
        if self.depth_zumpf_paker_combo == 'Да':
            self.depth_zumpf_paker_line = current_widget.depth_zumpf_paker_line.text()
            if self.depth_zumpf_paker_line not in ['', None]:
                self.depth_zumpf_paker_line = int(self.depth_zumpf_paker_line)
            else:
                question = QMessageBox.question(self, 'Глубина посадки', 'Не введена глубина посадки пакера зумпфа')
                if question == QMessageBox.StandardButton.No:
                    return
            self.determination_of_pickup_zumpf_combo = current_widget.determination_of_pickup_zumpf_combo.currentText()
            if self.determination_of_pickup_zumpf_combo == 'Да':
                self.saturation_volume_zumpf_line = current_widget.saturation_volume_zumpf_line.text()
                if self.saturation_volume_zumpf_line == '':
                    QMessageBox.warning(self, 'Объем насыщения', 'Не введен объем насыщения зумпфа')
                    return

                self.determination_of_pickup_zumpf_text = current_widget.determination_of_pickup_zumpf_text.text()
                if self.determination_of_pickup_zumpf_text == '':
                    QMessageBox.warning(self, 'Объем насыщения', 'Не введен текст определения Q Зумфпа')
                    return
        self.determination_of_pickup_combo = current_widget.determination_of_pickup_combo.currentText()
        if self.determination_of_pickup_combo == 'Да':
            self.saturation_volume_line = current_widget.saturation_volume_line.text()
            if self.saturation_volume_line == '':
                QMessageBox.warning(self, 'Объем насыщения', 'Не введен объем насыщения ')
                return

            self.determination_of_pickup_text = current_widget.determination_of_pickup_text.text()
            if self.determination_of_pickup_text == '':
                QMessageBox.warning(self, 'Объем насыщения', 'Не введен текст определения Q')
                return

        if self.select_paker_combo == '':
            return

        self.determination_of_pickup_sko_text_line = current_widget.determination_of_pickup_sko_text_line.text()
        self.saturation_volume_sko_line = current_widget.saturation_volume_sko_line.text()

        if self.determination_of_pickup_sko_text_line == "":
            determination_question = QMessageBox.question(self,
                                                          'Определение приемистости',
                                                          'Не введена текст определения приемистости, работ не было?')
            if determination_question == QMessageBox.StandardButton.No:
                return
            else:
                if self.saturation_volume_sko_line == '':
                    QMessageBox.warning(self, 'Объем насыщения', 'Введите объем насыщения после СКО')

        self.type_equipment = 'пакер'
        self.coefficient_lifting = 1.2

        self.depth_paker_text_edit = current_widget.depth_paker_text_edit.text()

        if self.depth_paker_text_edit not in ['', None]:
            self.depth_paker_text_edit = int(self.depth_paker_text_edit)
        else:
            question = QMessageBox.question(self, 'Глубина посадки', 'Не введена глубина посадки пакера зумпфа')
            if question == QMessageBox.StandardButton.No:
                return

        self.pressuar_ek_line = current_widget.pressuar_ek_line.text()
        if self.pressuar_ek_line != '':
            self.pressuar_ek_line = int(self.pressuar_ek_line)
        else:
            question = QMessageBox.question(self, 'Давление', 'Не указано давлени опрессовки?')
            if question == QMessageBox.StandardButton.No:
                return

        self.nkt_is_same_combo = current_widget.nkt_is_same_combo.currentText()

        try:
            self.nkt_48_lenght_edit = current_widget.nkt_48_lenght_edit.text()
            self.nkt_48_count_edit = current_widget.nkt_48_count_edit.text()
            self.nkt_60_lenght_edit = current_widget.nkt_60_lenght_edit.text()
            self.nkt_60_count_edit = current_widget.nkt_60_count_edit.text()
            self.nkt_73_lenght_edit = current_widget.nkt_73_lenght_edit.text()
            self.nkt_73_count_edit = current_widget.nkt_73_count_edit.text()
            self.nkt_89_lenght_edit = current_widget.nkt_89_lenght_edit.text()
            self.nkt_89_count_edit = current_widget.nkt_89_count_edit.text()
            if 6.5 < int(float(self.nkt_73_lenght_edit)) / int(float(self.nkt_73_count_edit)) < 12.5 == False:
                QMessageBox.warning(self, 'Ошибка в средней длине НКТ', 'Ошибка в средней длине НКТ')
                return
            if self.nkt_48_lenght_edit != '' and self.nkt_48_count_edit != '':
                self.dict_nkt.setdefault('48мм',
                                         (int(float(self.nkt_48_lenght_edit)), int(float(self.nkt_48_count_edit))))
            if self.nkt_60_lenght_edit != '' and self.nkt_60_count_edit != '':
                self.dict_nkt.setdefault('60мм',
                                         (int(float(self.nkt_60_lenght_edit)), int(float(self.nkt_60_count_edit))))
            if self.nkt_73_lenght_edit != '' and self.nkt_73_count_edit != '':
                self.dict_nkt.setdefault('73мм',
                                         (int(float(self.nkt_73_lenght_edit)), int(float(self.nkt_73_count_edit))))
            if self.nkt_89_lenght_edit != '' and self.nkt_89_count_edit != '':
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
        self.pressuar_tnkt_combo = current_widget.pressuar_tnkt_combo.currentText()
        self.solvent_injection_combo = current_widget.solvent_injection_combo.currentText()
        self.extra_work_question_combo = current_widget.extra_work_question_combo.currentText()
        self.complications_when_lifting_combo = current_widget.complications_when_lifting_combo.currentText()

        # self.pressuar_gno_combo = current_widget.pressuar_gno_combo.currentText()

        if self.pressuar_tnkt_combo == 'Да':
            self.pressuar_tnkt_text_line = current_widget.pressuar_tnkt_text_line.text()

            if current_widget.pressuar_tnkt_text_line.text() == self.pressuar_tnkt_time_begin_date:
                QMessageBox.warning(self, 'Даты совпадают', 'Даты совпадают')
                return

            if self.pressuar_tnkt_text_line == '':
                QMessageBox.warning(self, 'Ошибка', f'Не введены текст осложнения при срыве ПШ')
                return

            self.pressuar_tnkt_time_line = current_widget.pressuar_tnkt_time_line.text()
            if self.pressuar_tnkt_time_line != '':
                self.pressuar_tnkt_time_line = round(float(self.pressuar_tnkt_time_line), 1)

            else:
                QMessageBox.warning(self, 'Ошибка', f'Не введены время осложнения при срыве ПШ')
                return

            if self.pressuar_tnkt_time_line <= 0:
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
                QMessageBox.question(self, 'Ошибка', f'Не введены обьем доводки техводой растворителя')
                return

            if self.volume_flush_line != '':
                self.volume_flush_line = round(float(self.volume_flush_line), 1)
            else:
                QMessageBox.warning(self, 'Ошибка', f'Не обьем промывки скважины после реагирования')
                return

            if self.solvent_volume_time_line <= 0:
                QMessageBox.warning(self, 'Ошибка', f'Затраченное время при срыве ПШ не может быть отрицательным')
                return

        if self.extra_work_question_combo == 'Да':
            self.type_combo_work = current_widget.type_combo_work.currentText()
            if self.type_combo_work in ['Крезол', 'Кислота силами подрядчика']:
                self.count_nkt_line = current_widget.count_nkt_line.text()
                self.roof_definition_depth_line = current_widget.roof_definition_depth_line.text()
                if self.count_nkt_line not in [None, '']:
                    self.count_nkt_line = int(float(self.count_nkt_line))
                else:
                    count_question = QMessageBox.question(self, 'количество НКТ',
                                                          'Не указано количество НКТ при подьеме на доспуск, Допуска не было?')
                    if count_question == QMessageBox.StandardButton.No:
                        return
                    else:
                        if self.roof_definition_depth_line != '':
                            self.roof_definition_depth_line = int(float(self.roof_definition_depth_line))
                        else:
                            QMessageBox.warning(self, 'количество НКТ', 'Не указано глубина определения забоя')
                            return
                self.volume_flush_line_sko_line = current_widget.volume_flush_line_sko_line.text()
                if self.volume_flush_line_sko_line not in [None, '']:
                    self.volume_flush_line_sko_line = int(float(self.volume_flush_line_sko_line))
                else:
                    volume_sko_question = QMessageBox.question(self, 'Промывка после СКО',
                                                               'Не указано промывка после СКО '
                                                               'Промывки не было?')
                    if volume_sko_question == QMessageBox.StandardButton.No:
                        return

                self.response_text_line = current_widget.response_text_line.text()
                self.response_time_begin_date = \
                    current_widget.response_time_begin_date.dateTime().toPyDateTime()
                self.response_time_begin_date = \
                    self.change_string_in_date(self.response_time_begin_date)

                self.response_time_end_date = \
                    current_widget.response_time_end_date.dateTime().toPyDateTime()
                self.response_time_end_date = \
                    self.change_string_in_date(self.response_time_end_date)

                if current_widget.response_text_line.text() == self.response_time_begin_date:
                    QMessageBox.warning(self, 'Даты совпадают', 'Даты совпадают')
                    return

                if self.response_text_line == '':
                    QMessageBox.warning(self, 'Ошибка', f'Не введены текст работы подрядчика')
                    return

                self.response_time_line = current_widget.response_time_line.text()
                if self.response_time_line != '':
                    self.response_time_line = round(float(self.response_time_line), 1)

                else:
                    QMessageBox.warning(self, 'Ошибка', f'Не введены время работы подрядчика')
                    return

                if self.response_time_line <= 0:
                    QMessageBox.warning(self, 'Ошибка',
                                        f'Затраченное время при работы подрядчика не может быть отрицательным')
                    return

            self.extra_work_text_line = current_widget.extra_work_text_line.text()
            self.extra_work_time_begin_date = \
                current_widget.extra_work_time_begin_date.dateTime().toPyDateTime()
            self.extra_work_time_begin_date = \
                self.change_string_in_date(self.extra_work_time_begin_date)

            self.extra_work_time_end_date = \
                current_widget.extra_work_time_end_date.dateTime().toPyDateTime()
            self.extra_work_time_end_date = \
                self.change_string_in_date(self.extra_work_time_end_date)

            if current_widget.extra_work_text_line.text() == self.extra_work_time_begin_date:
                QMessageBox.warning(self, 'Даты совпадают', 'Даты совпадают')
                return

            if self.extra_work_text_line == '':
                QMessageBox.warning(self, 'Ошибка', f'Не введены текст работы подрядчика')
                return

            self.extra_work_time_line = current_widget.extra_work_time_line.text()
            if self.extra_work_time_line != '':
                self.extra_work_time_line = round(float(self.extra_work_time_line), 1)

            else:
                QMessageBox.warning(self, 'Ошибка', f'Не введены время работы подрядчика')
                return

            if self.extra_work_time_line <= 0:
                QMessageBox.warning(self, 'Ошибка',
                                    f'Затраченное время при работы подрядчика не может быть отрицательным')
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
                    QMessageBox.warning(self, 'Ошибка', f'Не введены текст осложнения при подьеме НКТ')
                    return
                else:
                    aaaaa = self.complications_when_lifting_time_line
                    self.complications_when_lifting_time_line = round(float(self.complications_when_lifting_time_line),
                                                                      1)

                if self.complications_when_lifting_time_line <= 0:
                    QMessageBox.warning(self, 'Ошибка',
                                        f'Затраченное время при подьеме штанг не может быть отрицательным')
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

        work_list = self.depth_paker_work()

        well_data.date_work = self.date_work_line

        MyWindow.populate_row(self, self.ins_ind, work_list, self.table_widget)
        well_data.pause = False
        self.close()

    def krezol_work(self):
        work_list = [
            ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', 'ОПЗ',
             f'{self.extra_work_text_line} {self.extra_work_time_begin_date}-{self.extra_work_time_end_date}',
             None, None,
             None, 'Крезол-НС', None, None, 'перед началом работ на скважине', None, 'АКТ№', None, None, None, 'факт',
             None, 'час', self.extra_work_time_line, 1, 1, '=V555*W555*X555', '=Y555-AA555-AB555-AC555-AD555', None,
             None, None, None, None]]
        if self.response_text_line != '':
            work_list.append([
                '=ROW()-ROW($A$46)', None, None, 'Тех.операции', 'ОПЗ',
                f'{self.response_text_line} ({self.response_time_begin_date}-{self.response_time_end_date})', None,
                None, None,
                None, None, None, None, None, 'АКТ№', None, None, None, 'простои', 'Тех. ожидание', 'час',
                self.response_time_line, 1, 1,
                '=V556*W556*X556', '=Y556-AA556-AB556-AC556-AD556', None, None, None, None, None])
        self.date_work_line = self.extra_work_time_end_date.split(' ')[0]

        return work_list

    def volume_after_sko_work(self):
        from normir.template_without_skm import TemplateWithoutSKM
        work_list = TemplateWithoutSKM.descent_nkt_work(self)

        for index in range(len(work_list)):
            if index == 0:
                work_list[index][12] = self.count_nkt_line * 10
            work_list[index][21] = self.count_nkt_line

        volume_list = [
            ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', 'Промывка', 'ПЗР при промывке скважины ', None, None,
             None, None, None, None, None, None, None, None, None, None, '§156,160р.1', None, 'шт', 1, 1, 1,
             '=V557*W557*X557', '=Y557-AA557-AB557-AC557-AD557', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', 'Промывка', 'Переход на обратную промывку', None, None,
             None, None, None, None, None, None, None, None, None, None, '§162разд.1', None, 'раз', 1, 0.15, 1,
             '=V558*W558*X558', '=Y558-AA558-AB558-AC558-AD558', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', 'Промывка',
             f'Промывка в объеме {self.volume_flush_line_sko_line}м3', None, None, None, None, None,
             None, None, None, None, None, None, None, '§300разд.1', None, 'м3',
             self.volume_flush_line_sko_line, 0.033, 1, '=V559*W559*X559',
             '=Y559-AA559-AB559-AC559-AD559', None, None, None, None, None]]

        work_list.extend(volume_list)

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
                ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None, 'М/ж спайдера', None, None, None, None, None,
                 None,
                 None, None, None, None, None, None, '§185разд.1', None, 'час', 1, 0.07, 1, '=V529*W529*X529',
                 '=Y529-AA529-AB529-AC529-AD529', None, None, None, None, None],
                ['=ROW()-ROW($A$46)', None, None, 'спо', self.type_equipment, 'ПЗР СПО ПЕРО, ВОРОНКА', None, None, None, None, None,
                 None, None, None, None, None, None, None, '§177разд.1', None, 'шт', 1, 0.17, 1, '=V530*W530*X530',
                 '=Y530-AA530-AB530-AC530-AD530', None, None, None, None, None],
                ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None, 'Д/ж спайдера', None, None, None, None, None,
                 None,
                 None, None, None, None, None, None, '§185разд.1', None, 'час', 1, 0.07, 1, '=V531*W531*X531',
                 '=Y531-AA531-AB531-AC531-AD531', None, None, None, None, None],
                ['=ROW()-ROW($A$46)', None, None, 'спо', 'Пакер', 'ПЗР СПО пакера', None, None, None, None, None, None,
                 None, None, None, None, None, None, '§136,142разд.1', None, 'шт', 1, 0.48, 1, '=V532*W532*X532',
                 '=Y532-AA532-AB532-AC532-AD532', None, None, None, None, None],
                ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None, 'М/ж спайдера', None, None, None, None, None,
                 None,
                 None, None, None, None, None, None, '§185разд.1', None, 'час', 1, 0.07, 1, '=V533*W533*X533',
                 '=Y533-AA533-AB533-AC533-AD533', None, None, None, None, None]]

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

        if self.depth_paker_text_edit != '':
            work_list.extend(self.pressuar_work())
        if self.depth_zumpf_paker_combo == 'Да':
            if self.depth_zumpf_paker_line != '':
                work_list.extend(self.pressuar_work())

        if self.pressuar_tnkt_combo == 'Да':
            pressuar_tnkt_list = self.pressuar_tnkt_combo_def()
            work_list.append(pressuar_tnkt_list)

        if self.solvent_injection_combo == 'Да':
            work_list.extend(TemplateWithoutSKM.solvent_injection_work(self))

        if self.extra_work_question_combo == 'Да':
            if self.type_combo_work in ['Крезол', 'Кислота силами подрядчика']:
                if self.type_combo_work == 'Крезол':
                    work_list.extend(self.krezol_work())
                work_list.extend(self.volume_after_sko_work())
                if self.determination_of_pickup_sko_text_line != '':
                    work_list.extend(self.determination_of_pickup_work(
                        self.saturation_volume_sko_line, self.determination_of_pickup_sko_text_line))


            self.date_work_line = self.extra_work_time_end_date.split(' ')[0]

        work_list.extend(TemplateWithoutSKM.lifting_nkt(self))

        return work_list

    def determination_of_pickup_work(self, saturation_volume, determination_of_pickup_text):
        determination_of_pickup_text_list = [
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'Промывка',
             f'Насыщение в объеме {saturation_volume}м3', None, None, None, None, None, None,
             None, None, 'АКТ№', None, None, None, '§301разд.1', None, 'м3',
             self.saturation_volume_sko_line, 0.033, 1, '=V550*W550*X550',
             '=Y550-AA550-AB550-AC550-AD550', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'Промывка', 'Переход на обратную промывку', None,
             None, None,
             None, None, None, None, None, None, None, None, None, '§162разд.1', None, 'раз', 1, 0.15, 1,
             '=V551*W551*X551', '=Y551-AA551-AB551-AC551-AD551', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
             'Подготовительные работы перед определением приемистости', None, None, None, None, None, None,
             None, None, None, None, None, None, '§169,171разд.1', None, 'шт', 1, 0.52, 1, '=V552*W552*X552',
             '=Y552-AA552-AB552-AC552-AD552', None, None, None, None, None]
            ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None, f'{determination_of_pickup_text}',
             None, None, None, None, None, None, None, None, 'АКТ№', None, None, None, '§170разд.1', None, 'шт', 1, 0.2, 1,
             '=V553*W553*X553', '=Y553-AA553-AB553-AC553-AD553', None, None, None, None, None]
        ]
        return determination_of_pickup_text_list

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
            determination_of_pickup_list =  work_list.extend(self.determination_of_pickup_work(
                        self.saturation_volume_line, self.determination_of_pickup_text_line))
            work_list.extend(determination_of_pickup_list)

        work_list.extend([
            ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None, 'Срыв пакера в эксплуатационной колонне', None,
             None,
             None, None, None, None, None, None, None, None, None, None, '§146разд.1', None, 'шт', 1, 0.15, 1,
             '=V554*W554*X554', '=Y554-AA554-AB554-AC554-AD554', None, None, None, None, None]])

        return work_list

    def solvent_injection_work(self):
        work_list = [
            ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', 'ОПЗ', 'Подготовительные работы, выполняемые ', None,
             None, None, 'ПО ТКРС', None, None, 'перед началом работ на скважине', None, None, 'РАСТВОРИТЕЛЬ',
             'Растворитель АСПО Реком 7125 серия 4, КР-4Р', None, '§227,229разд.1', None, 'шт', 1, 0.96, 1,
             '=V589*W589*X589', '=Y589-AA589-AB589-AC589-AD589', None, None, None, None, None]]
        if self.solvent_volume_text_line > 1:
            solvent_volume_list = [
                ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', 'ОПЗ', f'Закачка растворителя первого 1м3',
                 None, None, None, None, None, None, None, None, 'АКТ№', None, None, None, '§228разд.1', None, 'м3', 1,
                 0.2,
                 1, '=V590*W590*X590', '=Y590-AA590-AB590-AC590-AD590', None, None, None, None, None],
                ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', 'ОПЗ',
                 f'Закачка растворителя следующего {self.solvent_volume_text_line - 1}м3', None, None,
                 None, None, None, None, None, None, 'АКТ№', None, None, None, '§228разд.1', None, 'м3', 1, 0.1,
                 1, '=V591*W591*X591', '=Y591-AA591-AB591-AC591-AD591', None, None, None, None, None]]
        else:
            solvent_volume_list = [
                ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', 'ОПЗ',
                 f'Закачка растворителя первого {self.solvent_volume_text_line}м3', None,
                 None, None, None, None, None, None, None, 'АКТ№', None, None, None, '§228разд.1', None, 'м3', 1, 0.2,
                 1, '=V590*W590*X590', '=Y590-AA590-AB590-AC590-AD590', None, None, None, None, None],
            ]
        work_list.extend(solvent_volume_list)
        volume_list = [
            ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', 'ОПЗ',
             f'Доводка растворителя в объеме {self.volume_of_finishing_line}', None, None, None, None,
             None, None, None, None, None, None, None, None, '§228разд.1', None, 'м3', self.volume_of_finishing_line,
             0.033, 1, '=V592*W592*X592',
             '=Y592-AA592-AB592-AC592-AD592', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', 'ОПЗ',
             f'Реагирование {self.solvent_volume_time_begin_date}-{self.solvent_volume_time_end_date}', None, None,
             None,
             None,
             None, None, None, None, 'АКТ№', None, None, None, 'простои', 'Тех. ожидание', 'час',
             self.solvent_volume_time_line, 1, 1,
             '=V593*W593*X593', '=Y593-AA593-AB593-AC593-AD593', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', 'Промывка', 'Переход на труб.простр.', None, None,
             None,
             None, None, None, None, None, None, None, None, None, '§162разд.1', None, 'раз', 1, 0.15, 1,
             '=V594*W594*X594', '=Y594-AA594-AB594-AC594-AD594', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', 'Промывка', f'Промывка в объеме {self.volume_flush_line}',
             None, None, None, None, None, None, None, None, 'АКТ№', None, None, None, '§301разд.1', None, 'м3',
             {self.volume_flush_line}, 0.033, 1, '=V595*W595*X595',
             '=Y595-AA595-AB595-AC595-AD595', None, None, None, None, None]]
        work_list.extend(volume_list)
        return work_list

    def pressuar_tnkt_combo_def(self):
        work_list = [
            ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None, 'Сброс шара', None, None, None, None, None, None,
             None, None, 'АКТ№', None, None, None, 'факт', None, 'час', 0.5, 1, 1, '=V540*W540*X540',
             '=Y540-AA540-AB540-AC540-AD540', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None, 'ПЗР перед опрессовкой ', None, None, None, None,
             None, None, None, None, None, None, None, None, '§150/152 разд.1 ', None, 'шт', 1, 0.43, 1,
             '=V541*W541*X541', '=Y541-AA541-AB541-AC541-AD541', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None, f'{self.pressuar_tnkt_text_line}', None, None, None,
             None, None, None, None, None, 'АКТ№', None, None, None, '§151 разд.1', None, 'шт', 1, 0.25, 1,
             '=V542*W542*X542', '=Y542-AA542-AB542-AC542-AD542', None, None, None, None, None]]

        return work_list


if __name__ == "__main__":
    # app3 = QApplication(sys.argv)

    app = QApplication(sys.argv)
    window = SpoPakerAction(22, 22)
    window.show()
    sys.exit(app.exec_())
