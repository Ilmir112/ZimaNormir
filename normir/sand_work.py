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


class TabPage_SO_Sand(TabPage):
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
        self.volume_sand_label = QLabel('Объем отсыпанного песка')
        self.height_sand_label = QLabel('Высота намываемого моста')
        self.volume_sand_two_label = QLabel('Объем отсыпанного песка')
        self.bottom_sand_label = QLabel('Глубина определения ПМ')
        self.bottom_sand_two_label = QLabel('Глубина определения ПМ')
        self.sand_filling_two_label = QLabel('Был ли вымыв после определения')

        self.nkt_is_same_label = QLabel('Кол-во НКТ на подъем совпадает со спуском')
        self.deinstallation_perforation_label = QLabel('Был ли демонтаж трубного перфоратора')

        # self.count_of_nkt_extensions_label = QLabel('Кол-во метров райбирования')

    def update_complications_of_failure_2(self, index):

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

            self.grid.addWidget(self.complications_of_failure_text_label, 36, 2)
            self.grid.addWidget(self.complications_of_failure_text_line, 37, 2)
            self.grid.addWidget(self.complications_of_failure_time_begin_label, 36, 3)
            self.grid.addWidget(self.complications_of_failure_time_begin_date, 37, 3)
            self.grid.addWidget(self.complications_of_failure_time_end_label, 36, 4)
            self.grid.addWidget(self.complications_of_failure_time_end_date, 37, 4)
            self.grid.addWidget(self.complications_of_failure_time_label, 36, 5)
            self.grid.addWidget(self.complications_of_failure_time_line, 37, 5)

            self.complications_of_failure_time_end_date.dateTimeChanged.connect(self.update_date_of_failure)
            self.complications_of_failure_time_begin_date.dateTimeChanged.connect(self.update_date_of_failure)


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

        self.grid.addWidget(self.complications_of_failure_label, 36, 1)
        self.grid.addWidget(self.complications_of_failure_combo, 37, 1)


        self.grid.addWidget(self.complications_when_lifting_label, 46, 1)
        self.grid.addWidget(self.complications_when_lifting_combo, 47, 1)

        self.sand_filling_two_combo = QComboBox(self)
        self.sand_filling_two_combo.addItems(['', 'Досыпка', 'Вымыв'])

        self.grid.addWidget(self.sand_filling_two_label, 32, 1)
        self.grid.addWidget(self.sand_filling_two_combo, 33, 1)

        self.nkt_is_same_combo = QComboBox(self)
        self.nkt_is_same_combo.addItems(['Да', 'Нет'])

        self.grid.addWidget(self.nkt_is_same_label, 80, 1)
        self.grid.addWidget(self.nkt_is_same_combo, 81, 1)

        # self.deinstallation_perforation_combo = QComboBox(self)
        # self.deinstallation_perforation_combo.addItems(['Нет', 'Да'])
        #
        # self.grid.addWidget(self.deinstallation_perforation_label, 50, 1)
        # self.grid.addWidget(self.deinstallation_perforation_combo, 51, 1)

        self.equipment_audit_label = QLabel('Была ли ревизия')
        self.equipment_audit_combo = QComboBox(self)
        self.equipment_audit_combo.addItems(['Нет', 'Да'])

        self.grid.addWidget(self.equipment_audit_label, 94, 1)
        self.grid.addWidget(self.equipment_audit_combo, 95, 1)

        self.equipment_audit_combo.currentTextChanged.connect(self.update_equipment_audit_combo)
        # self.pressuar_gno_combo.currentTextChanged.connect(self.update_pressuar_gno_combo)
        # self.technological_crap_question_combo.currentTextChanged.connect(self.update_technological_crap_question_combo)
        self.sand_filling_two_combo.currentTextChanged.connect(
            self.update_sand_filling_two_combo)
        # self.pressuar_gno_combo.currentTextChanged.connect(self.update_pressuar_gno_combo)
        # self.deinstallation_perforation_combo.currentTextChanged.connect(self.update_deinstallation_perforation_combo)
        self.complications_of_failure_combo.currentTextChanged.connect(self.update_complications_of_failure_2)
        self.complications_when_lifting_combo.currentTextChanged.connect(self.update_complications_when_lifting)

        self.complications_during_tubing_running_combo.currentTextChanged.connect(
            self.update_complications_during_tubing_running_combo)
        self.nkt_is_same_combo.currentTextChanged.connect(self.update_nkt_is_same_combo)

        self.sand_filling_combo_label = QLabel('Была ли отсыпка?')
        self.sand_filling_combo = QComboBox(self)
        self.sand_filling_combo.addItems(['Нет', 'Да'])
        self.grid.addWidget(self.sand_filling_combo_label, 28, 1)
        self.grid.addWidget(self.sand_filling_combo, 29, 1)

        self.pressuar_ek_combo_label = QLabel('Была ли опрессовка')

        self.pressuar_ek_combo = QComboBox(self)
        self.pressuar_ek_combo.addItems(['Нет', 'Да'])

        self.grid.addWidget(self.pressuar_ek_combo_label, 30, 0)
        self.grid.addWidget(self.pressuar_ek_combo, 31, 0)

        self.pressuar_ek_combo.currentTextChanged.connect(self.update_pressuar_combo)



        # self.sand_filling_two_combo.setCurrentIndex(1)

        self.sand_filling_combo.currentTextChanged.connect(self.update_sand_filling_combo)
        self.sand_filling_combo.setCurrentIndex(1)
        # self.deinstallation_perforation_combo.setCurrentIndex(1)
        self.equipment_audit_combo.setCurrentIndex(1)

    def update_sand_filling_combo(self, index):
        if index == 'Нет':

            self.sand_filling_text_label.setParent(None)
            self.sand_filling_text_edit.setParent(None)

            self.sand_filling_time_begin_label.setParent(None)
            self.sand_filling_time_begin_date.setParent(None)

            self.sand_filling_time_end_label.setParent(None)
            self.sand_filling_time_end_date.setParent(None)

            self.sand_filling_time_label.setParent(None)
            self.sand_filling_time_line.setParent(None)

            self.volume_sand_line.setParent(None)
            self.volume_sand_line.setParent(None)

            self.count_of_nkt_extensions_label.setParent(None)
            self.count_of_nkt_extensions_line.setParent(None)

            self.bottom_sand_line.setParent(None)
            self.bottom_sand_line.setParent(None)

        else:

            self.sand_filling_text_label = QLabel('Интервал отсыпки')
            self.sand_filling_text_edit = QLineEdit(self)

            self.sand_filling_text_edit.editingFinished.connect(self.update_sand_filling_text)

            self.volume_sand_line = QLineEdit(self)
            self.volume_sand_line.setValidator(self.validator_float)

            self.grid.addWidget(self.volume_sand_label, 28, 3)
            self.grid.addWidget(self.volume_sand_line, 29, 3)

            self.height_sand_line = QLineEdit(self)
            self.height_sand_line.setValidator(self.validator_float)

            self.grid.addWidget(self.height_sand_label, 28, 4)
            self.grid.addWidget(self.height_sand_line, 29, 4)

            self.count_of_nkt_extensions_label.setText('Кол-во НКТ на спуск')
            self.count_of_nkt_extensions_line = QLineEdit(self)

            self.grid.addWidget(self.count_of_nkt_extensions_label, 28, 8)
            self.grid.addWidget(self.count_of_nkt_extensions_line, 29, 8)

            self.bottom_sand_line = QLineEdit(self)
            self.bottom_sand_line.setValidator(self.validator_float)

            self.grid.addWidget(self.bottom_sand_label, 28, 9)
            self.grid.addWidget(self.bottom_sand_line, 29, 9)

            self.sand_filling_time_begin_label = QLabel('начало оседания песка')
            self.sand_filling_time_begin_date = QDateTimeEdit(self)
            self.sand_filling_time_begin_date.setDisplayFormat("dd.MM.yyyy HH:mm")
            self.sand_filling_time_begin_date.setDateTime(self.date_work_str)

            self.sand_filling_time_end_label = QLabel('Окончание оседания песка')
            self.sand_filling_time_end_date = QDateTimeEdit(self)
            self.sand_filling_time_end_date.setDisplayFormat("dd.MM.yyyy HH:mm")
            self.sand_filling_time_end_date.setDateTime(self.date_work_str)

            self.sand_filling_time_label = QLabel('затраченное время')
            self.sand_filling_time_line = QLineEdit(self)
            self.sand_filling_time_line.setValidator(self.validator_float)

            self.grid.addWidget(self.sand_filling_time_begin_label, 28, 5)
            self.grid.addWidget(self.sand_filling_time_begin_date, 29, 5)
            self.grid.addWidget(self.sand_filling_time_end_label, 28, 6)
            self.grid.addWidget(self.sand_filling_time_end_date, 29, 6)
            self.grid.addWidget(self.sand_filling_time_label, 28, 7)
            self.grid.addWidget(self.sand_filling_time_line, 29, 7)

            self.sand_filling_time_end_date.dateTimeChanged.connect(self.update_date_of_raid)
            self.sand_filling_time_begin_date.dateTimeChanged.connect(self.update_date_of_raid)

            self.grid.addWidget(self.sand_filling_text_label, 28, 2)
            self.grid.addWidget(self.sand_filling_text_edit, 29, 2)

    def update_sand_filling_text(self):
        index = self.sand_filling_text_edit.text()
        if '-' in index:
            min_str = min(map(float, index.split('-')))
            max_str = max(map(float, index.split('-')))
            self.height_sand_line.setText(str(int(max_str - min_str)))
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

    def update_sand_filling_two_combo(self, index):

        if index not in ['Досыпка', 'Вымыв']:
            self.sand_filling_two_text_label.setParent(None)
            self.sand_filling_two_text_line.setParent(None)
            self.sand_filling_two_time_label.setParent(None)
            self.sand_filling_two_time_line.setParent(None)
            self.sand_filling_two_time_end_label.setParent(None)
            self.sand_filling_two_time_end_date.setParent(None)
            self.sand_filling_two_time_begin_label.setParent(None)
            self.sand_filling_two_time_begin_date.setParent(None)
            self.volume_of_finishing_label.setParent(None)
            # self.volume_of_finishing_line.setParent(None)
            # self.volume_flush_line.setParent(None)
            self.volume_sand_two_line.setParent(None)
            self.volume_sand_two_line.setParent(None)

            self.bottom_sand_two_line.setParent(None)
            self.bottom_sand_two_line.setParent(None)

            self.volume_flush_label.setParent(None)

        else:
            self.sand_filling_two_text_label = QLabel('интервал отсыпки')
            self.sand_filling_two_text_line = QLineEdit(self)

            self.volume_sand_two_line = QLineEdit(self)
            self.volume_sand_two_line.setValidator(self.validator_float)

            self.grid.addWidget(self.volume_sand_two_label, 32, 3)
            self.grid.addWidget(self.volume_sand_two_line, 33, 3)

            self.count_of_nkt_extensions_two_label = QLabel('Кол-во НКТ на спуск')
            self.count_of_nkt_extensions_two_line = QLineEdit(self)

            self.grid.addWidget(self.count_of_nkt_extensions_two_label, 32, 8)
            self.grid.addWidget(self.count_of_nkt_extensions_two_line, 33, 8)

            self.bottom_sand_two_line = QLineEdit(self)
            self.bottom_sand_two_line.setValidator(self.validator_float)

            self.height_sand_two_line = QLineEdit(self)
            self.height_sand_two_line.setValidator(self.validator_float)

            self.grid.addWidget(self.height_sand_label, 32, 4)
            self.grid.addWidget(self.height_sand_two_line, 33, 4)

            self.grid.addWidget(self.bottom_sand_two_label, 32, 9)
            self.grid.addWidget(self.bottom_sand_two_line, 33, 9)

            self.count_of_nkt_extensions_two_label = QLabel('Кол-во НКТ на спуск')
            self.count_of_nkt_extensions_two_line = QLineEdit(self)

            self.grid.addWidget(self.count_of_nkt_extensions_two_label, 32, 8)
            self.grid.addWidget(self.count_of_nkt_extensions_two_line, 33, 8)

            self.sand_filling_two_time_begin_label = QLabel('начало оседания')
            self.sand_filling_two_time_begin_date = QDateTimeEdit(self)
            self.sand_filling_two_time_begin_date.setDisplayFormat("dd.MM.yyyy HH:mm")
            self.sand_filling_two_time_begin_date.setDateTime(self.date_work_str)

            self.sand_filling_two_time_end_label = QLabel('Окончание оседания')
            self.sand_filling_two_time_end_date = QDateTimeEdit(self)
            self.sand_filling_two_time_end_date.setDisplayFormat("dd.MM.yyyy HH:mm")
            self.sand_filling_two_time_end_date.setDateTime(self.date_work_str)

            self.sand_filling_two_time_label = QLabel('затраченное время ')
            self.sand_filling_two_time_line = QLineEdit(self)
            self.sand_filling_two_time_line.setValidator(self.validator_float)

            self.grid.addWidget(self.sand_filling_two_text_label, 32, 2)
            self.grid.addWidget(self.sand_filling_two_text_line, 33, 2)

            self.grid.addWidget(self.sand_filling_two_time_begin_label, 32, 5)
            self.grid.addWidget(self.sand_filling_two_time_begin_date, 33, 5)
            self.grid.addWidget(self.sand_filling_two_time_end_label, 32, 6)
            self.grid.addWidget(self.sand_filling_two_time_end_date, 33, 6)
            self.grid.addWidget(self.sand_filling_two_time_label, 32, 7)
            self.grid.addWidget(self.sand_filling_two_time_line, 33, 7)

            self.sand_filling_two_time_end_date.dateTimeChanged.connect(
                self.update_date_sand_filling_two)
            self.sand_filling_two_time_begin_date.dateTimeChanged.connect(
                self.update_date_sand_filling_two)

        if index == 'Вымыв':
            self.volume_sand_two_label.setText('Объем Промывки')
            self.bottom_sand_two_label = QLabel('Глубина вымыва')
            self.height_sand_two_line.setDisabled(True)
        else:
            self.volume_sand_two_label.setText('Объем песка')
            self.bottom_sand_two_label = QLabel('Глубина определения ПМ')

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
        time_begin = self.sand_filling_time_begin_date.dateTime()
        time_end = self.sand_filling_time_end_date.dateTime()

        time_difference = self.calculate_date(time_begin, time_end)
        self.sand_filling_time_line.setText(str(time_difference))

    def update_date_tubing_running(self):
        time_begin = self.complications_during_tubing_running_time_begin_date.dateTime()
        time_end = self.complications_during_tubing_running_time_end_date.dateTime()

        time_difference = self.calculate_date(time_begin, time_end)
        self.complications_during_tubing_running_time_line.setText(str(time_difference))

    def update_date_sand_filling_two(self):
        time_begin = self.sand_filling_two_time_begin_date.dateTime()
        time_end = self.sand_filling_two_time_end_date.dateTime()

        time_difference = self.calculate_date(time_begin, time_end)
        self.sand_filling_two_time_line.setText(str(time_difference))


