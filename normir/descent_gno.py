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
from normir.template_without_skm import TemplateWithoutSKM

from normir.relocation_brigade import TextEditTableWidgetItem
from normir.work_of_third_parties_without_nkt import TabPage_SO_Timplate, WorkOfThirdPaties
from normir.spo_pakera import SpoPakerAction


class TabPage_SO_Lifting_gno(QWidget):
    def __init__(self, parent=None):
        super().__init__()

        self.validator_int = QIntValidator(0, 6000)
        self.validator_float = QDoubleValidator(0.2, 1000, 1)

        self.gno_label = QLabel('Вид спускаемого ГНО')
        self.gno_combo = QComboBox(self)
        self.gno_combo.addItems(['', 'ЗО', 'Фондовый пакер', 'Воронка', 'ЭЦН', 'пакер ГРП'])

        self.date_work_label = QLabel('Дата работы')
        self.date_work_line = QLineEdit(self)
        self.date_work_line.setText(f'{well_data.date_work}')

        self.date_work_str = datetime.strptime(self.date_work_line.text(), '%d.%m.%Y')

        self.grid = QGridLayout(self)

        self.grid.addWidget(self.gno_label, 4, 1)
        self.grid.addWidget(self.gno_combo, 5, 1)
        self.grid.addWidget(self.date_work_label, 4, 2)
        self.grid.addWidget(self.date_work_line, 5, 2)

        self.lift_installation_label = QLabel('Подьемника')
        self.lift_installation_combo = QComboBox(self)
        self.lift_installation_combo.addItems(['', 'СУРС-40', 'АЗИНМАШ-37А (Оснастка 2×3)', 'АПРС-32 (Оснастка 2×3)',
                                               'АПРС-40 (Оснастка 2×3)', 'АПРС-40 (Оснастка 3×4)',
                                               'АПРС-50 (Оснастка 3×4)',
                                               'АПР60/80 (Оснастка 3×4)', 'УПА-60/80 (Оснастка 3×4)',
                                               'УПТ-32 (Оснастка 3×4)', 'БАРС 60/80'])
        self.lift_installation_combo.setCurrentText(well_data.lifting_unit_combo)

        self.grid.addWidget(self.lift_installation_label, 4, 4)
        self.grid.addWidget(self.lift_installation_combo, 5, 4)

        self.anchor_lifts_label = QLabel('демонтаж якорей')
        self.anchor_lifts_combo = QComboBox(self)
        self.anchor_lifts_combo.addItems(['Нет', 'Да'])

        self.grid.addWidget(self.anchor_lifts_label, 4, 5)
        self.grid.addWidget(self.anchor_lifts_combo, 5, 5)

        self.lift_installation_combo.currentTextChanged.connect(self.update_lifting)

        if well_data.date_work != '':
            self.date_work_line.setText(well_data.date_work)

        self.gno_combo.currentTextChanged.connect(self.update_gno)

        self.depth_paker_text_label = QLabel('Глубина посадки пакера')
        self.pressuar_ek_label = QLabel('Давление опрессовки')
        self.rezult_pressuar_combo_label = QLabel('Результат опрессовки')
        self.complications_of_failure_armatura_label = QLabel('осложнения при монтаже арматуры')
        self.complications_when_lifting_label = QLabel('Осложнения при спуске НКТ')
        self.nkt_48_lenght_label = QLabel('Длина НКТ48')
        self.nkt_48_count_label = QLabel('Кол-во НКТ48')
        self.nkt_60_lenght_label = QLabel('Длина НКТ60')
        self.nkt_60_count_label = QLabel('Кол-во НКТ60')
        self.nkt_73_lenght_label = QLabel('Длина НКТ73')
        self.nkt_73_count_label = QLabel('Кол-во НКТ73')
        self.nkt_89_lenght_label = QLabel('Длина НКТ89-102')
        self.nkt_89_count_label = QLabel('Кол-во НКТ89-102')
        self.scheme_bop_installation_label = QLabel('Демонтаж превентора')
        self.scheme_bop_installation_combo_problem_label = QLabel('Осложнения при Демонтаже ПВО')
        self.extra_work_text_label = QLabel('Текст проведения работ РГД')
        self.response_text_label = QLabel('Текст интерпретации')
        self.response_time_begin_label = QLabel('начало интерпретации')
        self.response_time_end_label = QLabel('Окончание интерпретации')

    def update_lifting(self, index):
        if 'АПР60' in index or 'УПА-60' in index or 'БАРС 60/80' in index or 'А-50':
            self.anchor_lifts_combo.setCurrentIndex(1)

    def update_date_response(self):
        time_begin = self.response_time_begin_date.dateTime()
        time_end = self.response_time_end_date.dateTime()

        time_difference = self.calculate_date(time_begin, time_end)

        self.response_time_line.setText(str(time_difference))

    def update_date_technological_crap(self):
        time_begin = self.extra_work_time_begin_date.dateTime()
        time_end = self.extra_work_time_end_date.dateTime()

        time_difference = self.calculate_date(time_begin, time_end)

        self.extra_work_time_line.setText(str(time_difference))

    def update_gno(self, index):

        self.count_sections_esp_label = QLabel('Кол-во секций ЭЦН')
        self.count_sections_esp_combo = QComboBox(self)
        self.count_sections_esp_combo.addItems(['1', '2', '3', '4', '5', '6', '7', '8'])

        self.count_sections_ped_label = QLabel('Кол-во секций ПЭД')
        self.count_sections_ped_combo = QComboBox(self)
        self.count_sections_ped_combo.addItems(['1', '2', '3', '4', '5', '6', '7', '8'])

        self.esp_dismantling_text_label = QLabel('Тип монтируемого ЭЦН')
        self.esp_dismantling_text_line = QLineEdit(self)
        self.esp_dismantling_text_line.setText('монтаж ЭЦН')

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

        if index in 'ЭЦН':
            self.grid.addWidget(self.esp_dismantling_text_label, 9, 1, 1, 2)
            self.grid.addWidget(self.esp_dismantling_text_line, 10, 1, 1, 2)

            self.grid.addWidget(self.count_sections_esp_label, 7, 1)
            self.grid.addWidget(self.count_sections_esp_combo, 8, 1)
            self.grid.addWidget(self.count_sections_ped_label, 7, 2)
            self.grid.addWidget(self.count_sections_ped_combo, 8, 2)
            self.grid.addWidget(self.esp_dismantling_time_begin_label, 7, 3)
            self.grid.addWidget(self.esp_dismantling_time_begin_date, 8, 3)
            self.grid.addWidget(self.esp_dismantling_time_end_label, 7, 4)
            self.grid.addWidget(self.esp_dismantling_time_end_date, 8, 4)
            self.grid.addWidget(self.esp_dismantling_time_label, 7, 5)
            self.grid.addWidget(self.esp_dismantling_time_line, 8, 5)

        else:
            try:
                self.count_sections_esp_label.setParent(None)
                self.count_sections_esp_combo.setParent(None)
                self.esp_dismantling_text_label.setParent(None)

                self.esp_dismantling_text_line.setParent(None)

                self.count_sections_ped_label.setParent(None)
                self.count_sections_ped_combo.setParent(None)

                self.esp_dismantling_time_begin_label.setParent(None)
                self.esp_dismantling_time_begin_date.setParent(None)

                self.esp_dismantling_time_end_label.setParent(None)
                self.esp_dismantling_time_end_date.setParent(None)

                self.esp_dismantling_time_label.setParent(None)
                self.esp_dismantling_time_line.setParent(None)
            except:
                pass

        if index in ['Фондовый пакер', 'пакер ГРП']:
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
        else:
            self.depth_paker_text_label.setParent(None)
            self.depth_paker_text_edit.setParent(None)
            self.pressuar_ek_label.setParent(None)
            self.pressuar_ek_line.setParent(None)
            self.rezult_pressuar_combo_label.setParent(None)
            self.rezult_pressuar_combo.setParent(None)

        self.complications_of_failure_armatura_combo = QComboBox(self)
        self.complications_of_failure_armatura_combo.addItems(['Нет', 'Да'])
        #
        # self.complications_of_failure_label = QLabel('осложнения при cпуске (излив)')
        # self.complications_of_failure_combo = QComboBox(self)
        # self.complications_of_failure_combo.addItems(['Нет', 'Да'])
        #
        self.work_gis_gk_label = QLabel('Проведение ГИС ГК и ЛМ')
        self.work_gis_gk_combo = QComboBox(self)
        self.work_gis_gk_combo.addItems(['Нет', 'Да'])

        self.complications_when_lifting_combo = QComboBox(self)
        self.complications_when_lifting_combo.addItems(['Нет', 'Да'])

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

        self.grid.addWidget(self.complications_when_lifting_label, 26, 1)
        self.grid.addWidget(self.complications_when_lifting_combo, 27, 1)

        #
        # self.grid.addWidget(self.complications_of_failure_label, 8, 1)
        # self.grid.addWidget(self.complications_of_failure_combo, 9, 1)

        # self.grid.addWidget(self.complications_of_failure_label, 10, 1)
        # self.grid.addWidget(self.complications_of_failure_combo, 11, 1)

        self.grid.addWidget(self.work_gis_gk_label, 28, 1)
        self.grid.addWidget(self.work_gis_gk_combo, 29, 1)

        self.scheme_bop_installation_combo = QComboBox(self)
        self.scheme_bop_installation_combo.addItems(['Вторая', 'Первая'])

        self.scheme_bop_installation_problem_combo = QComboBox(self)
        self.scheme_bop_installation_problem_combo.addItems(["Нет", "Да"])

        self.grid.addWidget(self.scheme_bop_installation_label, 35, 1)
        self.grid.addWidget(self.scheme_bop_installation_combo, 36, 1)

        self.grid.addWidget(self.scheme_bop_installation_combo_problem_label, 37, 1)
        self.grid.addWidget(self.scheme_bop_installation_problem_combo, 38, 1)

        self.grid.addWidget(self.complications_of_failure_armatura_label, 39, 1)
        self.grid.addWidget(self.complications_of_failure_armatura_combo, 40, 1)

        # self.lowering_for_pressure_testing_label = QLabel('Спуск НКТ под опрессовку ПВО')
        # self.lowering_for_pressure_testing_combo = QComboBox(self)
        # self.lowering_for_pressure_testing_combo.addItems(["Нет", "Да"])
        #
        # self.grid.addWidget(self.lowering_for_pressure_testing_label, 10, 2)
        # self.grid.addWidget(self.lowering_for_pressure_testing_combo, 11, 2)

        # self.lowering_for_pressure_testing_combo.currentTextChanged.connect(
        #     self.update_lowering_for_pressure_testing)
        # self.lowering_for_pressure_testing_combo.setCurrentIndex(1)
        # self.pressuar_gno_combo.currentTextChanged.connect(self.update_pressuar_gno_combo)
        self.work_gis_gk_combo.currentTextChanged.connect(
            self.update_work_gis_gk)
        # self.complications_of_failure_combo.currentTextChanged.connect(self.update_complications_of_failure)
        self.complications_when_lifting_combo.currentTextChanged.connect(self.update_complications_when_lifting)
        self.scheme_bop_installation_problem_combo.currentTextChanged.connect(
            self.update_scheme_bop_installation_combo_problem)
        self.scheme_bop_installation_combo.currentTextChanged.connect(self.update_scheme_bop_installation_combo)
        self.complications_of_failure_armatura_combo.currentTextChanged.connect(
            self.update_complications_of_failure_armatura)
        if index == 'Фондовый пакер':
            self.extra_work_label = QLabel('Проведение РГД')
            self.extra_work_combo = QComboBox(self)
            self.extra_work_combo.addItems(['Нет', 'Да'])
            self.grid.addWidget(self.extra_work_label, 52, 0)
            self.grid.addWidget(self.extra_work_combo, 53, 0)
            self.extra_work_combo.currentTextChanged.connect(self.update_extra_work_time_combo)

    def update_extra_work_time_combo(self, index):
        if index == 'Нет':
            self.extra_work_text_label.setParent(None)
            self.extra_work_text_line.setParent(None)
            self.extra_work_time_begin_label.setParent(None)
            self.extra_work_time_begin_date.setParent(None)
            self.extra_work_time_end_label.setParent(None)
            self.extra_work_time_end_date.setParent(None)
            self.extra_work_time_label.setParent(None)
            self.extra_work_time_line.setParent(None)
            self.response_text_label.setParent(None)
            self.response_text_line.setParent(None)
            self.response_time_begin_label.setParent(None)
            self.response_time_begin_date.setParent(None)

            self.response_time_end_label.setParent(None)
            self.response_time_end_date.setParent(None)

            self.response_time_line_label.setParent(None)
            self.response_time_line.setParent(None)
        else:
            TabPage_SO_Timplate.update_select_work_of_third_parties(self, 'Фондовый пакер')

    def update_scheme_bop_installation_combo(self, index):
        if index == 'Первая':
            self.line_lenght_bop_label = QLabel('Длина линии 1 Категории')
            self.line_lenght_bop_line = QLineEdit(self)
            self.line_lenght_bop_line.setValidator(self.validator_int)
            self.line_lenght_bop_line.setText('30')
            self.grid.addWidget(self.line_lenght_bop_label, 35, 6)
            self.grid.addWidget(self.line_lenght_bop_line, 36, 6)
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

            self.grid.addWidget(self.scheme_bop_installation_text_label, 37, 2)
            self.grid.addWidget(self.scheme_bop_installation_text_line, 38, 2)
            self.grid.addWidget(self.scheme_bop_installation_time_begin_label, 37, 3)
            self.grid.addWidget(self.scheme_bop_installation_time_begin_date, 38, 3)
            self.grid.addWidget(self.scheme_bop_installation_time_end_label, 37, 4)
            self.grid.addWidget(self.scheme_bop_installation_time_end_date, 38, 4)
            self.grid.addWidget(self.scheme_bop_installation_time_label, 37, 5)
            self.grid.addWidget(self.scheme_bop_installation_time_line, 38, 5)

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
            self.pressuar_bop_text_line.setText(f'Опрессовка ПВО {well_data.max_admissible_pressure._value}(+)')
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

            self.grid.addWidget(self.complications_of_failure_text_label, 8, 2)
            self.grid.addWidget(self.complications_of_failure_text_line, 9, 2)
            self.grid.addWidget(self.complications_of_failure_time_begin_label, 8, 3)
            self.grid.addWidget(self.complications_of_failure_time_begin_date, 9, 3)
            self.grid.addWidget(self.complications_of_failure_time_end_label, 8, 4)
            self.grid.addWidget(self.complications_of_failure_time_end_date, 9, 4)
            self.grid.addWidget(self.complications_of_failure_time_label, 8, 5)
            self.grid.addWidget(self.complications_of_failure_time_line, 9, 5)

            self.complications_of_failure_time_end_date.dateTimeChanged.connect(self.update_date_of_failure)
            self.complications_of_failure_time_begin_date.dateTimeChanged.connect(self.update_date_of_failure)

    def update_complications_of_failure_armatura(self, index):

        if index == 'Нет':
            self.complications_of_failure_armatura_text_label.setParent(None)
            self.complications_of_failure_armatura_text_line.setParent(None)
            self.complications_of_failure_armatura_time_label.setParent(None)
            self.complications_of_failure_armatura_time_line.setParent(None)
            self.complications_of_failure_armatura_time_end_label.setParent(None)
            self.complications_of_failure_armatura_time_end_date.setParent(None)
            self.complications_of_failure_armatura_time_begin_label.setParent(None)
            self.complications_of_failure_armatura_time_begin_date.setParent(None)
        else:
            self.complications_of_failure_armatura_text_label = QLabel('Текст осложнения')
            self.complications_of_failure_armatura_text_line = QLineEdit(self)

            self.complications_of_failure_armatura_time_begin_label = QLabel('начало осложнения')
            self.complications_of_failure_armatura_time_begin_date = QDateTimeEdit(self)
            self.complications_of_failure_armatura_time_begin_date.setDisplayFormat("dd.MM.yyyy HH:mm")
            self.complications_of_failure_armatura_time_begin_date.setDateTime(self.date_work_str)

            self.complications_of_failure_armatura_time_end_label = QLabel('Окончание осложнения')
            self.complications_of_failure_armatura_time_end_date = QDateTimeEdit(self)
            self.complications_of_failure_armatura_time_end_date.setDisplayFormat("dd.MM.yyyy HH:mm")
            self.complications_of_failure_armatura_time_end_date.setDateTime(self.date_work_str)

            self.complications_of_failure_armatura_time_label = QLabel('затраченное время')
            self.complications_of_failure_armatura_time_line = QLineEdit(self)
            self.complications_of_failure_armatura_time_line.setValidator(self.validator_float)

            self.grid.addWidget(self.complications_of_failure_armatura_text_label, 39, 2)
            self.grid.addWidget(self.complications_of_failure_armatura_text_line, 40, 2)
            self.grid.addWidget(self.complications_of_failure_armatura_time_begin_label, 39, 3)
            self.grid.addWidget(self.complications_of_failure_armatura_time_begin_date, 40, 3)
            self.grid.addWidget(self.complications_of_failure_armatura_time_end_label, 39, 4)
            self.grid.addWidget(self.complications_of_failure_armatura_time_end_date, 40, 4)
            self.grid.addWidget(self.complications_of_failure_armatura_time_label, 39, 5)
            self.grid.addWidget(self.complications_of_failure_armatura_time_line, 40, 5)

            self.complications_of_failure_armatura_time_end_date.dateTimeChanged.connect(self.update_date_of_armatura)
            self.complications_of_failure_armatura_time_begin_date.dateTimeChanged.connect(self.update_date_of_armatura)

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
        time_begin = self.work_gis_gk_q_time_begin_date.dateTime()
        time_end = self.work_gis_gk_q_time_end_date.dateTime()

        time_difference = self.calculate_date(time_begin, time_end)
        self.work_gis_gk_time_line.setText(str(time_difference))

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
            self.grid.addWidget(self.complications_when_lifting_text_label, 26, 2)
            self.grid.addWidget(self.complications_when_lifting_text_line, 27, 2)

            self.grid.addWidget(self.complications_when_lifting_time_begin_label, 26, 3)
            self.grid.addWidget(self.complications_when_lifting_time_begin_date, 27, 3)

            self.grid.addWidget(self.complications_when_lifting_time_end_label, 26, 4)
            self.grid.addWidget(self.complications_when_lifting_time_end_date, 27, 4)

            self.grid.addWidget(self.complications_when_lifting_time_label, 26, 5)
            self.grid.addWidget(self.complications_when_lifting_time_line, 27, 5)

            self.complications_when_lifting_time_end_date.dateTimeChanged.connect(self.update_date_when_lifting)
            self.complications_when_lifting_time_begin_date.dateTimeChanged.connect(self.update_date_when_lifting)

    def update_work_gis_gk(self, index):
        if index == 'Нет':
            self.work_gis_gk_q_label.setParent(None)
            self.work_gis_gk_q_line.setParent(None)
            self.work_gis_gk_time_label.setParent(None)
            self.work_gis_gk_time_line.setParent(None)
            self.work_gis_gk_q_time_begin_label.setParent(None)
            self.work_gis_gk_q_time_begin_date.setParent(None)
            self.work_gis_gk_q_time_end_label.setParent(None)
            self.work_gis_gk_q_time_end_date.setParent(None)


        else:
            self.work_gis_gk_q_label = QLabel('Текст осложнения')
            self.work_gis_gk_q_line = QLineEdit(self)
            self.work_gis_gk_q_line.setText('ГИС ГК и ЛМ')

            self.work_gis_gk_q_time_begin_label = QLabel('начало осложнения')
            self.work_gis_gk_q_time_begin_date = QDateTimeEdit(self)
            self.work_gis_gk_q_time_begin_date.setDisplayFormat("dd.MM.yyyy HH:mm")
            self.work_gis_gk_q_time_begin_date.setDateTime(self.date_work_str)

            self.work_gis_gk_q_time_end_label = QLabel('Окончание осложнения')
            self.work_gis_gk_q_time_end_date = QDateTimeEdit(self)
            self.work_gis_gk_q_time_end_date.setDisplayFormat("dd.MM.yyyy HH:mm")
            self.work_gis_gk_q_time_end_date.setDateTime(self.date_work_str)

            self.work_gis_gk_time_label = QLabel('затраченное время')
            self.work_gis_gk_time_line = QLineEdit(self)

            self.work_gis_gk_time_line.setValidator(self.validator_float)
            self.grid.addWidget(self.work_gis_gk_q_label, 28, 2)
            self.grid.addWidget(self.work_gis_gk_q_line, 29, 2)

            self.grid.addWidget(self.work_gis_gk_q_time_begin_label, 28, 3)
            self.grid.addWidget(self.work_gis_gk_q_time_begin_date, 29, 3)

            self.grid.addWidget(self.work_gis_gk_q_time_begin_label, 28, 4)
            self.grid.addWidget(self.work_gis_gk_q_time_end_date, 29, 4)

            self.grid.addWidget(self.work_gis_gk_time_label, 28, 5)
            self.grid.addWidget(self.work_gis_gk_time_line, 29, 5)

            self.work_gis_gk_q_time_end_date.dateTimeChanged.connect(
                self.update_date_during_disassembly_q)
            self.work_gis_gk_q_time_begin_date.dateTimeChanged.connect(
                self.update_date_during_disassembly_q)


