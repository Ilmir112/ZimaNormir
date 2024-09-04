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

        self.dict_nkt = well_data.dict_nkt

        self.date_work_label = QLabel('Дата работы')
        self.date_work_line = QLineEdit(self)
        self.date_work_line.setText(f'{well_data.date_work}')

        self.date_work_str = datetime.strptime(self.date_work_line.text(), '%d.%m.%Y')

        self.select_work_of_third_parties_label = QLabel('Выбор оргазинации')
        self.select_work_of_third_parties = QComboBox(self)
        self.select_work_of_third_parties.addItems(['', 'Крезол', 'сваб', 'РИР 2С'])

        self.grid = QGridLayout(self)

        self.grid.addWidget(self.date_work_label, 4, 2)
        self.grid.addWidget(self.date_work_line, 5, 2)

        self.grid.addWidget(self.select_work_of_third_parties_label, 4, 3)
        self.grid.addWidget(self.select_work_of_third_parties, 5, 3)

        self.select_work_of_third_parties.currentTextChanged.connect(self.update_select_work_of_third_parties)

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
        self.volume_flush_line_sko_label = QLabel('Объем промывки после СКО')
        self.pressuar_combo_label = QLabel('Был ли опрессовка колонны после СКО для определения приемистости')

        self.definition_q_label = QLabel('Было ли определение Q после СКО')
        self.extra_work_text_label = QLabel('Текст проведения работ')
        self.depth_zumpf_paker_combo_label = QLabel('Опрессовка ЗУМПФа')
        self.depth_zumpf_paker_label = QLabel('Глубина посадки пакера ЗУМФПа')
        self.solvent_injection_label = QLabel('Закачка растворителя')
        self.nkt_is_same_label = QLabel('Кол-во НКТ на подъем совпадает со спуском')
        self.pressuar_tnkt_label = QLabel('Была ли опрессовка ТНКТ и вымыв шара')
        self.depth_paker_text_label = QLabel('Глубины посадки пакера')
        self.pressuar_ek_label = QLabel('Давление опрессовки')
        self.volume_swabing_label = QLabel('Объем свабирования')
        self.rezult_pressuar_combo_label = QLabel('Результат опрессовки')
        self.rezult_zumpf_pressuar_combo_label = QLabel('Результат опрессовки')
        self.determination_of_pickup_combo_label = QLabel('Было ли определение Q?')
        self.determination_of_pickup_combo_zumpf_label = QLabel('Было ли определение Q?')
        self.saturation_volume_label = QLabel('Объем Насыщения')
        self.determination_of_pickup_text_label = QLabel('Текст определение Q')
        self.saturation_volume_zumpf_label = QLabel('Объем Насыщения')
        self.determination_of_pickup_zumpf_text_label = QLabel('Текст определение Q')
        self.response_text_label = QLabel('Текст реагирование')
        self.response_time_begin_label = QLabel('начало реагирования')
        self.response_time_end_label = QLabel('Окончание реагирования')
        self.roof_definition_depth_label = QLabel('Глубина спуск воронки ')
        self.count_nkt_combo_label = QLabel('Были ли допуск НКТ?')

    def update_select_work_of_third_parties(self, index):

        self.combo_nkt_true_label = QLabel('Было ли спущено НКТ до операции')
        self.combo_nkt_true = QComboBox(self)
        self.combo_nkt_true.addItems(['Нет', 'Да'])

        self.grid.addWidget(self.combo_nkt_true_label, 22, 0)
        self.grid.addWidget(self.combo_nkt_true, 23, 0)

        self.combo_nkt_true.currentTextChanged.connect(self.update_combo_nkt_true)


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


        self.grid.addWidget(self.extra_work_text_label, 52, 1)
        self.grid.addWidget(self.extra_work_text_line, 53, 1)
        self.grid.addWidget(self.extra_work_time_begin_label, 52, 2)
        self.grid.addWidget(self.extra_work_time_begin_date, 53, 2)
        self.grid.addWidget(self.extra_work_time_end_label, 52, 3)
        self.grid.addWidget(self.extra_work_time_end_date, 53, 3)
        self.grid.addWidget(self.extra_work_time_label, 52, 4)
        self.grid.addWidget(self.extra_work_time_line, 53, 4)

        self.extra_work_time_end_date.dateTimeChanged.connect(self.update_date_technological_crap)
        self.extra_work_time_begin_date.dateTimeChanged.connect(
            self.update_date_technological_crap)
        aaaaaa  = index

        if index in ['Крезол', 'РИР 2С', 'сваб']:
            if index in ['Крезол', 'РИР 2С']:
                self.response_text_line = QLineEdit(self)

                self.response_time_begin_date = QDateTimeEdit(self)
                self.response_time_begin_date.setDisplayFormat("dd.MM.yyyy HH:mm")
                self.response_time_begin_date.setDateTime(self.date_work_str)

                self.response_time_end_date = QDateTimeEdit(self)
                self.response_time_end_date.setDisplayFormat("dd.MM.yyyy HH:mm")
                self.response_time_end_date.setDateTime(self.date_work_str)

                self.response_time_line_label = QLabel('Затраченное время')
                self.response_time_line = QLineEdit(self)
                self.grid.addWidget(self.response_text_label, 60, 1)
                self.grid.addWidget(self.response_text_line, 61, 1)

                self.grid.addWidget(self.response_time_begin_label, 60, 2)
                self.grid.addWidget(self.response_time_begin_date, 61, 2)

                self.grid.addWidget(self.response_time_end_label, 60, 3)
                self.grid.addWidget(self.response_time_end_date, 61, 3)

                self.grid.addWidget(self.response_time_line_label, 60, 4)
                self.grid.addWidget(self.response_time_line, 61, 4)
                self.pressuar_combo = QComboBox(self)
                self.pressuar_combo.addItems(['Нет', 'Да'])

                self.grid.addWidget(self.pressuar_combo_label, 62, 0)
                self.grid.addWidget(self.pressuar_combo, 63, 0)

                self.response_time_end_date.dateTimeChanged.connect(self.update_date_response)
                self.response_time_begin_date.dateTimeChanged.connect(
                    self.update_date_response)
                self.pressuar_combo.currentTextChanged.connect(self.update_pressuar_combo)


            self.count_nkt_combo = QComboBox(self)
            self.count_nkt_combo.addItems(['Нет', 'Да'])

            self.volume_flush_line_sko_line = QLineEdit(self)
            self.volume_flush_line_sko_line.setValidator(self.validator_float)

            self.definition_q_combo = QComboBox(self)
            self.definition_q_combo.addItems(['Нет', 'Да'])

            self.grid.addWidget(self.count_nkt_combo_label, 64, 0)
            self.grid.addWidget(self.count_nkt_combo, 65, 0)

            self.grid.addWidget(self.definition_q_label, 66, 0)
            self.grid.addWidget(self.definition_q_combo, 67, 0)

            self.type_equipment_combo_label = QLabel('оборудование спущенное')
            self.type_equipment_combo = QComboBox(self)

            self.grid.addWidget(self.type_equipment_combo_label, 52, 0)
            self.grid.addWidget(self.type_equipment_combo, 53, 0)

            self.type_equipment_combo.currentTextChanged.connect(self.update_type_equipment_combo)


            self.count_nkt_combo.currentTextChanged.connect(self.update_count_nkt_combo)
            self.definition_q_combo.currentTextChanged.connect(self.update_definition_q_combo)




            if index in ['Крезол']:
                self.type_equipment_combo.addItems(['', 'пакер', 'ПСШ', 'шаблон', 'перо', 'воронка'])

                self.pressuar_combo_label = QLabel('Был ли опрессовка колонны после СКО для определения приемистости')

                self.response_text_line.setText('Реагирование')

                self.extra_work_text_line.setText('Работа фирмы ООО "Крезол"')

                self.grid.addWidget(self.volume_flush_line_sko_label, 64, 4)
                self.grid.addWidget(self.volume_flush_line_sko_line, 65, 4)

            elif index in ['РИР 2С']:
                self.pressuar_combo_label = QLabel('Был ли опрессовка колонны')

                self.type_equipment_combo.addItems(['', 'пакер', 'РПП', 'РПК', 'перо'])
                self.pressuar_combo_label = QLabel('Была ли опрессовка колонны после ОЗЦ')
                self.response_text_line.setText('ОЗЦ')
                self.response_time_begin_label.setText('начало ОЗЦ')
                self.response_time_end_label.setText('Окончание ОЗЦ')
                self.response_text_label.setText('Текст ОЗЦ')
                self.roof_definition_depth_label.setText('Глубина спуск определения кровли ЦМ')
                self.extra_work_text_line.setText('Работа фирмы РИР 2С')
                self.extra_work_text_label.setText('РИР Текст')

                self.response_text_label.setText('ОЗЦ')
                self.response_text_line.setText('ОЗЦ')
                self.pressuar_combo_label.setText('Было ли опрессовка ЭК после РИР')
                self.definition_q_label.setText('Было ли определение Q после РИР')
                self.volume_flush_line_sko_label.setParent(None)
                self.volume_flush_line_sko_line.setParent(None)
            elif index in ['сваб']:
                self.type_equipment_combo.addItems(['', 'пакер', 'ПСШ', 'шаблон', 'перо', 'воронка'])
                self.extra_work_text_line.setText('ГИС - СВАБ')
                self.count_nkt_combo_label.setText('Был ли допуск после сваба')
                self.definition_q_label.setText('Было ли определение Q после сваба')
                self.volume_flush_line_sko_label('Объем промывки после сваба')
                self.grid.addWidget(self.volume_flush_line_sko_label, 64, 4)
                self.grid.addWidget(self.volume_flush_line_sko_line, 65, 4)


                self.volume_swabing_edit = QLineEdit(self)
                self.volume_swabing_edit.setValidator(self.validator_int)
                self.grid.addWidget(self.volume_swabing_label, 64, 1)
                self.grid.addWidget(self.volume_swabing_edit, 65, 1)



                try:
                    self.pressuar_combo_label.setParent(None)
                    self.pressuar_combo.setParent(None)
                    self.response_time_begin_date.setParent(None)
                    self.response_time_end_date.setParent(None)
                    self.response_time_line_label.setParent(None)
                    self.response_time_line.setParent(None)
                except:
                    pass

    def update_combo_nkt_true(self, index):
        if index == 'Нет':
            self.nkt_48_lenght_edit.setParent(None)
            self.nkt_48_count_edit.setParent(None)
            self.nkt_60_lenght_edit.setParent(None)
            self.nkt_60_count_edit.setParent(None)
            self.nkt_73_lenght_edit.setParent(None)
            self.nkt_73_count_edit.setParent(None)
            self.nkt_89_lenght_edit.setParent(None)
            self.nkt_89_count_edit.setParent(None)
            self.nkt_48_lenght_label.setParent(None)
            self.nkt_60_lenght_label.setParent(None)
            self.nkt_73_lenght_label.setParent(None)
            self.nkt_89_lenght_label.setParent(None)
            self.nkt_48_count_label.setParent(None)
            self.nkt_60_count_label.setParent(None)
            self.nkt_73_count_label.setParent(None)
            self.nkt_89_count_label.setParent(None)
        else:
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
            self.dict_nkt = well_data.dict_nkt

            if len(self.dict_nkt) != 0:
                for nkt_key, nkt_value in self.dict_nkt:
                    if '73' in nkt_key:
                        self.nkt_73_lenght_edit.setText(nkt_value[1])
                        self.nkt_73_count_edit.setText(nkt_value[0])
                    elif '60' in nkt_key:
                        self.nkt_60_lenght_edit.setText(nkt_value[1])
                        self.nkt_60_count_edit.setText(nkt_value[0])
                    elif '48' in nkt_key:
                        self.nkt_48_lenght_edit.setText(nkt_value[1])
                        self.nkt_48_count_edit.setText(nkt_value[0])
                    elif '89' in nkt_key or '102' in nkt_key:
                        self.nkt_89_lenght_edit.setText(nkt_value[1])
                        self.nkt_89_count_edit.setText(nkt_value[0])



        # elif index in ['Кислота силами подрядчика']:
        #     self.skv_combo_label = QLabel(self)
        #     self.skv_combo = QComboBox(self)
        #     self.skv_combo.addItems(['Нет', 'Да'])
        #
        #     self.response_skv_text_label = QLabel('Текст реагирование')
        #     self.response_skv_text_line = QLineEdit(self)
        #     self.response_skv_text_line.setText('Тех отстой')
        #
        #     self.response_skv_time_begin_label = QLabel('начало реагирования')
        #     self.response_skv_time_begin_date = QDateTimeEdit(self)
        #     self.response_skv_time_begin_date.setDisplayFormat("dd.MM.yyyy HH:mm")
        #     self.response_skv_time_begin_date.setDateTime(self.date_work_str)
        #
        #     self.response_skv_time_end_label = QLabel('Окончание реагирования')
        #     self.response_skv_time_end_date = QDateTimeEdit(self)
        #     self.response_skv_time_end_date.setDisplayFormat("dd.MM.yyyy HH:mm")
        #     self.response_skv_time_end_date.setDateTime(self.date_work_str)
        #
        #     self.grid.addWidget(self.skv_combo_label, 54, 2)
        #     self.grid.addWidget(self.skv_combo_label, 55, 2)
        #     self.skv_combo.currentTextChanged.connect(self.update_skv_combo)


    def update_type_equipment_combo(self, index):
        if index in ['РПП', 'РПК']:
            self.count_nkt_combo.setParent(None)
            self.count_nkt_combo_label.setParent(None)
        else:
            self.grid.addWidget(self.count_nkt_combo_label, 64, 0)
            self.grid.addWidget(self.count_nkt_combo, 65, 0)

    def update_count_nkt_combo(self, index):
        if index == 'Нет':
            self.count_nkt_label.setParent(None)
            self.count_nkt_line.setParent(None)
            self.roof_definition_depth_line.setParent(None)
            self.roof_definition_depth_label.setParent(None)
        elif index == 'Да':
            self.count_nkt_label = QLabel('Количество НКТ на допуск')
            self.count_nkt_line = QLineEdit(self)
            self.count_nkt_line.setValidator(self.validator_int)
            self.count_nkt_line.setText('3')
            self.roof_definition_depth_line = QLineEdit(self)
            self.roof_definition_depth_line.setValidator(self.validator_float)

            self.grid.addWidget(self.count_nkt_label, 64, 2)
            self.grid.addWidget(self.count_nkt_line, 65, 2)

            self.grid.addWidget(self.roof_definition_depth_label, 64, 3)
            self.grid.addWidget(self.roof_definition_depth_line, 65, 3)

    def update_definition_q_combo(self, index):
        if index == 'Нет':
            self.saturation_volume_sko_label.setParent(None)
            self.saturation_volume_sko_line.setParent(None)

            self.determination_of_pickup_sko_text_label.setParent(None)
            self.determination_of_pickup_sko_text_line.setParent(None)

        elif index == 'Да':

            self.saturation_volume_sko_label = QLabel('Насыщение')
            self.saturation_volume_sko_line = QLineEdit(self)
            self.saturation_volume_sko_line.setValidator(self.validator_float)

            self.determination_of_pickup_sko_text_label = QLabel('Текст определение Q')
            self.determination_of_pickup_sko_text_line = QLineEdit(self)

            self.grid.addWidget(self.saturation_volume_sko_label, 66, 2)
            self.grid.addWidget(self.saturation_volume_sko_line, 67, 2)
            self.grid.addWidget(self.determination_of_pickup_sko_text_label, 66, 3)
            self.grid.addWidget(self.determination_of_pickup_sko_text_line, 67, 3)

    def update_pressuar_combo(self, index):
        if index == 'Нет':
            self.rezult_pressuar_combo.setParent(None)
            self.pressuar_ek_line.setParent(None)
            self.pressuar_ek_label.setParent(None)
            self.rezult_pressuar_combo_label.setParent(None)

            self.depth_paker_text_edit.setParent(None)
            self.depth_paker_text_label.setParent(None)
        else:

            self.depth_paker_text_edit = QLineEdit(self)
            self.rezult_pressuar_combo = QComboBox(self)
            self.rezult_pressuar_combo.addItems(['+', '-'])

            self.pressuar_ek_line = QLineEdit(self)
            self.pressuar_ek_line.setValidator(self.validator_float)

            self.grid.addWidget(self.depth_paker_text_label, 62, 1)
            self.grid.addWidget(self.depth_paker_text_edit, 63, 1)

            self.grid.addWidget(self.pressuar_ek_label, 62, 2)
            self.grid.addWidget(self.pressuar_ek_line, 63, 2)
            self.grid.addWidget(self.rezult_pressuar_combo_label, 62, 3)
            self.grid.addWidget(self.rezult_pressuar_combo, 63, 3)

    def update_skv_combo(self, index):
        if index == 'Нет':
            pass
        else:
            self.volume_skv_label = QLabel(self)
            self.volume_skv_line = QLineEdit(self)
            self.volume_skv_line.setValidator(self.validator_float)

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

    @staticmethod
    def calculate_date(time_begin, time_end):
        # Вычисляем разницу в секундах
        difference_in_seconds = time_begin.secsTo(time_end)

        # Преобразуем в часы
        difference_in_hours = round(difference_in_seconds / 3600, 1)
        return difference_in_hours