class TabWidget(QTabWidget):
    def __init__(self):
        super().__init__()
        self.addTab(TabPage_SO_Sand(self), 'Трубный перфоратор')


class SandWork(TemplateWork):
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

        current_widget = self.tabWidget.currentWidget()

        self.date_work_line = current_widget.date_work_line.text()
        self.select_type_combo = current_widget.select_type_combo.currentText()
        if self.select_type_combo == '':
            return
        elif self.select_type_combo in ['НКТ']:
            self.coefficient_lifting = 1

            self.sand_filling_text_edit = current_widget.sand_filling_text_edit.text()

        self.nkt_is_same_combo = current_widget.nkt_is_same_combo.currentText()
        self.type_equipment = 'Перо,воронка'
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

        self.sand_filling_two_combo = current_widget.sand_filling_two_combo.currentText()

        self.complications_when_lifting_combo = current_widget.complications_when_lifting_combo.currentText()
        self.sand_filling_combo = current_widget.sand_filling_combo.currentText()
        if self.sand_filling_combo == 'Да':
            self.height_sand_line = current_widget.height_sand_line.text()
            if self.height_sand_line == '':
                QMessageBox.warning(self, 'Ошибка', 'Не введена высота ПМ')
                return

            self.volume_sand_line = current_widget.volume_sand_line.text()
            if self.volume_sand_line == '':
                QMessageBox.warning(self, 'Ошибка', 'Не введен объем песка')
                return
            else:
                self.volume_sand_line = float(self.volume_sand_line )


            self.bottom_sand_line = current_widget.bottom_sand_line.text()
            if self.bottom_sand_line == '':
                QMessageBox.warning(self, 'Ошибка', 'Не введен глубина определения ПМ')
                return
            else:
                self.bottom_sand_line = float(self.bottom_sand_line)

            self.count_of_nkt_extensions_line = current_widget.count_of_nkt_extensions_line.text()
            if self.count_of_nkt_extensions_line == '':
                QMessageBox.warning(self, 'Ошибка', 'Не введен кол-во НКТ на допуск')
                return
            else:
                self.count_of_nkt_extensions_line = int(float(self.count_of_nkt_extensions_line))

            # self.pressuar_gno_combo = current_widget.pressuar_gno_combo.currentText()

            self.sand_filling_time_begin_date = \
                current_widget.sand_filling_time_begin_date.dateTime().toPyDateTime()
            self.sand_filling_time_begin_date = \
                self.change_string_in_date(self.sand_filling_time_begin_date)

            self.sand_filling_time_end_date = \
                current_widget.sand_filling_time_end_date.dateTime().toPyDateTime()
            self.sand_filling_time_end_date = \
                self.change_string_in_date(self.sand_filling_time_end_date)

            if self.sand_filling_time_end_date == self.sand_filling_time_begin_date:
                QMessageBox.warning(self, 'Даты совпадают', 'Даты совпадают')
                return

            self.sand_filling_time_line = current_widget.sand_filling_time_line.text()
            if self.sand_filling_time_line != '':
                self.sand_filling_time_line = round(float(self.sand_filling_time_line), 1)

            else:
                QMessageBox.warning(self, 'Ошибка', f'Не введены время осложнения при срыве ПШ')
                return

            if self.sand_filling_time_line <= 0:
                QMessageBox.warning(self, 'Ошибка', f'Затраченное время при срыве ПШ не может быть отрицательным')
                return

        if self.sand_filling_two_combo in ['Вымыв', 'Досыпка']:

            self.height_sand_two_line = current_widget.height_sand_two_line.text()
            if self.height_sand_two_line == '':
                QMessageBox.warning(self, 'Ошибка', 'Не введена высота ПМ')
                return

            self.volume_sand_two_line = current_widget.volume_sand_two_line.text()
            if self.volume_sand_line == '':
                QMessageBox.warning(self, 'Ошибка', 'Не введен объем песка')
                return
            else:
                self.volume_sand_two_line = float(self.volume_sand_two_line)

            self.bottom_sand_two_line = current_widget.bottom_sand_two_line.text()
            if self.bottom_sand_two_line == '':
                QMessageBox.warning(self, 'Ошибка', 'Не введен глубина определения ПМ')
                return
            else:
                self.bottom_sand_two_line = float(self.bottom_sand_two_line)

            self.sand_filling_two_text_line = current_widget.sand_filling_two_text_line.text()
            self.sand_filling_two_time_begin_date = \
                current_widget.sand_filling_two_time_begin_date.dateTime().toPyDateTime()
            self.sand_filling_two_time_begin_date = \
                self.change_string_in_date(self.sand_filling_two_time_begin_date)

            self.sand_filling_two_time_end_date = \
                current_widget.sand_filling_two_time_end_date.dateTime().toPyDateTime()
            self.sand_filling_two_time_end_date = \
                self.change_string_in_date(self.sand_filling_two_time_end_date)

            if current_widget.sand_filling_two_text_line.text() == self.sand_filling_two_time_begin_date:
                QMessageBox.warning(self, 'Даты совпадают', 'Даты совпадают')
                return

            if self.sand_filling_two_text_line == '':
                QMessageBox.warning(self, 'Ошибка', f'Не введены обьем растворителя')
                return

            self.sand_filling_two_time_line = current_widget.sand_filling_two_time_line.text()
            self.count_of_nkt_extensions_two_line = current_widget.count_of_nkt_extensions_two_line.text()
            if self.count_of_nkt_extensions_two_line == '':
                QMessageBox.warning(self, 'Ошибка', 'Не введен кол-во НКТ на допуск')
                return
            else:
                self.count_of_nkt_extensions_two_line = int(float(self.count_of_nkt_extensions_two_line))

            if self.sand_filling_two_time_line != '':
                self.sand_filling_two_time_line = round(float(self.sand_filling_two_time_line),
                                                                    1)
            else:
                QMessageBox.warning(self, 'Ошибка', f'Не введены время ожидания песка')
                return

            if self.sand_filling_two_time_line <= 0:
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

        self.pressuar_ek_combo = current_widget.pressuar_ek_combo.currentText()
        if self.pressuar_ek_combo == 'Да':
            read_data = self.read_pressuar_combo(current_widget)
            if read_data is None:
                return

        # self.deinstallation_perforation_combo = current_widget.deinstallation_perforation_combo.currentText()
        #
        # if self.deinstallation_perforation_combo == 'Да':
        #     self.deinstallation_perforation_text_line = current_widget.deinstallation_perforation_text_line.text()
        #     self.deinstallation_perforation_time_begin_date = \
        #         current_widget.deinstallation_perforation_time_begin_date.dateTime().toPyDateTime()
        #     self.deinstallation_perforation_time_begin_date = \
        #         self.change_string_in_date(self.deinstallation_perforation_time_begin_date)
        #
        #     self.deinstallation_perforation_time_end_date = \
        #         current_widget.deinstallation_perforation_time_end_date.dateTime().toPyDateTime()
        #     self.deinstallation_perforation_time_end_date = \
        #         self.change_string_in_date(self.deinstallation_perforation_time_end_date)
        #
        #     if current_widget.deinstallation_perforation_text_line.text() == self.deinstallation_perforation_time_begin_date:
        #         QMessageBox.warning(self, 'Даты совпадают', 'Даты совпадают')
        #         return
        #
        #     if self.deinstallation_perforation_text_line == '':
        #         QMessageBox.warning(self, 'Ошибка', f'Не введены текст осложнения при срыве ПШ')
        #         return
        #
        #     self.deinstallation_perforation_time_line = current_widget.deinstallation_perforation_time_line.text()
        #     if self.deinstallation_perforation_time_line != '':
        #         self.deinstallation_perforation_time_line = round(float(self.deinstallation_perforation_time_line), 1)
        #
        #     else:
        #         QMessageBox.warning(self, 'Ошибка', f'Не введены время осложнения при срыве ПШ')
        #         return
        #
        #     if self.deinstallation_perforation_time_line <= 0:
        #         QMessageBox.warning(self, 'Ошибка', f'Затраченное время при срыве ПШ не может быть отрицательным')
        #         return

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



    def raid_work(self):
        complications_of_failure_list = []
        complications_during_disassembly_list = []
        work_list = [
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', 'Перо,воронка', 'ПЗР СПО перо, воронка',
             None, None, None, None, None,
             None, None, None, None, None, None, None, '§176разд.1', None, 'шт', 1, 0.5, 1, '=V1161*W1161*X1161',
             '=Y1161-AA1161-AB1161-AC1161-AD1161', None, None, None, None, None]]

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

        work_list.extend(self.sand_work(self.sand_filling_text_edit, self.volume_sand_line, self.height_sand_line,
                                        self.sand_filling_time_begin_date, self.sand_filling_time_end_date,
                                        self.sand_filling_time_line, self.count_of_nkt_extensions_line, self.bottom_sand_line))


        aaas = self.sand_filling_two_combo
        if self.sand_filling_two_combo in ['Вымыв', 'Досыпка']:
            if self.sand_filling_two_combo == 'Досыпка':
                work_list.extend(self.dopusk_lifting(self.count_of_nkt_extensions_line))
                work_list.extend(self.sand_work(self.sand_filling_text_edit, self.volume_sand_two_line, self.height_sand_two_line,
                               self.sand_filling_two_time_begin_date, self.sand_filling_two_time_end_date,
                               self.sand_filling_two_time_line, self.count_of_nkt_extensions_line, self.bottom_sand_line))
            else:
                work_list.extend(self.sand_flushing(self.sand_filling_two_text_line, self.volume_sand_two_line,
                                                    self.height_sand_two_line,
                               self.sand_filling_two_time_begin_date, self.sand_filling_two_time_end_date,
                               self.sand_filling_two_time_line, self.count_of_nkt_extensions_line, self.bottom_sand_line))
        if self.pressuar_ek_combo == 'Да':
            work_list.extend(self.pressuar_work())
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

        work_list.extend(self.lifting_nkt())


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

    def sand_flushing(self, sand_filling_text_edit, volume_sand_two_line, height_sand_two_line,
                               sand_filling_time_begin_date, sand_filling_time_end_date,
                               sand_filling_time_line, count_of_nkt_extensions_line, bottom_sand_line):
        work_list = [
            ['=ROW()-ROW($A$56)', None, None, 'Тех.операции', 'Промывка', 'ПР  перед вымывом излишков пропанта', None, None,
         None, None, None, None, None, None, None, None, None, None, '§285разд.1', None, 'раз', 1, 0.15, 1,
         '=V1171*W1171*X1171', '=Y1171-AA1171-AB1171-AC1171-AD1171', None, None, None, None, None],
        ['=ROW()-ROW($A$56)', None, None, 'Тех.операции', 'Промывка', f'Промывка в инт {sand_filling_text_edit}',
         None, None, None, None, None, None, None,
         None, 'АКТ№', None, None, None, '§301разд.1', None, 'м3', volume_sand_two_line, 0.033, 1, '=V1172*W1172*X1172',
         '=Y1172-AA1172-AB1172-AC1172-AD1172', None, None, None, None, None],
        ['=ROW()-ROW($A$56)', None, None, 'Тех.операции', 'Промывка', 'Разобрать промывочное оборудование', None, None,
         None, None, None, None, None, None, None, None, None, None, '§161разд.1', None, 'раз', 1, 0.23, 1,
         '=V1173*W1173*X1173', '=Y1173-AA1173-AB1173-AC1173-AD1173', None, None, None, None, None]]
        work_list.extend(self.dopusk_lifting(self.count_of_nkt_extensions_line))

        work_list.extend([['=ROW()-ROW($A$56)', None, None, 'Тех.операции', 'кварцевый песок',
             f'Ожидание оседание песка {sand_filling_time_begin_date}-{sand_filling_time_end_date}',
             None, None, None,
             None, None, None, None, None, 'АКТ№', None, None, None, 'простои', 'Тех. ожидание', 'час',
             sand_filling_time_line, 1, 1,
             '=V1168*W1168*X1168', '=Y1168-AA1168-AB1168-AC1168-AD1168', None, None, None, None, None]])
        work_list.extend(self.dopusk(count_of_nkt_extensions_line))

        work_list.append(['=ROW()-ROW($A$56)', None, None, 'Тех.операции', None,
                          f'Определение кровли песчанного моста на гл. {bottom_sand_line}м', None,
                          None, None, None, None, None, None, None, 'АКТ№', None, None, None, '§289разд.1', None, 'раз',
                          1, 0.17, 1,
                          '=V1169*W1169*X1169', '=Y1169-AA1169-AB1169-AC1169-AD1169', None, None, None, None, None])
        return work_list
    def sand_work(self, sand_filling_text_edit, volume_sand_line, height_sand_line, sand_filling_time_begin_date,
                  sand_filling_time_end_date, sand_filling_time_line, count_of_nkt_extensions_line, bottom_sand_line):

        lenght_nkt = sum(list(map(lambda x: x[0], self.dict_nkt.values())))

        normir_sand = f'=((1*{height_sand_line})+5+(((2.6/400)*0.75)*{lenght_nkt})+2+1+' \
                      f'(1.6*{height_sand_line})+(((2.6/400)*0.75)*{lenght_nkt})+1+39+27)/60'
        work_list = [
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'кварцевый песок',
             f'ПЗР+Отсыпка песком в инт. {sand_filling_text_edit} в объеме {volume_sand_line}л',
         None, None, None, None, None, 'Исполнитель', 'ПО ТКРС', None, 'АКТ№', 'ПЕСОК', 'Песок кварцевый фр.1-2', None,
         '§276разд.1', None, 'м', lenght_nkt, height_sand_line, 1,
         normir_sand,
         '=Y1167-AA1167-AB1167-AC1167-AD1167', None, None, None, None, None],
        ['=ROW()-ROW($A$56)', self.date_work_line, None, 'Тех.операции', 'кварцевый песок',
         f'Ожидание оседание песка {sand_filling_time_begin_date}-{sand_filling_time_end_date}',
         None, None, None,
         None, None, None, None, None, 'АКТ№', None, None, None, 'простои', 'Тех. ожидание', 'час',
         sand_filling_time_line, 1, 1,
         '=V1168*W1168*X1168', '=Y1168-AA1168-AB1168-AC1168-AD1168', None, None, None, None, None]]

        work_list.extend(self.dopusk(count_of_nkt_extensions_line))

        work_list.append(['=ROW()-ROW($A$56)', self.date_work_line, None, 'Тех.операции', None,
                          f'Определение кровли песчанного моста на гл. {bottom_sand_line}м', None,
         None, None, None, None, None, None, None, 'АКТ№', None, None, None, '§289разд.1', None, 'раз', 1, 0.17, 1,
         '=V1169*W1169*X1169', '=Y1169-AA1169-AB1169-AC1169-AD1169', None, None, None, None, None])

        return work_list




if __name__ == "__main__":
    # app3 = QApplication(sys.argv)

    app = QApplication(sys.argv)
    window = SandWork(22, 22)
    window.show()
    sys.exit(app.exec_())
