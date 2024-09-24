import re

from PyQt5.QtCore import QDate
from PyQt5.QtGui import QIntValidator, QDoubleValidator
from PyQt5.QtWidgets import QWidget, QLabel, QComboBox, QLineEdit, QGridLayout, QTabWidget, QMainWindow, QPushButton, \
    QMessageBox, QApplication, QHeaderView, QTableWidget, QTableWidgetItem, QTabWidget, QTextEdit, QDateEdit, \
    QDateTimeEdit

import well_data
from datetime import datetime, timedelta

from main import MyWindow
from normir.files_with_list import cause_discharge_list, cause_presence_of_downtime_list, \
    cause_presence_of_downtime_classifocations_list, operations_of_downtimes_list

from normir.norms import DESCENT_NORM_NKT, LIFTING_NORM_NKT


class TabPage(QWidget):

    def __init__(self, parent=None):
        super().__init__()

        self.descent_layout_label = QLabel('Компоновка на спуск')
        self.determination_of_pickup_combo_label = QLabel('Было ли определение Q?')
        self.saturation_volume_label = QLabel('объем насыщения')
        self.extra_work_question_label = QLabel('Дополнительные работы')
        self.depth_paker_text_label = QLabel('Глубина посадки пакера')
        self.pressuar_ek_label = QLabel('Давление опрессовки')
        self.rezult_zumpf_pressuar_combo_label = QLabel('Результат опрессовки')
        self.determination_of_pickup_combo_zumpf_label = QLabel('Было ли определение Q?')
        self.rezult_pressuar_combo_label = QLabel('Результат опрессовки')
        self.definition_q_label = QLabel('Было ли определение Q после РИР')
        self.count_nkt_combo_label = QLabel('Была ли допуск НКТ?')
        self.depth_zumpf_paker_label = QLabel('Глубина посадки пакера ЗУМФПа')
        self.saturation_volume_zumpf_label = QLabel('Объем Насыщения')
        self.ovtr_work_text_label = QLabel('ОВТР')
        self.ovtr_work_time_begin_label = QLabel('Начало ОВТР')
        self.ovtr_work_time_end_label = QLabel('Окончание ОВТР')
        self.ovtr_work_time_line_label = QLabel('Текст ОВТР')
        self.rir_with_pero_text_label = QLabel('Текст РИР')

        self.complications_during_tubing_running_label = QLabel('Осложнение при спуске НКТ')
        self.complications_of_failure_label = QLabel('Получен ли прихват, наличие рассхаживания')
        self.complications_when_lifting_label = QLabel('Осложнения при подъеме НКТ')
        self.nkt_48_lenght_label = QLabel('Длина на спуск НКТ48')
        self.nkt_48_count_label = QLabel('Кол-во на спуск НКТ48')
        self.nkt_60_lenght_label = QLabel('Длина на спуск НКТ60')
        self.technological_crap_question_label = QLabel('Был ли допуск')
        self.nkt_60_count_label = QLabel('Кол-во на спуск НКТ60')
        self.fishing_works_time_end_label = QLabel('Окончание ловильных')
        self.fishing_works_label = QLabel('Текст Ловильных работ')
        self.depth_zumpf_paker_combo_label = QLabel('Опрессовка ЗУМПФа')
        self.fishing_works_time_begin_label = QLabel('начало ловильных')
        self.fishing_works_time_label = QLabel('затраченное работ')
        self.nkt_73_lenght_label = QLabel('Длина НКТ73')
        self.nkt_73_count_label = QLabel('Кол-во НКТ73')
        self.nkt_89_lenght_label = QLabel('Длина НКТ89-102')
        self.nkt_89_count_label = QLabel('Кол-во НКТ89-102')
        self.determination_of_pickup_text_label = QLabel('Текст определение Q')
        self.volume_well_flush_label = QLabel('Объем промывки')
        self.solvent_injection_label = QLabel('Закачка растворителя')
        self.nkt_is_same_label = QLabel('Кол-во НКТ на подъем совпадает со спуском')
        self.normalization_question_label = QLabel('Было ли дренирование?')
        self.interval_skm_text_label = QLabel('Интервалы скреперования')
        self.count_of_nkt_extensions_label = QLabel('Кол-во метров скреперования')
        self.volume_cement_line_label = QLabel('Объем цемента')
        self.rir_with_pero_text_label = QLabel('Интервал УЦМ')
        self.volume_of_finishing_label = QLabel('Объем доводки тех водой')
        self.response_text_label = QLabel('Текст реагирование')
        self.volume_flush_label = QLabel('Объем промывки')
        self.solvent_volume_time_begin_label = QLabel('начало реагирования')
        self.solvent_volume_time_end_label = QLabel('Окончание реагирования')
        self.solvent_volume_time_label = QLabel('затраченное время реагирования')
        self.select_type_nkt_combo_label = QLabel('Выбор спущенной компоновки')
        self.solvent_volume_text_label = QLabel(self)
        self.extra_work_text_label = QLabel('Текст проведения работ')
        self.extra_work_time_begin_label = QLabel('начало проведения работ')
        self.extra_work_time_end_label = QLabel('Окончание проведения работ')
        self.extra_work_time_label = QLabel('затраченное время')
        self.response_text_label = QLabel('Текст реагирование')
        self.response_time_begin_label = QLabel('начало реагирования')
        self.response_time_end_label = QLabel('Окончание реагирования')
        self.pressuar_tnkt_label = QLabel('Была ли опрессовка ТНКТ и вымыв шара')

        self.date_work_label = QLabel('Дата работы')
        self.date_work_line = QDateEdit(self)
        day, month, year = list(map(int, well_data.date_work.split('.')))
        self.date_work_line.setDate(QDate(year, month, day))

        self.date_work_str = datetime.strptime(self.date_work_line.text(), '%d.%m.%Y')

        self.validator_int = QIntValidator(0, 6000)
        self.validator_float = QDoubleValidator(0.2, 6000, 1)

    def sucker_up(self):
        self.sucker_pod_19_lenght_label = QLabel('Длина штанги 19мм')
        self.sucker_pod_22_lenght_label = QLabel('Длина штанги 22мм')
        self.sucker_pod_25_lenght_label = QLabel('Длина штанги 25мм')

        self.sucker_pod_19_lenght_edit = QLineEdit(self)
        self.sucker_pod_19_lenght_edit.setValidator(self.validator_float)
        self.sucker_pod_19_lenght_edit.setText('8')

        self.sucker_pod_22_lenght_edit = QLineEdit(self)
        self.sucker_pod_22_lenght_edit.setText('8')
        self.sucker_pod_22_lenght_edit.setValidator(self.validator_float)

        self.sucker_pod_25_lenght_edit = QLineEdit(self)
        self.sucker_pod_25_lenght_edit.setText('8')
        self.sucker_pod_25_lenght_edit.setValidator(self.validator_float)

        self.sucker_pod_19_count_label = QLabel('Кол-во штанги 19мм')
        self.sucker_pod_19_count_edit = QLineEdit(self)
        self.sucker_pod_19_count_edit.setValidator(self.validator_float)

        self.sucker_pod_22_count_label = QLabel('Кол-во штанги 22мм')
        self.sucker_pod_22_count_edit = QLineEdit(self)
        self.sucker_pod_22_count_edit.setValidator(self.validator_float)

        self.sucker_pod_25_count_label = QLabel('Кол-во штанги 25мм')
        self.sucker_pod_25_count_edit = QLineEdit(self)
        self.sucker_pod_25_count_edit.setValidator(self.validator_float)

        self.grid.addWidget(self.sucker_pod_19_lenght_label, 10, 1)
        self.grid.addWidget(self.sucker_pod_19_lenght_edit, 11, 1)

        self.grid.addWidget(self.sucker_pod_22_lenght_label, 10, 2)
        self.grid.addWidget(self.sucker_pod_22_lenght_edit, 11, 2)

        self.grid.addWidget(self.sucker_pod_25_lenght_label, 10, 3)
        self.grid.addWidget(self.sucker_pod_25_lenght_edit, 11, 3)

        self.grid.addWidget(self.sucker_pod_19_count_label, 12, 1)
        self.grid.addWidget(self.sucker_pod_19_count_edit, 13, 1)

        self.grid.addWidget(self.sucker_pod_22_count_label, 12, 2)
        self.grid.addWidget(self.sucker_pod_22_count_edit, 13, 2)

        self.grid.addWidget(self.sucker_pod_25_count_label, 12, 3)
        self.grid.addWidget(self.sucker_pod_25_count_edit, 13, 3)

    def insert_date_in_ois(self, index_date):
        day_to_day = index_date.date().day()
        month_to_day = index_date.date().month()
        for datа_day, data_work, _, _ in well_data.work_list_in_ois[1:]:
            day,  month, year = list(map(int, datа_day.split('\n')[0].split('.')))
            if day_to_day == day and month_to_day == month:

                if ' спуск ' in data_work.lower() and ' на тНКТ':
                    # Паттерн для извлечения нужной части
                    pattern = r"(спуск.*?на тНКТ[^–]*)"
                    # Поиск в тексте
                    match = re.search(pattern, data_work)

                    if match:
                        result = match.group(1)
                          # Получаем найденную подстроку
                        self.descent_layout_line.setText(result[:])

    def extra_work(self, index):

        self.extra_work_text_line = QLineEdit(self)

        self.extra_work_time_begin_date = QDateTimeEdit(self)
        self.extra_work_time_begin_date.setDisplayFormat("dd.MM.yyyy HH:mm")
        self.extra_work_time_begin_date.setDateTime(self.date_work_str)

        self.extra_work_time_end_date = QDateTimeEdit(self)
        self.extra_work_time_end_date.setDisplayFormat("dd.MM.yyyy HH:mm")
        self.extra_work_time_end_date.setDateTime(self.date_work_str)

        self.extra_work_time_line = QLineEdit(self)
        self.extra_work_time_line.setValidator(self.validator_float)

        self.grid.addWidget(self.extra_work_text_label, 52, 3)
        self.grid.addWidget(self.extra_work_text_line, 53, 3)
        self.grid.addWidget(self.extra_work_time_begin_label, 52, 4)
        self.grid.addWidget(self.extra_work_time_begin_date, 53, 4)
        self.grid.addWidget(self.extra_work_time_end_label, 52, 5)
        self.grid.addWidget(self.extra_work_time_end_date, 53, 5)
        self.grid.addWidget(self.extra_work_time_label, 52, 6)
        self.grid.addWidget(self.extra_work_time_line, 53, 6)

        self.extra_work_time_end_date.dateTimeChanged.connect(self.update_date_technological_crap)
        self.extra_work_time_begin_date.dateTimeChanged.connect(
            self.update_date_technological_crap)

        self.response_combo_label = QLabel('Реагирование')
        self.response_combo = QComboBox(self)
        self.response_combo.addItems(['Нет', 'Да'])

        self.response_combo.currentTextChanged.connect(self.update_sko_combo)

        self.volume_flush_line_combo_label = QLabel('Были ли промывка после СКО')
        self.volume_flush_line_combo = QComboBox(self)
        self.volume_flush_line_combo.addItems(['Нет', 'Да'])

        self.volume_flush_line_combo.currentTextChanged.connect(self.update_volume_flush_line_combo)

        self.determination_of_pickup_sko_combo_label = QLabel('Было ли определение Q после СКО')
        self.determination_of_pickup_sko_combo = QComboBox(self)
        self.determination_of_pickup_sko_combo.addItems(['Нет', 'Да'])

        self.grid.addWidget(self.response_combo_label, 62, 1)
        self.grid.addWidget(self.response_combo, 63, 1)
        self.grid.addWidget(self.volume_flush_line_combo_label, 64, 1)
        self.grid.addWidget(self.volume_flush_line_combo, 65, 1)
        self.grid.addWidget(self.determination_of_pickup_sko_combo_label, 90, 1)
        self.grid.addWidget(self.determination_of_pickup_sko_combo, 91, 1)

        self.determination_of_pickup_sko_combo.currentTextChanged.connect(
            self.update_determination_of_pickup_sko_combo)

        if index == 'Крезол':
            self.response_combo.setCurrentIndex(1)
            self.extra_work_text_line.setText('Работа фирмы ООО "Крезол"')
        elif index == 'Сваб':
            self.volume_swabing_edit = QLineEdit(self)
            self.volume_swabing_edit.setValidator(self.validator_int)
            self.grid.addWidget(self.volume_swabing_label, 52, 1)
            self.grid.addWidget(self.volume_swabing_edit, 53, 1)
            self.volume_flush_line_combo_label.setText('Была ли промывка после сваба')
            self.determination_of_pickup_sko_combo_label.setText('Было ли определение Q после сваба')

        # Сначала скрываем все виджеты
        self._hide_all_widgets()

        # Затем показываем только нужные виджеты в зависимости от значения index
        if index == 'Крезол':
            self.response_combo_label.show()
            self.response_combo.show()
            self.volume_flush_line_combo_label.show()
            self.volume_flush_line_combo.show()
            self.determination_of_pickup_sko_combo_label.show()
            self.determination_of_pickup_sko_combo.show()
        elif index == 'РИР 2С':
            self.count_nkt_combo = QComboBox(self)
            self.count_nkt_combo.addItems(['Нет', 'Да'])

            self.volume_flush_line_sko_line = QLineEdit(self)
            self.volume_flush_line_sko_line.setValidator(self.validator_float)

            self.definition_q_combo = QComboBox(self)
            self.definition_q_combo.addItems(['Нет', 'Да'])

            self.grid.addWidget(self.count_nkt_combo_label, 64, 0)
            self.grid.addWidget(self.count_nkt_combo, 65, 0)

            self.pressuar_ek_combo = QComboBox(self)
            self.pressuar_ek_combo.addItems(['Нет', 'Да'])

            self.grid.addWidget(self.pressuar_ek_combo_label, 66, 0)
            self.grid.addWidget(self.pressuar_ek_combo, 67, 0)

            self.grid.addWidget(self.definition_q_label, 68, 0)
            self.grid.addWidget(self.definition_q_combo, 69, 0)

            self.pressuar_ek_combo.currentTextChanged.connect(self.update_pressuar_ek_combo)

            self.count_nkt_combo.currentTextChanged.connect(self.update_count_nkt_combo)
            # self.definition_q_combo.currentTextChanged.connect(self.update_definition_q_combo)
            self.response_combo_label.show()
            self.response_combo.show()
        elif index == 'Сваб':
            self.volume_flush_line_combo_label.show()
            self.volume_flush_line_combo.show()
            self.determination_of_pickup_sko_combo_label.show()
            self.determination_of_pickup_sko_combo.show()

        elif index == 'РГД':
            self.response_combo_label.setText('Интерпретация')
            self.response_combo_label.show()
            self.response_combo.show()
            self.response_combo.setCurrentIndex(1)


    def _hide_all_widgets(self):
        self.response_combo_label.hide()
        self.response_combo.hide()
        self.volume_flush_line_combo_label.hide()
        self.volume_flush_line_combo.hide()
        self.determination_of_pickup_sko_combo_label.hide()
        self.determination_of_pickup_sko_combo.hide()

    def update_fishing_works_combo(self, index):
        if index == 'Нет':
            self.fishing_works_label.setParent(None)
            self.fishing_works_line.setParent(None)

            self.fishing_works_time_begin_label.setParent(None)
            self.fishing_works_time_begin_date.setParent(None)

            self.fishing_works_time_end_label.setParent(None)
            self.fishing_works_time_end_date.setParent(None)

            self.fishing_works_time_label.setParent(None)
            self.fishing_works_time_line.setParent(None)
        else:

            self.fishing_works_line = QLineEdit(self)

            self.fishing_works_time_begin_date = QDateTimeEdit(self)
            self.fishing_works_time_begin_date.setDisplayFormat("dd.MM.yyyy HH:mm")
            self.fishing_works_time_begin_date.setDateTime(self.date_work_str)

            self.fishing_works_time_end_date = QDateTimeEdit(self)
            self.fishing_works_time_end_date.setDisplayFormat("dd.MM.yyyy HH:mm")
            self.fishing_works_time_end_date.setDateTime(self.date_work_str)

            self.fishing_works_time_line = QLineEdit(self)

            self.fishing_works_time_line.setValidator(self.validator_float)
            self.grid.addWidget(self.fishing_works_label, 30, 2)
            self.grid.addWidget(self.fishing_works_line, 31, 2)

            self.grid.addWidget(self.fishing_works_time_begin_label, 30, 3)
            self.grid.addWidget(self.fishing_works_time_begin_date, 31, 3)

            self.grid.addWidget(self.fishing_works_time_begin_label, 30, 4)
            self.grid.addWidget(self.fishing_works_time_end_date, 31, 4)

            self.grid.addWidget(self.fishing_works_time_label, 30, 5)
            self.grid.addWidget(self.fishing_works_time_line, 31, 5)

            self.fishing_works_time_end_date.dateTimeChanged.connect(
                self.update_fishing_works)
            self.fishing_works_time_begin_date.dateTimeChanged.connect(
                self.update_fishing_works)

    def sucker_down(self, index):
        if index == 'Да':
            self.sucker_pod_19_lenght_up_label.setParent(None)
            self.sucker_pod_22_lenght_up_label.setParent(None)
            self.sucker_pod_25_lenght_up_label.setParent(None)

            self.sucker_pod_19_lenght_up_edit.setParent(None)

            self.sucker_pod_19_count_up_label.setParent(None)
            self.sucker_pod_19_count_up_edit.setParent(None)

            self.sucker_pod_22_lenght_up_edit.setParent(None)

            self.sucker_pod_22_count_up_label.setParent(None)
            self.sucker_pod_22_count_up_edit.setParent(None)

            self.sucker_pod_25_lenght_up_edit.setParent(None)
            self.sucker_pod_25_count_up_label.setParent(None)
            self.sucker_pod_25_count_up_edit.setParent(None)

        else:

            self.sucker_pod_19_lenght_up_label = QLabel('Длина штанг на подьем 19мм')
            self.sucker_pod_22_lenght_up_label = QLabel('Длина штанг на подьем 22мм')
            self.sucker_pod_25_lenght_up_label = QLabel('Длина штанг на подьем 25мм')

            self.sucker_pod_19_lenght_up_edit = QLineEdit(self)
            self.sucker_pod_19_lenght_up_edit.setValidator(self.validator_float)
            self.sucker_pod_19_lenght_up_edit.setText('8')

            self.sucker_pod_19_count_up_label = QLabel('Кол-во штанг 19мм')
            self.sucker_pod_19_count_up_edit = QLineEdit(self)
            self.sucker_pod_19_count_up_edit.setValidator(self.validator_float)

            self.sucker_pod_22_lenght_up_edit = QLineEdit(self)
            self.sucker_pod_22_lenght_up_edit.setText('8')
            self.sucker_pod_22_lenght_up_edit.setValidator(self.validator_float)

            self.sucker_pod_22_count_up_label = QLabel('Кол-во штанг 22мм')
            self.sucker_pod_22_count_up_edit = QLineEdit(self)
            self.sucker_pod_22_count_up_edit.setValidator(self.validator_float)

            self.sucker_pod_25_lenght_up_edit = QLineEdit(self)
            self.sucker_pod_25_lenght_up_edit.setText('8')
            self.sucker_pod_25_lenght_up_edit.setValidator(self.validator_float)

            self.sucker_pod_25_count_up_label = QLabel('Кол-во штанг 25мм')
            self.sucker_pod_25_count_up_edit = QLineEdit(self)
            self.sucker_pod_25_count_up_edit.setValidator(self.validator_float)

            self.grid.addWidget(self.sucker_pod_19_lenght_up_label, 42, 1)
            self.grid.addWidget(self.sucker_pod_19_lenght_up_edit, 43, 1)

            self.grid.addWidget(self.sucker_pod_22_lenght_up_label, 42, 2)
            self.grid.addWidget(self.sucker_pod_22_lenght_up_edit, 43, 2)

            self.grid.addWidget(self.sucker_pod_25_lenght_up_label, 42, 3)
            self.grid.addWidget(self.sucker_pod_25_lenght_up_edit, 43, 3)

            self.grid.addWidget(self.sucker_pod_19_count_up_label, 44, 1)
            self.grid.addWidget(self.sucker_pod_19_count_up_edit, 45, 1)

            self.grid.addWidget(self.sucker_pod_22_count_up_label, 44, 2)
            self.grid.addWidget(self.sucker_pod_22_count_up_edit, 45, 2)

            self.grid.addWidget(self.sucker_pod_25_count_up_label, 44, 3)
            self.grid.addWidget(self.sucker_pod_25_count_up_edit, 45, 3)

        # self.grid.addWidget(self.pressuar_gno_label, 6, 1)
        # self.grid.addWidget(self.pressuar_gno_combo, 7, 1)

    def update_lifting(self, index):
        if 'АПР60' in index or 'УПА-60' in index or 'БАРС 60/80' in index or 'А-50':
            self.anchor_lifts_combo.setCurrentIndex(1)

    def update_presence_of_downtime_combo(self, index):
        if index == 'Да':
            self.cause_presence_of_downtime_label = QLabel('Предварительная причина простоя')
            self.cause_presence_of_downtime_combo = QComboBox(self)

            self.cause_presence_of_downtime_combo.addItems(cause_presence_of_downtime_list)
            self.cause_presence_of_downtime_combo.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContents)

            self.presence_of_downtime_text_label = QLabel('текст простоя')
            self.presence_of_downtime_text_line = QLineEdit(self)

            self.cause_presence_of_downtime_classification_label = QLabel('Классификация простоя')
            self.cause_presence_of_downtime_classification_combo = QComboBox(self)

            self.cause_presence_of_downtime_classification_combo.addItems(
                cause_presence_of_downtime_classifocations_list)
            self.cause_presence_of_downtime_classification_combo.setSizeAdjustPolicy(
                QComboBox.SizeAdjustPolicy.AdjustToContents)

            self.tehnological_operation_label = QLabel('Тип простоя')
            self.tehnological_operation_combo = QComboBox(self)
            self.tehnological_operation_combo.addItems(operations_of_downtimes_list)

            self.presence_of_downtime_time_begin_label = QLabel('начало простоя')
            self.presence_of_downtime_time_begin_date = QDateTimeEdit(self)
            self.presence_of_downtime_time_begin_date.setDisplayFormat("dd.MM.yyyy HH:mm")
            self.presence_of_downtime_time_begin_date.setDateTime(self.date_work_str)

            self.presence_of_downtime_time_end_label = QLabel('Окончание простоя')
            self.presence_of_downtime_time_end_date = QDateTimeEdit(self)
            self.presence_of_downtime_time_end_date.setDisplayFormat("dd.MM.yyyy HH:mm")
            self.presence_of_downtime_time_end_date.setDateTime(self.date_work_str)

            self.presence_of_downtime_time_label = QLabel('затраченное время О')
            self.presence_of_downtime_time_line = QLineEdit(self)

            self.presence_of_downtime_time_line.setValidator(self.validator_float)
            self.grid.addWidget(self.presence_of_downtime_text_label, 20, 2, 1, 2)
            self.grid.addWidget(self.presence_of_downtime_text_line, 21, 2, 1, 2)

            self.grid.addWidget(self.presence_of_downtime_time_begin_label, 20, 4)
            self.grid.addWidget(self.presence_of_downtime_time_begin_date, 21, 4)

            self.grid.addWidget(self.presence_of_downtime_time_end_label, 20, 5)
            self.grid.addWidget(self.presence_of_downtime_time_end_date, 21, 5)

            self.grid.addWidget(self.presence_of_downtime_time_label, 20, 6)
            self.grid.addWidget(self.presence_of_downtime_time_line, 21, 6)

            self.presence_of_downtime_time_end_date.dateTimeChanged.connect(self.update_date_presence_of_downtime)
            self.presence_of_downtime_time_begin_date.dateTimeChanged.connect(self.update_date_presence_of_downtime)

            # self.time_presence_of_downtime_label = QLabel('Время простоя')
            # self.time_presence_of_downtime_line = QLineEdit(self)
            # self.time_presence_of_downtime_line.setValidator(self.validator_float)

            self.grid.addWidget(self.presence_of_downtime_label, 14, 2)
            self.grid.addWidget(self.presence_of_downtime_combo, 15, 2)
            self.grid.addWidget(self.cause_presence_of_downtime_label, 14, 3)
            self.grid.addWidget(self.cause_presence_of_downtime_combo, 15, 3)
            # self.grid.addWidget(self.cause_presence_of_downtime_text_label, 14, 4)
            # self.grid.addWidget(self.cause_presence_of_downtime_text_line, 15, 4)
            self.grid.addWidget(self.cause_presence_of_downtime_classification_label, 14, 4)
            self.grid.addWidget(self.cause_presence_of_downtime_classification_combo, 15, 4)
            self.grid.addWidget(self.tehnological_operation_label, 14, 5)
            self.grid.addWidget(self.tehnological_operation_combo, 15, 5)
            # self.grid.addWidget(self.time_presence_of_downtime_label, 14, 7)
            # self.grid.addWidget(self.time_presence_of_downtime_line, 15, 7)
        else:
            self.tehnological_operation_label.setParent(None)
            self.tehnological_operation_combo.setParent(None)
            self.cause_presence_of_downtime_label.setParent(None)
            self.cause_presence_of_downtime_combo.setParent(None)
            self.cause_presence_of_downtime_text_label.setParent(None)
            self.cause_presence_of_downtime_text_line.setParent(None)
            self.cause_presence_of_downtime_classification_label.setParent(None)
            self.cause_presence_of_downtime_classification_combo.setParent(None)
            self.cause_presence_of_downtime_classification_combo.setParent(None)
            self.tehnological_operation_label.setParent(None)
            self.tehnological_operation_combo.setParent(None)
            self.time_presence_of_downtime_label.setParent(None)
            self.time_presence_of_downtime_line.setParent(None)

        # self.lift_installation_combo.currentTextChanged.connect(self.update_lifting)

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
            self.solvent_volume_text_label = QLabel('Объем растворителя')
            self.solvent_volume_text_line = QLineEdit(self)
            self.solvent_volume_text_line.setValidator(self.validator_float)
            self.solvent_volume_text_line.setText('2')

            self.volume_of_finishing_label = QLabel('Объем доводки тех водой')
            self.volume_of_finishing_line = QLineEdit(self)
            self.volume_of_finishing_line.setValidator(self.validator_float)

            self.volume_flush_label = QLabel('Объем промывки')
            self.volume_flush_line = QLineEdit(self)
            self.volume_flush_line.setValidator(self.validator_float)

            self.solvent_volume_time_begin_label = QLabel('начало работ')
            self.solvent_volume_time_begin_date = QDateTimeEdit(self)
            self.solvent_volume_time_begin_date.setDisplayFormat("dd.MM.yyyy HH:mm")
            self.solvent_volume_time_begin_date.setDateTime(self.date_work_str)

            self.solvent_volume_time_end_label = QLabel('Окончание работ')
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

    def update_complications_during_disassembly(self, index):
        if index == 'Нет':
            self.complications_during_disassembly_q_label.setParent(None)
            self.complications_during_disassembly_q_line.setParent(None)
            self.complications_during_disassembly_time_label.setParent(None)
            self.complications_during_disassembly_time_line.setParent(None)
            self.complications_during_disassembly_q_time_begin_label.setParent(None)
            self.complications_during_disassembly_q_time_begin_date.setParent(None)
            self.complications_during_disassembly_q_time_end_label.setParent(None)
            self.complications_during_disassembly_q_time_end_date.setParent(None)

        else:
            self.complications_during_disassembly_q_label = QLabel('Текст осложнения')
            self.complications_during_disassembly_q_line = QLineEdit(self)

            self.complications_during_disassembly_q_time_begin_label = QLabel('начало осложнения')
            self.complications_during_disassembly_q_time_begin_date = QDateTimeEdit(self)
            self.complications_during_disassembly_q_time_begin_date.setDisplayFormat("dd.MM.yyyy HH:mm")
            self.complications_during_disassembly_q_time_begin_date.setDateTime(self.date_work_str)

            self.complications_during_disassembly_q_time_end_label = QLabel('Окончание осложнения')
            self.complications_during_disassembly_q_time_end_date = QDateTimeEdit(self)
            self.complications_during_disassembly_q_time_end_date.setDisplayFormat("dd.MM.yyyy HH:mm")
            self.complications_during_disassembly_q_time_end_date.setDateTime(self.date_work_str)

            self.complications_during_disassembly_time_label = QLabel('затраченное время')
            self.complications_during_disassembly_time_line = QLineEdit(self)

            self.complications_during_disassembly_time_line.setValidator(self.validator_float)
            self.grid.addWidget(self.complications_during_disassembly_q_label, 48, 2)
            self.grid.addWidget(self.complications_during_disassembly_q_line, 49, 2)

            self.grid.addWidget(self.complications_during_disassembly_q_time_begin_label, 48, 3)
            self.grid.addWidget(self.complications_during_disassembly_q_time_begin_date, 49, 3)

            self.grid.addWidget(self.complications_during_disassembly_q_time_begin_label, 48, 4)
            self.grid.addWidget(self.complications_during_disassembly_q_time_end_date, 49, 4)

            self.grid.addWidget(self.complications_during_disassembly_time_label, 48, 5)
            self.grid.addWidget(self.complications_during_disassembly_time_line, 49, 5)

            self.complications_during_disassembly_q_time_end_date.dateTimeChanged.connect(
                self.update_date_during_disassembly_q)
            self.complications_during_disassembly_q_time_begin_date.dateTimeChanged.connect(
                self.update_date_during_disassembly_q)

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

    def update_need_well_discharge_combo(self, index):

        if index == 'Нет':
            self.need_well_discharge_more_label.setParent(None)
            self.need_well_discharge_more_combo.setParent(None)

            self.cause_discharge_label.setParent(None)
            self.cause_discharge_combo.setParent(None)

            self.time_well_discharge_label.setParent(None)
            self.time_well_discharge_line.setParent(None)

            self.volume_well_discharge_label.setParent(None)
            self.volume_well_discharge_line.setParent(None)
            self.time_well_discharge_end_label.setParent(None)
            self.time_well_discharge_end_date.setParent(None)
            self.time_well_discharge_begin_label.setParent(None)
            self.time_well_discharge_begin_date.setParent(None)
        else:
            self.volume_well_discharge_label = QLabel('Объем разрядки')
            self.volume_well_discharge_line = QLineEdit(self)

            self.time_well_discharge_begin_label = QLabel('начало разрядки')
            self.time_well_discharge_begin_date = QDateTimeEdit(self)
            self.time_well_discharge_begin_date.setDisplayFormat("dd.MM.yyyy HH:mm")
            self.time_well_discharge_begin_date.setDateTime(self.date_work_str)

            self.time_well_discharge_end_label = QLabel('Окончание разрядки')
            self.time_well_discharge_end_date = QDateTimeEdit(self)
            self.time_well_discharge_end_date.setDisplayFormat("dd.MM.yyyy HH:mm")
            self.time_well_discharge_end_date.setDateTime(self.date_work_str)

            self.time_well_discharge_label = QLabel('Продолжительность разрядки')
            self.time_well_discharge_line = QLineEdit(self)
            self.time_well_discharge_line.setValidator(self.validator_float)

            self.need_well_discharge_more_label = QLabel('Была ли разрядка более 2ч')
            self.need_well_discharge_more_combo = QComboBox(self)
            self.need_well_discharge_more_combo.addItems(['Нет', 'Да'])

            self.cause_discharge_label = QLabel('Причина разрядки')
            self.cause_discharge_combo = QComboBox(self)
            self.cause_discharge_combo.addItems(cause_discharge_list)
            self.cause_discharge_combo.setCurrentIndex(1)

            self.grid.addWidget(self.volume_well_discharge_label, 16, 2)
            self.grid.addWidget(self.volume_well_discharge_line, 17, 2)
            self.grid.addWidget(self.time_well_discharge_begin_label, 16, 3)
            self.grid.addWidget(self.time_well_discharge_begin_date, 17, 3)
            self.grid.addWidget(self.time_well_discharge_end_label, 16, 4)
            self.grid.addWidget(self.time_well_discharge_end_date, 17, 4)
            self.grid.addWidget(self.time_well_discharge_label, 16, 5)
            self.grid.addWidget(self.time_well_discharge_line, 17, 5)
            self.grid.addWidget(self.cause_discharge_label, 16, 6)
            self.grid.addWidget(self.cause_discharge_combo, 17, 6)
            self.grid.addWidget(self.need_well_discharge_more_label, 18, 1)
            self.grid.addWidget(self.need_well_discharge_more_combo, 19, 1)

            self.need_well_discharge_more_combo.currentTextChanged.connect(self.update_need_well_discharge_more_combo)

            self.time_well_discharge_begin_date.dateTimeChanged.connect(
                self.update_time_well_discharge_time)
            self.time_well_discharge_end_date.dateTimeChanged.connect(
                self.update_time_well_discharge_time)

    def update_need_well_discharge_more_combo(self, index):
        if index == 'Нет':
            self.need_well_discharge_more_text_label.setParent(None)
            self.need_well_discharge_more_text_line.setParent(None)

            self.cause_discharge_more_label.setParent(None)
            self.cause_discharge_more_combo.setParent(None)

            self.cause_discharge_more_label.setParent(None)
            self.cause_discharge_more_combo.setParent(None)

        else:

            self.need_well_discharge_more_text_label = QLabel('Текст разрядки скважины')
            self.need_well_discharge_more_text_line = QLineEdit(self)
            self.need_well_discharge_more_text_line.setText(f'Разрядка скважины '
                                                            f'{self.volume_well_discharge_line.text()}м3')

            self.volume_well_discharge_more_label = QLabel('Объем разрядки')
            self.volume_well_discharge_more_line = QLineEdit(self)

            self.cause_discharge_more_label = QLabel('Причина разрядки')
            self.cause_discharge_more_combo = QComboBox(self)
            self.cause_discharge_more_combo.addItems(cause_discharge_list)

            self.grid.addWidget(self.need_well_discharge_more_text_label, 18, 2, 1, 2)
            self.grid.addWidget(self.need_well_discharge_more_text_line, 19, 2, 1, 2)

            self.grid.addWidget(self.cause_discharge_more_label, 18, 4)
            self.grid.addWidget(self.cause_discharge_more_combo, 19, 4)

    def update_need_well_discharge_more_after_combo(self, index):
        if index == 'Нет':
            self.need_well_discharge_more_text_after_label.setParent(None)
            self.need_well_discharge_more_text_after_line.setParent(None)

            self.cause_discharge_more_after_label.setParent(None)
            self.cause_discharge_more_after_combo.setParent(None)

            self.cause_discharge_more_after_label.setParent(None)
            self.cause_discharge_more_after_combo.setParent(None)

        else:

            self.need_well_discharge_more_text_after_label = QLabel('Текст разрядки скважины')
            self.need_well_discharge_more_text_after_line = QLineEdit(self)
            self.need_well_discharge_more_text_after_line.setText(f'Разрядка скважины '
                                                                  f'{self.volume_well_discharge_after_line.text()}м3')

            self.volume_well_discharge_more_after_label = QLabel('Объем разрядки')
            self.volume_well_discharge_more_after_line = QLineEdit(self)

            self.cause_discharge_more_after_label = QLabel('Причина разрядки')
            self.cause_discharge_more_after_combo = QComboBox(self)
            self.cause_discharge_more_after_combo.addItems(cause_discharge_list)

            self.grid.addWidget(self.need_well_discharge_more_text_after_label, 38, 2, 1, 2)
            self.grid.addWidget(self.need_well_discharge_more_text_after_line, 39, 2, 1, 2)

            self.grid.addWidget(self.cause_discharge_more_after_label, 38, 4)
            self.grid.addWidget(self.cause_discharge_more_after_combo, 39, 4)

    def update_need_well_discharge_after_combo(self, index):
        if index == 'Нет':
            self.need_well_discharge_more_after_label.setParent(None)
            self.need_well_discharge_more_after_combo.setParent(None)

            self.cause_discharge_after_label.setParent(None)
            self.cause_discharge_after_combo.setParent(None)

            self.time_well_discharge_after_label.setParent(None)
            self.time_well_discharge_after_line.setParent(None)

            self.volume_well_discharge_after_label.setParent(None)
            self.volume_well_discharge_after_line.setParent(None)
            self.time_well_discharge_end_after_label.setParent(None)
            self.time_well_discharge_end_after_date.setParent(None)
            self.time_well_discharge_begin_after_label.setParent(None)
            self.time_well_discharge_begin_after_date.setParent(None)
        else:
            self.volume_well_discharge_after_label = QLabel('Объем разрядки')
            self.volume_well_discharge_after_line = QLineEdit(self)

            self.time_well_discharge_begin_after_label = QLabel('начало разрядки')
            self.time_well_discharge_begin_after_date = QDateTimeEdit(self)
            self.time_well_discharge_begin_after_date.setDisplayFormat("dd.MM.yyyy HH:mm")
            self.time_well_discharge_begin_after_date.setDateTime(self.date_work_str)

            self.time_well_discharge_end_after_label = QLabel('Окончание разрядки')
            self.time_well_discharge_end_after_date = QDateTimeEdit(self)
            self.time_well_discharge_end_after_date.setDisplayFormat("dd.MM.yyyy HH:mm")
            self.time_well_discharge_end_after_date.setDateTime(self.date_work_str)

            self.time_well_discharge_after_label = QLabel('Продолжительность разрядки')
            self.time_well_discharge_after_line = QLineEdit(self)
            self.time_well_discharge_after_line.setValidator(self.validator_float)

            self.need_well_discharge_more_after_label = QLabel('Была ли разрядка более 2ч')
            self.need_well_discharge_more_after_combo = QComboBox(self)
            self.need_well_discharge_more_after_combo.addItems(['Нет', 'Да'])

            self.cause_discharge_after_label = QLabel('Причина разрядки')
            self.cause_discharge_after_combo = QComboBox(self)
            self.cause_discharge_after_combo.addItems(cause_discharge_list)
            self.cause_discharge_after_combo.setCurrentIndex(1)

            self.grid.addWidget(self.volume_well_discharge_after_label, 26, 2)
            self.grid.addWidget(self.volume_well_discharge_after_line, 27, 2)
            self.grid.addWidget(self.time_well_discharge_begin_after_label, 26, 3)
            self.grid.addWidget(self.time_well_discharge_begin_after_date, 27, 3)
            self.grid.addWidget(self.time_well_discharge_end_after_label, 26, 4)
            self.grid.addWidget(self.time_well_discharge_end_after_date, 27, 4)
            self.grid.addWidget(self.time_well_discharge_after_label, 26, 5)
            self.grid.addWidget(self.time_well_discharge_after_line, 27, 5)
            self.grid.addWidget(self.cause_discharge_after_label, 26, 6)
            self.grid.addWidget(self.cause_discharge_after_combo, 27, 6)
            self.grid.addWidget(self.need_well_discharge_more_after_label, 38, 1)
            self.grid.addWidget(self.need_well_discharge_more_after_combo, 39, 1)

            self.need_well_discharge_more_after_combo.currentTextChanged.connect(
                self.update_need_well_discharge_more_after_combo)

            self.time_well_discharge_begin_after_date.dateTimeChanged.connect(
                self.update_time_well_discharge_after_time)
            self.time_well_discharge_end_after_date.dateTimeChanged.connect(
                self.update_time_well_discharge_after_time)

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

        self.grid.addWidget(self.nkt_is_same_label, 80, 1)
        self.grid.addWidget(self.nkt_is_same_combo, 81, 1)

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

        self.pressuar_ek_combo.currentTextChanged.connect(self.update_pressuar_combo)

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

        self.equipment_audit_label = QLabel('Была ли ревизия')
        self.equipment_audit_combo = QComboBox(self)
        self.equipment_audit_combo.addItems(['Нет', 'Да'])

        self.grid.addWidget(self.equipment_audit_label, 94, 1)
        self.grid.addWidget(self.equipment_audit_combo, 95, 1)
        self.equipment_audit_combo.currentTextChanged.connect(self.update_equipment_audit_combo)

    def update_pressuar_combo(self, index):
        if index == 'Нет':
            self.depth_paker_text_label.setParent(None)
            self.depth_paker_text_edit.setParent(None)

            self.pressuar_ek_label.setParent(None)
            self.pressuar_ek_line.setParent(None)

            self.rezult_pressuar_combo_label.setParent(None)
            self.rezult_pressuar_combo.setParent(None)
        else:
            self.depth_paker_text_edit = QLineEdit(self)
            if self.gno_combo.currentText() not in ['ЭЦН', 'ЗО']:
                self.depth_paker_text_edit.setValidator(self.validator_int)

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
            self.depth_paker_text_edit.setValidator(self.validator_int)

            self.pressuar_ek_line = QLineEdit(self)
            self.pressuar_ek_line.setValidator(self.validator_float)

            self.rezult_pressuar_combo = QComboBox(self)
            self.rezult_pressuar_combo.addItems(['+', '-'])

            self.grid.addWidget(self.depth_paker_text_label, 66, 1)
            self.grid.addWidget(self.depth_paker_text_edit, 67, 1)

            self.grid.addWidget(self.pressuar_ek_label, 66, 2)
            self.grid.addWidget(self.pressuar_ek_line, 67, 2)
            self.grid.addWidget(self.rezult_pressuar_combo_label, 66, 3)
            self.grid.addWidget(self.rezult_pressuar_combo, 67, 3)

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

            self.grid.addWidget(self.nkt_48_lenght_up_label, 82, 2)
            self.grid.addWidget(self.nkt_48_lenght_up_edit, 83, 2)

            self.grid.addWidget(self.nkt_48_count_up_label, 84, 2)
            self.grid.addWidget(self.nkt_48_count_up_edit, 85, 2)

            self.grid.addWidget(self.nkt_60_lenght_up_label, 82, 3)
            self.grid.addWidget(self.nkt_60_lenght_up_edit, 83, 3)

            self.grid.addWidget(self.nkt_60_count_up_label, 84, 3)
            self.grid.addWidget(self.nkt_60_count_up_edit, 85, 3)

            self.grid.addWidget(self.nkt_73_lenght_up_label, 82, 4)
            self.grid.addWidget(self.nkt_73_lenght_up_edit, 83, 4)

            self.grid.addWidget(self.nkt_73_count_up_label, 84, 4)
            self.grid.addWidget(self.nkt_73_count_up_edit, 85, 4)

            self.grid.addWidget(self.nkt_89_lenght_up_label, 82, 5)
            self.grid.addWidget(self.nkt_89_lenght_up_edit, 83, 5)

            self.grid.addWidget(self.nkt_89_count_up_label, 84, 5)
            self.grid.addWidget(self.nkt_89_count_up_edit, 85, 5)

    def update_pressuar_tnkt_combo(self, index):

        if index == 'Нет':
            self.pressuar_tnkt_text_label.setParent(None)
            self.pressuar_tnkt_text_line.setParent(None)
        else:
            self.pressuar_tnkt_text_label = QLabel('Текст опрессовки')
            self.pressuar_tnkt_text_line = QLineEdit(self)

            self.grid.addWidget(self.pressuar_tnkt_text_label, 50, 2)
            self.grid.addWidget(self.pressuar_tnkt_text_line, 51, 2)

    # def update_solvent_injection_combo(self, index):
    #
    #     if index == 'Нет':
    #         self.solvent_volume_text_label.setParent(None)
    #         self.solvent_volume_text_line.setParent(None)
    #         self.solvent_volume_time_label.setParent(None)
    #         self.solvent_volume_time_line.setParent(None)
    #         self.solvent_volume_time_end_label.setParent(None)
    #         self.solvent_volume_time_end_date.setParent(None)
    #         self.solvent_volume_time_begin_label.setParent(None)
    #         self.solvent_volume_time_begin_date.setParent(None)
    #         self.volume_of_finishing_label.setParent(None)
    #
    #
    #     else:
    #         self.solvent_volume_text_label = QLabel(self)
    #         self.solvent_volume_text_line = QLineEdit(self)
    #         self.solvent_volume_text_line.setValidator(self.validator_float)
    #         self.solvent_volume_text_line.setText('2')
    #
    #         self.volume_of_finishing_label = QLabel('Объем доводки тех водой')
    #         self.volume_of_finishing_line = QLineEdit(self)
    #         self.volume_of_finishing_line.setValidator(self.validator_float)
    #
    #         # self.volume_flush_label = QLabel('Объем промывки')
    #         # self.volume_flush_line = QLineEdit(self)
    #         # self.volume_flush_line.setValidator(self.validator_float)
    #
    #         self.solvent_volume_time_begin_label = QLabel('начало закачки')
    #         self.solvent_volume_time_begin_date = QDateTimeEdit(self)
    #         self.solvent_volume_time_begin_date.setDisplayFormat("dd.MM.yyyy HH:mm")
    #         self.solvent_volume_time_begin_date.setDateTime(self.date_work_str)
    #
    #         self.solvent_volume_time_end_label = QLabel('Окончание закачки')
    #         self.solvent_volume_time_end_date = QDateTimeEdit(self)
    #         self.solvent_volume_time_end_date.setDisplayFormat("dd.MM.yyyy HH:mm")
    #         self.solvent_volume_time_end_date.setDateTime(self.date_work_str)
    #
    #         self.solvent_volume_time_label = QLabel('затраченное время')
    #         self.solvent_volume_time_line = QLineEdit(self)
    #         self.solvent_volume_time_line.setValidator(self.validator_float)
    #
    #         self.grid.addWidget(self.solvent_volume_text_label, 32, 2)
    #         self.grid.addWidget(self.solvent_volume_text_line, 33, 2)
    #         self.grid.addWidget(self.volume_of_finishing_label, 32, 3)
    #         self.grid.addWidget(self.volume_of_finishing_line, 33, 3)
    #         # self.grid.addWidget(self.volume_flush_label, 32, 4)
    #         # self.grid.addWidget(self.volume_flush_line, 33, 4)
    #         self.grid.addWidget(self.solvent_volume_time_begin_label, 32, 5)
    #         self.grid.addWidget(self.solvent_volume_time_begin_date, 33, 5)
    #         self.grid.addWidget(self.solvent_volume_time_end_label, 32, 6)
    #         self.grid.addWidget(self.solvent_volume_time_end_date, 33, 6)
    #         self.grid.addWidget(self.solvent_volume_time_label, 32, 7)
    #         self.grid.addWidget(self.solvent_volume_time_line, 33, 7)
    #
    #         self.solvent_volume_time_end_date.dateTimeChanged.connect(
    #             self.update_date_solvent_volume)
    #         self.solvent_volume_time_begin_date.dateTimeChanged.connect(
    #             self.update_date_solvent_volume)

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
            self.type_combo_work.addItems(['', 'Крезол', 'Сваб',
                                           'РИР 2С', 'ГРП', 'РГД', 'Огневые, земляные работы'])

            self.grid.addWidget(self.type_combo_work_label, 52, 2)
            self.grid.addWidget(self.type_combo_work, 53, 2)

            # self.type_combo_work.currentTextChanged.connect(self.update_type_combo_work)
            self.type_combo_work.currentTextChanged.connect(self.extra_work)

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

            self.grid.addWidget(self.count_nkt_combo_label, 67, 1)
            self.grid.addWidget(self.count_nkt_combo, 68, 1)

            self.count_nkt_combo.currentTextChanged.connect(self.update_count_nkt_combo)

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

            self.grid.addWidget(self.saturation_volume_sko_label, 90, 4)
            self.grid.addWidget(self.saturation_volume_sko_line, 91, 4)
            self.grid.addWidget(self.determination_of_pickup_sko_text_label, 90, 5)
            self.grid.addWidget(self.determination_of_pickup_sko_text_line, 91, 5)

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

    def update_ovtr_work_combo(self, index):
        if index == 'Нет':

            self.ovtr_work_text_label.setParent(None)
            self.ovtr_work_text_line.setParent(None)

            self.ovtr_work_time_begin_label.setParent(None)
            self.ovtr_work_time_begin_date.setParent(None)

            self.ovtr_work_time_end_label.setParent(None)
            self.ovtr_work_time_end_date.setParent(None)

            self.ovtr_work_time_line_label.setParent(None)
            self.ovtr_work_time_line.setParent(None)

        else:

            self.ovtr_work_text_line = QLineEdit(self)
            self.ovtr_work_text_line.setText('Интерпретация данных ГИС')
            # self.ovtr_work_text_line.setText('Реагирование')

            self.ovtr_work_time_begin_date = QDateTimeEdit(self)
            self.ovtr_work_time_begin_date.setDisplayFormat("dd.MM.yyyy HH:mm")
            self.ovtr_work_time_begin_date.setDateTime(self.date_work_str)

            self.ovtr_work_time_end_date = QDateTimeEdit(self)
            self.ovtr_work_time_end_date.setDisplayFormat("dd.MM.yyyy HH:mm")
            self.ovtr_work_time_end_date.setDateTime(self.date_work_str)

            self.ovtr_work_time_line_label = QLabel('Затраченное время')
            self.ovtr_work_time_line = QLineEdit(self)

            self.grid.addWidget(self.ovtr_work_text_label, 50, 4)
            self.grid.addWidget(self.ovtr_work_text_line, 51, 4)

            self.grid.addWidget(self.ovtr_work_time_begin_label, 50, 5)
            self.grid.addWidget(self.ovtr_work_time_begin_date, 51, 5)

            self.grid.addWidget(self.ovtr_work_time_end_label, 50, 6)
            self.grid.addWidget(self.ovtr_work_time_end_date, 51, 6)

            self.grid.addWidget(self.ovtr_work_time_line_label, 50, 7)
            self.grid.addWidget(self.ovtr_work_time_line, 51, 7)

            self.ovtr_work_time_end_date.dateTimeChanged.connect(self.update_date_ovtr_work)
            self.ovtr_work_time_begin_date.dateTimeChanged.connect(
                self.update_date_ovtr_work)
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

            self.response_text_line = QLineEdit(self)
            # self.response_text_line.setText('Реагирование')

            self.response_time_begin_date = QDateTimeEdit(self)
            self.response_time_begin_date.setDisplayFormat("dd.MM.yyyy HH:mm")
            self.response_time_begin_date.setDateTime(self.date_work_str)

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

            self.grid.addWidget(self.equipment_audit_text_label, 94, 3)
            self.grid.addWidget(self.equipment_audit_text_line, 95, 3)

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

    def update_date_of_normalization(self):
        time_begin = self.normalization_question_time_begin_date.dateTime()
        time_end = self.normalization_question_time_end_date.dateTime()

        time_difference = self.calculate_date(time_begin, time_end)
        self.normalization_question_time_line.setText(str(time_difference))