class TabWidget(QTabWidget):
    def __init__(self):
        super().__init__()
        self.addTab(TabPage_SO_Timplate(self), 'Работа сторонних организация')


class WorkOfThirdPaties(QMainWindow):
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
        self.select_work_of_third_parties = current_widget.select_work_of_third_parties.currentText()
        self.combo_nkt_true = current_widget.combo_nkt_true.currentText()
        self.count_nkt_combo = current_widget.count_nkt_combo.currentText()
        self.definition_q_combo = current_widget.definition_q_combo.currentText()

        if self.select_work_of_third_parties == '':
            return

        elif self.select_work_of_third_parties in ['Крезол', 'РИР 2С']:
            if self.definition_q_combo == 'Да':
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

            self.volume_flush_line_sko_line = current_widget.volume_flush_line_sko_line.text()

            if self.select_work_of_third_parties == 'Крезол':
                if self.volume_flush_line_sko_line not in [None, '']:
                    self.volume_flush_line_sko_line = int(float(self.volume_flush_line_sko_line))
                else:
                    volume_sko_question = QMessageBox.question(self, 'Промывка после СКО',
                                                               'Не указано промывка после СКО '
                                                               'Промывки не было?')
                    if volume_sko_question == QMessageBox.StandardButton.No:
                        return

            elif self.select_work_of_third_parties == 'сваб':
                self.volume_swabing_edit = current_widget.volume_swabing_edit.text()
                if self.volume_swabing_edit == '':
                    QMessageBox.warning(self, 'Ошибка', 'Необходимо ввести объем свабирования')
                    return
                else:
                    self.volume_swabing_edit = int(float(self.volume_swabing_edit))

            self.pressuar_combo = current_widget.pressuar_combo.currentText()
            if self.pressuar_combo == 'Да':
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

        if self.combo_nkt_true == 'Да':
            self.type_equipment = current_widget.type_equipment_combo.currentText()
            if self.type_equipment == '':
                QMessageBox.warning(self, 'не выбрана', 'Не выбрана вид спущенной компоновки')
                return

            self.coefficient_lifting = 1

            if self.type_equipment in ['пакер']:
                self.coefficient_lifting = 1.2
            elif self.type_equipment in ['шаблон']:
                self.coefficient_lifting = 1.15

            if self.count_nkt_combo == 'Да':
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

                self.dict_nkt_up = self.dict_nkt

                if len(self.dict_nkt) == 0:
                    question = QMessageBox.question(self, 'Ошибка', f'НКТ отсутствуют?')
                    if question == QMessageBox.StandardButton.No:
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

    def rir_work(self):
        work_list = [
            ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None,
             f'{self.extra_work_text_line} {self.extra_work_time_begin_date}-{self.extra_work_time_end_date}', None,
             None, None,
             None, None, 'Исполнитель', '2С', None, 'АКТ№', None, None, None, 'факт', None, 'час',
             self.extra_work_time_line, 1, 1,
             '=V388*W388*X388', '=Y388-AA388-AB388-AC388-AD388', None, None, None, None, None]]
        if self.response_text_line != '':
            work_list.append(
                ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', 'ОЗЦ',
                 f'{self.response_text_line} ({self.response_time_begin_date}-{self.response_time_end_date})', None,
                 None, None, None, None, None,
                 None, None, None, None, None, None, 'Простои', 'Тех. ожидание', 'час', self.response_time_line, 1, 1,
                 '=V389*W389*X389',
                 '=Y389-AA389-AB389-AC389-AD389', None, None, None, None, None])

            return work_list

    def dopusk(self):
        from normir.template_without_skm import TemplateWithoutSKM
        work_list = TemplateWithoutSKM.descent_nkt_work(self)
        for index in range(len(work_list)):
            if index == 0:
                work_list[index][12] = self.count_nkt_line * 10
            work_list[index][21] = self.count_nkt_line
        return work_list

    def volume_after_sko_work(self):
        from normir.template_without_skm import TemplateWithoutSKM
        work_list = []
        if self.combo_nkt_true == 'Да':
            if self.count_nkt_combo == 'Да':
                work_list.extend(self.dopusk())
        if self.volume_flush_line_sko_line != '' and self.select_work_of_third_parties == 'Крезол':
            volume_list = [
                ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', 'Промывка', 'ПЗР при промывке скважины ', None, None,
                 None, None, None, None, None, None, None, None, None, None, '§156,160р.1', None, 'шт', 1, 1, 1,
                 '=V557*W557*X557', '=Y557-AA557-AB557-AC557-AD557', None, None, None, None, None],
                ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', 'Промывка', 'Переход на обратную промывку', None,
                 None,
                 None, None, None, None, None, None, None, None, None, None, '§162разд.1', None, 'раз', 1, 0.15, 1,
                 '=V558*W558*X558', '=Y558-AA558-AB558-AC558-AD558', None, None, None, None, None],
                ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', 'Промывка',
                 f'Промывка в объеме {self.volume_flush_line_sko_line}м3', None, None, None, None, None,
                 None, None, None, None, None, None, None, '§300разд.1', None, 'м3',
                 self.volume_flush_line_sko_line, 0.033, 1, '=V559*W559*X559',
                 '=Y559-AA559-AB559-AC559-AD559', None, None, None, None, None]]
            self.complications_when_lifting_combo = 'Нет'
            if self.combo_nkt_true == 'Да':
                if self.count_nkt_combo == 'Да':
                    work_list_lift = TemplateWithoutSKM.lifting_nkt(self)[:-2]
                    count_lift = 0
                    for index, row in enumerate(work_list_lift):

                        if index == 0:
                            work_list_lift[index][12] = self.count_nkt_line * 10
                        work_list_lift[index][21] = self.count_nkt_line
                        if any(['Подъем' in str(row1) for row1 in row]):
                            count_lift += 1
                    if count_lift == 2:
                        work_list_lift.pop(2)
                    elif count_lift == 3:
                        work_list_lift.pop(2)
                        work_list_lift.pop(2)
                    volume_list.extend(work_list_lift)

            work_list.extend(volume_list)

        return work_list

    @staticmethod
    def change_string_in_date(date_str):
        # Преобразуем строку в объект datetime

        formatted_date = date_str.strftime("%d.%m.%Y %H:%M")
        return formatted_date

    def depth_paker_work(self):
        from normir.template_without_skm import TemplateWithoutSKM

        work_list = []

        if self.select_work_of_third_parties in ['Крезол', 'Кислота силами подрядчика']:
            if self.select_work_of_third_parties == 'Крезол':
                work_list.extend(self.krezol_work())
            work_list.extend(self.volume_after_sko_work())

            if self.definition_q_combo == 'Да':
                work_list.extend(self.determination_of_pickup_work(
                    self.saturation_volume_sko_line, self.determination_of_pickup_sko_text_line))

            self.date_work_line = self.extra_work_time_end_date.split(' ')[0]
        elif self.select_work_of_third_parties in ['РИР 2С']:
            work_list.extend(self.rir_work())
            if self.combo_nkt_true == 'Да':
                if self.count_nkt_combo == 'Да':
                    work_list.extend(self.dopusk())
                    aaaa = self.dict_nkt
                    if '73мм' in list(self.dict_nkt.keys()):
                        self.dict_nkt['73мм'] = (self.depth_paker_text_edit, self.dict_nkt['73мм'][1] + self.count_nkt_line)
                    elif '60мм' in list(self.dict_nkt.keys()):
                        self.dict_nkt['60мм'] = (
                            self.depth_paker_text_edit, self.dict_nkt['60мм'][1] + self.count_nkt_line)
                aaa = self.dict_nkt
                work_list.extend(self.pressuar_ek_rir())

                self.complications_when_lifting_combo = 'Нет'

                work_list_lift = TemplateWithoutSKM.lifting_nkt(self)
                work_list.extend(work_list_lift)
        elif self.select_work_of_third_parties in ['сваб']:
            work_list = self.swabbing_work()

        return work_list

    def pressuar_ek_rir(self):
        work_list = []
        if self.count_nkt_combo == 'Да':
            work_list = [
                ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None,
                 f'Определение кровли на гл. {self.depth_paker_text_edit}м', None, None, None,
                 None, None, None, None, None, 'АКТ№', None, None, None, '§289разд.1', None, 'шт', 1, 0.17, 1,
                 '=V404*W404*X404', '=Y404-AA404-AB404-AC404-AD404', None, None, None, None, None]]
        if self.pressuar_combo == 'Да':
            pressuar_list = [
                ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None, 'ПЗР перед опрессовкой ', None, None, None,
                 None,
                 None, None, None, None, None, None, None, None, '§150/152 разд.1 ', None, 'шт', 1, 0.43, 1,
                 '=V394*W394*X394', '=Y394-AA394-AB394-AC394-AD394', None, None, None, None, None],
                ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None, 'Опрессовка по НКТ Р=100атм (+)', None, None,
                 None,
                 None, None, None, None, None, 'АКТ№', None, None, None, '§151 разд.1', None, 'шт', 1, 0.25, 1,
                 '=V395*W395*X395', '=Y395-AA395-AB395-AC395-AD395', None, None, None, None, None],
                ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None,
                 'Опрессовка нагнетательной линии на Р=40атм (+)',
                 None, None, None, None, None, None, None, None, None, None, None, None, '§113 разд.1 ', None, 'раз', 1,
                 '=8/60', 1, '=V396*W396*X396', '=Y396-AA396-AB396-AC396-AD396', None, None, None, None, None]]

            work_list.extend(pressuar_list)
        return work_list

    def determination_of_pickup_work(self, saturation_volume, determination_of_pickup_text):
        if self.pressuar_combo == 'Да':
            work_list = self.pressuar_work()[:-1]
        determination_of_pickup_text_list = [
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'Промывка',
             f'Насыщение в объеме {saturation_volume}м3', None, None, None, None, None, None,
             None, None, 'АКТ№', None, None, None, '§301разд.1', None, 'м3',
             self.saturation_volume_sko_line, 0.033, 1, '=V550*W550*X550',
             '=Y550-AA550-AB550-AC550-AD550', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'Промывка',
             'Переход на обратную промывку',
             None,
             None, None,
             None, None, None, None, None, None, None, None, None, '§162разд.1', None, 'раз', 1, 0.15, 1,
             '=V551*W551*X551', '=Y551-AA551-AB551-AC551-AD551', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
             'Подготовительные работы перед определением приемистости', None, None, None, None, None, None,
             None, None, None, None, None, None, '§169,171разд.1', None, 'шт', 1, 0.52, 1, '=V552*W552*X552',
             '=Y552-AA552-AB552-AC552-AD552', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None, f'{determination_of_pickup_text}',
             None, None, None, None, None, None, None, None, 'АКТ№', None, None, None, '§170разд.1', None, 'шт', 1,
             0.2,
             1,
             '=V553*W553*X553', '=Y553-AA553-AB553-AC553-AD553', None, None, None, None, None]
        ]

        work_list.extend(determination_of_pickup_text_list)
        return work_list

    def pressuar_work(self):
        work_list = []

        pressuar_work_list = [

            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
             f'Посадка пакера на гл.{self.depth_paker_text_edit}',
             None, None, None, None,
             None, None, None, None, None, None, None, None, '§138разд.1', None, 'шт', 1, 0.23, 1,
             '=V547*W547*X547',
             '=Y547-AA547-AB547-AC547-AD547', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'ПЗР перед опрессовкой ', None,
             None,
             None, None,
             None,
             None, None, None, None, None, None, None, '§147,149разд.1', None, 'шт', 1, 0.43, 1, '=V548*W548*X548',
             '=Y548-AA548-AB548-AC548-AD548', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
             f'Опрессовка ЭК в инт. на Р={self.pressuar_ek_line}атм ({self.rezult_pressuar_combo})', None, None,
             None, None, None, None, None, None, 'АКТ№', None, None, None, '§148разд.1', None, 'шт', 1, 0.583, 1,
             '=V549*W549*X549', '=Y549-AA549-AB549-AC549-AD549', None, None, None, None, None]]
        work_list.extend(pressuar_work_list)
        # if self.determination_of_pickup_combo == 'Да':
        #     determination_of_pickup_list = work_list.extend(self.determination_of_pickup_work(
        #         self.saturation_volume_line, self.determination_of_pickup_text_line))
        #     work_list.extend(determination_of_pickup_list)

        work_list.extend([
            ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None, 'Срыв пакера в эксплуатационной колонне', None,
             None,
             None, None, None, None, None, None, None, None, None, None, '§146разд.1', None, 'шт', 1, 0.15, 1,
             '=V554*W554*X554', '=Y554-AA554-AB554-AC554-AD554', None, None, None, None, None]])

        return work_list

    def swabbing_work(self):
        work_list = [
            ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None, 'Монтаж/демонтаж штангового превентора', None, None,
             None, None, None, None, None, None, None, None, None, None, '§120разд.1', None, 'шт', 1, 0.6, 1,
             '=V338*W338*X338', '=Y338-AA338-AB338-AC338-AD338', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None, 'Поднести и установить на колонном фланце тройник ',
             None, None, None, None, None, None, None, None, None, None, None, None, '§278разд.1', None, 'шт', 1, 0.37,
             1, '=V339*W339*X339', '=Y339-AA339-AB339-AC339-AD339', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None, 'Поднести и установить на колонном фланце задвижку',
             None, None, None, None, None, None, None, None, None, None, None, None, '§278разд.1', None, 'шт', 1, 0.37,
             1, '=V340*W340*X340', '=Y340-AA340-AB340-AC340-AD340', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None, 'Монтаж выкидной линии', None, None, None, None,
             None, None, None, None, None, None, None, None, '§301разд.1', None, 'раз', 1, 0.3, 1, '=V341*W341*X341',
             '=Y341-AA341-AB341-AC341-AD341', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', None, None, 'ГИС', 'Свабирование',
             f'{self.extra_work_text_line} {self.extra_work_time_begin_date}-{self.extra_work_time_end_date}', None, None,
             None, None, None, None, 'Объем', self.volume_swabing_edit , 'АКТ№', None, None, None, 'Факт', None,
             'час', self.extra_work_time_line, 1, 1,
             '=V342*W342*X342', '=Y342-AA342-AB342-AC342-AD342', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None, 'Демонтаж выкидной линии', None, None, None, None,
             None, None, None, None, None, None, None, None, '§301разд.1', None, 'раз', 1, 0.17, 1, '=V343*W343*X343',
             '=Y343-AA343-AB343-AC343-AD343', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None,
             'Демонтировать и отнести на колонном фланце тройник ', None, None, None, None, None, None, None, None,
             None, None, None, None, '§278разд.1', None, 'шт', 1, 0.35, 1, '=V344*W344*X344',
             '=Y344-AA344-AB344-AC344-AD344', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None,
             'Демонтировать и отнести на колонном фланце задвижку', None, None, None, None, None, None, None, None,
             None, None, None, None, '§278разд.1', None, 'шт', 1, 0.35, 1, '=V345*W345*X345',
             '=Y345-AA345-AB345-AC345-AD345', None, None, None, None, None]]
        return work_list


if __name__ == "__main__":
    # app3 = QApplication(sys.argv)

    app = QApplication(sys.argv)
    window = WorkOfThirdPaties(22, 22)
    window.show()
    sys.exit(app.exec_())