class TabWidget(QTabWidget):
    def __init__(self):
        super().__init__()
        self.addTab(TabPage_SO_Lifting_gno(self), 'Спуск ГНО')


class DescentGnoWindow(QMainWindow):
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
        self.dict_sucker_pod = {}
        self.dict_nkt = {}
        self.need_saturation_well_text_line = None
        self.need_saturation_q_text_line = None
        self.cycle_count_combo = None
        self.volume_jamming_line = None
        self.work_gis_gk_text_line = None
        self.work_gis_gk_time_line = None
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
        self.gno_combo = current_widget.gno_combo.currentText()

        if self.gno_combo in ['Фондовый пакер']:
            self.coefficient_lifting = 1.2
        elif self.gno_combo in ['ЭЦН']:
            self.coefficient_lifting = 1
            self.type_equipment = 'ЭЦН'
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
        elif self.gno_combo in ['ЗО']:
            self.type_equipment = 'ЗО'
            self.coefficient_lifting = 1
        elif self.gno_combo in ['воронка']:
            self.type_equipment = 'воронка'
            self.coefficient_lifting = 1
        elif self.gno_combo in ['Фондовый пакер']:
            self.type_equipment = 'Фондовый пакер'
            self.coefficient_lifting = 1.2
            self.depth_paker_text_edit = current_widget.depth_paker_text_edit.text()

            if self.depth_paker_text_edit not in ['', None]:
                self.depth_paker_text_edit = int(self.depth_paker_text_edit)
            else:
                question = QMessageBox.question(self, 'Глубина посадки', 'Не введена глубина посадки пакера ')
                if question == QMessageBox.StandardButton.No:
                    return

            self.pressuar_ek_line = current_widget.pressuar_ek_line.text()
            if self.pressuar_ek_line != '':
                self.pressuar_ek_line = int(self.pressuar_ek_line)
            else:
                question = QMessageBox.question(self, 'Давление', 'Не указано давление опрессовки?')
                if question == QMessageBox.StandardButton.No:
                    return
        else:
            self.coefficient_lifting = 1

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

        self.lift_installation_combo = current_widget.lift_installation_combo.currentText()
        self.extra_work_combo = current_widget.extra_work_combo.currentText()
        # self.complications_of_failure_combo = current_widget.complications_of_failure_combo.currentText()
        self.complications_of_failure_armatura_combo = current_widget.complications_of_failure_armatura_combo.currentText()
        self.work_gis_gk_combo = current_widget.work_gis_gk_combo.currentText()
        self.complications_when_lifting_combo = current_widget.complications_when_lifting_combo.currentText()
        self.scheme_bop_installation_problem_combo = current_widget.scheme_bop_installation_problem_combo.currentText()
        self.anchor_lifts_combo = current_widget.anchor_lifts_combo.currentText()
        # self.pressuar_gno_combo = current_widget.pressuar_gno_combo.currentText()
        # self.lowering_for_pressure_testing_combo = current_widget.lowering_for_pressure_testing_combo.currentText()
        self.scheme_bop_installation_combo = current_widget.scheme_bop_installation_combo.currentText()
        if self.scheme_bop_installation_combo == 'Первая':
            self.line_lenght_bop_line = current_widget.line_lenght_bop_line.text()
            if self.line_lenght_bop_line != '':
                self.line_lenght_bop_line = int(float(self.line_lenght_bop_line))
        # if self.lowering_for_pressure_testing_combo == 'Да':
        #     self.count_nkt_line = current_widget.count_nkt_line.text()
        #     if self.count_nkt_line != '':
        #         self.count_nkt_line = int(float(self.count_nkt_line))
        #     self.pressuar_bop_text_line = current_widget.pressuar_bop_text_line.text()

        # if self.pressuar_gno_combo == 'Да':
        #     self.pressuar_gno_text_line = current_widget.pressuar_gno_text_line.text()
        #     if self.pressuar_gno_text_line == '':
        #         QMessageBox.warning(self, 'Ошибка', f'Не введены текст опрессовки ГНО')
        #         return

        # if self.complications_of_failure_combo == 'Да':
        #     self.complications_of_failure_text_line = current_widget.complications_of_failure_text_line.text()
        #     self.complications_of_failure_time_begin_date = \
        #         current_widget.complications_of_failure_time_begin_date.dateTime().toPyDateTime()
        #     self.complications_of_failure_time_begin_date = \
        #         self.change_string_in_date(self.complications_of_failure_time_begin_date)
        #
        #     self.complications_of_failure_time_end_date = \
        #         current_widget.complications_of_failure_time_end_date.dateTime().toPyDateTime()
        #     self.complications_of_failure_time_end_date = \
        #         self.change_string_in_date(self.complications_of_failure_time_end_date)
        #
        #     if current_widget.complications_of_failure_text_line.text() == self.complications_of_failure_time_begin_date:
        #         QMessageBox.warning(self, 'Даты совпадают', 'Даты совпадают')
        #         return
        #
        #     if self.complications_of_failure_text_line == '':
        #         QMessageBox.warning(self, 'Ошибка', f'Не введены текст осложнения при срыве ПШ')
        #         return
        #
        #     self.complications_of_failure_time_line = current_widget.complications_of_failure_time_line.text()
        #     if self.complications_of_failure_time_line != '':
        #         self.complications_of_failure_time_line = round(float(self.complications_of_failure_time_line), 1)
        #
        #     else:
        #         QMessageBox.warning(self, 'Ошибка', f'Не введены время осложнения при срыве ПШ')
        #         return
        #
        #     if self.complications_of_failure_time_line <= 0:
        #         QMessageBox.warning(self, 'Ошибка', f'Затраченное время при срыве ПШ не может быть отрицательным')
        #         return

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
            self.complications_of_failure_armatura_text_line = current_widget.complications_of_failure_armatura_text_line.text()
            self.complications_of_failure_armatura_time_begin_date = \
                current_widget.complications_of_failure_armatura_time_begin_date.dateTime().toPyDateTime()
            self.complications_of_failure_armatura_time_begin_date = \
                self.change_string_in_date(self.complications_of_failure_armatura_time_begin_date)

            self.complications_of_failure_armatura_time_end_date = \
                current_widget.complications_of_failure_armatura_time_end_date.dateTime().toPyDateTime()
            self.complications_of_failure_armatura_time_end_date = \
                self.change_string_in_date(self.complications_of_failure_armatura_time_end_date)

            if current_widget.complications_of_failure_armatura_text_line.text() == self.complications_of_failure_armatura_time_begin_date:
                QMessageBox.warning(self, 'Даты совпадают', 'Даты совпадают')
                return

            if self.complications_of_failure_armatura_text_line == '':
                QMessageBox.warning(self, 'Ошибка', f'Не введены текст осложнения демонтаже арматуры')
                return

            self.complications_of_failure_armatura_time_line = current_widget.complications_of_failure_armatura_time_line.text()
            if self.complications_of_failure_armatura_time_line != '':
                self.complications_of_failure_armatura_time_line = round(
                    float(self.complications_of_failure_armatura_time_line), 1)

            else:
                QMessageBox.warning(self, 'Ошибка', f'Не введены время осложнения при демонтаже арматуры')
                return

            if self.complications_of_failure_armatura_time_line <= 0:
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
        if self.extra_work_combo == 'Да':
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

        if self.work_gis_gk_combo == 'Да':
            self.work_gis_gk_q_line = current_widget.work_gis_gk_q_line.text()

            self.work_gis_gk_q_time_begin_date = \
                current_widget.work_gis_gk_q_time_begin_date.dateTime().toPyDateTime()
            self.work_gis_gk_q_time_begin_date = \
                self.change_string_in_date(self.work_gis_gk_q_time_begin_date)

            self.work_gis_gk_q_time_end_date = \
                current_widget.work_gis_gk_q_time_end_date.dateTime().toPyDateTime()
            self.work_gis_gk_q_time_end_date = \
                self.change_string_in_date(self.work_gis_gk_q_time_end_date)

            if self.work_gis_gk_q_time_end_date == \
                    self.work_gis_gk_q_time_begin_date:
                QMessageBox.warning(self, 'Даты совпадают', 'Даты совпадают')
                return

            if self.work_gis_gk_q_line == '':
                QMessageBox.warning(self, 'Ошибка', f'Не введены текст Работы ГИС')
                return

            self.work_gis_gk_time_line = \
                current_widget.work_gis_gk_time_line.text()

            if self.work_gis_gk_time_line != '':
                self.work_gis_gk_time_line = round(
                    float(self.work_gis_gk_time_line), 1)
            else:
                QMessageBox.warning(self, 'Ошибка', f'Не введены время работе ГИС ')

            if self.work_gis_gk_time_line <= 0:
                QMessageBox.warning(self, 'Ошибка', f'Затраченное время при работе ГИС не может быть отрицательным')
                return

        if len(self.dict_nkt) == 0:
            question = QMessageBox.question(self, 'Ошибка', f'НКТ отсутствуют?')
            if question == QMessageBox.StandardButton.No:
                return

        work_list = self.descent_paker_def()

        well_data.date_work = self.date_work_line

        MyWindow.populate_row(self, self.ins_ind, work_list, self.table_widget)
        well_data.pause = False
        self.close()

    @staticmethod
    def change_string_in_date(date_str):
        # Преобразуем строку в объект datetime

        formatted_date = date_str.strftime("%d.%m.%Y %H:%M")
        return formatted_date

    def finish_krs(self):

        work_list = [
            ['=ROW()-ROW($A$46)', None, None, 'ЗР.после.ремонта', None, 'Погрузка оборудования', None, None, None, None,
             None, None, None, None, None, None, None, None, '§299разд.1', None, 'шт', 1, 1.7, 1, '=V1115*W1115*X1115',
             '=Y1115-AA1115-AB1115-AC1115-AD1115', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', None, None, 'ЗР.после.ремонта', None, 'Уборка рабочей зоны', None, None, None, None,
             None, None, None, None, None, None, None, None, '§9разд.1', None, 'шт', 1, 0.37, 1, '=V1116*W1116*X1116',
             '=Y1116-AA1116-AB1116-AC1116-AD1116', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', None, None, 'ПР.перед.ремонтом', None, 'Разборка линии долива', None, None, None,
             None, None, None, None, None, None, None, None, None, '§15разд.1', None, 'шт', 1, 0.17, 1,
             '=V1117*W1117*X1117', '=Y1117-AA1117-AB1117-AC1117-AD1117', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', None, None, 'ЗР.после.ремонта', None,
             'Снять  заземления (2 куль.будки, доливная, мостки, площадка,2 щита, ПА)(с испытанием )', None, None, None,
             None, None, None, None, None, None, None, None, None, '§33разд.1', None, 'шт', 10, 0.08, 1,
             '=V1118*W1118*X1118', '=Y1118-AA1118-AB1118-AC1118-AD1118', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', None, None, 'ЗР.после.ремонта', None,
             'Размотать электрокабель и отключить оборудование к электросети ', None, None, None, None, None, None,
             None, None, None, None, None, None, '§34разд.1', None, 'шт', 4, 0.1, 1, '=V1119*W1119*X1119',
             '=Y1119-AA1119-AB1119-AC1119-AD1119', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', None, None, 'ЗР.после.ремонта', None, 'Убрать подставки (1шт.)', None, None, None,
             None, None, None, None, None, None, None, None, None, '§35разд.1', None, 'раз', 10, 0.02, 1,
             '=V1120*W1120*X1120', '=Y1120-AA1120-AB1120-AC1120-AD1120', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', None, None, 'ЗР.после.ремонта', None, 'Отключить прожектора', None, None, None, None,
             None, None, None, None, None, None, None, None, '§36разд.1', None, 'шт', 1, 0.08, 1, '=V1121*W1121*X1121',
             '=Y1121-AA1121-AB1121-AC1121-AD1121', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', None, None, 'ЗР.после.ремонта', None, 'Погрузка труб на трал', None, None, None, None,
             None, None, None, None, None, None, None, None, '§39разд.1', None, 'шт', 150, 0.00417, 1,
             '=V1122*W1122*X1122', '=Y1122-AA1122-AB1122-AC1122-AD1122', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', None, None, 'ЗР.после.ремонта', None, 'Погрузить или выгрузить штангу', None, None,
             None, None, None, None, None, None, None, None, None, None, '§39разд.1', None, 'шт', 150, 0.003, 1,
             '=V1123*W1123*X1123', '=Y1123-AA1123-AB1123-AC1123-AD1123', None, None, None, None, None]]

        return work_list

    def descent_paker_def(self):
        complications_of_failure_list = []
        work_gis_gk_list = []
        if self.gno_combo in ['ЭЦН']:
            work_list = self.descent_ecn()
        elif self.gno_combo in ['ЗО']:
            work_list = [
                ['=ROW()-ROW($A$56)', None, None, 'спо', 'Воронка', 'ПЗР СПО воронка', None, None, None, None, None,
                 None, None, None, None, None, None, None, '§177разд.1', None, 'шт', 1, 0.17, 1, '=V1060*W1060*X1060',
                 '=Y1060-AA1060-AB1060-AC1060-AD1060', None, None, None, None, None]]
        elif self.gno_combo in ['Фондовый пакер', 'пакер ГРП']:
            self.type_equipment = 'Фондовый пакер'
            work_list = [
                ['=ROW()-ROW($A$46)', None, None, 'спо', self.type_equipment, 'ПЗР СПО ПЕРО, ВОРОНКА', None, None,
                 None, None, None,
                 None, None, None, None, None, None, None, '§177разд.1', None, 'шт', 1, 0.17, 1, '=V530*W530*X530',
                 '=Y530-AA530-AB530-AC530-AD530', None, None, None, None, None],
                ['=ROW()-ROW($A$46)', None, None, 'спо', self.type_equipment, 'ПЗР СПО пакера', None, None, None,
                 None, None, None,
                 None, None, None, None, None, None, '§136,142разд.1', None, 'шт', 1, 0.48, 1, '=V532*W532*X532',
                 '=Y532-AA532-AB532-AC532-AD532', None, None, None, None, None],
            ]

        if len(self.dict_nkt) != 0:
            work_list.extend(TemplateWithoutSKM.descent_nkt_work(self))

        if self.complications_when_lifting_combo == 'Да':
            work_list.append(['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', self.type_equipment,
                              f'{self.complications_when_lifting_text_line} '
                              f'{self.complications_when_lifting_time_begin_date}'
                              f'{self.complications_when_lifting_time_end_date}',
                              None, None,
                              None, None, None,
                              None, 'Объем', 0, None, None, None, None, 'факт', None,
                              'час', self.complications_when_lifting_time_end_date, 1, 1, '=V206*W206*X206',
                              '=Y206-AA206-AB206-AC206-AD206', None, None, None, None, None])
            self.date_work_line = self.complications_when_lifting_time_end_date.split(' ')[0]

        if self.work_gis_gk_combo == 'Да':
            work_list.extend(WorkOfThirdPaties.work_gis(self))

        if self.gno_combo in ['ЭЦН']:
            work_list.extend(self.finish_ecn())

        work_list.extend(self.equipment_dismantling_work())

        work_list.extend(self.pvo_dismantling())

        if self.depth_paker_text_edit != '':
            work_list.extend(SpoPakerAction.pressuar_work(self))

        if self.scheme_bop_installation_problem_combo == 'Да':
            work_list.append(['=ROW()-ROW($A$46)', self.date_work_line, None, 'первая.категория', '30м',
                              f'{self.scheme_bop_installation_text_line} '
                              f'{self.scheme_bop_installation_time_begin_date}-{self.scheme_bop_installation_time_end_date}',
                              None, None, None, None, None, None, None,
                              None, None, None, None, None, 'факт', None, 'час', self.scheme_bop_installation_time_line,
                              1, 1,
                              '=V305*W305*X305',
                              '=Y305-AA305-AB305-AC305-AD305', None, None, None, None, None])

            self.date_work_line = self.scheme_bop_installation_time_end_date.split(' ')[0]

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

        if self.extra_work_combo == 'Да':
            work_list.extend(self.rgd_work())

        work_list.extend(self.dismantling_lifting())

        work_list.extend(self.finish_krs())

        return work_list

    def rgd_work(self):
        work_list = [
            ['=ROW()-ROW($A$46)', None, None, 'ГИС', 'РГД ВТ',
             f'{self.extra_work_text_line} {self.extra_work_time_begin_date}-{self.extra_work_time_end_date}',
             None, None, None, None, None, None, None, None, 'АКТ№', None, None, None, 'Факт', None, 'час',
             5, 1, 1, '=V353*W353*X353', '=Y353-AA353-AB353-AC353-AD353', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None,
             f'{self.response_text_line} ({self.response_time_begin_date}-{self.response_time_end_date})', None,
             None, None, None, None, None,
             None, None, None, None, None, None, 'Простои', 'Тех. ожидание', 'час', self.response_time_line, 1, 1,
             '=V389*W389*X389',
             '=Y389-AA389-AB389-AC389-AD389', None, None, None, None, None]]

        return work_list