class TemplateWork(MyWindow):
    def __init__(self, ins_ind, table_widget, parent=None):
        super(QMainWindow, self).__init__()

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
        self.dict_sucker_pod = {}
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

    def volume_after_sko_work_2(self):

        work_list = []
        if self.count_nkt_combo == 'Да':
            work_list.extend(self.descent_nkt_work())

            for index in range(len(work_list)):
                if index == 0:
                    work_list[index][12] = self.count_nkt_line * 10
                work_list[index][21] = self.count_nkt_line

        volume_list = [
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'Промывка', 'ПЗР при промывке скважины ', None, None,
             None, None, None, None, None, None, None, None, None, None, '§156,160р.1', None, 'шт', 1, 1, 1,
             '=V557*W557*X557', '=Y557-AA557-AB557-AC557-AD557', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'Промывка', 'Переход на обратную промывку', None, None,
             None, None, None, None, None, None, None, None, None, None, '§162разд.1', None, 'раз', 1, 0.15, 1,
             '=V558*W558*X558', '=Y558-AA558-AB558-AC558-AD558', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'Промывка',
             f'Промывка в объеме {self.volume_flush_line_sko_line}м3', None, None, None, None, None,
             None, None, None, None, None, None, None, '§300разд.1', None, 'м3',
             self.volume_flush_line_sko_line, 0.033, 1, '=V559*W559*X559',
             '=Y559-AA559-AB559-AC559-AD559', None, None, None, None, None]]

        work_list.extend(volume_list)

        return work_list

    def swabbing_work(self):
        work_list = [
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'Монтаж/демонтаж штангового превентора', None, None,
             None, None, None, None, None, None, None, None, None, None, '§120разд.1', None, 'шт', 1, 0.6, 1,
             '=V338*W338*X338', '=Y338-AA338-AB338-AC338-AD338', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'Поднести и установить на колонном фланце тройник ',
             None, None, None, None, None, None, None, None, None, None, None, None, '§278разд.1', None, 'шт', 1, 0.37,
             1, '=V339*W339*X339', '=Y339-AA339-AB339-AC339-AD339', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'Поднести и установить на колонном фланце задвижку',
             None, None, None, None, None, None, None, None, None, None, None, None, '§278разд.1', None, 'шт', 1, 0.37,
             1, '=V340*W340*X340', '=Y340-AA340-AB340-AC340-AD340', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'Монтаж выкидной линии', None, None, None, None,
             None, None, None, None, None, None, None, None, '§301разд.1', None, 'раз', 1, 0.3, 1, '=V341*W341*X341',
             '=Y341-AA341-AB341-AC341-AD341', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'ГИС', 'Свабирование',
             f'{self.extra_work_text_line} {self.extra_work_time_begin_date}-{self.extra_work_time_end_date}', None,
             None,
             None, None, None, None, 'Объем', self.volume_swabing_edit, 'АКТ№', None, None, None, 'Факт', None,
             'час', self.extra_work_time_line, 1, 1,
             '=V342*W342*X342', '=Y342-AA342-AB342-AC342-AD342', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'Демонтаж выкидной линии', None, None, None, None,
             None, None, None, None, None, None, None, None, '§301разд.1', None, 'раз', 1, 0.17, 1, '=V343*W343*X343',
             '=Y343-AA343-AB343-AC343-AD343', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
             'Демонтировать и отнести на колонном фланце тройник ', None, None, None, None, None, None, None, None,
             None, None, None, None, '§278разд.1', None, 'шт', 1, 0.35, 1, '=V344*W344*X344',
             '=Y344-AA344-AB344-AC344-AD344', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
             'Демонтировать и отнести на колонном фланце задвижку', None, None, None, None, None, None, None, None,
             None, None, None, None, '§278разд.1', None, 'шт', 1, 0.35, 1, '=V345*W345*X345',
             '=Y345-AA345-AB345-AC345-AD345', None, None, None, None, None]]
        return work_list

    def read_extra_work_question(self, current_widget):

        self.type_combo_work = current_widget.type_combo_work.currentText()
        read_data = self.read_extra_work(current_widget)
        if read_data is None:
            return
        if self.type_combo_work in ['Крезол', 'РИР 2С']:
            self.response_combo = current_widget.response_combo.currentText()
            if self.response_combo == 'Да':
                read_data = self.read_responce(current_widget)
                if read_data is None:
                    return
        if self.type_combo_work == 'Сваб':

            self.volume_swabing_edit = current_widget.volume_swabing_edit.text()
            if self.volume_swabing_edit == '':
                QMessageBox.warning(self, 'ошибка', 'Нужно ввести объем свабирования')
                return
        if self.type_combo_work in ['Крезол', 'Сваб', 'РИР 2С']:

            self.volume_flush_line_combo = current_widget.volume_flush_line_combo.currentText()
            if self.volume_flush_line_combo == 'Да':
                read_data = self.read_volume_flush_line(current_widget)
                if read_data is None:
                    return



                self.count_nkt_combo = current_widget.count_nkt_combo.currentText()
                if self.count_nkt_combo == 'Да':
                    read_data = self.read_count_nkt_combo(current_widget)
                    if read_data is None:
                        return
            self.pressuar_ek_combo = current_widget.pressuar_ek_combo.currentText()

        if self.type_combo_work in ['РИР 2С']:
            self.count_nkt_combo = current_widget.count_nkt_combo.currentText()
            if self.count_nkt_combo == 'Да':
                read_data = self.read_count_nkt_combo(current_widget)
                if read_data is None:
                    return

            self.determination_of_pickup_sko_combo = current_widget.determination_of_pickup_sko_combo.currentText()
            if self.determination_of_pickup_sko_combo == 'Да':
                read_data = self.read_determination_of_pickup_sko_combo(current_widget)
                if read_data is None:
                    return
        return True

    def read_extra_work(self, current_widget):
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
        return True

    def read_paker_combo(self, current_widget):
        self.depth_paker_text_edit = current_widget.depth_paker_text_edit.text()
        if self.depth_paker_text_edit not in ['', None]:
            self.depth_paker_text_edit = int(self.depth_paker_text_edit)
        else:
            question = QMessageBox.question(self, 'Глубина посадки', 'Не введена глубина посадки пакера ')
            if question == QMessageBox.StandardButton.No:
                return
        self.rezult_pressuar_combo = current_widget.rezult_pressuar_combo.currentText()
        self.pressuar_ek_line = current_widget.pressuar_ek_line.text()
        if self.pressuar_ek_line != '':
            self.pressuar_ek_line = int(self.pressuar_ek_line)
        else:
            question = QMessageBox.question(self, 'Давление', 'Не указано давление опрессовки?')
            if question == QMessageBox.StandardButton.No:
                return

        return True

    def read_fishing_works(self, current_widget):
        self.fishing_works_text_line = current_widget.fishing_works_line.text()
        self.fishing_works_time_begin_date = \
            current_widget.fishing_works_time_begin_date.dateTime().toPyDateTime()
        self.fishing_works_time_begin_date = \
            self.change_string_in_date(self.fishing_works_time_begin_date)

        self.fishing_works_time_end_date = \
            current_widget.fishing_works_time_end_date.dateTime().toPyDateTime()
        self.fishing_works_time_end_date = \
            self.change_string_in_date(self.fishing_works_time_end_date)

        if self.fishing_works_time_end_date == self.fishing_works_time_begin_date:
            QMessageBox.warning(self, 'Даты совпадают', 'Даты совпадают')
            return

        if self.fishing_works_text_line == '':
            QMessageBox.warning(self, 'Ошибка', f'Не введены текст осложнения при срыве ПШ')
            return

        self.fishing_works_time_line = current_widget.fishing_works_time_line.text()
        if self.fishing_works_time_line != '':
            self.fishing_works_time_line = round(float(self.fishing_works_time_line), 1)

        else:
            QMessageBox.warning(self, 'Ошибка', f'Не введены время осложнения при срыве ПШ')
            return

        if self.fishing_works_time_line <= 0:
            QMessageBox.warning(self, 'Ошибка', f'Затраченное время при срыве ПШ не может быть отрицательным')
            return
        return True

    def read_pressuar_combo(self, current_widget):
        self.depth_paker_text_edit = current_widget.depth_paker_text_edit.text()
        if self.depth_paker_text_edit not in ['', None]:
            self.depth_paker_text_edit = int(self.depth_paker_text_edit)
        else:
            question = QMessageBox.question(self, 'Глубина посадки', 'Не введена глубина посадки пакера')
            if question == QMessageBox.StandardButton.No:
                return
        self.pressuar_ek_line = current_widget.pressuar_ek_line.text()
        if self.pressuar_ek_line != '':
            self.pressuar_ek_line = int(self.pressuar_ek_line)
        else:
            question = QMessageBox.question(self, 'Давление', 'Не указано давление опрессовки?')
            if question == QMessageBox.StandardButton.No:
                return

        self.rezult_pressuar_combo = current_widget.rezult_pressuar_combo.currentText()

        return True

    def read_complications_of_failure_armatura(self, current_widget):
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
        return True

    def read_sucker_down(self, current_widget):
        self.sucker_pod_19_lenght_up_edit = current_widget.sucker_pod_19_lenght_up_edit.text()
        self.sucker_pod_19_count_up_edit = current_widget.sucker_pod_19_count_up_edit.text()

        self.sucker_pod_22_lenght_up_edit = current_widget.sucker_pod_22_lenght_up_edit.text()
        self.sucker_pod_22_count_up_edit = current_widget.sucker_pod_22_count_up_edit.text()

        self.sucker_pod_25_lenght_up_edit = current_widget.sucker_pod_25_lenght_up_edit.text()
        self.sucker_pod_25_count_up_edit = current_widget.sucker_pod_25_count_up_edit.text()

        if self.sucker_pod_19_lenght_up_edit != '' and self.sucker_pod_19_count_up_edit != '':
            self.dict_sucker_pod_up.setdefault(19,
                                               (int(float(self.sucker_pod_19_lenght_up_edit)),
                                                int(float(self.sucker_pod_19_count_up_edit))))
        if self.sucker_pod_22_lenght_up_edit != '' and self.sucker_pod_22_count_up_edit != '':
            self.dict_sucker_pod_up.setdefault(22,
                                               (int(float(self.sucker_pod_22_lenght_up_edit)),
                                                int(float(self.sucker_pod_22_count_up_edit))))
        if self.sucker_pod_25_lenght_up_edit != '' and self.sucker_pod_25_count_up_edit != '':
            self.dict_sucker_pod_up.setdefault(25,
                                               (int(float(self.sucker_pod_25_lenght_up_edit)),
                                                int(float(self.sucker_pod_25_count_up_edit))))

    def read_sucker_up(self, current_widget):

        self.sucker_pod_19_lenght_edit = current_widget.sucker_pod_19_lenght_edit.text()
        self.sucker_pod_19_count_edit = current_widget.sucker_pod_19_count_edit.text()

        self.sucker_pod_22_lenght_edit = current_widget.sucker_pod_22_lenght_edit.text()
        self.sucker_pod_22_count_edit = current_widget.sucker_pod_22_count_edit.text()

        self.sucker_pod_25_lenght_edit = current_widget.sucker_pod_25_lenght_edit.text()
        self.sucker_pod_25_count_edit = current_widget.sucker_pod_25_count_edit.text()

        if self.sucker_pod_19_lenght_edit != '' and self.sucker_pod_19_count_edit != '':
            self.dict_sucker_pod.setdefault(19,
                                            (int(float(self.sucker_pod_19_lenght_edit)),
                                             int(float(self.sucker_pod_19_count_edit))))
        if self.sucker_pod_22_lenght_edit != '' and self.sucker_pod_22_count_edit != '':
            self.dict_sucker_pod.setdefault(22,
                                            (int(float(self.sucker_pod_22_lenght_edit)),
                                             int(float(self.sucker_pod_22_count_edit))))
        if self.sucker_pod_25_lenght_edit != '' and self.sucker_pod_25_count_edit != '':
            self.dict_sucker_pod.setdefault(25,
                                            (int(float(self.sucker_pod_25_lenght_edit)),
                                             int(float(self.sucker_pod_25_count_edit))))

        return True

    def lifting_nkt(self):
        work_list = []
        middle_nkt = '9.6-10.5'
        count_nkt = 0
        for nkt_key, nkt_value in self.dict_nkt_up.items():
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

            max_count_3 = LIFTING_NORM_NKT[well_data.lifting_unit_combo][nkt_key]['III'][middle_nkt][1]
            koef_norm_3 = LIFTING_NORM_NKT[well_data.lifting_unit_combo][nkt_key]['III'][middle_nkt][0]
            razdel_3 = LIFTING_NORM_NKT[well_data.lifting_unit_combo][nkt_key]['III']['раздел']

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
                             'Подъем НКТ  3 скорость',
                             None, None, None, None, nkt_key, lenght_nkt_3, middle_nkt, max_count_3,
                             None, None, None, None, razdel_3, None, 'шт', nkt_count_3, koef_norm_3,
                             self.coefficient_lifting, '=V202*W202*X202', '=Y202-AA202-AB202-AC202-AD202',
                             None, None, None, None, None]

            work_list.append(podien_3_list)

            nkt_count -= max_count_3

            if nkt_count > 0:
                max_count_2 = LIFTING_NORM_NKT[well_data.lifting_unit_combo][nkt_key]['II'][middle_nkt][1]
                koef_norm_2 = LIFTING_NORM_NKT[well_data.lifting_unit_combo][nkt_key]['II'][middle_nkt][0]
                razdel_2 = LIFTING_NORM_NKT[well_data.lifting_unit_combo][nkt_key]['II']['раздел']
                if max_count_2 > nkt_count:
                    nkt_count_2 = nkt_count
                else:
                    nkt_count_2 = max_count_2
                lenght_nkt_2 = int(middle_nkt_value * nkt_count_2)
                podiem_list_2 = ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', self.type_equipment,
                                 'Подъем НКТ  2 скорость',
                                 None, None, None, None, nkt_key, lenght_nkt_2, middle_nkt, max_count_2,
                                 None, None, None, None, razdel_2, None, 'шт', nkt_count_2, koef_norm_2,
                                 self.coefficient_lifting, '=V202*W202*X202', '=Y202-AA202-AB202-AC202-AD202', None,
                                 None, None, None, None]
                nkt_count -= max_count_2
                work_list.insert(1, podiem_list_2)

            if nkt_count > 0:
                max_count_1 = LIFTING_NORM_NKT[well_data.lifting_unit_combo][nkt_key]['I'][middle_nkt][1]
                koef_norm_1 = LIFTING_NORM_NKT[well_data.lifting_unit_combo][nkt_key]['I'][middle_nkt][0]
                razdel_1 = LIFTING_NORM_NKT[well_data.lifting_unit_combo][nkt_key]['I']['раздел']

                lenght_nkt_1 = int(middle_nkt_value * nkt_count)
                podiem_list_1 = [
                    '=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', self.type_equipment,
                    'Подъем НКТ  1 скорость',
                    None, None, None, None, nkt_key, lenght_nkt_1, middle_nkt, max_count_1,
                    None, None, None, None, razdel_1, None, 'шт', nkt_count, koef_norm_1,
                    self.coefficient_lifting, '=V202*W202*X202', '=Y202-AA202-AB202-AC202-AD202', None, None, None,
                    None, None]
                nkt_count -= max_count_1
                work_list.insert(1, podiem_list_1)

        nkt_sum = sum(list(map(lambda x: x[1], self.dict_nkt_up.values())))

        if self.complications_when_lifting_combo == 'Да':
            work_list.extend(self.complications_when_lifting_work)


        if nkt_sum > 201:
            work_list.extend([['=ROW()-ROW($A$46)', 'подъем НКТ', None, 'спо', self.type_equipment,
                               'Откатывание труб с 201 трубы ',
                               None, None, None,
                               None, None, None, None, None, None, None, None, None, '§40разд.1', None, 'шт',
                               nkt_sum - 201, 0.008, 1,
                               '=V208*W208*X208', '=Y208-AA208-AB208-AC208-AD208', None, None, None, None, None]])

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

        return work_list

    def ovtr_work(self):
        work_list = [
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
             f'{self.ovtr_work_text_line} ({self.ovtr_work_time_begin_date}-{self.ovtr_work_time_begin_date})', None,
             None, None, None, None, None,
             None, None, None, None, None, None, 'Простои', 'Тех. ожидание', 'час', self.ovtr_work_time_line, 1, 1,
             '=V389*W389*X389',
             '=Y389-AA389-AB389-AC389-AD389', None, None, None, None, None]]
        return work_list

    def complications_when_lifting_work(self):

        nkt_sum =  nkt_sum = sum(list(map(lambda x: x[1], self.dict_nkt_up.values())))
        work_list = [
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', self.type_equipment,
                 f'{self.complications_when_lifting_text_line} '
                 f'{self.complications_when_lifting_time_begin_date}'
                 f'{self.complications_when_lifting_time_end_date}',
                 None, None, None, None, None,
                 None, 'Объем', 0, None, None, None, None, 'факт', None,
                 'час', self.complications_when_lifting_time_end_date, 1, 1, '=V206*W206*X206',
                 '=Y206-AA206-AB206-AC206-AD206', None, None, None, None, None]]
        if 'псю' in self.complications_when_lifting_text_line.lower():
            work_list.extend([
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'М/ж и д/ж ПСЮ', None, None,
                 None, None,
                 None, None, None, None, None, None, None, None, '§98,99разд.1 ', None,
                 'раз', 1, 0.21666666666666667, 1, '=V363*W363*X363', '=Y363-AA363-AB363-AC363-AD363', None,
                 None, None, None, None],
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
                 'Крепление и открепление приспособления на трубу и слив техн.жидкости',
                 None, None, None, None, None, None, None, None, None, None, None, None,
                 ' §98 разд.1 ', None, 'шт', nkt_sum, 0.03, 1, '=V364*W364*X364',
                 '=Y364-AA364-AB364-AC364-AD364', None, None, None, None, None]]
            )
        return work_list
    def deinstallation_of_washing_equipment(self):
        work_list = [
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'Д/ж спайдера', None, None, None,
             None,
             None, None, None, None, None, None, None, None, '§185разд.1', None, 'час', 1, 0.07, 1,
             '=V469*W469*X469', '=Y469-AA469-AB469-AC469-AD469', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'Демонтаж КГОМ', None, None, None,
             None,
             None, None, None, None, None, None, None, None, '§301разд.1', None, 'час', 1, 0.17, 1,
             '=V470*W470*X470', '=Y470-AA470-AB470-AC470-AD470', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'М/ж спайдера', None, None, None,
             None,
             None, None, None, None, None, None, None, None, '§185разд.1', None, 'час', 1, 0.07, 1,
             '=V471*W471*X471', '=Y471-AA471-AB471-AC471-AD471', None, None, None, None, None]]
        return work_list

    def installation_of_washing_equipment(self):
        work_list = [
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'Д/ж спайдера', None, None, None,
             None,
             None, None, None, None, None, None, None, None, '§185разд.1', None, 'час', 1, 0.07, 1,
             '=V453*W453*X453', '=Y453-AA453-AB453-AC453-AD453', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'Монтаж КГОМ', None, None, None,
             None,
             None, None, None, None, None, None, None, None, '§301разд.1', None, 'час', '=SUM(V453)', 0.17, 1,
             '=V454*W454*X454', '=Y454-AA454-AB454-AC454-AD454', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'М/ж спайдера', None, None, None,
             None,
             None, None, None, None, None, None, None, None, '§185разд.1', None, 'час', 1, 0.07, 1,
             '=V455*W455*X455', '=Y455-AA455-AB455-AC455-AD455', None, None, None, None, None]]
        return work_list

    def read_complications_during_tubing_running_combo(self, current_widget):
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
        return True

    def read_complications_during_disassembly_combo(self, current_widget):

        self.complications_during_disassembly_q_line = current_widget.complications_during_disassembly_q_line.text()

        self.complications_during_disassembly_q_time_begin_date = \
            current_widget.complications_during_disassembly_q_time_begin_date.dateTime().toPyDateTime()
        self.complications_during_disassembly_q_time_begin_date = \
            self.change_string_in_date(self.complications_during_disassembly_q_time_begin_date)

        self.complications_during_disassembly_q_time_end_date = \
            current_widget.complications_during_disassembly_q_time_end_date.dateTime().toPyDateTime()
        self.complications_during_disassembly_q_time_end_date = \
            self.change_string_in_date(self.complications_during_disassembly_q_time_end_date)

        if self.complications_during_disassembly_q_time_end_date == \
                self.complications_during_disassembly_q_time_begin_date:
            QMessageBox.warning(self, 'Даты совпадают', 'Даты совпадают')
            return

        if self.complications_during_disassembly_q_line == '':
            QMessageBox.warning(self, 'Ошибка', f'Не введены текст осложнения при демонтаже ПШ ')
            return

        self.complications_during_disassembly_time_line = \
            current_widget.complications_during_disassembly_time_line.text()

        if self.complications_during_disassembly_time_line != '':
            self.complications_during_disassembly_time_line = round(
                float(self.complications_during_disassembly_time_line), 1)
        else:
            QMessageBox.warning(self, 'Ошибка', f'Не введены время при демонтаже ПШ ')

        if self.complications_during_disassembly_time_line <= 0:
            QMessageBox.warning(self, 'Ошибка', f'Затраченное время при демонтаже ПШ не может быть отрицательным')
            return
        return True

    def read_complications_of_failure(self, current_widget):
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
        return True

    def read_complications_when_lifting(self, current_widget):
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
        return True

    def update_data_in_ois(self):

        # Заполнение QTableWidget данными из списка
        for datа_in in well_data.work_list_in_ois[1:]:
            date_in_work = datа_in[0]
            day, month, year = list(map(int, date_in_work.split('\n')[0].split('.')))
            day1, month1, year1 = list(map(int, well_data.date_work.split('.')))
            input_date = QDate(year1, month1, day1 + 7)
            comparison_date = QDate(year, month, day)
            if input_date >= comparison_date:
                row_position = self.tableWidget.rowCount()
                self.tableWidget.insertRow(row_position)
                self.tableWidget.setItem(row_position, 0, QTableWidgetItem(datа_in[0]))

                # Создание QTextEdit для переноса текста в ячейке
                text_edit = QTextEdit()
                text_edit.setText(datа_in[1])
                text_edit.setReadOnly(True)  # Сделаем текст редактируемым только для чтения

                self.tableWidget.setCellWidget(row_position, 1, text_edit)

                # Устанавливаем высоту строки в зависимости от текста
                self.adjustRowHeight(row_position, text_edit.toPlainText())
                # Устанавливаем высоту строки в зависимости от текста
                self.adjustRowHeight(row_position, datа_in[1])

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

    def presence_of_downtime_def(self):

        technological_downtime_list = [[
            '=ROW()-ROW($A$46)', self.date_work_line, None, 'простои',
            f'{self.cause_presence_of_downtime_combo} '
            f'{self.presence_of_downtime_time_begin_date}-{self.presence_of_downtime_time_end_date}',
            f'{self.presence_of_downtime_text_line}',
            None, None,
            None, None, 'классификация простоя', None, self.cause_presence_of_downtime_classification_combo,
            None, None, None, None, None, 'Простои', self.tehnological_operation_combo, 'час',
            self.presence_of_downtime_time_line, 1, 1, '=V66*W66*X66',
            '=Y66-AA66-AB66-AC66-AD66', None, None, None, None, None]]

        return technological_downtime_list

    def solvent_injection_work(self):
        work_list = [
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'ОПЗ', 'Подготовительные работы, выполняемые ', None,
             None, None, 'ПО ТКРС', None, None, 'перед началом работ на скважине', None, None, 'РАСТВОРИТЕЛЬ',
             'Растворитель АСПО Реком 7125 серия 4, КР-4Р', None, '§227,229разд.1', None, 'шт', 1, 0.96, 1,
             '=V589*W589*X589', '=Y589-AA589-AB589-AC589-AD589', None, None, None, None, None]]
        if self.solvent_volume_text_line > 1:
            solvent_volume_list = [
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'ОПЗ', f'Закачка растворителя первого 1м3',
                 None, None, None, None, None, None, None, None, 'АКТ№', None, None, None, '§228разд.1', None, 'м3', 1,
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
                 None, None, None, None, None, None, None, 'АКТ№', None, None, None, '§228разд.1', None, 'м3', 1, 0.2,
                 1, '=V590*W590*X590', '=Y590-AA590-AB590-AC590-AD590', None, None, None, None, None],
            ]

        work_list.extend(solvent_volume_list)

        volume_list = [
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'ОПЗ',
             f'Доводка растворителя в объеме {self.volume_of_finishing_line}', None, None, None, None,
             None, None, None, None, None, None, None, None, '§228разд.1', None, 'м3', self.volume_of_finishing_line,
             0.033, 1, '=V592*W592*X592',
             '=Y592-AA592-AB592-AC592-AD592', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'ОПЗ',
             f'Реагирование {self.solvent_volume_time_begin_date}-{self.solvent_volume_time_end_date}', None, None,
             None,
             None,
             None, None, None, None, 'АКТ№', None, None, None, 'простои', 'Тех. ожидание', 'час',
             self.solvent_volume_time_line, 1, 1,
             '=V593*W593*X593', '=Y593-AA593-AB593-AC593-AD593', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'Промывка', 'Переход на труб.простр.', None, None,
             None,
             None, None, None, None, None, None, None, None, None, '§162разд.1', None, 'раз', 1, 0.15, 1,
             '=V594*W594*X594', '=Y594-AA594-AB594-AC594-AD594', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'Промывка', f'Промывка в объеме {self.volume_flush_line}',
             None, None, None, None, None, None, None, None, 'АКТ№', None, None, None, '§301разд.1', None, 'м3',
             {self.volume_flush_line}, 0.033, 1, '=V595*W595*X595',
             '=Y595-AA595-AB595-AC595-AD595', None, None, None, None, None]]

        work_list.extend(volume_list)
        return work_list

    def read_pressuar_combo(self, current_widget):

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
        return True

    def read_determination_of_pickup_combo(self, current_widget):

        self.saturation_volume_line = current_widget.saturation_volume_line.text()
        if self.saturation_volume_line == '':
            QMessageBox.warning(self, 'Объем насыщения', 'Не введен объем насыщения ')
            return

        self.determination_of_pickup_text = current_widget.determination_of_pickup_text.text()
        if self.determination_of_pickup_text == '':
            QMessageBox.warning(self, 'Объем насыщения', 'Не введен текст определения Q')
            return
        return True

    def pressuar_work_end(self):
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
            determination_of_pickup_list = self.determination_of_pickup_work(
                self.saturation_volume_line, self.determination_of_pickup_text)
            work_list.extend(determination_of_pickup_list)



        return work_list

    def read_pressuar_zumpf(self, current_widget):

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
        return True

    def dovodka(self, time_skv_norm):
        work_list = []
        sum_nkt = sum(list(map(lambda x: x[0], list(self.dict_nkt.values()))))
        norm_nkt = round(0.34 + (sum_nkt - 200) / 200 * 0.02, 2)
        nkt_list = [
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'ОПЗ', 'Доводка тех.водой', None, None,
             None, None,
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
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'Промывка', 'ПЗР при промывке скважины ',
             None, None,
             None, None, None, None, None, None, None, None, None, None, '§156,160р.1', None, 'шт', 1, 1, 1,
             '=V557*W557*X557', '=Y557-AA557-AB557-AC557-AD557', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'Промывка', 'Переход на обратную промывку',
             None, None,
             None, None, None, None, None, None, None, None, None, None, '§162разд.1', None, 'раз', 1, 0.15, 1,
             '=V558*W558*X558', '=Y558-AA558-AB558-AC558-AD558', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'Промывка',
             f'Промывка в объеме {self.volume_flush_line_sko_line}м3', None, None, None, None, None,
             None, None, None, None, None, None, None, '§300разд.1', None, 'м3',
             self.volume_flush_line_sko_line, 0.033, 1, '=V559*W559*X559',
             '=Y559-AA559-AB559-AC559-AD559', None, None, None, None, None]]

        return volume_list

    def rir_work(self):
        work_list = [
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
             f'{self.extra_work_text_line} {self.extra_work_time_begin_date}-{self.extra_work_time_end_date}', None,
             None, None,
             None, None, 'Исполнитель', '2С', None, 'АКТ№', None, None, None, 'факт', None, 'час',
             self.extra_work_time_line, 1, 1,
             '=V388*W388*X388', '=Y388-AA388-AB388-AC388-AD388', None, None, None, None, None]]

        if self.response_combo == 'Да':
            work_list.append(
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'ОЗЦ',
                 f'{self.response_text_line} ({self.response_time_begin_date}-{self.response_time_end_date})', None,
                 None, None, None, None, None,
                 None, None, None, None, None, None, 'Простои', 'Тех. ожидание', 'час', self.response_time_line, 1, 1,
                 '=V389*W389*X389',
                 '=Y389-AA389-AB389-AC389-AD389', None, None, None, None, None])

            return work_list

    def work_pzr(self, descent_layout_line):
        work_list = []

        pzr_paker = [['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'Д/ж спайдера', None, None, None, None, None,
                 None,
                 None, None, None, None, None, None, '§185разд.1', None, 'час', 1, 0.07, 1, '=V531*W531*X531',
                 '=Y531-AA531-AB531-AC531-AD531', None, None, None, None, None],
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', 'Пакер', 'ПЗР СПО пакера', None, None, None, None, None, None,
                 None, None, None, None, None, None, '§136,142разд.1', None, 'шт', 1, 0.48, 1, '=V532*W532*X532',
                 '=Y532-AA532-AB532-AC532-AD532', None, None, None, None, None],
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'М/ж спайдера', None, None, None, None, None,
                 None,
                 None, None, None, None, None, None, '§185разд.1', None, 'час', 1, 0.07, 1, '=V533*W533*X533',
                 '=Y533-AA533-AB533-AC533-AD533', None, None, None, None, None]]

        pzr_voronka = [
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', 'Воронка', 'ПЗР СПО воронка', None, None, None, None, None,
             None, None, None, None, None, None, None, '§177разд.1', None, 'шт', 1, 0.17, 1, '=V212*W212*X212',
             '=Y212-AA212-AB212-AC212-AD212', None, None, None, None, None]]
        pzr_template = [
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', 'ПСШ', 'ПЗР СПО ПЕРО ШАБЛОН', None, None, None, None, None,
             None, None, None, None, None, None, None, '§176разд.1', None, 'шт', 1, 0.52, 1, '=V446*W446*X446',
             '=Y446-AA446-AB446-AC446-AD446', None, None, None, None, None],

        ]
        pzr_pssh = [
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', 'ПСШ', 'ПЗР СПО ПСШ', None, None, None, None, None, None,
             None, None, None, None, None, None, '§178разд.1', None, 'шт', 1, 1.27, 1, '=V447*W447*X447',
             '=Y447-AA447-AB447-AC447-AD447', None, None, None, None, None]]

        pzr_pssh_paker = [
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', 'СКМ+шаблон+пакер', 'ПЗР СПО ПСШ+пакер', None, None, None,
             None, None, None, None, None, None, None, None, None, '§178разд.1', None, 'шт', 1, 1.65, 1,
             '=V512*W512*X512', '=Y512-AA512-AB512-AC512-AD512', None, None, None, None, None]]
        pzr_zaglushka = [
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', 'Пакер', 'ПЗР СПО заглушки', None, None, None, None, None,
             None, None, None, None, None, None, None, '§177разд.1', None, 'шт', 1, 0.17, 1, '=V515*W515*X515',
             '=Y515-AA515-AB515-AC515-AD515', None, None, None, None, None]]
        pzr_2_paker = [
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', 'Пакер', 'ПЗР СПО пакера', None, None, None, None, None,
             None, None, None, None, None, None, None, '§136,142разд.1', None, 'шт', 1, 0.35, 1,
             '=V516*W516*X516', '=Y516-AA516-AB516-AC516-AD516', None, None, None, None, None]]
        pzr_filter = [
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', 'Пакер', 'ПЗР СПО фильтра', None, None, None, None, None,
             None, None, None, None, None, None, None, '§176разд.1', None, 'шт', 1, 0.35, 1, '=V517*W517*X517',
             '=Y517-AA517-AB517-AC517-AD517', None, None, None, None, None]]

        pzr_reper = [
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', 'Пакер', 'ПЗР СПО реперного патрубка', None, None, None,
             None, None, None, None, None, None, None, None, None, '§176разд.1', None, 'шт', 1, 0.35, 1,
             '=V519*W519*X519', '=Y519-AA519-AB519-AC519-AD519', None, None, None, None, None]]
        pzr_konteyner = [
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', 'Пакер', 'ПЗР СПО контейнера под манометр', None, None,
             None, None, None, None, None, None, None, None, None, None, '§176разд.1', None, 'шт', 1, 0.35, 1,
             '=V520*W520*X520', '=Y520-AA520-AB520-AC520-AD520', None, None, None, None, None]]
        pzr_print = [
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', 'Печать', 'ПЗР СПО НКТ с печатью', None, None, None, None,
             None, None, None, None, None, None, None, None, '§269разд.1', None, 'шт', 1, 0.38, 1,
             '=V639*W639*X639', '=Y639-AA639-AB639-AC639-AD639', None, None, None, None, None]]
        pzr_magnit = [
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', 'магнит', 'ПЗР СПО НКТ с магнитом', None, None, None, None,
             None, None, None, None, None, None, None, None, '§269разд.1', None, 'шт', 1, 0.38, 1,
             '=V666*W666*X666', '=Y666-AA666-AB666-AC666-AD666', None, None, None, None, None]]
        pzr_lar = [
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', 'Ловильный инструмент',
             'ПЗР СПО работы перед спуском ловильного инструмента (метчик, колокол, кабелерезка, овершот, труболовка, крючок, мятая труба, щучья пасть )',
             None, None, None, None, None, None, None, None, None, None, None, None, '§240разд.1', None, 'шт',
             1, 0.17, 1, '=V693*W693*X693', '=Y693-AA693-AB693-AC693-AD693', None, None, None, None, None]]
        pzr_raiber = [
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', 'Райбер', 'ПЗР СПО райбер', None, None, None, None, None,
             None, None, None, None, None, None, None, '§260,262разд.1', None, 'шт', 1, 0.4, 1,
             '=V730*W730*X730', '=Y730-AA730-AB730-AC730-AD730', None, None, None, None, None]]
        pzr_shlam = [
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', 'Райбер', 'ПЗР СПО шламоуловитель', None, None, None, None,
             None, None, None, None, None, None, None, None, ' §174,175 разд.1', None, 'раз', 1, '=0.13+0.17',
             1, '=V732*W732*X732', '=Y732-AA732-AB732-AC732', None, None, None, None, None]]
        pzr_vzd = [
            ['=ROW()-ROW($A$46)', 'новый шаблон', None, 'спо', 'Райбер', 'ПЗР СПО ЗД', None, None, None, None,
             None, None, None, None, None, None, None, None, '§263разд.1', None, 'шт', 1, 0.38, 1,
             '=V733*W733*X733', '=Y733-AA733-AB733-AC733-AD733', None, None, None, None, None]]
        pzr_doloto = [
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', 'Долото', 'ПЗР СПО фрез (долото)', None, None, None, None,
             None, None, None, None, None, None, None, None, '§263,264разд.1', None, 'шт', 1, 0.38, 1,
             '=V763*W763*X763', '=Y763-AA763-AB763-AC763-AD763', None, None, None, None, None]]
        pzr_gvzh = [
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', 'ГВЖ', 'ПЗР СПО перед спуском компоновки гидрожелонки',
             None, None, None, None, None, None, None, None, None, None, None, None, '§176разд.1', None, 'шт',
             1, 0.63, 1, '=V836*W836*X836', '=Y836-AA836-AB836-AC836-AD836', None, None, None, None, None]]

        pzr_tpvr = [
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', 'Перфоратор', 'ПЗР СПО трубного перфоратора', None, None,
             None, None, None, None, None, None, None, None, None, None, '§311разд.1', None, 'шт', 1, 0.9, 1,
             '=V902*W902*X902', '=Y902-AA902-AB902-AC902-AD902', None, None, None, None, None]]

        pzr_fpaker = [
            ['=ROW()-ROW($A$56)', None, None, 'спо', 'Фондовый пакер', 'ПЗР СПО перо, воронка', None, None,
             None, None, None, None, None, None, None, None, None, None, '§177разд.1', None, 'шт', 1, 0.1, 1,
             '=V1013*W1013*X1013', '=Y1013-AA1013-AB1013-AC1013-AD1013', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', 'Фондовый пакер', 'ПЗР СПО пакера', None, None, None, None,
             None, None, None, None, None, None, None, None, '§136разд.1', None, 'шт', 1, 0.46, 1,
             '=V1014*W1014*X1014', '=Y1014-AA1014-AB1014-AC1014-AD1014', None, None, None, None, None]]
        pzr_zo = [
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', 'ЗО', 'ПЗР СПО работы перед спуском  НКТ ', None, None,
             None, None, None, None, None, None, None, None, None, None, '§194разд.1', None, 'шт', 1, 0.35, 1,
             '=V1062*W1062*X1062', '=Y1062-AA1062-AB1062-AC1062-AD1062', None, None, None, None, None]]

        if 'перо' in descent_layout_line.lower() or 'воронк' in descent_layout_line.lower() :
            work_list.extend(pzr_voronka)
        if 'пакер' in descent_layout_line.lower():
            work_list.extend(pzr_paker)
        if ' зо ' in descent_layout_line.lower() or 'з.о' in descent_layout_line.lower():
            work_list.extend(pzr_zo)
        if 'мл-' in descent_layout_line.lower() or 'магнит' in descent_layout_line.lower():
            work_list.extend(pzr_magnit)
        if 'печат' in descent_layout_line.lower():
            work_list.extend(pzr_print)
        if 'заглушк' in descent_layout_line.lower():
            work_list.extend(pzr_zaglushka)
        if 'skm' in descent_layout_line.lower() and 'шаблон-' in descent_layout_line.lower():
            work_list.extend(pzr_pssh)
        if 'skm' not in descent_layout_line.lower() and 'шаблон-' in descent_layout_line.lower():
            work_list.extend(pzr_template)
        if 'skm' in descent_layout_line.lower() and 'шаблон-' in descent_layout_line.lower() \
                and 'пакер' in descent_layout_line.lower():
            work_list.extend(pzr_pssh_paker)
        if 'заглушк' in descent_layout_line.lower():
            work_list.extend(pzr_zaglushka)
        if 'трубн' in descent_layout_line.lower() and 'перфо' in descent_layout_line.lower():
            work_list.extend(pzr_tpvr)
        if 'контей' in descent_layout_line.lower():
            work_list.extend(pzr_konteyner)
        if 'фильт' in descent_layout_line.lower():
            work_list.extend(pzr_filter)
        if 'репер' in descent_layout_line.lower():
            work_list.extend(pzr_reper)
        if 'райбер' in descent_layout_line.lower() or 'фкк' in descent_layout_line.lower():
            work_list.extend(pzr_raiber)
        if 'д-' in descent_layout_line.lower():
            work_list.extend(pzr_vzd)
        if 'долото' in descent_layout_line.lower():
            work_list.extend(pzr_doloto)
        if 'шламо' in descent_layout_line.lower():
            work_list.extend(pzr_shlam)
        if 'гвж' in descent_layout_line.lower():
            work_list.extend(pzr_gvzh)
        return work_list






    def pressuar_ek_rir(self):

        work_list = []
        if self.count_nkt_combo == 'Да':
            work_list = [
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
                 f'Определение кровли на гл. {self.roof_definition_depth_line}м', None, None, None,
                 None, None, None, None, None, 'АКТ№', None, None, None, '§289разд.1', None, 'шт', 1, 0.17, 1,
                 '=V404*W404*X404', '=Y404-AA404-AB404-AC404-AD404', None, None, None, None, None]]
        if self.pressuar_ek_combo == 'Да':
            pressuar_list = [
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'ПЗР перед опрессовкой ', None, None, None,
                 None,
                 None, None, None, None, None, None, None, None, '§150/152 разд.1 ', None, 'шт', 1, 0.43, 1,
                 '=V394*W394*X394', '=Y394-AA394-AB394-AC394-AD394', None, None, None, None, None],
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
                 f'Опрессовка по НКТ Р={self.pressuar_ek_line}атм ({self.rezult_pressuar_combo})', None, None,
                 None,
                 None, None, None, None, None, 'АКТ№', None, None, None, '§151 разд.1', None, 'шт', 1, 0.25, 1,
                 '=V395*W395*X395', '=Y395-AA395-AB395-AC395-AD395', None, None, None, None, None],
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
                 'Опрессовка нагнетательной линии на Р=40атм (+)',
                 None, None, None, None, None, None, None, None, None, None, None, None, '§113 разд.1 ', None, 'раз', 1,
                 '=8/60', 1, '=V396*W396*X396', '=Y396-AA396-AB396-AC396-AD396', None, None, None, None, None]]

            work_list.extend(pressuar_list)
        return work_list

    def dopusk_lifting(self, count_nkt):
        count_lift = 0
        work_list = self.lifting_nkt()
        for index in range(len(work_list)):
            if index == 0:
                pass
            elif index == 1:
                work_list[index][11] = count_nkt * 10
                work_list[index][21] = count_nkt
            else:
                work_list[index][21] = count_nkt

            if 'Подъем НКТ' in work_list[index][5]:
                count_lift += 1
        if count_lift > 1:
            while count_lift != 1:
                work_list.pop(2)
                count_lift -= 1
            count_lift += 1
        return work_list[:-1]

    def dopusk(self, count_nkt_line):

        work_list = self.descent_nkt_work()
        for index in range(len(work_list)):
            if index == 0:
                work_list[index][12] = count_nkt_line * 10
            work_list[index][21] = count_nkt_line
        return work_list

    def determination_of_pickup_work(self, saturation_volume, determination_of_pickup_text):
        determination_of_pickup_text_list = [
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'Промывка', 'Переход на труб.простр.',
             None,
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
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, f'{determination_of_pickup_text}',
             None, None, None, None, None, None, None, None, 'АКТ№', None, None, None, '§170разд.1', None, 'шт', 1,
             0.2, 1,
             '=V553*W553*X553', '=Y553-AA553-AB553-AC553-AD553', None, None, None, None, None]
        ]
        return determination_of_pickup_text_list

    def read_presence_of_downtime(self, current_widget):
        if self.presence_of_downtime_combo == 'Да':
            try:
                self.cause_presence_of_downtime_combo = current_widget.cause_presence_of_downtime_combo.currentText()
                if self.cause_presence_of_downtime_combo == '':
                    QMessageBox.warning(self, 'причины', 'Нужно выбрать причину')
                    return
                self.presence_of_downtime_text_line = current_widget.presence_of_downtime_text_line.text()

                self.presence_of_downtime_time_begin_date = \
                    current_widget.presence_of_downtime_time_begin_date.dateTime().toPyDateTime()
                self.presence_of_downtime_time_begin_date = \
                    self.change_string_in_date(self.presence_of_downtime_time_begin_date)

                self.presence_of_downtime_time_end_date = \
                    current_widget.presence_of_downtime_time_end_date.dateTime().toPyDateTime()
                self.presence_of_downtime_time_end_date = \
                    self.change_string_in_date(self.presence_of_downtime_time_end_date)

                self.presence_of_downtime_time_line = current_widget.presence_of_downtime_time_line.text()

                self.cause_presence_of_downtime_classification_combo = \
                    current_widget.cause_presence_of_downtime_classification_combo.currentText()
                self.tehnological_operation_combo = current_widget.tehnological_operation_combo.currentText()

                if self.presence_of_downtime_time_end_date == self.presence_of_downtime_time_begin_date:
                    QMessageBox.warning(self, 'Даты совпадают', 'Даты совпадают')
                    return

                if self.presence_of_downtime_text_line == '':
                    QMessageBox.warning(self, 'Ошибка', f'Не введены текст осложнения при подьеме НКТ')
                    return
                else:
                    aaaaa = self.presence_of_downtime_time_line
                    self.presence_of_downtime_time_line = round(float(self.presence_of_downtime_time_line),
                                                                1)

                if self.presence_of_downtime_time_line <= 0:
                    QMessageBox.warning(self, 'Ошибка',
                                        f'Затраченное время при подьеме штанг не может быть отрицательным')
                    return

            except Exception as e:
                QMessageBox.warning(self, 'Ошибка', f'ВВедены не все значения {e}')
                return
        return True

    def read_volume_flush_line(self, current_widget):
        self.volume_flush_line_sko_line = current_widget.volume_flush_line_sko_line.text()
        if self.volume_flush_line_sko_line not in [None, '']:
            self.volume_flush_line_sko_line = int(float(self.volume_flush_line_sko_line))
        else:
            volume_sko_question = QMessageBox.question(self, 'Промывка после СКО',
                                                       'Не указано промывка после СКО '
                                                       'Промывки не было?')
            if volume_sko_question == QMessageBox.StandardButton.No:
                return
        return True

    def read_ovtr_work_combo(self, current_widget):
        self.ovtr_work_text_line = current_widget.ovtr_work_text_line.text()
        self.ovtr_work_time_begin_date = \
            current_widget.ovtr_work_time_begin_date.dateTime().toPyDateTime()
        self.ovtr_work_time_begin_date = \
            self.change_string_in_date(self.ovtr_work_time_begin_date)

        self.ovtr_work_time_end_date = \
            current_widget.ovtr_work_time_end_date.dateTime().toPyDateTime()
        self.ovtr_work_time_end_date = \
            self.change_string_in_date(self.ovtr_work_time_end_date)

        if current_widget.ovtr_work_text_line.text() == self.ovtr_work_time_begin_date:
            QMessageBox.warning(self, 'Даты совпадают', 'Даты совпадают')
            return

        if self.ovtr_work_text_line == '':
            QMessageBox.warning(self, 'Ошибка', f'Не введены текст работы подрядчика')
            return

        self.ovtr_work_time_line = current_widget.ovtr_work_time_line.text()
        if self.ovtr_work_time_line != '':
            self.ovtr_work_time_line = round(float(self.ovtr_work_time_line), 1)

        else:
            QMessageBox.warning(self, 'Ошибка', f'Не введены время работы подрядчика')
            return

        if self.ovtr_work_time_line <= 0:
            QMessageBox.warning(self, 'Ошибка',
                                f'Затраченное время при работы подрядчика не может быть отрицательным')
            return
        return True

    def read_responce(self, current_widget):

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
        return True

    def read_volume_after_sko(self, current_widget):

        self.volume_flush_line_sko_line = current_widget.volume_flush_line_sko_line.text()
        if self.volume_flush_line_sko_line == '':
            QMessageBox.warning(self, 'Объем насыщения', 'Введите объем промывки после СКО')
            return
        else:
            self.volume_flush_line_sko_line = float(self.volume_flush_line_sko_line)
        return True

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
        return True

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
        return True

    def response_sko(self):
        work_list = [
                        '=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'ОПЗ',
                        f'{self.response_text_line} ({self.response_time_begin_date}-{self.response_time_end_date})',
                        None,
                        None, None,
                        None, None, None, None, None, 'АКТ№', None, None, None, 'простои', 'Тех. ожидание', 'час',
                        self.response_time_line, 1, 1,
                        '=V556*W556*X556', '=Y556-AA556-AB556-AC556-AD556', None, None, None, None, None],

        return work_list

    def technological_crap_question_work(self):
        work_list = [
        ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
         f'{self.technological_crap_question_text_line} ', None, None, None,
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
         None, None]]
        return work_list

    def ozc_work(self):
        work_list = [
            ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', 'ОЗЦ',
             f'{self.ovtr_work_text_line} ({self.ovtr_work_time_begin_date}-{self.ovtr_work_time_end_date})',
             None, None, None, None, None, None, None, None, 'АКТ№', None, None, None,
             'простои', 'Тех. ожидание', 'час',
             self.ovtr_work_time_line, 1, 1,
             '=V556*W556*X556', '=Y556-AA556-AB556-AC556-AD556', None, None, None, None, None]]

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

        return True

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

        return True

    @staticmethod
    def change_string_in_date(date_str):
        # Преобразуем строку в объект datetime

        formatted_date = date_str.strftime("%d.%m.%Y %H:%M")
        return formatted_date

    def read_need_well_discharge_combo(self, current_widget):
        self.need_well_discharge_more_combo = current_widget.need_well_discharge_more_combo.currentText()
        self.source_of_work_combo = current_widget.source_of_work_combo.currentText()
        self.cause_discharge_combo = current_widget.cause_discharge_combo.currentText()
        self.volume_well_discharge_line = current_widget.volume_well_discharge_line.text()
        if self.volume_well_discharge_line != '':
            self.volume_well_discharge_line = float(self.volume_well_discharge_line)
        self.time_well_discharge_line = current_widget.time_well_discharge_line.text()
        if self.time_well_discharge_line != '':
            self.time_well_discharge_line = float(self.time_well_discharge_line)
        if self.time_well_discharge_line > 2:
            self.time_well_discharge_line_2 = 2

        self.time_well_discharge_end_date = current_widget.time_well_discharge_end_date.dateTime().toPyDateTime()

        self.time_well_discharge_end_date = \
            self.change_string_in_date(self.time_well_discharge_end_date)

        self.time_well_discharge_begin_date = current_widget.time_well_discharge_begin_date.dateTime().toPyDateTime()

        self.time_well_discharge_begin_date = \
            self.change_string_in_date(self.time_well_discharge_begin_date)

        if self.time_well_discharge_line != '':
            self.time_well_discharge_line = round(float(self.time_well_discharge_line), 1)

        else:
            QMessageBox.warning(self, 'Ошибка', f'Не введены время разрядки')
            return

        if self.time_well_discharge_line <= 0:
            QMessageBox.warning(self, 'Ошибка',
                                f'Затраченное время разрядки не может быть отрицательным или равным нулю')
            return

        if self.need_well_discharge_more_combo == 'Да':
            try:
                self.need_well_discharge_more_text_line = current_widget.need_well_discharge_more_text_line.text()
                self.cause_discharge_more_combo = current_widget.cause_discharge_more_combo.currentText()
                self.volume_well_discharge_more_line = self.volume_well_discharge_line

                self.time_well_discharge_more_line = self.time_well_discharge_line - 2.00


            except Exception as e:
                QMessageBox.warning(self, 'Ошибка', f'ВВедены не все значения {e}')
                return
        return True

    def read_need_well_discharge_after_combo(self, current_widget):
        self.need_well_discharge_more_after_combo = current_widget.need_well_discharge_more_after_combo.currentText()

        self.cause_discharge_after_combo = current_widget.cause_discharge_after_combo.currentText()
        self.volume_well_discharge_after_line = current_widget.volume_well_discharge_after_line.text()
        if self.volume_well_discharge_after_line != '':
            self.volume_well_discharge_after_line = float(self.volume_well_discharge_after_line.replace(',', '.'))
        self.time_well_discharge_after_line = current_widget.time_well_discharge_after_line.text()
        if self.time_well_discharge_after_line != '':
            self.time_well_discharge_after_line = float(self.time_well_discharge_after_line.replace(',', '.'))
        else:
            QMessageBox.warning(self, 'Ошибка', 'не введен время')
            return
        if self.time_well_discharge_after_line > 2:
            self.time_well_discharge_after_line_2 = 2

        self.time_well_discharge_end_after_date = current_widget.time_well_discharge_end_after_date.dateTime().toPyDateTime()

        self.time_well_discharge_end_after_date = \
            self.change_string_in_date(self.time_well_discharge_end_after_date)

        self.time_well_discharge_begin_after_date = \
            current_widget.time_well_discharge_begin_after_date.dateTime().toPyDateTime()

        self.time_well_discharge_begin_after_date = \
            self.change_string_in_date(self.time_well_discharge_begin_after_date)

        if self.time_well_discharge_after_line != '':
            self.time_well_discharge_after_line = round(float(self.time_well_discharge_after_line), 1)

        else:
            QMessageBox.warning(self, 'Ошибка', f'Не введены время разрядки')
            return

        if self.time_well_discharge_after_line <= 0:
            QMessageBox.warning(self, 'Ошибка',
                                f'Затраченное время разрядки не может быть отрицательным или равным нулю')
            return

        if self.need_well_discharge_more_after_combo == 'Да':
            try:
                self.need_well_discharge_more_text_after_line = current_widget.need_well_discharge_more_text_after_line.text()
                self.cause_discharge_more_after_combo = current_widget.cause_discharge_more_after_combo.currentText()
                self.volume_well_discharge_more_after_line = self.volume_well_discharge_after_line

                self.time_well_discharge_more_after_line = self.time_well_discharge_after_line - 2.00


            except Exception as e:
                QMessageBox.warning(self, 'Ошибка', f'ВВедены не все значения {e}')
                return
        return True

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

        return True

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

        return True

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

        return True

    # def solvent_injection_work(self):
    #     work_list = [
    #         ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'ОПЗ', 'Подготовительные работы, выполняемые ', None,
    #          None, None, 'ПО ТКРС', None, None, 'перед началом работ на скважине', None, None, 'РАСТВОРИТЕЛЬ',
    #          'Растворитель АСПО Реком 7125 серия 4, КР-4Р', None, '§227,229разд.1', None, 'шт', 1, 0.96, 1,
    #          '=V589*W589*X589', '=Y589-AA589-AB589-AC589-AD589', None, None, None, None, None]]
    #     if self.solvent_volume_text_line > 1:
    #         solvent_volume_list = [
    #             ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'ОПЗ', f'Закачка растворителя первого 1м3',
    #              None, None, None, None, None, None, None, None, 'АКТ№', None, None, None, '§228разд.1', None, 'м3', 1,
    #              0.2,
    #              1, '=V590*W590*X590', '=Y590-AA590-AB590-AC590-AD590', None, None, None, None, None],
    #             ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'ОПЗ',
    #              f'Закачка растворителя следующего {self.solvent_volume_text_line - 1}м3', None, None,
    #              None, None, None, None, None, None, 'АКТ№', None, None, None, '§228разд.1', None, 'м3', 1, 0.1,
    #              1, '=V591*W591*X591', '=Y591-AA591-AB591-AC591-AD591', None, None, None, None, None]]
    #     else:
    #         solvent_volume_list = [
    #             ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'ОПЗ',
    #              f'Закачка растворителя первого {self.solvent_volume_text_line}м3', None,
    #              None, None, None, None, None, None, None, 'АКТ№', None, None, None, '§228разд.1', None, 'м3', 1, 0.2,
    #              1, '=V590*W590*X590', '=Y590-AA590-AB590-AC590-AD590', None, None, None, None, None],
    #         ]
    #     work_list.extend(solvent_volume_list)
    #     volume_list = [
    #         ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'ОПЗ',
    #          f'Доводка растворителя в объеме {self.volume_of_finishing_line}', None, None, None, None,
    #          None, None, None, None, None, None, None, None, '§228разд.1', None, 'м3', self.volume_of_finishing_line,
    #          0.033, 1, '=V592*W592*X592',
    #          '=Y592-AA592-AB592-AC592-AD592', None, None, None, None, None]]
    #     work_list.extend(volume_list)
    #
    #     return work_list

    def pressuar_work(self):
        pressuar_list = [
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'ПЗР перед опрессовкой ', None, None, None,
             None,
             None, None, None, None, None, None, None, None, '§150/152 разд.1 ', None, 'шт', 1, 0.43, 1,
             '=V394*W394*X394', '=Y394-AA394-AB394-AC394-AD394', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
             f'Опрессовка на Р={self.pressuar_ek_line}атм {self.rezult_pressuar_combo}', None, None,
             None,
             None, None, None, None, None, 'АКТ№', None, None, None, '§151 разд.1', None, 'шт', 1, 0.25, 1,
             '=V395*W395*X395', '=Y395-AA395-AB395-AC395-AD395', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
             'Опрессовка нагнетательной линии',
             None, None, None, None, None, None, None, None, None, None, None, None, '§113 разд.1 ', None, 'раз', 1,
             '=8/60', 1, '=V396*W396*X396', '=Y396-AA396-AB396-AC396-AD396', None, None, None, None, None]
        ]
        return pressuar_list
