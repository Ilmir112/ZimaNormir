from PyQt5.QtGui import QIntValidator, QDoubleValidator
from PyQt5.QtWidgets import QWidget, QLabel, QComboBox, QLineEdit, QGridLayout, QTabWidget, QMainWindow, QPushButton, \
    QMessageBox, QApplication, QHeaderView, QTableWidget, QTableWidgetItem, QTabWidget, QTextEdit, QDateEdit, QDateTimeEdit

import well_data
from datetime import datetime, timedelta

from normir.norms import DESCENT_NORM_NKT


class TabPage(QWidget):
    def __init__(self, parent=None):
        super().__init__()

        self.complications_during_tubing_running_label = QLabel('Осложнение при спуске НКТ')
        self.complications_of_failure_label = QLabel('Получен ли прихват, наличие рассхаживания')
        self.complications_when_lifting_label = QLabel('Осложнения при подъеме НКТ')
        self.nkt_48_lenght_label = QLabel('Длина на спуск НКТ48')
        self.nkt_48_count_label = QLabel('Кол-во на спуск НКТ48')
        self.nkt_60_lenght_label = QLabel('Длина на спуск НКТ60')
        self.technological_crap_question_label = QLabel('Был ли допуск')
        self.nkt_60_count_label = QLabel('Кол-во на спуск НКТ60')
        self.nkt_73_lenght_label = QLabel('Длина НКТ73')
        self.nkt_73_count_label = QLabel('Кол-во НКТ73')
        self.nkt_89_lenght_label = QLabel('Длина НКТ89-102')
        self.nkt_89_count_label = QLabel('Кол-во НКТ89-102')
        self.volume_well_flush_label = QLabel('Объем промывки')
        self.solvent_injection_label = QLabel('Закачка растворителя')
        self.nkt_is_same_label = QLabel('Кол-во НКТ на подъем совпадает со спуском')
        self.normalization_question_label = QLabel('Было ли дренирование?')
        self.interval_skm_text_label = QLabel('Интервалы скреперования')
        self.count_of_nkt_extensions_label = QLabel('Кол-во метров скреперования')
        self.volume_of_finishing_label = QLabel('Объем доводки тех водой')
        self.response_text_label = QLabel('Текст реагирование')
        self.volume_flush_label = QLabel('Объем промывки')
        self.solvent_volume_time_begin_label = QLabel('начало реагирования')
        self.solvent_volume_time_end_label = QLabel('Окончание реагирования')
        self.solvent_volume_time_label = QLabel('затраченное время реагирования')
        self.select_type_nkt_combo_label = QLabel('Выбор спущенной компоновки')
        self.solvent_volume_text_label = QLabel(self)

        self.date_work_label = QLabel('Дата работы')
        self.date_work_line = QLineEdit(self)
        self.date_work_line.setText(f'{well_data.date_work}')

        self.date_work_str = datetime.strptime(self.date_work_line.text(), '%d.%m.%Y')


    def update_select_type_nkt_combo(self, index):
        self.nkt_label()

    def update_select_paker_combo(self, index):
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

        # self.solvent_injection_combo = QComboBox(self)
        # self.solvent_injection_combo.addItems(['Нет', 'Да'])
        #
        # self.grid.addWidget(self.solvent_injection_label, 32, 1)
        # self.grid.addWidget(self.solvent_injection_combo, 33, 1)
        #
        # self.solvent_injection_combo.currentTextChanged.connect(self.update_solvent_injection_combo)

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

        self.pressuar_ek_combo_label = QLabel('Была ли опрессовка')

        self.pressuar_ek_combo = QComboBox(self)
        self.pressuar_ek_combo.addItems(['Нет', 'Да'])

        self.grid.addWidget(self.pressuar_ek_combo_label, 30, 0)
        self.grid.addWidget(self.pressuar_ek_combo, 31, 0)

        self.pressuar_ek_combo.currentTextChanged.connect(self.update_pressuar_ek_combo)


        self.depth_zumpf_paker_combo.currentTextChanged.connect(self.update_depth_zumpf_paker)

        self.determination_of_pickup_combo.currentTextChanged.connect(self.update_determination_of_pickup_combo)
        # self.pressuar_gno_combo.currentTextChanged.connect(self.update_pressuar_gno_combo)
        self.extra_work_question_combo.currentTextChanged.connect(self.update_extra_work_question_combo)

        # self.pressuar_gno_combo.currentTextChanged.connect(self.update_pressuar_gno_combo)
        self.pressuar_tnkt_combo.currentTextChanged.connect(self.update_pressuar_tnkt_combo)
        self.complications_of_failure_combo.currentTextChanged.connect(self.update_complications_of_failure)
        self.complications_when_lifting_combo.currentTextChanged.connect(self.update_complications_when_lifting)

        self.complications_during_tubing_running_combo.currentTextChanged.connect(
            self.update_complications_during_tubing_running_combo)
        self.nkt_is_same_combo.currentTextChanged.connect(self.update_nkt_is_same_combo)

    def update_pressuar_ek_combo(self, index):
        if index == 'Нет':
            self.depth_paker_text_label.setParent(None)
            self.depth_paker_text_edit.setParent(None)

            self.pressuar_ek_label.setParent(None)
            self.pressuar_ek_line.setParent(None)

            self.rezult_pressuar_combo_label.setParent(None)
            self.rezult_pressuar_combo.setParent(None)
        else:
            self.depth_paker_text_edit = QLineEdit(self)

            self.pressuar_ek_line = QLineEdit(self)
            self.pressuar_ek_line.setValidator(self.validator_float)

            self.rezult_pressuar_combo = QComboBox(self)
            self.rezult_pressuar_combo.addItems(['+', '-'])

            self.grid.addWidget(self.depth_paker_text_label, 30, 1)
            self.grid.addWidget(self.depth_paker_text_edit, 31, 1)

            self.grid.addWidget(self.pressuar_ek_label, 30, 2)
            self.grid.addWidget(self.pressuar_ek_line, 31, 2)
            self.grid.addWidget(self.rezult_pressuar_combo_label, 30, 3)
            self.grid.addWidget(self.rezult_pressuar_combo, 31, 3)


    def nkt_label(self):
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

    # def update_determination_of_pickup_combo(self, index):
    #     if index == 'Нет':
    #         self.saturation_volume_label.setParent(None)
    #         self.determination_of_pickup_text_label.setParent(None)
    #         self.saturation_volume_line.setParent(None)
    #         self.determination_of_pickup_text.setParent(None)
    #     else:
    #         self.saturation_volume_line = QLineEdit(self)
    #         self.saturation_volume_line.setValidator(self.validator_float)
    #
    #         self.determination_of_pickup_sko_text = QLineEdit(self)
    #
    #         self.grid.addWidget(self.saturation_volume_label, 30, 5)
    #         self.grid.addWidget(self.saturation_volume_line, 31, 5)
    #         self.grid.addWidget(self.determination_of_pickup_text_label, 30, 6)
    #         self.grid.addWidget(self.determination_of_pickup_text, 31, 6)

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


        else:
            self.solvent_volume_text_label = QLabel(self)
            self.solvent_volume_text_line = QLineEdit(self)
            self.solvent_volume_text_line.setValidator(self.validator_float)
            self.solvent_volume_text_line.setText('2')

            self.volume_of_finishing_label = QLabel('Объем доводки тех водой')
            self.volume_of_finishing_line = QLineEdit(self)
            self.volume_of_finishing_line.setValidator(self.validator_float)

            # self.volume_flush_label = QLabel('Объем промывки')
            # self.volume_flush_line = QLineEdit(self)
            # self.volume_flush_line.setValidator(self.validator_float)

            self.solvent_volume_time_begin_label = QLabel('начало закачки')
            self.solvent_volume_time_begin_date = QDateTimeEdit(self)
            self.solvent_volume_time_begin_date.setDisplayFormat("dd.MM.yyyy HH:mm")
            self.solvent_volume_time_begin_date.setDateTime(self.date_work_str)

            self.solvent_volume_time_end_label = QLabel('Окончание закачки')
            self.solvent_volume_time_end_date = QDateTimeEdit(self)
            self.solvent_volume_time_end_date.setDisplayFormat("dd.MM.yyyy HH:mm")
            self.solvent_volume_time_end_date.setDateTime(self.date_work_str)

            self.solvent_volume_time_label = QLabel('затраченное время')
            self.solvent_volume_time_line = QLineEdit(self)
            self.solvent_volume_time_line.setValidator(self.validator_float)

            self.grid.addWidget(self.solvent_volume_text_label, 32, 2)
            self.grid.addWidget(self.solvent_volume_text_line, 33, 2)
            self.grid.addWidget(self.volume_of_finishing_label, 32, 3)
            self.grid.addWidget(self.volume_of_finishing_line, 33, 3)
            # self.grid.addWidget(self.volume_flush_label, 32, 4)
            # self.grid.addWidget(self.volume_flush_line, 33, 4)
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
            try:
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
            except:
                pass

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



        if index in ['Крезол']:
            self.extra_work_text_line.setText('Работа фирмы ООО "Крезол"')

            self.volume_flush_line_combo_label = QLabel('Были ли промывка после СКО')
            self.volume_flush_line_combo = QComboBox(self)
            self.volume_flush_line_combo.addItems(['Нет', 'Да'])

            self.grid.addWidget(self.volume_flush_line_combo_label, 64, 1)
            self.grid.addWidget(self.volume_flush_line_combo, 65, 1)
            self.volume_flush_line_combo.currentTextChanged.connect(self.update_volume_flush_line_combo)

            self.skv_combo_label = QLabel('было ли СКВ силами КРС?')
            self.skv_combo = QComboBox(self)
            self.skv_combo.addItems(['Нет', 'Да'])

            self.skv_combo.currentTextChanged.connect(self.update_response_sko_combo)
        else:
            try:
                self.skv_combo_label.setParent(None)
                self.skv_combo.setParent(None)
                self.determination_of_pickup_combo_label.setParent(None)
                self.determination_of_pickup_combo.setParent(None)
                self.count_nkt_combo_label.setParent(None)
                self.count_nkt_combo.setParent(None)
            except:
                pass
            # self.update_skv_combo(index)

    def update_volume_flush_line_combo(self, index):
        if index == 'Нет':
            self.volume_flush_line_sko_label.setParent(None)
            self.volume_flush_line_sko_line.setParent(None)
            self.count_nkt_combo_label.setParent(None)
            self.count_nkt_combo.setParent(None)
        else:
            self.volume_flush_line_sko_label = QLabel('Объем промывки после СКО')
            self.volume_flush_line_sko_line = QLineEdit(self)
            self.volume_flush_line_sko_line.setValidator(self.validator_float)

            self.grid.addWidget(self.volume_flush_line_sko_label, 64, 6)
            self.grid.addWidget(self.volume_flush_line_sko_line, 65, 6)

            self.count_nkt_combo_label = QLabel('был ли допуск?')
            self.count_nkt_combo = QComboBox(self)
            self.count_nkt_combo.addItems(['Нет', 'Да'])

            self.grid.addWidget(self.count_nkt_combo_label, 64, 2)
            self.grid.addWidget(self.count_nkt_combo, 65, 2)

            self.count_nkt_combo.currentTextChanged.connect(self.update_count_nkt_combo)

            # self.count_nkt_combo.currentTextChanged.connect(TabPage_SO_Timplate.update_count_nkt_combo)



    def update_determination_of_pickup_sko_combo(self, index):
        if index == 'Нет':
            self.saturation_volume_sko_label.setParent(None)
            self.saturation_volume_sko_line.setParent(None)
            self.determination_of_pickup_sko_text_label.setParent(None)
            self.determination_of_pickup_sko_text_line.setParent(None)
        else:
            self.saturation_volume_sko_label = QLabel('Насыщение')
            self.saturation_volume_sko_line = QLineEdit(self)
            self.saturation_volume_sko_line.setValidator(self.validator_float)

            self.determination_of_pickup_sko_text_label = QLabel('Текст определение Q')
            self.determination_of_pickup_sko_text_line = QLineEdit(self)

            self.grid.addWidget(self.saturation_volume_sko_label, 66, 4)
            self.grid.addWidget(self.saturation_volume_sko_line, 67, 4)
            self.grid.addWidget(self.determination_of_pickup_sko_text_label, 66, 5)
            self.grid.addWidget(self.determination_of_pickup_sko_text_line, 67, 5)

    def update_count_nkt_combo(self, index):

        if index == 'Нет':
            self.count_nkt_label.setParent(None)
            self.count_nkt_line.setParent(None)
            self.roof_definition_depth_label.setParent(None)
            self.roof_definition_depth_line.setParent(None)

        else:
            self.count_nkt_label = QLabel('Количество НКТ на допуск')
            self.count_nkt_line = QLineEdit(self)
            self.count_nkt_line.setValidator(self.validator_int)
            self.count_nkt_line.setText('3')

            self.roof_definition_depth_label = QLabel('Глубина воронки')
            self.roof_definition_depth_line = QLineEdit(self)
            self.roof_definition_depth_line.setValidator(self.validator_float)

            self.grid.addWidget(self.count_nkt_label, 64, 4)
            self.grid.addWidget(self.count_nkt_line, 65, 4)
            self.grid.addWidget(self.roof_definition_depth_label, 64, 5)
            self.grid.addWidget(self.roof_definition_depth_line, 65, 5)

    def update_sko_combo(self, index):
        if index == 'Нет':

            self.response_text_label.setParent(None)
            self.response_text_line.setParent(None)

            self.response_time_begin_label.setParent(None)
            self.response_time_begin_date.setParent(None)

            self.response_time_end_label.setParent(None)
            self.response_time_end_date.setParent(None)

            self.response_time_line_label.setParent(None)
            self.response_time_line.setParent(None)

        else:
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

            self.grid.addWidget(self.response_text_label, 62, 2)
            self.grid.addWidget(self.response_text_line, 63, 2)

            self.grid.addWidget(self.response_time_begin_label, 62, 3)
            self.grid.addWidget(self.response_time_begin_date, 63, 3)

            self.grid.addWidget(self.response_time_end_label, 62, 4)
            self.grid.addWidget(self.response_time_end_date, 63, 4)

            self.grid.addWidget(self.response_time_line_label, 62, 5)
            self.grid.addWidget(self.response_time_line, 63, 5)

            self.response_time_end_date.dateTimeChanged.connect(self.update_date_response)
            self.response_time_begin_date.dateTimeChanged.connect(
                self.update_date_response)

    def update_response_sko_combo(self, index):
        if index == 'Да':
            self.volume_skv_label = QLabel('Объем СКВ')
            self.volume_skv_line = QLineEdit(self)
            self.volume_skv_line.setValidator(self.validator_float)

            self.response_skv_text_label = QLabel('Текст реагирование')
            self.response_skv_text_line = QLineEdit(self)
            self.response_skv_text_line.setText('Реагирование')

            self.response_skv_time_begin_label = QLabel('начало реагирования')
            self.response_skv_time_begin_date = QDateTimeEdit(self)
            self.response_skv_time_begin_date.setDisplayFormat("dd.MM.yyyy HH:mm")
            self.response_skv_time_begin_date.setDateTime(self.date_work_str)

            self.response_skv_time_end_label = QLabel('Окончание реагирования')
            self.response_skv_time_end_date = QDateTimeEdit(self)
            self.response_skv_time_end_date.setDisplayFormat("dd.MM.yyyy HH:mm")
            self.response_skv_time_end_date.setDateTime(self.date_work_str)

            self.response_skv_time_line_label = QLabel('Затраченное время')
            self.response_skv_time_line = QLineEdit(self)

            self.grid.addWidget(self.volume_skv_label, 68, 2)
            self.grid.addWidget(self.volume_skv_line, 69, 2)

            self.grid.addWidget(self.response_skv_text_label, 70, 2)
            self.grid.addWidget(self.response_skv_text_line, 71, 2)

            self.grid.addWidget(self.response_skv_time_begin_label, 70, 3)
            self.grid.addWidget(self.response_skv_time_begin_date, 71, 3)

            self.grid.addWidget(self.response_skv_time_end_label, 70, 4)
            self.grid.addWidget(self.response_skv_time_end_date, 71, 4)

            self.grid.addWidget(self.response_skv_time_line_label, 70, 5)
            self.grid.addWidget(self.response_skv_time_line, 71, 5)

        else:
            self.response_skv_text_label.setParent(None)
            self.response_skv_text_line.setParent(None)

            self.response_skv_time_begin_label.setParent(None)
            self.response_skv_time_begin_date.setParent(None)

            self.response_skv_time_end_label.setParent(None)
            self.response_skv_time_end_date.setParent(None)

            self.response_skv_time_line_label.setParent(None)
            self.response_skv_time_line.setParent(None)

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

    def update_equipment_audit_combo(self, index):
        if index == 'Нет':
            self.equipment_audit_text_label.setParent(None)
            self.equipment_audit_text_line.setParent(None)
        else:

            self.equipment_audit_text_label = QLabel('Текст ревизии')
            self.equipment_audit_text_line = QLineEdit(self)

            self.grid.addWidget(self.equipment_audit_text_label, 74, 3)
            self.grid.addWidget(self.equipment_audit_text_line, 75, 3)

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
            self.normalization_question_text_label = QLabel('Текст дренирования')
            self.normalization_question_text_line = QLineEdit(self)

            self.normalization_question_time_begin_label = QLabel('начало дренирования')
            self.normalization_question_time_begin_date = QDateTimeEdit(self)
            self.normalization_question_time_begin_date.setDisplayFormat("dd.MM.yyyy HH:mm")
            self.normalization_question_time_begin_date.setDateTime(self.date_work_str)

            self.normalization_question_time_end_label = QLabel('Окончание дренирования')
            self.normalization_question_time_end_date = QDateTimeEdit(self)
            self.normalization_question_time_end_date.setDisplayFormat("dd.MM.yyyy HH:mm")
            self.normalization_question_time_end_date.setDateTime(self.date_work_str)

            self.normalization_question_time_label = QLabel('затраченное время')
            self.normalization_question_time_line = QLineEdit(self)
            self.normalization_question_time_line.setValidator(self.validator_float)

            self.grid.addWidget(self.normalization_question_text_label, 70, 2)
            self.grid.addWidget(self.normalization_question_text_line, 71, 2)
            self.grid.addWidget(self.normalization_question_time_begin_label, 70, 3)
            self.grid.addWidget(self.normalization_question_time_begin_date, 71, 3)
            self.grid.addWidget(self.normalization_question_time_end_label, 70, 4)
            self.grid.addWidget(self.normalization_question_time_end_date, 71, 4)
            self.grid.addWidget(self.normalization_question_time_label, 70, 5)
            self.grid.addWidget(self.normalization_question_time_line, 71, 5)

            self.normalization_question_time_end_date.dateTimeChanged.connect(self.update_date_of_normalization)
            self.normalization_question_time_begin_date.dateTimeChanged.connect(self.update_date_of_normalization)

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

            self.grid.addWidget(self.technological_crap_question_text_label, 72, 2)
            self.grid.addWidget(self.technological_crap_question_text_line, 73, 2)
            self.grid.addWidget(self.technological_crap_question_time_begin_label, 72, 3)
            self.grid.addWidget(self.technological_crap_question_time_begin_date, 73, 3)
            self.grid.addWidget(self.technological_crap_question_time_end_label, 72, 4)
            self.grid.addWidget(self.technological_crap_question_time_end_date, 73, 4)
            self.grid.addWidget(self.technological_crap_question_time_label, 72, 5)
            self.grid.addWidget(self.technological_crap_question_time_line, 73, 5)
            self.grid.addWidget(self.count_nkt_label, 72, 6)
            self.grid.addWidget(self.count_nkt_line, 73, 6)
            self.grid.addWidget(self.roof_definition_depth_label, 72, 7)
            self.grid.addWidget(self.roof_definition_depth_line, 73, 7)

            self.technological_crap_question_time_end_date.dateTimeChanged.connect(self.update_date_technological_crap)
            self.technological_crap_question_time_begin_date.dateTimeChanged.connect(
                self.update_date_technological_crap)

    def update_date_of_normalization(self):
        time_begin = self.normalization_question_time_begin_date.dateTime()
        time_end = self.normalization_question_time_end_date.dateTime()

        time_difference = self.calculate_date(time_begin, time_end)
        self.normalization_question_time_line.setText(str(time_difference))