def descent_ecn(self):
    time_difference = round(
        (((117 + ((self.count_sections_esp_combo - 1) * 15)) + ((self.count_sections_ped_combo - 1) * 23)) / 60), 2)
    work_list = [
        ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', 'ЭЦН', 'Разгрузить барабан, автонаматыватель', None, None,
         None, None, None, None, None, None, None, None, None, None, '§299разд.1', None, 'раз', 2, 0.33, 1,
         '=V953*W953*X953', '=Y953-AA953-AB953-AC953', None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', 'ЭЦН', 'Разгрузить подвесной ролик', None, None, None,
         None, None, None, None, None, None, None, None, None, '§299разд.1', None, 'раз', 1, 0.05, 1,
         '=V954*W954*X954', '=Y954-AA954-AB954-AC954', None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None,
         'Установить подвесной ролик для кабеля ЭЦН на мачте', None, None, None, None, None, None, None, None, None,
         None, None, None, '§96п.18 разд.1', None, 'час', 1, '=11/60', 1, '=V955*W955*X955',
         '=Y955-AA955-AB955-AC955-AD955', None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None,
         'Протаскивание электрокабеля через подвесной ролик (10м)', None, None, None, None, None, None, None, None,
         None, None, None, None, '§209разд.1', None, 'раз', 1, '=3/60', 1, '=V956*W956*X956',
         '=Y956-AA956-AB956-AC956-AD956', None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None,
         f'Монтаж УЭЦН  {self.esp_dismantling_time_begin_date}-{self.esp_dismantling_time_end_date}', None,
         'Кол-во секций ЭЦН',
         None, None, self.count_sections_esp_combo, 'Кол-во ПЭД', None, self.count_sections_ped_combo, 'АКТ№',
         None, None, None, 'факт', None, 'час', self.esp_dismantling_time_line - time_difference, 1, 1,
         '=V957*W957*X957', '=Y957-AA957-AB957-AC957-AD957', None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None,
         f'Монтаж {self.esp_dismantling_text_line}', None,
         'Кол-во секций ЭЦН', None,
         None, self.count_sections_esp_combo, 'Кол-во ПЭД', None, self.count_sections_ped_combo, None, None,
         None, None, '§221разд.1', None, 'шт', 1,
         '=((117+((K958-1)*15))+((N958-1)*23))/60', 1, '=V958*W958*X958', '=Y958-AA958-AB958-AC958-AD958', None,
         None, None, None, None]]

    if self.esp_dismantling_time_line - time_difference <= 0:
        work_list.pop(-2)

    return work_list


def finish_ecn(self):
    if '60' in list(self.dict_nkt.keys()) or '48' in list(self.dict_nkt.keys()):
        count_60 = 0
        for nkt_key, nkt_value in self.dict_nkt:
            if '60' in nkt_key or '48' in nkt_key:
                count_60 += nkt_value[0]

        work_list = [
            ['=ROW()-ROW($A$46)', 'на 60мм НКТ', None, 'Тех.операции', None, 'Рубка клямсы на кабеле', None, None,
             None,
             None, None, None, None, None, None, None, None, None, '§215разд.1', None, 'шт', f'={count_60}*2',
             '=0.25/60', 1,
             '=V966*W966*X966', '=Y966-AA966-AB966-AC966-AD966', None, None, None, None, None]]
    else:
        work_list = []

    nkt_sum = sum(list(map(lambda x: x[1], self.dict_nkt.values())))
    nkt_lenght = sum(list(map(lambda x: x[0], self.dict_nkt.values())))

    work_list_ecn = [
        ['=ROW()-ROW($A$46)', None, None, 'спо', 'ЭЦН',
         'Определить отклонение талевого блока, расслабить оттяжки, отцентрировать вышку и подтянуть оттяжки во время ремонта',
         None, None, None, None, None, None, None, None, None, None, None, None, '§59п.1 разд.1', None, 'час', 0.42,
         1, 1, '=V967*W967*X967', '=Y967-AA967-AB967-AC967-AD967', None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'спо', 'ЭЦН', 'Замер сопротивления через  300м', None, None, None, None,
         None, None, None, None, None, None, None, None, '§221разд.1', None, 'шт', nkt_lenght,
         '=(2+V968/300+2)*0.06',
         1,
         '=W968', '=Y968-AA968-AB968-AC968-AD968', None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None, 'Закл.работы после спуска труб', None, None, None,
         None, None, None, None, None, None, None, None, None, '§208разд.1', None, 'раз', 1, 0.82, 1,
         '=V969*W969*X969', '=Y969-AA969-AB969-AC969-AD969', None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None, 'Снять с мачты подвесной ролик кабеля ЭНЦ', None,
         None, None, None, None, None, None, None, None, None, None, None, '§97п.12 разд.1', None, 'час', 1,
         '=9/60', 1, '=V970*W970*X970', '=Y970-AA970-AB970-AC970-AD970', None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'спо', 'ЭЦН', 'Погрузить барабан, автонаматыватель', None, None, None,
         None, None, None, None, None, None, None, None, None, '§299разд.1', None, 'час', 2, 0.23, 1,
         '=V971*W971*X971', '=Y971-AA971-AB971-AC971-AD971', None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', 'ЭЦН', 'Погрузить подвесной ролик', None, None, None,
         None, None, None, None, None, None, None, None, None, '§299разд.1', None, 'раз', 1, 0.05, 1,
         '=V972*W972*X972', '=Y972-AA972-AB972-AC972', None, None, None, None, None]]

    work_list.extend(work_list_ecn)

    return work_list