class TemplateWork(QMainWindow):
    def __init__(self, ins_ind, table_widget, parent=None):
        super(QMainWindow, self).__init__(parent)

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

    def adjustRowHeight(self, row, text):
        font_metrics = self.tableWidget.fontMetrics()  # Получаем метрики шрифта
        text_height = font_metrics.height()  # Высота строки на основе шрифта
        text_length = len(text)

        # Предположим, что мы используем фиксированную ширину для текстовой ячейки
        width = self.tableWidget.columnWidth(1)
        # Оцениваем количество необходимых строк для текста
        number_of_lines = (text_length // (width // font_metrics.averageCharWidth())) + 1
        self.tableWidget.setRowHeight(row, int((text_height * number_of_lines) / 2))  # Устанавливаем высоту


    def descent_nkt_work(self):
        sum_nkt = sum(list(map(lambda x: x[1], list(self.dict_nkt.values()))))
        work_list = []
        middle_nkt = '9.6-10.5'
        for nkt_key, nkt_value in self.dict_nkt.items():

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

            aaaa = DESCENT_NORM_NKT[well_data.lifting_unit_combo]
            koef_norm_down = DESCENT_NORM_NKT[well_data.lifting_unit_combo][nkt_key][middle_nkt]
            razdel_2_down = DESCENT_NORM_NKT[well_data.lifting_unit_combo][nkt_key]['раздел']

            work_list.extend([
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', self.type_equipment,
                 f'Спуск НКТ компоновка {nkt_key}', None,
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

    def read_pressuar_combo(self, current_widget):

        self.pressuar_ek_combo = current_widget.pressuar_ek_combo.currentText()
        if self.pressuar_ek_combo == 'Да':
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

    def dovodka(self, time_skv_norm):
        work_list = []
        sum_nkt = sum(list(map(lambda x: x[0], list(self.dict_nkt.values()))))
        norm_nkt = round(0.34 + (sum_nkt - 200) / 200 * 0.02, 2)
        nkt_list = [
            ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', 'ОПЗ', 'Доводка тех.водой', None, None, None, None,
             None, None, None, None, 'АКТ№', None, None, None, '§284разд.1', None, 'м', sum_nkt, 0.34, 1,
             norm_nkt, '=Y810-AA810-AB810-AC810-AD810', None, None, None, None, None]]
        work_list.extend(nkt_list)
        time_skv_norm += norm_nkt

        return work_list

    def count_nkt_down(self):
        work_list = []

        work_list.extend(self.descent_nkt_work())

        for index in range(len(work_list)):
            if index == 0:
                work_list[index][12] = self.count_nkt_line * 10
            work_list[index][21] = self.count_nkt_line
        return work_list

    def volume_after_sko_work(self):

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



        return volume_list

    def determination_of_pickup_work(self, saturation_volume, determination_of_pickup_text):
        determination_of_pickup_text_list = [
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'Промывка', 'Переход на труб.простр.', None,
             None, None,
             None, None, None, None, None, None, None, None, None, '§162разд.1', None, 'раз', 1, 0.15, 1,
             '=V551*W551*X551', '=Y551-AA551-AB551-AC551-AD551', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'Промывка',
             f'Насыщение в объеме {saturation_volume}м3', None, None, None, None, None, None,
             None, None, 'АКТ№', None, None, None, '§301разд.1', None, 'м3',
             saturation_volume, 0.033, 1, '=V550*W550*X550',
             '=Y550-AA550-AB550-AC550-AD550', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
             'Подготовительные работы перед определением приемистости', None, None, None, None, None, None,
             None, None, None, None, None, None, '§169,171разд.1', None, 'шт', 1, 0.52, 1, '=V552*W552*X552',
             '=Y552-AA552-AB552-AC552-AD552', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None, f'{determination_of_pickup_text}',
             None, None, None, None, None, None, None, None, 'АКТ№', None, None, None, '§170разд.1', None, 'шт', 1,
             0.2, 1,
             '=V553*W553*X553', '=Y553-AA553-AB553-AC553-AD553', None, None, None, None, None]
        ]
        return determination_of_pickup_text_list

    def read_responce(self, current_widget):

        if self.response_combo == 'Да':
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

    def read_volume_after_sko(self, current_widget):

        self.volume_flush_line_sko_line = current_widget.volume_flush_line_sko_line.text()
        if self.volume_flush_line_sko_line == '':
            QMessageBox.warning(self, 'Объем насыщения', 'Введите объем промывки после СКО')
            return
        else:
            self.volume_flush_line_sko_line = float(self.volume_flush_line_sko_line)

    def read_determination_of_pickup_sko_combo(self, current_widget):

        self.determination_of_pickup_sko_text_line = current_widget.determination_of_pickup_sko_text_line.text()
        self.saturation_volume_sko_line = current_widget.saturation_volume_sko_line.text()

        if self.determination_of_pickup_sko_text_line == "":
            determination_question = QMessageBox.question(self,
                                                          'Определение приемистости',
                                                          'Не введена текст определения приемистости, работ не было?')
            if determination_question == QMessageBox.StandardButton.No:
                return

        if self.saturation_volume_sko_line == '':
            QMessageBox.warning(self, 'Объем насыщения', 'Введите объем насыщения после СКО')
            return
        else:
            self.saturation_volume_sko_line = float(self.saturation_volume_sko_line)


    def read_count_nkt_combo(self, current_widget):

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


    def response_sko(self):
        work_list = [
                '=ROW()-ROW($A$46)', None, None, 'Тех.операции', 'ОПЗ',
                f'{self.response_text_line} ({self.response_time_begin_date}-{self.response_time_end_date})', None,
                None, None,
                None, None, None, None, None, 'АКТ№', None, None, None, 'простои', 'Тех. ожидание', 'час',
                self.response_time_line, 1, 1,
                '=V556*W556*X556', '=Y556-AA556-AB556-AC556-AD556', None, None, None, None, None],

        return work_list

    def read_nkt_down(self, current_widget):
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



    def read_nkt_up(self, current_widget):

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

        if len(self.dict_nkt) == 0:
            question = QMessageBox.question(self, 'Ошибка', f'НКТ отсутствуют?')
            if question == QMessageBox.StandardButton.No:
                return

    @staticmethod
    def change_string_in_date(date_str):
        # Преобразуем строку в объект datetime

        formatted_date = date_str.strftime("%d.%m.%Y %H:%M")
        return formatted_date

    def read_normalization_question(self, current_widget):
        self.normalization_question_text_line = current_widget.normalization_question_text_line.text()
        self.normalization_question_time_begin_date = \
            current_widget.normalization_question_time_begin_date.dateTime().toPyDateTime()
        self.normalization_question_time_begin_date = \
            self.change_string_in_date(self.normalization_question_time_begin_date)

        self.normalization_question_time_end_date = \
            current_widget.normalization_question_time_end_date.dateTime().toPyDateTime()
        self.normalization_question_time_end_date = \
            self.change_string_in_date(self.normalization_question_time_end_date)

        if current_widget.normalization_question_text_line.text() == self.normalization_question_time_begin_date:
            QMessageBox.warning(self, 'Даты совпадают', 'Даты совпадают')
            return

        if self.normalization_question_text_line == '':
            QMessageBox.warning(self, 'Ошибка', f'Не введены текст осложнения при срыве ПШ')
            return

        self.normalization_question_time_line = current_widget.normalization_question_time_line.text()
        if self.normalization_question_time_line != '':
            self.normalization_question_time_line = round(float(self.normalization_question_time_line), 1)

        else:
            QMessageBox.warning(self, 'Ошибка', f'Не введены время осложнения при срыве ПШ')
            return

        if self.normalization_question_time_line <= 0:
            QMessageBox.warning(self, 'Ошибка', f'Затраченное время при срыве ПШ не может быть отрицательным')
            return

    def read_technological_crap_question(self, current_widget):
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

    def read_solvent_volume(self, current_widget):
        self.volume_of_finishing_line = current_widget.volume_of_finishing_line.text()
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

        if self.volume_of_finishing_line == '':
            QMessageBox.warning(self, 'Ошибка', f'Не введены обьем растворителя')
            return
        else:

            self.volume_of_finishing_line = round(float(self.volume_of_finishing_line), 1)

        self.solvent_volume_time_line = current_widget.solvent_volume_time_line.text()
        if self.solvent_volume_time_line != '':
            self.solvent_volume_time_line = round(float(self.solvent_volume_time_line), 1)

        else:
            QMessageBox.warning(self, 'Ошибка', f'Не введены время реагирования')
            return

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
             '=Y592-AA592-AB592-AC592-AD592', None, None, None, None, None]]
        work_list.extend(volume_list)

        return work_list