def equipment_dismantling_work(self):
    work_list = [
        ['=ROW()-ROW($A$46)', None, None, 'ЗР.после.ремонта', None, 'Демонтаж ГКШ-1200', None, None, None, None,
         None, None, None, None, None, None, None, None, '§184разд.1', None, 'шт', 1, 0.12, 1, '=V974*W974*X974',
         '=Y974-AA974-AB974-AC974-AD974', None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'ЗР.после.ремонта', None, 'Демонтаж СПГ', None, None, None, None, None,
         None, None, None, None, None, None, None, '§185разд.1', None, 'шт', 1, 0.07, 1, '=V975*W975*X975',
         '=Y975-AA975-AB975-AC975-AD975', None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None, 'Разборка рабочей площадки ', None, None, None,
         None, None, None, None, None, None, None, None, None, '§54разд.1', None, 'шт', 1, 0.58, 1,
         '=V976*W976*X976', '=Y976-AA976-AB976-AC976-AD976', None, None, None, None, None]]
    if self.gno_combo in ['ЗО']:
        work_list[-1] = ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None,
                         'Разборка  рабочей площадки частично', None, None, None,
                         None, None, None, None, None, None, None, None, None, '§54разд.1', None, 'шт', 1, 0.3, 1,
                         '=V976*W976*X976', '=Y976-AA976-AB976-AC976-AD976', None, None, None, None, None]
    return work_list


def pvo_dismantling(self):
    if self.scheme_bop_installation_combo == 'Первая':
        work_list = [
            ['=ROW()-ROW($A$46)', None, None, 'первая.категория', '30м', 'Демонтаж Схема №1', None, None, None,
             None,
             None, None, None, None, None, None, None, None, '§24аразд.1', None, 'шт', 1, 1.47, 1,
             '=V978*W978*X978',
             '=Y978-AA978-AB978-AC978-AD978', None, None, None, None, None]]
    else:
        work_list = []

    work_list_ecn = [
        ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None, 'Демонтаж превентора', None, None, None, None, None,
         None, None, None, None, None, None, None, '§119разд.1', None, 'шт', 1, 0.52, 1, '=V979*W979*X979',
         '=Y979-AA979-AB979-AC979-AD979', None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None, 'Монтаж крестовины', None, None, None, None, None,
         None, None, None, None, None, None, None, '§300разд.1', None, 'шт', 1, 0.5, 1, '=V980*W980*X980',
         '=Y980-AA980-AB980-AC980-AD980', None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None, 'Монтаж АУ фонтанной арматуры ', None, None,
         None, None, None, None, None, None, None, None, None, None, '§103разд.1', None, 'раз', 1, 0.6, 1,
         '=V981*W981*X981', '=Y981-AA981-AB981-AC981-AD981', None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None, 'Монтаж планшайбы на устье скважины', None, None,
         None, None, None, None, None, None, None, None, None, None, '§106разд.1', None, 'шт', 1, 0.37, 1,
         '=V982*W982*X982', '=Y982-AA982-AB982-AC982-AD982', None, None, None, None, None]]
    if self.gno_combo in ['ЭЦН']:
        work_list_ecn.extend([['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None,
                               'Опрессовка сальникового уплотнения кабельного ввода', None, None, None, None, None,
                               None, None, None,
                               None, None, None, None, '§212разд.1', None, 'раз', 1, 0.5, 1, '=V983*W983*X983',
                               '=Y983-AA983-AB983-AC983-AD983', None, None, None, None, None],
                              ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None,
                               'Заполнить колонны труб водой для проверки работы глубинного насоса на 100м', None, None,
                               None, None, None,
                               None, None, None, None, None, None, None, '§201разд.1', None, 'м', '=M960', 1, 1,
                               '=ROUNDUP(SUM((V984*0.00058)+0.06),2)', '=ROUNDUP(Y984-AA984-AB984-AC984-AD984,2)', None,
                               None, None, None,
                               None],
                              ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None,
                               'ПЗР.Опрессовка ГНО при Р=60атм (+)', None, None,
                               None, None, None, None, None, None, 'АКТ№', None, None, None, '§150-152разд.1', None,
                               'шт', 1, 0.67, 1,
                               '=V985*W985*X985', '=Y985-AA985-AB985-AC985-AD985', None, None, None, None, None],
                              ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None, 'Контрольный замер изоляции (+)',
                               None, None, None,
                               None, None, None, None, None, 'АКТ№', None, None, None, '§221разд.1', None, 'раз', 1,
                               0.22, 1,
                               '=V986*W986*X986', '=Y986-AA986-AB986-AC986-AD986', None, None, None, None, None],
                              ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None, 'Пробная эксплуатация ', None,
                               None, None, None,
                               None, None, None, None, 'АКТ№', None, None, None, 'Простои', None, 'шт', 1, 0.57, 1,
                               '=V987*W987*X987',
                               '=Y987-AA987-AB987-AC987-AD987', None, None, None, None, None],
                              ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None, 'Пробная эксплуатация ', None,
                               None, None, None,
                               None, None, None, None, None, None, None, None, 'Простои', 'Тех. ожидание', 'шт', 1, 1.6,
                               1,
                               '=V988*W988*X988', '=Y988-AA988-AB988-AC988-AD988', None, None, None, None, None]])
    work_list.extend(work_list_ecn)
    return work_list


def dismantling_lifting(self):
    if 'А5-40' in self.lift_installation_combo:
        lift_installation_list = [
            ['=ROW()-ROW($A$46)', None, None, 'ЗР.после.ремонта', None, 'Демонтаж А5-40', None, None, None, None,
             None,
             None, None, None, None, None, None, None, '§69разд.1', None, 'шт', 1, 0.97, 1, '=V993*W993*X993',
             '=Y993-AA993-AB993-AC993-AD993', None, None, None, None, None]]
    elif 'СУРС-40' in self.lift_installation_combo:
        lift_installation_list = [
            ['=ROW()-ROW($A$46)', None, None, 'ЗР.после.ремонта', None,
             'Демонтаж подъемного агрегата СУРС-40 (подгот.)', None, None, None, None, None, None, None, None, None,
             None, None, None, '§63разд.1', None, 'шт', 1, 0.97, 1, '=V994*W994*X994',
             '=Y994-AA994-AB994-AC994-AD994',
             None, None, None, None, None]]
    elif 'УП 32/40' in self.lift_installation_combo:
        lift_installation_list = [
            ['=ROW()-ROW($A$46)', None, None, 'ЗР.после.ремонта', None,
             'Демонтаж подъемного агрегата УП32/40 (подгот.)', None, None, None, None,
             None, None, None, None, None, None, None, None, '§63разд.1', None, 'шт', 1,
             0.65, 1, '=V995*W995*X995', '=Y995-AA995-AB995-AC995-AD995', None, None,
             None, None, None], ]
    elif 'АПРС-40' in self.lift_installation_combo:
        lift_installation_list = [
            ['=ROW()-ROW($A$46)', None, None, 'ЗР.после.ремонта', None, 'Демонтаж подъемника АПРС-40', None, None,
             None,
             None, None, None, None, None, None, None, None, None, '§63разд.1', None, 'раз', 1, 0.65, 1,
             '=V990*W990*X990', '=Y990-AA990-AB990-AC990-AD990', None, None, None, None, None], ]
    elif 'АПРС-50' in self.lift_installation_combo:
        lift_installation_list = [
            ['=ROW()-ROW($A$46)', None, None, 'ЗР.после.ремонта', None, 'Демонтаж подъемника АПРС-50', None, None,
             None,
             None, None, None, None, None, None, None, None, None, '§71разд.1', None, 'раз', 1, 1.02, 1,
             '=V991*W991*X991', '=Y991-AA991-AB991-AC991-AD991', None, None, None, None, None]]
    elif 'АПР-60/80' in self.lift_installation_combo:
        lift_installation_list = [
            ['=ROW()-ROW($A$46)', None, None, 'ЗР.после.ремонта', None, 'Демонтаж подъемника АПР-60/80', None, None,
             None, None, None, None, None, None, None, None, None, None, '§87разд.1', None, 'шт', 1, 3.07, 1,
             '=V992*W992*X992', '=Y992-AA992-AB992-AC992-AD992', None, None, None, None, None]]
    elif 'УПА-60' in self.lift_installation_combo:
        lift_installation_list = [
            ['=ROW()-ROW($A$46)', None, None, 'ЗР.после.ремонта', None,
             'Демонтаж подъемного агрегата УПА-60 (подгот.)',
             None, None, None, None, None, None, None, None, None, None, None, None, '§83разд.1', None, 'шт', 1,
             3.13,
             1, '=V996*W996*X996', '=Y996-AA996-AB996-AC996-AD996', None, None, None, None, None], ]
    elif 'А5-40' in self.lift_installation_combo:
        lift_installation_list = [
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'ПР.перед.ремонтом', None,
             'Центрирование мачты подъемника А5-40 во время монтажа', None, None, None,
             None, None, None, None, None, None, None, None, None, '§59разд.1', None, 'шт',
             1, 0.67, 1, '=V103*W103*X103', '=Y103-AA103-AB103-AC103-AD103', None, None,
             None, None, None]]
    elif 'А-50М' in self.lift_installation_combo:
        lift_installation_list = [
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'ПР.перед.ремонтом', None, 'Монтаж подъемника А-50М',
             None, None,
             None,
             None,
             None, None, None, None, None, None, None, None, '§72 р.1', None, 'шт', 1, 3.25, 1, '=V104*W104*X104',
             '=Y104-AA104-AB104-AC104-AD104', None, None, None, None, None]]
    elif 'БАРС-80' in self.lift_installation_combo:
        lift_installation_list = [
            ['=ROW()-ROW($A$56)', None, None, 'ЗР.после.ремонта', None, 'Демонтаж подъемника БАРС-80 (с оттяжками)',
             None, None, None, None, None, None, None, None, None, None, None, None, '§89разд.1', None, 'шт', 1,
             2.81, 1, '=V998*W998*X998', '=Y998-AA998-AB998-AC998-AD998', None, None, None, None, None]]

    if self.anchor_lifts_combo == 'Да':
        anchor_lifts = [
            ['=ROW()-ROW($A$46)', None, None, 'Оттяжки', None, 'Вытаскивание  якорей', None, None, None, None, None,
             None, None, None, None, None, None, None, '§31разд.1', None, 'шт', 4, 0.05, 1, '=V999*W999*X999',
             '=Y999-AA999-AB999-AC999-AD999', None, None, None, None, None]
        ]
        lift_installation_list.extend(anchor_lifts)

    return lift_installation_list


def dismantling_lifting_222(self):
    work_list = [
        ['=ROW()-ROW($A$56)', None, None, 'ЗР.после.ремонта', None, 'Демонтаж подъемника БАРС-80 (без оттяжек)',
         None, None, None, None, None, None, None, None, None, None, None, None, '§89разд.1', None, 'шт', 1, 2.05,
         1, '=V997*W997*X997', '=Y997-AA997-AB997-AC997-AD997', None, None, None, None, None],
        ['=ROW()-ROW($A$56)', None, None, 'ЗР.после.ремонта', None, 'Демонтаж подъемника БАРС-80 (с оттяжками)',
         None, None, None, None, None, None, None, None, None, None, None, None, '§89разд.1', None, 'шт', 1, 2.81,
         1, '=V998*W998*X998', '=Y998-AA998-AB998-AC998-AD998', None, None, None, None, None],
    ]


if __name__ == "__main__":
    # app3 = QApplication(sys.argv)

    app = QApplication(sys.argv)
    window = DescentGnoWindow(22, 22)
    window.show()
    sys.exit(app.exec_())
