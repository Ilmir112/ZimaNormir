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

from normir.TabPageAll import TabPage, TemplateWork


class TabPage_SO_Timplate(TabPage):
    def __init__(self, parent=None):
        super().__init__()

        self.date_work_str = datetime.strptime(self.date_work_line.text(), '%d.%m.%Y')

        self.select_type_combo_label = QLabel('Выбор компоновки спуска')
        self.select_type_combo = QComboBox(self)
        self.select_type_combo.addItems(['', 'НКТ', 'СБТ'])

        self.grid = QGridLayout(self)

        self.grid.addWidget(self.date_work_label, 4, 2)
        self.grid.addWidget(self.date_work_line, 5, 2)

        self.grid.addWidget(self.select_type_combo_label, 4, 3)
        self.grid.addWidget(self.select_type_combo, 5, 3)

        self.descent_layout_line = QLineEdit(self)

        self.grid.addWidget(self.descent_layout_label, 6, 1)
        self.grid.addWidget(self.descent_layout_line, 8, 1, 2, 3)
        self.date_work_line.dateTimeChanged.connect(self.insert_date_in_ois)

        self.select_type_combo.currentTextChanged.connect(self.update_select_type_combo)

        # if well_data.date_work != '':
        #     self.date_work_line.setText(well_data.date_work)

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

        self.emergency_work_text_label = QLabel('Глубина ЛАР')
        self.count_of_nkt_extensions_label = QLabel('Кол-во метров бурения')
        self.drilling_ek_combo_label = QLabel('Что бурили')
        self.select_type_drill_combo_label = QLabel('Фрез или долото')
        self.emergency_work_time_begin_label = QLabel('начало ЛАР')

        self.emergency_work_time_end_label = QLabel('Окончание ЛАР')
        self.emergency_work_time_label = QLabel('затраченное время')

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

        self.complications_of_failure_combo = QComboBox(self)
        self.complications_of_failure_combo.addItems(['Нет', 'Да'])

        self.grid.addWidget(self.complications_of_failure_label, 28, 1)
        self.grid.addWidget(self.complications_of_failure_combo, 29, 1)

        self.complications_of_failure_combo.currentTextChanged.connect(self.update_complications_of_failure)

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

        self.nkt_label()

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

        self.technological_crap_question_combo = QComboBox(self)
        self.technological_crap_question_combo.addItems(['Нет', 'Да'])

        self.grid.addWidget(self.technological_crap_question_label, 52, 1)
        self.grid.addWidget(self.technological_crap_question_combo, 53, 1)

        self.equipment_audit_label = QLabel('Была ли ревизия')
        self.equipment_audit_combo = QComboBox(self)
        self.equipment_audit_combo.addItems(['Нет', 'Да'])

        self.grid.addWidget(self.equipment_audit_label, 94, 1)
        self.grid.addWidget(self.equipment_audit_combo, 95, 1)

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

        self.emergency_work_text_edit = QLineEdit(self)

        self.count_of_nkt_extensions_line = QLineEdit(self)
        self.count_of_nkt_extensions_line.setValidator(self.validator_float)

        self.grid.addWidget(self.emergency_work_text_label, 30, 1)
        self.grid.addWidget(self.emergency_work_text_edit, 31, 1)

        # self.drilling_ek_combo = QComboBox(self)
        # self.drilling_ek_combo.addItems(drilling_ek_list)
        #
        # self.grid.addWidget(self.drilling_ek_combo_label, 30, 2)
        # self.grid.addWidget(self.drilling_ek_combo, 31, 2)
        #
        # self.select_type_drill_combo = QComboBox(self)
        # self.select_type_drill_combo.addItems(['', 'фрез', 'долото'])
        #
        # self.grid.addWidget(self.select_type_drill_combo_label, 30, 3)
        # self.grid.addWidget(self.select_type_drill_combo, 31, 3)
        #
        # self.grid.addWidget(self.count_of_nkt_extensions_label, 30, 5)
        # self.grid.addWidget(self.count_of_nkt_extensions_line, 31, 5)

        self.emergency_work_time_begin_date = QDateTimeEdit(self)
        self.emergency_work_time_begin_date.setDisplayFormat("dd.MM.yyyy HH:mm")
        self.emergency_work_time_begin_date.setDateTime(self.date_work_str)

        self.emergency_work_time_end_date = QDateTimeEdit(self)
        self.emergency_work_time_end_date.setDisplayFormat("dd.MM.yyyy HH:mm")
        self.emergency_work_time_end_date.setDateTime(self.date_work_str)

        self.emergency_work_time_line = QLineEdit(self)
        self.emergency_work_time_line.setValidator(self.validator_float)

        self.grid.addWidget(self.emergency_work_time_begin_label, 30, 6)
        self.grid.addWidget(self.emergency_work_time_begin_date, 31, 6)
        self.grid.addWidget(self.emergency_work_time_end_label, 30, 7)
        self.grid.addWidget(self.emergency_work_time_end_date, 31, 7)
        self.grid.addWidget(self.emergency_work_time_label, 30, 8)
        self.grid.addWidget(self.emergency_work_time_line, 31, 8)

        self.emergency_work_time_end_date.dateTimeChanged.connect(self.update_date_of_raid)
        self.emergency_work_time_begin_date.dateTimeChanged.connect(self.update_date_of_raid)

        self.emergency_work_text_edit.editingFinished.connect(self.update_emergency_work)

    def update_emergency_work(self):
        text = self.emergency_work_text_edit.text()
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
        time_begin = self.emergency_work_time_begin_date.dateTime()
        time_end = self.emergency_work_time_end_date.dateTime()

        time_difference = self.calculate_date(time_begin, time_end)
        self.emergency_work_time_line.setText(str(time_difference))

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


class TabWidget(QTabWidget):
    def __init__(self):
        super().__init__()
        self.addTab(TabPage_SO_Timplate(self), 'ЛАР')


class EmergencyWork(TemplateWork):
    def __init__(self, ins_ind, table_widget, parent=None):
        super(QMainWindow, self).__init__()
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
        self.descent_layout_line = current_widget.descent_layout_line.text()
        if self.select_type_combo == '':
            return
        elif self.select_type_combo in ['НКТ', 'СБТ']:
            self.type_equipment = 'Ловильный инструмент'
            self.coefficient_lifting = 1

            self.emergency_work_text_edit = current_widget.emergency_work_text_edit.text()

            # self.count_of_nkt_extensions_line = current_widget.count_of_nkt_extensions_line.text()
            # if self.count_of_nkt_extensions_line != '':
            #     self.count_of_nkt_extensions_line = int(self.count_of_nkt_extensions_line)
            # else:
            #     question = QMessageBox.question(self, 'Бурение', 'Нормализации не было?')
            #     if question == QMessageBox.StandardButton.No:
            #         return

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

        read_data = self.read_nkt_up(current_widget)
        if read_data is None:
            return

        if self.nkt_is_same_combo == 'Нет':
            read_data = self.read_nkt_down(current_widget)
            if read_data is None:
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
        # if self.drilling_ek_combo == '':
        #     QMessageBox.warning(self, 'Нужно выбрать что бурили')
        #     return
        # self.select_type_drill_combo = current_widget.select_type_drill_combo.currentText()
        # if self.select_type_drill_combo == '':
        #     QMessageBox.warning(self, 'Нужно выбрать тип долото')
        #     return

        # self.pressuar_gno_combo = current_widget.pressuar_gno_combo.currentText()

        self.emergency_work_time_begin_date = \
            current_widget.emergency_work_time_begin_date.dateTime().toPyDateTime()
        self.emergency_work_time_begin_date = \
            self.change_string_in_date(self.emergency_work_time_begin_date)

        self.emergency_work_time_end_date = \
            current_widget.emergency_work_time_end_date.dateTime().toPyDateTime()
        self.emergency_work_time_end_date = \
            self.change_string_in_date(self.emergency_work_time_end_date)

        if self.emergency_work_time_end_date == self.emergency_work_time_begin_date:
            QMessageBox.warning(self, 'Даты совпадают', 'Даты совпадают')
            return

        self.emergency_work_time_line = current_widget.emergency_work_time_line.text()
        if self.emergency_work_time_line != '':
            self.emergency_work_time_line = round(float(self.emergency_work_time_line), 1)

        else:
            QMessageBox.warning(self, 'Ошибка', f'Не введены время осложнения при срыве ПШ')
            return

        if self.emergency_work_time_line <= 0:
            QMessageBox.warning(self, 'Ошибка', f'Затраченное время при срыве ПШ не может быть отрицательным')
            return

        if self.solvent_injection_combo == 'Да':
            read_data = self.read_solvent_volume(current_widget)
            if read_data is None:
                return

        if self.technological_crap_question_combo == 'Да':
            read_data = self.read_technological_crap_question(current_widget)
            if read_data is None:
                return

        if self.complications_of_failure_combo == 'Да':
            read_data = self.read_complications_of_failure(current_widget)
            if read_data is None:
                return

        if self.complications_during_tubing_running_combo == 'Да':
            read_data = self.read_complications_during_tubing_running_combo(current_widget)
            if read_data is None:
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

        work_list = self.emergency_work()

        well_data.date_work = self.date_work_line

        self.populate_row(self.ins_ind, work_list, self.table_widget)

        well_data.pause = False
        self.close()

    def raid_interval_work(self):
        work_list = []
        if self.volume_well_flush_line != '':
            work_list = self.installation_of_washing_equipment()
            drilling_list = [
                ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', 'ловильные работы с провыкой',
                 'ПЗР при промывке скважины', None,
                 None, None, None, None, None, None, None, None, None, None, None, '§159,161разд.1', None, 'шт', 1, 1,
                 1,
                 '=V700*W700*X700', '=Y700-AA700-AB700-AC700', None, None, None, None, None],
                ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', 'ловильные работы с провыкой',
                 'Опрессовка нагнетательной линии',
                 None, None, None, None, None, None, None, None, None, None, None, None, '§113 разд.1', None, 'раз', 1,
                 0.13, 1,
                 '=X701*W701*V701', '=Y701-AA701-AB701-AC701', None, None, None, None, None],
                ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', 'ловильные работы с провыкой',
                 'Промывка (вызов циркуляции)',
                 None, None, None, None, None, None, None, None, None, None, None, None, '§301разд.1п.119', None, 'м3',
                 5, 0.0333,
                 1, '=V702*W702*X702', '=Y702-AA702-AB702-AC702', None, None, None, None, None],
                ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', 'ловильные работы с провыкой',
                 'Ловля аварийных труб в скважине с промывкой', None, None, None, None, None, None, None, None, 'АКТ№',
                 None, None,
                 None, '§254разд.1', None, 'шт', 1, 0.55, 1, '=V703*W703*X703', '=Y703-AA703-AB703-AC703-AD703', None,
                 None, None,
                 None, None]
            ]
            work_list.extend(drilling_list)
        else:
            work_list.extend(['=ROW()-ROW($A$46)', None, None, 'Тех.операции', 'ловильные работы без провыки',
                              'Ловля аварийных труб в скважине без промывки', None, None, None, None, None, None, None,
                              None,
                              'АКТ№', None, None, None, '§254разд.1', None, 'шт', 1, 0.33, 1, '=V704*W704*X704',
                              '=Y704-AA704-AB704-AC704-AD704', None, None, None, None, None])
        lar_list = [
            ['=ROW()-ROW($A$46)', 'кроме ТВЛ, цанги, овершота', None, 'Тех.операции', 'ловильные работы с провыкой',
             f'{self.emergency_work_text_edit} {self.emergency_work_time_begin_date}-{self.emergency_work_time_end_date}',
             None, None, None, None, None, None, None, None, 'АКТ№', None, None, None, 'факт',
             None, 'час', self.emergency_work_time_line, 1, 1, '=V705*W705*X705', '=Y705-AA705-AB705-AC705-AD705',
             None, None, None, None, None]]
        # ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', 'расхаживание при прихватах',
        #  'Расхаживание при прихватах  (ВРЕМЯ)', None, None, None, None, None, None, None, None, 'АКТ№', None, None, None,
        #  'факт', None, 'час', 1, 1, 1, '=V706*W706*X706', '=Y706-AA706-AB706-AC706-AD706', None, None, None, None, None],
        # ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', 'ловильные работы с провыкой',
        #  'Ловля аварийных труб в скважине с промывкой', None, None, None, None, None, None, None, None, None, None, None,
        #  None, '§254разд.1', None, 'шт', 1, 0.55, 1, '=V707*W707*X707', '=Y707-AA707-AB707-AC707-AD707', None, None, None,
        #  None, None], ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', 'ловильные работы без провыки',
        #                'Ловля аварийных труб в скважине без промывки', None, None, None, None, None, None, None, None, None,
        #                None, None, None, '§254разд.1', None, 'шт', 1, 0.33, 1, '=V708*W708*X708',
        #                '=Y708-AA708-AB708-AC708-AD708', None, None, None, None, None],
        # ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', 'расхаживание при прихватах', 'Расхаживание при прихватах', None,
        #  None, None, None, None, None, None, None, None, None, None, None, 'факт', None, 'час', 1, 1, 1, '=V709*W709*X709',
        #  '=Y709-AA709-AB709-AC709-AD709', None, None, None, None, None]]
        work_list.extend(lar_list)

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

    def emergency_work(self):
        complications_of_failure_list = []
        complications_during_disassembly_list = []

        work_list = [
            ['=ROW()-ROW($A$46)', None, None, 'спо', 'Ловильный инструмент',
             'ПЗР СПО работы перед спуском ловильного инструмента (метчик, колокол, кабелерезка,'
             ' овершот, труболовка, крючок, мятая труба, щучья пасть )',
             None, None, None, None, None, None, None, None, None, None, None, None, '§240разд.1', None, 'шт', 1,
             0.17, 1,
             '=V693*W693*X693', '=Y693-AA693-AB693-AC693-AD693', None, None, None, None, None], ]

        work_spo_list = [
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'М/ж спайдера', None, None, None,
             None, None, None,
             None, None, None, None, None, None, '§185разд.1', None, 'час', 1, 0.07, 1, '=V731*W731*X731',
             '=Y731-AA731-AB731-AC731-AD731', None, None, None, None, None], ]

        work_spo_list.extend(self.work_pzr(self.descent_layout_line))

        if self.select_type_combo != 'СБТ':
            work_list.extend([['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', self.type_equipment, 'ПЗР СПО ЗД',
                               None, None, None,
                               None, None,
                               None, None, None, None, None, None, None, '§263разд.1', None, 'шт', 1, 0.38, 1,
                               '=V733*W733*X733',
                               '=Y733-AA733-AB733-AC733-AD733', None, None, None, None, None]])

        work_list.extend(work_spo_list)

        if len(self.dict_nkt) != 0:
            if self.select_type_combo == 'НКТ':
                work_list.extend(self.descent_nkt_work())
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
            work_list.extend(self.raid_interval_work())

        if self.select_type_combo == 'СБТ':
            work_list.extend(self.drilling_with_sbt_work_up())

        if self.solvent_injection_combo == 'Да':
            work_list.extend(self.solvent_injection_work())

        work_list.extend(self.deinstallation_of_washing_equipment())
        if self.select_type_combo == 'НКТ':
            work_list.extend(self.lifting_nkt())
        else:
            work_list.extend(self.lifting_SBT())
            well_data.count_SBT += 1

            if self.type_key_combo == 'Да':
                work_list.extend(self.deinstallation_key())

        if self.equipment_audit_combo == 'Да':
            if 'ОВ-' in self.descent_layout_line or 'щучь' in self.descent_layout_line or 'мятой трубы' in self.descent_layout_line:
                work_list.extend([
                    ['=ROW()-ROW($A$46)', None, None, 'спо', 'Ловильный инструмент',
                     'Освобождение овершота, мятой трубы, щучьей пасти',
                     None, None, None, None, None, None, None, None, None, None, None, None, '§242разд.1', None, 'шт',
                     1, 0.32,
                     1,
                     '=V720*W720*X720', '=Y720-AA720-AB720-AC720-AD720', None, None, None, None, None]])
            elif 'колокол' in self.descent_layout_line:
                work_list.extend([
                    ['=ROW()-ROW($A$46)', None, None, 'спо', 'Ловильный инструмент', 'Освобождение колокола', None,
                     None, None,
                     None,
                     None, None, None, None, None, None, None, None, '§242разд.1', None, 'шт', 1, 0.33, 1,
                     '=V721*W721*X721',
                     '=Y721-AA721-AB721-AC721-AD721', None, None, None, None, None]])
            elif 'наружней труболовки' in self.descent_layout_line:
                 work_list.extend(  [ 
                ['=ROW()-ROW($A$46)', None, None, 'спо', 'Ловильный инструмент', 'Освобождение наружней труболовки', None,
                    None,
                    None, None, None, None, None, None, None, None, None, None, '§242разд.1', None, 'шт', 1, 0.38, 1,
                    '=V722*W722*X722', '=Y722-AA722-AB722-AC722-AD722', None, None, None, None, None]])
            elif 'Крючок' in self.descent_layout_line:
                work_list.extend([
                ['=ROW()-ROW($A$46)', None, None, 'спо', 'Ловильный инструмент', 'Освобождение крючка', None, None,
                 None,
                 None,
                 None, None, None, None, None, None, None, None, '§242разд.1', None, 'шт', 1, 0.23, 1,
                 '=V723*W723*X723',
                 '=Y723-AA723-AB723-AC723-AD723', None, None, None, None, None]])
            elif 'шлипс' in self.descent_layout_line:
                work_list.extend([
                ['=ROW()-ROW($A$46)', None, None, 'спо', 'Ловильный инструмент', 'Освобождение шлипса', None, None,
                 None,
                 None,
                 None, None, None, None, None, None, None, None, '§242разд.1', None, 'шт', 1, 0.2, 1, '=V724*W724*X724',
                 '=Y724-AA724-AB724-AC724-AD724', None, None, None, None, None]])
            elif 'метчик' in self.descent_layout_line or 'ВТ' in self.descent_layout_line:
                work_list.extend([['=ROW()-ROW($A$46)', None, None, 'спо', 'Ловильный инструмент',
                 'Освобождение труболовки внутренней, метчика',
                 None, None, None, None, None, None, None, None, None, None, None, None, '§242разд.1', None, 'шт', 1,
                 0.27,
                 1,
                 '=V725*W725*X725', '=Y725-AA725-AB725-AC725-AD725', None, None, None, None, None]])

        else:
            work_list.extend(
                ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None, 'ЗР после подъема ловиля (холостая ходка)',
                 None, None, None, None, None, None, None, None, None, None, None, None, '§241разд.1', None, 'шт',
                 1, 0.13, 1,
                 '=V718*W718*X718', '=Y718-AA718-AB718-AC718-AD718', None, None, None, None, None])

        return work_list

    def drilling_with_sbt_work_up(self):
        work_list = [

            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'Демонтаж спецтрубы', None, None,
             None, None,
             None,
             None, None, None, None, None, None, None, '§300разд.1 п.148', None, 'шт', 1, 0.27, 1,
             '=V932*W932*X932',
             '=Y932-AA932-AB932-AC932-AD932', None, None, None, None, None]]
        if self.type_rotor_combo == 'Гидроротор':
            work_list.extend([
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'Демонтаж гидроротора ',
                 None,
                 None, None, None,
                 None, None, None, None, None, None, None, None, '§245разд.1', None, 'шт', 1, 0.38, 1,
                 '=V933*W933*X933',
                 '=Y933-AA933-AB933-AC933-AD933', None, None, None, None, None]])
        else:
            work_list.extend([
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'Демонтаж мех. ротора', None,
                 None, None, None,
                 None, None, None, None, None, None, None, None, '§247разд.1', None, 'шт', 1, 0.68, 1,
                 '=V934*W934*X934',
                 '=Y934-AA934-AB934-AC934-AD934', None, None, None, None, None]])

        if self.type_key_combo == 'Да':
            if self.count_spo_sbt_combo == 'Да':
                work_list.extend([
                    ['=ROW()-ROW($A$46)', 'подъем СБТ с УМК', None, 'Тех.операции', None,
                     'М/ж машинных ключей (первый монтаж)',
                     None, None, None, None, None, None, None, None, None, None, None, None, '§256разд.1', None,
                     'час',
                     1,
                     1, 1,
                     '=V936*W936*X936', '=Y936-AA936-AB936-AC936-AD936', None, None, None, None, None]])
            else:
                work_list.extend(
                    [['=ROW()-ROW($A$46)', 'подъем СБТ', None, 'Тех.операции', None,
                      'М/ж машинных ключей (след.монтаж)',
                      None, None, None, None, None, None, None, None, None, None, None, None, '§256разд.1', None,
                      'час',
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
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'Демонтаж спайдера СПГ', None,
                 None,
                 None, None,
                 None, None, None, None, None, None, None, None, '§185разд.1', None, 'шт', 1, 0.07, 1,
                 '=V922*W922*X922',
                 '=Y922-AA922-AB922-AC922-AD922', None, None, None, None, None],
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
                 'Демонтаж гидравлических ключей трубных(ГШК-1200, ГШК-1500 )', None, None, None, None, None, None,
                 None,
                 None, None, None, None, None, '§184разд.1', None, 'шт', 1, 0.12, 1, '=V923*W923*X923',
                 '=Y923-AA923-AB923-AC923-AD923', None, None, None, None, None]]
            if self.type_rotor_combo == 'Гидротор':
                work_list.extend([
                    ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'Монтаж гидроротора', None,
                     None,
                     None,
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
                        ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'Монтаж мех. ротора',
                         None,
                         None, None,
                         None, None,
                         None, None, None, None, None, None, None, '§246разд.1', None, 'шт', 1, 1.02, 1,
                         '=V926*W926*X926',
                         '=Y926-AA926-AB926-AC926-AD926', None, None, None, None, None]])

                work_list.extend([
                    ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'Монтаж  ведущий трубы',
                     None,
                     None, None,
                     None,
                     None, None, None, None, None, None, None, None, '§300разд.1 п.148', None, 'шт', 1, 0.27, 1,
                     '=V927*W927*X927', '=Y927-AA927-AB927-AC927-AD927', None, None, None, None, None]])

            return work_list

sss = [
    ['=ROW()-ROW($A$46)', None, None, 'спо', 'Ловильный инструмент',
     'ПЗР СПО работы перед спуском ловильного инструмента (метчик, колокол, кабелерезка, овершот, труболовка, крючок, мятая труба, щучья пасть )',
     None, None, None, None, None, None, None, None, None, None, None, None, '§240разд.1', None, 'шт', 1, 0.17, 1,
     '=V693*W693*X693', '=Y693-AA693-AB693-AC693-AD693', None, None, None, None, None],
    ['=ROW()-ROW($A$46)', None, None, 'спо', 'Ловильный инструмент', 'Спуск НКТ компоновка ', None, None, None,
     None,
     None, '73мм', 1500,
     '=IF(AND(M694/V694>=ЦИКЛ!$V$9,M694/V694<=ЦИКЛ!$W$9),ЦИКЛ!$U$9,IF(AND(M694/V694>=ЦИКЛ!$V$10,M694/V694<=ЦИКЛ!$W$10),ЦИКЛ!$U$10,IF(AND(M694/V694>=ЦИКЛ!$V$11,M694/V694<=ЦИКЛ!$W$11),ЦИКЛ!$U$11,IF(AND(M694/V694>=ЦИКЛ!$V$12,M694/V694<=ЦИКЛ!$W$12),ЦИКЛ!$U$12,IF(AND(M694/V694>=ЦИКЛ!$V$13,M694/V694<=ЦИКЛ!$W$13),ЦИКЛ!$U$13,IF(AND(M694/V694>=ЦИКЛ!$V$14,M694/V694<=ЦИКЛ!$W$14),ЦИКЛ!$U$14))))))',
     None, None, None, None,
     '=IF($AD$8=ЦИКЛ!$A$4,ЦИКЛ!$P$4,IF($AD$8=ЦИКЛ!$A$7,ЦИКЛ!$P$7,IF($AD$8=ЦИКЛ!$A$10,ЦИКЛ!$P$7,IF($AD$8=ЦИКЛ!$A$52,ЦИКЛ!$P$52,IF($AD$8=ЦИКЛ!$A$70,ЦИКЛ!$P$70,IF($AD$8=ЦИКЛ!$A$88,ЦИКЛ!$P$88,IF($AD$8=ЦИКЛ!$A$106,ЦИКЛ!$P$106,IF($AD$8=ЦИКЛ!$A$133,ЦИКЛ!$P$133,IF($AD$8=ЦИКЛ!$Q$4,ЦИКЛ!$P$4,IF($AD$8=ЦИКЛ!$R$4,ЦИКЛ!$P$4))))))))))',
     None, 'шт', 150,
     '=IF(AND($AD$8=ЦИКЛ!$A$4,ЦИКЛ!$D$3=N694,ЦИКЛ!$B$37=АВР!L694),ЦИКЛ!$D$37,IF(AND($AD$8=ЦИКЛ!$A$4,ЦИКЛ!$E$3=N694,ЦИКЛ!$B$37=АВР!L694),ЦИКЛ!$E$37,IF(AND($AD$8=ЦИКЛ!$A$4,ЦИКЛ!$F$3=N694,ЦИКЛ!$B$37=АВР!L694),ЦИКЛ!$F$37,IF(AND($AD$8=ЦИКЛ!$A$4,ЦИКЛ!$G$3=N694,ЦИКЛ!$B$37=АВР!L694),ЦИКЛ!$G$37,IF(AND($AD$8=ЦИКЛ!$A$4,ЦИКЛ!$H$3=N694,ЦИКЛ!$B$37=АВР!L694),ЦИКЛ!$H$37,IF(AND($AD$8=ЦИКЛ!$A$4,ЦИКЛ!$I$3=N694,ЦИКЛ!$B$37=АВР!L694),ЦИКЛ!$I$37,IF(AND($AD$8=ЦИКЛ!$Q$4,ЦИКЛ!$D$3=N694,ЦИКЛ!$B$37=АВР!L694),ЦИКЛ!$D$37,IF(AND($AD$8=ЦИКЛ!$Q$4,ЦИКЛ!$E$3=N694,ЦИКЛ!$B$37=АВР!L694),ЦИКЛ!$E$37,IF(AND($AD$8=ЦИКЛ!$Q$4,ЦИКЛ!$F$3=N694,ЦИКЛ!$B$37=АВР!L694),ЦИКЛ!$F$37,IF(AND($AD$8=ЦИКЛ!$Q$4,ЦИКЛ!$G$3=N694,ЦИКЛ!$B$37=АВР!L694),ЦИКЛ!$G$37,IF(AND($AD$8=ЦИКЛ!$Q$4,ЦИКЛ!$H$3=N694,ЦИКЛ!$B$37=АВР!L694),ЦИКЛ!$H$37,IF(AND($AD$8=ЦИКЛ!$Q$4,ЦИКЛ!$I$3=N694,ЦИКЛ!$B$37=АВР!L694),ЦИКЛ!$I$37,IF(AND($AD$8=ЦИКЛ!$R$4,ЦИКЛ!$D$3=N694,ЦИКЛ!$B$37=АВР!L694),ЦИКЛ!$D$37,IF(AND($AD$8=ЦИКЛ!$R$4,ЦИКЛ!$E$3=N694,ЦИКЛ!$B$37=АВР!L694),ЦИКЛ!$E$37,IF(AND($AD$8=ЦИКЛ!$R$4,ЦИКЛ!$F$3=N694,ЦИКЛ!$B$37=АВР!L694),ЦИКЛ!$F$37,IF(AND($AD$8=ЦИКЛ!$R$4,ЦИКЛ!$G$3=N694,ЦИКЛ!$B$37=АВР!L694),ЦИКЛ!$G$37,IF(AND($AD$8=ЦИКЛ!$R$4,ЦИКЛ!$H$3=N694,ЦИКЛ!$B$37=АВР!L694),ЦИКЛ!$H$37,IF(AND($AD$8=ЦИКЛ!$R$4,ЦИКЛ!$I$3=N694,ЦИКЛ!$B$37=АВР!L694),ЦИКЛ!$I$37,IF(AND($AD$8=ЦИКЛ!$A$7,ЦИКЛ!$D$3=N694,ЦИКЛ!$B$37=АВР!L694),ЦИКЛ!$D$37,IF(AND($AD$8=ЦИКЛ!$A$7,ЦИКЛ!$E$3=N694,ЦИКЛ!$B$37=АВР!L694),ЦИКЛ!$E$37,IF(AND($AD$8=ЦИКЛ!$A$7,ЦИКЛ!$F$3=N694,ЦИКЛ!$B$37=АВР!L694),ЦИКЛ!$F$37,IF(AND($AD$8=ЦИКЛ!$A$7,ЦИКЛ!$G$3=N694,ЦИКЛ!$B$37=АВР!L694),ЦИКЛ!$G$37,IF(AND($AD$8=ЦИКЛ!$A$7,ЦИКЛ!$H$3=N694,ЦИКЛ!$B$37=АВР!L694),ЦИКЛ!$H$37,IF(AND($AD$8=ЦИКЛ!$A$7,ЦИКЛ!$I$3=N694,ЦИКЛ!$B$37=АВР!L694),ЦИКЛ!$I$37,IF(AND($AD$8=ЦИКЛ!$A$10,ЦИКЛ!$D$3=N694,ЦИКЛ!$B$37=АВР!L694),ЦИКЛ!$D$37,IF(AND($AD$8=ЦИКЛ!$A$10,ЦИКЛ!$E$3=N694,ЦИКЛ!$B$37=АВР!L694),ЦИКЛ!$E$37,IF(AND($AD$8=ЦИКЛ!$A$10,ЦИКЛ!$F$3=N694,ЦИКЛ!$B$37=АВР!L694),ЦИКЛ!$F$37,IF(AND($AD$8=ЦИКЛ!$A$10,ЦИКЛ!$G$3=N694,ЦИКЛ!$B$37=АВР!L694),ЦИКЛ!$G$37,IF(AND($AD$8=ЦИКЛ!$A$10,ЦИКЛ!$H$3=N694,ЦИКЛ!$B$37=АВР!L694),ЦИКЛ!$H$37,IF(AND($AD$8=ЦИКЛ!$A$10,ЦИКЛ!$I$3=N694,ЦИКЛ!$B$37=АВР!L694),ЦИКЛ!$I$37,IF(AND($AD$8=ЦИКЛ!$A$52,ЦИКЛ!$D$3=N694,ЦИКЛ!$B$37=АВР!L694),ЦИКЛ!$D$63,IF(AND($AD$8=ЦИКЛ!$A$52,ЦИКЛ!$E$3=N694,ЦИКЛ!$B$37=АВР!L694),ЦИКЛ!$E$63,IF(AND($AD$8=ЦИКЛ!$A$52,ЦИКЛ!$F$3=N694,ЦИКЛ!$B$37=АВР!L694),ЦИКЛ!$F$63,IF(AND($AD$8=ЦИКЛ!$A$52,ЦИКЛ!$G$3=N694,ЦИКЛ!$B$37=АВР!L694),ЦИКЛ!$G$63,IF(AND($AD$8=ЦИКЛ!$A$52,ЦИКЛ!$H$3=N694,ЦИКЛ!$B$37=АВР!L694),ЦИКЛ!$H$63,IF(AND($AD$8=ЦИКЛ!$A$52,ЦИКЛ!$I$3=N694,ЦИКЛ!$B$37=АВР!L694),ЦИКЛ!$I$63,IF(AND($AD$8=ЦИКЛ!$A$70,ЦИКЛ!$D$3=N694,ЦИКЛ!$B$37=АВР!L694),ЦИКЛ!$D$81,IF(AND($AD$8=ЦИКЛ!$A$70,ЦИКЛ!$E$3=N694,ЦИКЛ!$B$37=АВР!L694),ЦИКЛ!$E$81,IF(AND($AD$8=ЦИКЛ!$A$70,ЦИКЛ!$F$3=N694,ЦИКЛ!$B$37=АВР!L694),ЦИКЛ!$F$81,IF(AND($AD$8=ЦИКЛ!$A$70,ЦИКЛ!$G$3=N694,ЦИКЛ!$B$37=АВР!L694),ЦИКЛ!$G$81,IF(AND($AD$8=ЦИКЛ!$A$70,ЦИКЛ!$H$3=N694,ЦИКЛ!$B$37=АВР!L694),ЦИКЛ!$H$81,IF(AND($AD$8=ЦИКЛ!$A$70,ЦИКЛ!$I$3=N694,ЦИКЛ!$B$37=АВР!L694),ЦИКЛ!$I$81,IF(AND($AD$8=ЦИКЛ!$A$88,ЦИКЛ!$D$3=N694,ЦИКЛ!$B$37=АВР!L694),ЦИКЛ!$D$99,IF(AND($AD$8=ЦИКЛ!$A$88,ЦИКЛ!$E$3=N694,ЦИКЛ!$B$37=АВР!L694),ЦИКЛ!$E$99,IF(AND($AD$8=ЦИКЛ!$A$88,ЦИКЛ!$F$3=N694,ЦИКЛ!$B$37=АВР!L694),ЦИКЛ!$F$99,IF(AND($AD$8=ЦИКЛ!$A$88,ЦИКЛ!$G$3=N694,ЦИКЛ!$B$37=АВР!L694),ЦИКЛ!$G$99,IF(AND($AD$8=ЦИКЛ!$A$88,ЦИКЛ!$H$3=N694,ЦИКЛ!$B$37=АВР!L694),ЦИКЛ!$H$99,IF(AND($AD$8=ЦИКЛ!$A$88,ЦИКЛ!$I$3=N694,ЦИКЛ!$B$37=АВР!L694),ЦИКЛ!$I$99,IF(AND($AD$8=ЦИКЛ!$A$106,ЦИКЛ!$D$3=N694,ЦИКЛ!$B$37=АВР!L694),ЦИКЛ!$D$120,IF(AND($AD$8=ЦИКЛ!$A$106,ЦИКЛ!$E$3=N694,ЦИКЛ!$B$37=АВР!L694),ЦИКЛ!$E$120,IF(AND($AD$8=ЦИКЛ!$A$106,ЦИКЛ!$F$3=N694,ЦИКЛ!$B$37=АВР!L694),ЦИКЛ!$F$120,IF(AND($AD$8=ЦИКЛ!$A$106,ЦИКЛ!$G$3=N694,ЦИКЛ!$B$37=АВР!L694),ЦИКЛ!$G$120,IF(AND($AD$8=ЦИКЛ!$A$106,ЦИКЛ!$H$3=N694,ЦИКЛ!$B$37=АВР!L694),ЦИКЛ!$H$120,IF(AND($AD$8=ЦИКЛ!$A$106,ЦИКЛ!$I$3=N694,ЦИКЛ!$B$37=АВР!L694),ЦИКЛ!$I$120,IF(AND($AD$8=ЦИКЛ!$A$128,ЦИКЛ!$D$3=N694,ЦИКЛ!$B$37=АВР!L694),ЦИКЛ!$D$142,IF(AND($AD$8=ЦИКЛ!$A$128,ЦИКЛ!$E$3=N694,ЦИКЛ!$B$37=АВР!L694),ЦИКЛ!$E$142,IF(AND($AD$8=ЦИКЛ!$A$128,ЦИКЛ!$F$3=N694,ЦИКЛ!$B$37=АВР!L694),ЦИКЛ!$F$142,IF(AND($AD$8=ЦИКЛ!$A$128,ЦИКЛ!$G$3=N694,ЦИКЛ!$B$37=АВР!L694),ЦИКЛ!$G$142,IF(AND($AD$8=ЦИКЛ!$A$128,ЦИКЛ!$H$3=N694,ЦИКЛ!$B$37=АВР!L694),ЦИКЛ!$H$142,IF(AND(АВР!$AD$8=ЦИКЛ!$A$128,ЦИКЛ!$I$3=N694,ЦИКЛ!$B$37=АВР!L694),ЦИКЛ!$I$142))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))',
     1, '=V694*W694*X694', '=Y694-AA694-AB694-AC694-AD694', None, None, None, None, None],
    ['=ROW()-ROW($A$46)', None, None, 'спо', 'Ловильный инструмент', 'Навернуть/отвернуть предохранительное кольцо',
     None, None, None, None, None, None, None, None, None, None, None, None, '§300разд.1', None, 'шт', '=SUM(V694)',
     0.003, 1, '=V695*W695*X695', '=Y695-AA695-AB695-AC695-AD695', None, None, None, None, None],
    ['=ROW()-ROW($A$46)', None, None, 'спо', 'Ловильный инструмент', 'Замер НКТ ', None, None, None, None, None,
     None,
     None, None, None, None, None, None, '§47разд.1', None, 'шт', None, '=0.5/60', 1, '=V696*W696*X696',
     '=Y696-AA696-AB696-AC696-AD696', None, None, None, None, None],
    ['=ROW()-ROW($A$46)', 'спуск 73мм', None, 'спо', 'Ловильный инструмент', 'Подкатывание труб с 201 трубы ', None,
     None, None, None, None, None, None, None, None, None, None, None, '§40разд.1', None, 'шт', None, 0.008, 1,
     '=V697*W697*X697', '=Y697-AA697-AB697-AC697-AD697', None, None, None, None, None],
    ['=ROW()-ROW($A$46)', None, None, 'спо', 'Ловильный инструмент', 'Осложнение при спуске НКТ-вытеснение (ВРЕМЯ)',
     None, None, None, None, None, None, 'Объем', 0, 'АКТ№', None, None, None, 'факт', None, 'час', 0, 1, 1,
     '=V698*W698*X698', '=Y698-AA698-AB698-AC698-AD698', None, None, None, None, None],
    ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None, 'Д/ж, м/ж спайдера', None, None, None, None, None, None,
     None, None, None, None, None, None, '§185разд.1', None, 'час', 1, 0.14, 1, '=V699*W699*X699',
     '=Y699-AA699-AB699-AC699-AD699', None, None, None, None, None],
    ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', 'ловильные работы с провыкой', 'ПЗР при промывке скважины',
     None,
     None, None, None, None, None, None, None, None, None, None, None, '§159,161разд.1', None, 'шт', 1, 1, 1,
     '=V700*W700*X700', '=Y700-AA700-AB700-AC700', None, None, None, None, None],
    ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', 'ловильные работы с провыкой',
     'Опрессовка нагнетательной линии',
     None, None, None, None, None, None, None, None, None, None, None, None, '§113 разд.1', None, 'раз', 1, 0.13, 1,
     '=X701*W701*V701', '=Y701-AA701-AB701-AC701', None, None, None, None, None],
    ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', 'ловильные работы с провыкой', 'Промывка (вызов циркуляции)',
     None, None, None, None, None, None, None, None, None, None, None, None, '§301разд.1п.119', None, 'м3', 5,
     0.0333,
     1, '=V702*W702*X702', '=Y702-AA702-AB702-AC702', None, None, None, None, None],
    ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', 'ловильные работы с провыкой',
     'Ловля аварийных труб в скважине с промывкой', None, None, None, None, None, None, None, None, 'АКТ№', None,
     None,
     None, '§254разд.1', None, 'шт', 1, 0.55, 1, '=V703*W703*X703', '=Y703-AA703-AB703-AC703-AD703', None, None,
     None,
     None, None], ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', 'ловильные работы без провыки',
                   'Ловля аварийных труб в скважине без промывки', None, None, None, None, None, None, None, None,
                   'АКТ№', None, None, None, '§254разд.1', None, 'шт', 1, 0.33, 1, '=V704*W704*X704',
                   '=Y704-AA704-AB704-AC704-AD704', None, None, None, None, None],
    ['=ROW()-ROW($A$46)', 'кроме ТВЛ, цанги, овершота', None, 'Тех.операции', 'ловильные работы с провыкой',
     'Ловильные работы  (ВРЕМЯ)', None, None, None, None, None, None, None, None, 'АКТ№', None, None, None, 'факт',
     None, 'час', 1, 1, 1, '=V705*W705*X705', '=Y705-AA705-AB705-AC705-AD705', None, None, None, None, None],
    ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', 'расхаживание при прихватах',
     'Расхаживание при прихватах  (ВРЕМЯ)', None, None, None, None, None, None, None, None, 'АКТ№', None, None,
     None,
     'факт', None, 'час', 1, 1, 1, '=V706*W706*X706', '=Y706-AA706-AB706-AC706-AD706', None, None, None, None,
     None],
    ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', 'ловильные работы с провыкой',
     'Ловля аварийных труб в скважине с промывкой', None, None, None, None, None, None, None, None, None, None,
     None,
     None, '§254разд.1', None, 'шт', 1, 0.55, 1, '=V707*W707*X707', '=Y707-AA707-AB707-AC707-AD707', None, None,
     None,
     None, None], ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', 'ловильные работы без провыки',
                   'Ловля аварийных труб в скважине без промывки', None, None, None, None, None, None, None, None,
                   None,
                   None, None, None, '§254разд.1', None, 'шт', 1, 0.33, 1, '=V708*W708*X708',
                   '=Y708-AA708-AB708-AC708-AD708', None, None, None, None, None],
    ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', 'расхаживание при прихватах', 'Расхаживание при прихватах',
     None,
     None, None, None, None, None, None, None, None, None, None, None, 'факт', None, 'час', 1, 1, 1,
     '=V709*W709*X709',
     '=Y709-AA709-AB709-AC709-AD709', None, None, None, None, None],
    ['=ROW()-ROW($A$46)', None, None, 'спо', 'Ловильный инструмент', 'Подъем НКТ  1 скорость ', None, None, None,
     None,
     '73мм', 1000,
     '=IF(AND(L710/V710>=ЦИКЛ!$V$9,L710/V710<=ЦИКЛ!$W$9),ЦИКЛ!$U$9,IF(AND(L710/V710>=ЦИКЛ!$V$10,L710/V710<=ЦИКЛ!$W$10),ЦИКЛ!$U$10,IF(AND(L710/V710>=ЦИКЛ!$V$11,L710/V710<=ЦИКЛ!$W$11),ЦИКЛ!$U$11,IF(AND(L710/V710>=ЦИКЛ!$V$12,L710/V710<=ЦИКЛ!$W$12),ЦИКЛ!$U$12,IF(AND(L710/V710>=ЦИКЛ!$V$13,L710/V710<=ЦИКЛ!$W$13),ЦИКЛ!$U$13,IF(AND(L710/V710>=ЦИКЛ!$V$14,L710/V710<=ЦИКЛ!$W$14),ЦИКЛ!$U$14))))))',
     '=IF(AND(АВР!$AD$8=ЦИКЛ!$A$4,ЦИКЛ!$D$3=M710),ЦИКЛ!$J$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$4,ЦИКЛ!$E$3=M710),ЦИКЛ!$K$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$4,ЦИКЛ!$F$3=M710),ЦИКЛ!$L$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$4,ЦИКЛ!$M$3=M710),ЦИКЛ!$M$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$4,ЦИКЛ!$H$3=M710),ЦИКЛ!$N$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$4,ЦИКЛ!$I$3=M710),ЦИКЛ!$O$28,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$4,ЦИКЛ!$D$3=M710),ЦИКЛ!$J$28,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$4,ЦИКЛ!$E$3=M710),ЦИКЛ!$K$28,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$4,ЦИКЛ!$F$3=M710),ЦИКЛ!$L$28,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$4,ЦИКЛ!$G$3=M710),ЦИКЛ!$M$28,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$4,ЦИКЛ!$H$3=M710),ЦИКЛ!$N$28,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$4,ЦИКЛ!$O$3=M710),ЦИКЛ!$I$28,IF(AND(АВР!$AD$8=ЦИКЛ!$R$4,ЦИКЛ!$D$3=M710),ЦИКЛ!$J$28,IF(AND(АВР!$AD$8=ЦИКЛ!$R$4,ЦИКЛ!$E$3=M710),ЦИКЛ!$K$28,IF(AND(АВР!$AD$8=ЦИКЛ!$R$4,ЦИКЛ!$F$3=M710),ЦИКЛ!$L$28,IF(AND(АВР!$AD$8=ЦИКЛ!$R$4,ЦИКЛ!$G$3=M710),ЦИКЛ!$M$28,IF(AND(АВР!$AD$8=ЦИКЛ!$R$4,ЦИКЛ!$N$3=M710),ЦИКЛ!$H$28,IF(AND(АВР!$AD$8=ЦИКЛ!$R$4,ЦИКЛ!$I$3=M710),ЦИКЛ!$O$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$7,ЦИКЛ!$D$3=M710),ЦИКЛ!$J$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$7,ЦИКЛ!$E$3=M710),ЦИКЛ!$K$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$7,ЦИКЛ!$F$3=M710),ЦИКЛ!$L$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$7,ЦИКЛ!$G$3=M710),ЦИКЛ!$M$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$7,ЦИКЛ!$N$3=M710),ЦИКЛ!$H$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$7,ЦИКЛ!$I$3=M710),ЦИКЛ!$O$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$10,ЦИКЛ!$D$3=M710),ЦИКЛ!$J$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$10,ЦИКЛ!$E$3=M710),ЦИКЛ!$K$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$10,ЦИКЛ!$F$3=M710),ЦИКЛ!$L$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$10,ЦИКЛ!$G$3=M710),ЦИКЛ!$M$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$10,ЦИКЛ!$H$3=M710),ЦИКЛ!$N$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$10,ЦИКЛ!$I$3=M710),ЦИКЛ!$O$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$52,ЦИКЛ!$D$3=M710),ЦИКЛ!$J$60,IF(AND(АВР!$AD$8=ЦИКЛ!$A$52,ЦИКЛ!$E$3=M710),ЦИКЛ!$K$60,IF(AND(АВР!$AD$8=ЦИКЛ!$A$52,ЦИКЛ!$F$3=M710),ЦИКЛ!$L$60,IF(AND(АВР!$AD$8=ЦИКЛ!$A$52,ЦИКЛ!$G$3=M710),ЦИКЛ!$M$60,IF(AND(АВР!$AD$8=ЦИКЛ!$A$52,ЦИКЛ!$H$3=M710),ЦИКЛ!$N$60,IF(AND(АВР!$AD$8=ЦИКЛ!$A$52,ЦИКЛ!$I$3=M710),ЦИКЛ!$O$60,IF(AND(АВР!$AD$8=ЦИКЛ!$A$70,ЦИКЛ!$D$3=M710),ЦИКЛ!$J$78,IF(AND(АВР!$AD$8=ЦИКЛ!$A$70,ЦИКЛ!$E$3=M710),ЦИКЛ!$K$78,IF(AND(АВР!$AD$8=ЦИКЛ!$A$70,ЦИКЛ!$F$3=M710),ЦИКЛ!$L$78,IF(AND(АВР!$AD$8=ЦИКЛ!$A$70,ЦИКЛ!$G$3=M710),ЦИКЛ!$M$78,IF(AND(АВР!$AD$8=ЦИКЛ!$A$70,ЦИКЛ!$H$3=M710),ЦИКЛ!$N$78,IF(AND(АВР!$AD$8=ЦИКЛ!$A$70,ЦИКЛ!$I$3=M710),ЦИКЛ!$O$78,IF(AND(АВР!$AD$8=ЦИКЛ!$A$88,ЦИКЛ!$D$3=M710),ЦИКЛ!$J$96,IF(AND(АВР!$AD$8=ЦИКЛ!$A$88,ЦИКЛ!$E$3=M710),ЦИКЛ!$K$96,IF(AND(АВР!$AD$8=ЦИКЛ!$A$88,ЦИКЛ!$F$3=M710),ЦИКЛ!$L$96,IF(AND(АВР!$AD$8=ЦИКЛ!$A$88,ЦИКЛ!$G$3=M710),ЦИКЛ!$M$96,IF(AND(АВР!$AD$8=ЦИКЛ!$A$88,ЦИКЛ!$H$3=M710),ЦИКЛ!$N$96,IF(AND(АВР!$AD$8=ЦИКЛ!$A$88,ЦИКЛ!$I$3=M710),ЦИКЛ!$O$96,IF(AND(АВР!$AD$8=ЦИКЛ!$A$116,ЦИКЛ!$D$3=M710),ЦИКЛ!$J$116,IF(AND(АВР!$AD$8=ЦИКЛ!$A$116,ЦИКЛ!$E$3=M710),ЦИКЛ!$K$116,IF(AND(АВР!$AD$8=ЦИКЛ!$A$116,ЦИКЛ!$F$3=M710),ЦИКЛ!$L$116,IF(AND(АВР!$AD$8=ЦИКЛ!$A$116,ЦИКЛ!$G$3=M710),ЦИКЛ!$M$116,IF(AND(АВР!$AD$8=ЦИКЛ!$A$116,ЦИКЛ!$H$3=M710),ЦИКЛ!$N$116,IF(AND(АВР!$AD$8=ЦИКЛ!$A$116,ЦИКЛ!$I$3=M710),ЦИКЛ!$O$116,IF(AND(АВР!$AD$8=ЦИКЛ!$A$128,ЦИКЛ!$D$3=M710),ЦИКЛ!$J$138,IF(AND(АВР!$AD$8=ЦИКЛ!$A$128,ЦИКЛ!$E$3=M710),ЦИКЛ!$K$138,IF(AND(АВР!$AD$8=ЦИКЛ!$A$128,ЦИКЛ!$F$3=M710),ЦИКЛ!$L$138,IF(AND(АВР!$AD$8=ЦИКЛ!$A$128,ЦИКЛ!$G$3=M710),ЦИКЛ!$M$138,IF(AND(АВР!$AD$8=ЦИКЛ!$A$128,ЦИКЛ!$H$3=M710),ЦИКЛ!$N$138,IF(AND(АВР!$AD$8=ЦИКЛ!$A$128,ЦИКЛ!$I$3=M710),ЦИКЛ!$O$138))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))',
     None, None, None, None,
     '=IF($AD$8=ЦИКЛ!$A$4,ЦИКЛ!$P$4,IF($AD$8=ЦИКЛ!$A$7,ЦИКЛ!$P$7,IF($AD$8=ЦИКЛ!$A$10,ЦИКЛ!$P$7,IF($AD$8=ЦИКЛ!$A$52,ЦИКЛ!$P$52,IF($AD$8=ЦИКЛ!$A$70,ЦИКЛ!$P$70,IF($AD$8=ЦИКЛ!$A$88,ЦИКЛ!$P$88,IF($AD$8=ЦИКЛ!$A$106,ЦИКЛ!$P$106,IF($AD$8=ЦИКЛ!$A$133,ЦИКЛ!$P$133,IF($AD$8=ЦИКЛ!$Q$4,ЦИКЛ!$P$4,IF($AD$8=ЦИКЛ!$R$4,ЦИКЛ!$P$4))))))))))',
     None, 'шт', 100,
     '=IF(AND(АВР!$AD$8=ЦИКЛ!$A$4,ЦИКЛ!$D$3=M710,ЦИКЛ!$B$37=АВР!K710),ЦИКЛ!$D$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$4,ЦИКЛ!$E$3=M710,ЦИКЛ!$B$37=АВР!K710),ЦИКЛ!$E$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$4,ЦИКЛ!$F$3=M710,ЦИКЛ!$B$37=АВР!K710),ЦИКЛ!$F$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$4,ЦИКЛ!$G$3=M710,ЦИКЛ!$B$37=АВР!K710),ЦИКЛ!$G$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$4,ЦИКЛ!$H$3=M710,ЦИКЛ!$B$37=АВР!K710),ЦИКЛ!$H$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$4,ЦИКЛ!$I$3=M710,ЦИКЛ!$B$37=АВР!K710),ЦИКЛ!$I$28,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$4,ЦИКЛ!$D$3=M710,ЦИКЛ!$B$37=АВР!K710),ЦИКЛ!$D$28,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$4,ЦИКЛ!$E$3=M710,ЦИКЛ!$B$37=АВР!K710),ЦИКЛ!$E$28,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$4,ЦИКЛ!$F$3=M710,ЦИКЛ!$B$37=АВР!K710),ЦИКЛ!$F$28,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$4,ЦИКЛ!$G$3=M710,ЦИКЛ!$B$37=АВР!K710),ЦИКЛ!$G$28,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$4,ЦИКЛ!$H$3=M710,ЦИКЛ!$B$37=АВР!K710),ЦИКЛ!$H$28,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$4,ЦИКЛ!$I$3=M710,ЦИКЛ!$B$37=АВР!K710),ЦИКЛ!$I$28,IF(AND(АВР!$AD$8=ЦИКЛ!$R$4,ЦИКЛ!$D$3=M710,ЦИКЛ!$B$37=АВР!K710),ЦИКЛ!$D$28,IF(AND(АВР!$AD$8=ЦИКЛ!$R$4,ЦИКЛ!$E$3=M710,ЦИКЛ!$B$37=АВР!K710),ЦИКЛ!$E$28,IF(AND(АВР!$AD$8=ЦИКЛ!$R$4,ЦИКЛ!$F$3=M710,ЦИКЛ!$B$37=АВР!K710),ЦИКЛ!$F$28,IF(AND(АВР!$AD$8=ЦИКЛ!$R$4,ЦИКЛ!$G$3=M710,ЦИКЛ!$B$37=АВР!K710),ЦИКЛ!$G$28,IF(AND(АВР!$AD$8=ЦИКЛ!$R$4,ЦИКЛ!$H$3=M710,ЦИКЛ!$B$37=АВР!K710),ЦИКЛ!$H$28,IF(AND(АВР!$AD$8=ЦИКЛ!$R$4,ЦИКЛ!$I$3=M710,ЦИКЛ!$B$37=АВР!K710),ЦИКЛ!$I$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$7,ЦИКЛ!$D$3=M710,ЦИКЛ!$B$37=АВР!K710),ЦИКЛ!$D$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$7,ЦИКЛ!$E$3=M710,ЦИКЛ!$B$37=АВР!K710),ЦИКЛ!$E$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$7,ЦИКЛ!$F$3=M710,ЦИКЛ!$B$37=АВР!K710),ЦИКЛ!$F$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$7,ЦИКЛ!$G$3=M710,ЦИКЛ!$B$37=АВР!K710),ЦИКЛ!$G$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$7,ЦИКЛ!$H$3=M710,ЦИКЛ!$B$37=АВР!K710),ЦИКЛ!$H$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$7,ЦИКЛ!$I$3=M710,ЦИКЛ!$B$37=АВР!K710),ЦИКЛ!$I$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$10,ЦИКЛ!$D$3=M710,ЦИКЛ!$B$37=АВР!K710),ЦИКЛ!$D$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$10,ЦИКЛ!$E$3=M710,ЦИКЛ!$B$37=АВР!K710),ЦИКЛ!$E$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$10,ЦИКЛ!$F$3=M710,ЦИКЛ!$B$37=АВР!K710),ЦИКЛ!$F$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$10,ЦИКЛ!$G$3=M710,ЦИКЛ!$B$37=АВР!K710),ЦИКЛ!$G$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$10,ЦИКЛ!$H$3=M710,ЦИКЛ!$B$37=АВР!K710),ЦИКЛ!$H$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$10,ЦИКЛ!$I$3=M710,ЦИКЛ!$B$37=АВР!K710),ЦИКЛ!$I$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$52,ЦИКЛ!$D$3=M710,ЦИКЛ!$B$37=АВР!K710),ЦИКЛ!$D$60,IF(AND(АВР!$AD$8=ЦИКЛ!$A$52,ЦИКЛ!$E$3=M710,ЦИКЛ!$B$37=АВР!K710),ЦИКЛ!$E$60,IF(AND(АВР!$AD$8=ЦИКЛ!$A$52,ЦИКЛ!$F$3=M710,ЦИКЛ!$B$37=АВР!K710),ЦИКЛ!$F$60,IF(AND(АВР!$AD$8=ЦИКЛ!$A$52,ЦИКЛ!$G$3=M710,ЦИКЛ!$B$37=АВР!K710),ЦИКЛ!$G$60,IF(AND(АВР!$AD$8=ЦИКЛ!$A$52,ЦИКЛ!$H$3=M710,ЦИКЛ!$B$37=АВР!K710),ЦИКЛ!$H$60,IF(AND(АВР!$AD$8=ЦИКЛ!$A$52,ЦИКЛ!$I$3=M710,ЦИКЛ!$B$37=АВР!K710),ЦИКЛ!$I$60,IF(AND(АВР!$AD$8=ЦИКЛ!$A$70,ЦИКЛ!$D$3=M710,ЦИКЛ!$B$37=АВР!K710),ЦИКЛ!$D$78,IF(AND(АВР!$AD$8=ЦИКЛ!$A$70,ЦИКЛ!$E$3=M710,ЦИКЛ!$B$37=АВР!K710),ЦИКЛ!$E$78,IF(AND(АВР!$AD$8=ЦИКЛ!$A$70,ЦИКЛ!$F$3=M710,ЦИКЛ!$B$37=АВР!K710),ЦИКЛ!$F$78,IF(AND(АВР!$AD$8=ЦИКЛ!$A$70,ЦИКЛ!$G$3=M710,ЦИКЛ!$B$37=АВР!K710),ЦИКЛ!$G$78,IF(AND(АВР!$AD$8=ЦИКЛ!$A$70,ЦИКЛ!$H$3=M710,ЦИКЛ!$B$37=АВР!K710),ЦИКЛ!$H$78,IF(AND(АВР!$AD$8=ЦИКЛ!$A$70,ЦИКЛ!$I$3=M710,ЦИКЛ!$B$37=АВР!K710),ЦИКЛ!$I$78,IF(AND(АВР!$AD$8=ЦИКЛ!$A$88,ЦИКЛ!$D$3=M710,ЦИКЛ!$B$37=АВР!K710),ЦИКЛ!$D$96,IF(AND(АВР!$AD$8=ЦИКЛ!$A$88,ЦИКЛ!$E$3=M710,ЦИКЛ!$B$37=АВР!K710),ЦИКЛ!$E$96,IF(AND(АВР!$AD$8=ЦИКЛ!$A$88,ЦИКЛ!$F$3=M710,ЦИКЛ!$B$37=АВР!K710),ЦИКЛ!$F$96,IF(AND(АВР!$AD$8=ЦИКЛ!$A$88,ЦИКЛ!$G$3=M710,ЦИКЛ!$B$37=АВР!K710),ЦИКЛ!$G$96,IF(AND(АВР!$AD$8=ЦИКЛ!$A$88,ЦИКЛ!$H$3=M710,ЦИКЛ!$B$37=АВР!K710),ЦИКЛ!$H$96,IF(AND(АВР!$AD$8=ЦИКЛ!$A$88,ЦИКЛ!$I$3=M710,ЦИКЛ!$B$37=АВР!K710),ЦИКЛ!$I$96,IF(AND(АВР!$AD$8=ЦИКЛ!$A$106,ЦИКЛ!$D$3=M710,ЦИКЛ!$B$37=АВР!K710),ЦИКЛ!$D$116,IF(AND(АВР!$AD$8=ЦИКЛ!$A$106,ЦИКЛ!$E$3=M710,ЦИКЛ!$B$37=АВР!K710),ЦИКЛ!$E$116,IF(AND(АВР!$AD$8=ЦИКЛ!$A$106,ЦИКЛ!$F$3=M710,ЦИКЛ!$B$37=АВР!K710),ЦИКЛ!$F$116,IF(AND(АВР!$AD$8=ЦИКЛ!$A$106,ЦИКЛ!$G$3=M710,ЦИКЛ!$B$37=АВР!K710),ЦИКЛ!$G$116,IF(AND(АВР!$AD$8=ЦИКЛ!$A$106,ЦИКЛ!$H$3=M710,ЦИКЛ!$B$37=АВР!K710),ЦИКЛ!$H$116,IF(AND(АВР!$AD$8=ЦИКЛ!$A$106,ЦИКЛ!$I$3=M710,ЦИКЛ!$B$37=АВР!K710),ЦИКЛ!$I$116,IF(AND(АВР!$AD$8=ЦИКЛ!$A$128,ЦИКЛ!$D$3=M710,ЦИКЛ!$B$37=АВР!K710),ЦИКЛ!$D$138,IF(AND(АВР!$AD$8=ЦИКЛ!$A$128,ЦИКЛ!$E$3=M710,ЦИКЛ!$B$37=АВР!K710),ЦИКЛ!$E$138,IF(AND(АВР!$AD$8=ЦИКЛ!$A$128,ЦИКЛ!$F$3=M710,ЦИКЛ!$B$37=АВР!K710),ЦИКЛ!$F$138,IF(AND(АВР!$AD$8=ЦИКЛ!$A$128,ЦИКЛ!$G$3=M710,ЦИКЛ!$B$37=АВР!K710),ЦИКЛ!$G$138,IF(AND(АВР!$AD$8=ЦИКЛ!$A$128,ЦИКЛ!$H$3=M710,ЦИКЛ!$B$37=АВР!K710),ЦИКЛ!$H$138,IF(AND(АВР!$AD$8=ЦИКЛ!$A$128,ЦИКЛ!$I$3=M710,ЦИКЛ!$B$37=АВР!K710),ЦИКЛ!$I$138))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))',
     1, '=V710*W710*X710', '=Y710-AA710-AB710-AC710-AD710', None, None, None, None, None],
    ['=ROW()-ROW($A$46)', None, None, 'спо', 'Ловильный инструмент', 'Подъем НКТ  2 скорость', None, None, None,
     None,
     '73мм', 300,
     '=IF(AND(L711/V711>=ЦИКЛ!$V$9,L711/V711<=ЦИКЛ!$W$9),ЦИКЛ!$U$9,IF(AND(L711/V711>=ЦИКЛ!$V$10,L711/V711<=ЦИКЛ!$W$10),ЦИКЛ!$U$10,IF(AND(L711/V711>=ЦИКЛ!$V$11,L711/V711<=ЦИКЛ!$W$11),ЦИКЛ!$U$11,IF(AND(L711/V711>=ЦИКЛ!$V$12,L711/V711<=ЦИКЛ!$W$12),ЦИКЛ!$U$12,IF(AND(L711/V711>=ЦИКЛ!$V$13,L711/V711<=ЦИКЛ!$W$13),ЦИКЛ!$U$13,IF(AND(L711/V711>=ЦИКЛ!$V$14,L711/V711<=ЦИКЛ!$W$14),ЦИКЛ!$U$14))))))',
     '=IF(AND(АВР!$AD$8=ЦИКЛ!$A$5,ЦИКЛ!$D$3=M711),ЦИКЛ!$J$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$5,ЦИКЛ!$E$3=M711),ЦИКЛ!$K$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$5,ЦИКЛ!$F$3=M711),ЦИКЛ!$L$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$5,ЦИКЛ!$G$3=M711),ЦИКЛ!$M$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$5,ЦИКЛ!$H$3=M711),ЦИКЛ!$N$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$5,ЦИКЛ!$I$3=M711),ЦИКЛ!$O$29,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$5,ЦИКЛ!$D$3=M711),ЦИКЛ!$J$29,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$5,ЦИКЛ!$E$3=M711),ЦИКЛ!$K$29,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$5,ЦИКЛ!$F$3=M711),ЦИКЛ!$L$29,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$5,ЦИКЛ!$G$3=M711),ЦИКЛ!$M$29,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$5,ЦИКЛ!$H$3=M711),ЦИКЛ!$N$29,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$5,ЦИКЛ!$I$3=M711),ЦИКЛ!$O$29,IF(AND(АВР!$AD$8=ЦИКЛ!$R$5,ЦИКЛ!$D$3=M711),ЦИКЛ!$J$29,IF(AND(АВР!$AD$8=ЦИКЛ!$R$5,ЦИКЛ!$E$3=M711),ЦИКЛ!$K$29,IF(AND(АВР!$AD$8=ЦИКЛ!$R$5,ЦИКЛ!$F$3=M711),ЦИКЛ!$L$29,IF(AND(АВР!$AD$8=ЦИКЛ!$R$5,ЦИКЛ!$G$3=M711),ЦИКЛ!$M$29,IF(AND(АВР!$AD$8=ЦИКЛ!$R$5,ЦИКЛ!$H$3=M711),ЦИКЛ!$N$29,IF(AND(АВР!$AD$8=ЦИКЛ!$R$5,ЦИКЛ!$I$3=M711),ЦИКЛ!$O$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$8,ЦИКЛ!$D$3=M711),ЦИКЛ!$J$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$8,ЦИКЛ!$E$3=M711),ЦИКЛ!$K$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$8,ЦИКЛ!$F$3=M711),ЦИКЛ!$L$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$8,ЦИКЛ!$G$3=M711),ЦИКЛ!$M$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$8,ЦИКЛ!$H$3=M711),ЦИКЛ!$N$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$8,ЦИКЛ!$I$3=M711),ЦИКЛ!$O$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$11,ЦИКЛ!$D$3=M711),ЦИКЛ!$J$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$11,ЦИКЛ!$E$3=M711),ЦИКЛ!$K$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$11,ЦИКЛ!$F$3=M711),ЦИКЛ!$L$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$11,ЦИКЛ!$G$3=M711),ЦИКЛ!$M$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$11,ЦИКЛ!$H$3=M711),ЦИКЛ!$N$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$11,ЦИКЛ!$I$3=M711),ЦИКЛ!$O$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$53,ЦИКЛ!$D$3=M711),ЦИКЛ!#REF!,IF(AND(АВР!$AD$8=ЦИКЛ!$A$53,ЦИКЛ!$E$3=M711),ЦИКЛ!$K$61,IF(AND(АВР!$AD$8=ЦИКЛ!$A$53,ЦИКЛ!$F$3=M711),ЦИКЛ!$L$61,IF(AND(АВР!$AD$8=ЦИКЛ!$A$53,ЦИКЛ!$G$3=M711),ЦИКЛ!$M$61,IF(AND(АВР!$AD$8=ЦИКЛ!$A$53,ЦИКЛ!$H$3=M711),ЦИКЛ!$N$61,IF(AND(АВР!$AD$8=ЦИКЛ!$A$53,ЦИКЛ!$I$3=M711),ЦИКЛ!$O$61,IF(AND(АВР!$AD$8=ЦИКЛ!$A$71,ЦИКЛ!$D$3=M711),ЦИКЛ!$J$79,IF(AND(АВР!$AD$8=ЦИКЛ!$A$71,ЦИКЛ!$E$3=M711),ЦИКЛ!$K$79,IF(AND(АВР!$AD$8=ЦИКЛ!$A$71,ЦИКЛ!$F$3=M711),ЦИКЛ!$L$79,IF(AND(АВР!$AD$8=ЦИКЛ!$A$71,ЦИКЛ!$G$3=M711),ЦИКЛ!$M$79,IF(AND(АВР!$AD$8=ЦИКЛ!$A$71,ЦИКЛ!$H$3=M711),ЦИКЛ!$N$79,IF(AND(АВР!$AD$8=ЦИКЛ!$A$71,ЦИКЛ!$I$3=M711),ЦИКЛ!$O$79,IF(AND(АВР!$AD$8=ЦИКЛ!$A$89,ЦИКЛ!$D$3=M711),ЦИКЛ!$J$97,IF(AND(АВР!$AD$8=ЦИКЛ!$A$89,ЦИКЛ!$E$3=M711),ЦИКЛ!$K$97,IF(AND(АВР!$AD$8=ЦИКЛ!$A$89,ЦИКЛ!$F$3=M711),ЦИКЛ!$L$97,IF(AND(АВР!$AD$8=ЦИКЛ!$A$89,ЦИКЛ!$G$3=M711),ЦИКЛ!$M$97,IF(AND(АВР!$AD$8=ЦИКЛ!$A$89,ЦИКЛ!$H$3=M711),ЦИКЛ!$N$97,IF(AND(АВР!$AD$8=ЦИКЛ!$A$89,ЦИКЛ!$I$3=M711),ЦИКЛ!$O$97,IF(AND(АВР!$AD$8=ЦИКЛ!$A$107,ЦИКЛ!$D$3=M711),ЦИКЛ!$J$117,IF(AND(АВР!$AD$8=ЦИКЛ!$A$107,ЦИКЛ!$E$3=M711),ЦИКЛ!$K$117,IF(AND(АВР!$AD$8=ЦИКЛ!$A$107,ЦИКЛ!$F$3=M711),ЦИКЛ!$L$117,IF(AND(АВР!$AD$8=ЦИКЛ!$A$107,ЦИКЛ!$G$3=M711),ЦИКЛ!$M$117,IF(AND(АВР!$AD$8=ЦИКЛ!$A$107,ЦИКЛ!$H$3=M711),ЦИКЛ!$N$117,IF(AND(АВР!$AD$8=ЦИКЛ!$A$107,ЦИКЛ!$I$3=M711),ЦИКЛ!$O$117,IF(AND(АВР!$AD$8=ЦИКЛ!$A$129,ЦИКЛ!$D$3=M711),ЦИКЛ!$J$139,IF(AND(АВР!$AD$8=ЦИКЛ!$A$129,ЦИКЛ!$E$3=M711),ЦИКЛ!$K$139,IF(AND(АВР!$AD$8=ЦИКЛ!$A$129,ЦИКЛ!$F$3=M711),ЦИКЛ!$L$139,IF(AND(АВР!$AD$8=ЦИКЛ!$A$129,ЦИКЛ!$G$3=M711),ЦИКЛ!$M$139,IF(AND(АВР!$AD$8=ЦИКЛ!$A$129,ЦИКЛ!$H$3=M711),ЦИКЛ!$N$139,IF(AND(АВР!$AD$8=ЦИКЛ!$A$129,ЦИКЛ!$I$3=M711),ЦИКЛ!$O$139))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))',
     None, None, None, None,
     '=IF($AD$8=ЦИКЛ!$A$4,ЦИКЛ!$P$4,IF($AD$8=ЦИКЛ!$A$7,ЦИКЛ!$P$7,IF($AD$8=ЦИКЛ!$A$10,ЦИКЛ!$P$7,IF($AD$8=ЦИКЛ!$A$52,ЦИКЛ!$P$52,IF($AD$8=ЦИКЛ!$A$70,ЦИКЛ!$P$70,IF($AD$8=ЦИКЛ!$A$88,ЦИКЛ!$P$88,IF($AD$8=ЦИКЛ!$A$106,ЦИКЛ!$P$106,IF($AD$8=ЦИКЛ!$A$133,ЦИКЛ!$P$133,IF($AD$8=ЦИКЛ!$Q$4,ЦИКЛ!$P$4,IF($AD$8=ЦИКЛ!$R$4,ЦИКЛ!$P$4))))))))))',
     None, 'шт', 30,
     '=IF(AND(АВР!$AD$8=ЦИКЛ!$A$5,ЦИКЛ!$D$3=M711,ЦИКЛ!$B$37=АВР!K711),ЦИКЛ!$D$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$5,ЦИКЛ!$E$3=M711,ЦИКЛ!$B$37=АВР!K711),ЦИКЛ!$E$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$5,ЦИКЛ!$F$3=M711,ЦИКЛ!$B$37=АВР!K711),ЦИКЛ!$F$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$5,ЦИКЛ!$G$3=M711,ЦИКЛ!$B$37=АВР!K711),ЦИКЛ!$G$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$5,ЦИКЛ!$H$3=M711,ЦИКЛ!$B$37=АВР!K711),ЦИКЛ!$H$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$5,ЦИКЛ!$I$3=M711,ЦИКЛ!$B$37=K711),ЦИКЛ!$I$29,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$5,ЦИКЛ!$D$3=M711,ЦИКЛ!$B$37=K711),ЦИКЛ!$D$29,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$5,ЦИКЛ!$E$3=M711,ЦИКЛ!$B$37=K711),ЦИКЛ!$E$29,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$5,ЦИКЛ!$F$3=M711,ЦИКЛ!$B$37=K711),ЦИКЛ!$F$29,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$5,ЦИКЛ!$G$3=M711,ЦИКЛ!$B$37=K711),ЦИКЛ!$G$29,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$5,ЦИКЛ!$H$3=M711,ЦИКЛ!$B$37=K711),ЦИКЛ!$H$29,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$5,ЦИКЛ!$I$3=M711,ЦИКЛ!$B$37=K711),ЦИКЛ!$I$29,IF(AND(АВР!$AD$8=ЦИКЛ!$R$5,ЦИКЛ!$D$3=M711,ЦИКЛ!$B$37=K711),ЦИКЛ!$D$29,IF(AND(АВР!$AD$8=ЦИКЛ!$R$5,ЦИКЛ!$E$3=M711,ЦИКЛ!$B$37=K711),ЦИКЛ!$E$29,IF(AND(АВР!$AD$8=ЦИКЛ!$R$5,ЦИКЛ!$F$3=M711,ЦИКЛ!$B$37=K711),ЦИКЛ!$F$29,IF(AND(АВР!$AD$8=ЦИКЛ!$R$5,ЦИКЛ!$G$3=M711,ЦИКЛ!$B$37=K711),ЦИКЛ!$G$29,IF(AND(АВР!$AD$8=ЦИКЛ!$R$5,ЦИКЛ!$H$3=M711,ЦИКЛ!$B$37=K711),ЦИКЛ!$H$29,IF(AND(АВР!$AD$8=ЦИКЛ!$R$5,ЦИКЛ!$I$3=M711,ЦИКЛ!$B$37=K711),ЦИКЛ!$I$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$8,ЦИКЛ!$D$3=M711,ЦИКЛ!$B$37=K711),ЦИКЛ!$D$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$8,ЦИКЛ!$E$3=M711,ЦИКЛ!$B$37=K711),ЦИКЛ!$E$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$8,ЦИКЛ!$F$3=M711,ЦИКЛ!$B$37=K711),ЦИКЛ!$F$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$8,ЦИКЛ!$G$3=M711,ЦИКЛ!$B$37=K711),ЦИКЛ!$G$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$8,ЦИКЛ!$H$3=M711,ЦИКЛ!$B$37=K711),ЦИКЛ!$H$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$8,ЦИКЛ!$I$3=M711,ЦИКЛ!$B$37=K711),ЦИКЛ!$I$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$11,ЦИКЛ!$D$3=M711,,ЦИКЛ!$B$37=K711),ЦИКЛ!$D$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$11,ЦИКЛ!$E$3=M711,ЦИКЛ!$B$37=K711),ЦИКЛ!$E$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$11,ЦИКЛ!$F$3=M711,ЦИКЛ!$B$37=K711),ЦИКЛ!$F$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$11,ЦИКЛ!$G$3=M711,ЦИКЛ!$B$37=K711),ЦИКЛ!$G$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$11,ЦИКЛ!$H$3=M711,ЦИКЛ!$B$37=K711),ЦИКЛ!$H$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$11,ЦИКЛ!$I$3=M711,ЦИКЛ!$B$37=K711),ЦИКЛ!$I$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$53,ЦИКЛ!$D$3=M711,ЦИКЛ!$B$37=K711),ЦИКЛ!$D$61,IF(AND(АВР!$AD$8=ЦИКЛ!$A$53,ЦИКЛ!$E$3=M711,ЦИКЛ!$B$37=K711),ЦИКЛ!$E$61,IF(AND(АВР!$AD$8=ЦИКЛ!$A$53,ЦИКЛ!$F$3=M711,ЦИКЛ!$B$37=K711),ЦИКЛ!$F$61,IF(AND(АВР!$AD$8=ЦИКЛ!$A$53,ЦИКЛ!$G$3=M711,ЦИКЛ!$B$37=K711),ЦИКЛ!$G$61,IF(AND(АВР!$AD$8=ЦИКЛ!$A$53,ЦИКЛ!$H$3=M711,ЦИКЛ!$B$37=K711),ЦИКЛ!$H$61,IF(AND(АВР!$AD$8=ЦИКЛ!$A$53,ЦИКЛ!$I$3=M711,ЦИКЛ!$B$37=K711),ЦИКЛ!$I$61,IF(AND(АВР!$AD$8=ЦИКЛ!$A$71,ЦИКЛ!$D$3=M711,ЦИКЛ!$B$37=K711),ЦИКЛ!$D$79,IF(AND(АВР!$AD$8=ЦИКЛ!$A$71,ЦИКЛ!$E$3=M711,ЦИКЛ!$B$37=K711),ЦИКЛ!$E$79,IF(AND(АВР!$AD$8=ЦИКЛ!$A$71,ЦИКЛ!$F$3=M711,ЦИКЛ!$B$37=K711),ЦИКЛ!$F$79,IF(AND(АВР!$AD$8=ЦИКЛ!$A$71,ЦИКЛ!$G$3=M711,ЦИКЛ!$B$37=K711),ЦИКЛ!$G$79,IF(AND(АВР!$AD$8=ЦИКЛ!$A$71,ЦИКЛ!$H$3=M711,ЦИКЛ!$B$37=K711),ЦИКЛ!$H$79,IF(AND(АВР!$AD$8=ЦИКЛ!$A$71,ЦИКЛ!$I$3=M711,ЦИКЛ!$B$37=K711),ЦИКЛ!$I$79,IF(AND(АВР!$AD$8=ЦИКЛ!$A$89,ЦИКЛ!$D$3=M711,ЦИКЛ!$B$37=K711),ЦИКЛ!$D$97,IF(AND(АВР!$AD$8=ЦИКЛ!$A$89,ЦИКЛ!$E$3=M711,ЦИКЛ!$B$37=K711),ЦИКЛ!$E$97,IF(AND(АВР!$AD$8=ЦИКЛ!$A$89,ЦИКЛ!$F$3=M711,ЦИКЛ!$B$37=K711),ЦИКЛ!$F$97,IF(AND(АВР!$AD$8=ЦИКЛ!$A$89,ЦИКЛ!$G$3=M711,ЦИКЛ!$B$37=K711),ЦИКЛ!$G$97,IF(AND(АВР!$AD$8=ЦИКЛ!$A$89,ЦИКЛ!$H$3=M711,ЦИКЛ!$B$37=K711),ЦИКЛ!$H$97,IF(AND(АВР!$AD$8=ЦИКЛ!$A$89,ЦИКЛ!$I$3=M711,ЦИКЛ!$B$37=K711),ЦИКЛ!$I$97,IF(AND(АВР!$AD$8=ЦИКЛ!$A$107,ЦИКЛ!$D$3=M711,ЦИКЛ!$B$37=K711),ЦИКЛ!$D$117,IF(AND(АВР!$AD$8=ЦИКЛ!$A$107,ЦИКЛ!$E$3=M711,ЦИКЛ!$B$37=K711),ЦИКЛ!$E$117,IF(AND(АВР!$AD$8=ЦИКЛ!$A$107,ЦИКЛ!$F$3=M711,ЦИКЛ!$B$37=K711),ЦИКЛ!$F$117,IF(AND(АВР!$AD$8=ЦИКЛ!$A$107,ЦИКЛ!$G$3=M711,ЦИКЛ!$B$37=K711),ЦИКЛ!$G$117,IF(AND(АВР!$AD$8=ЦИКЛ!$A$107,ЦИКЛ!$H$3=M711,ЦИКЛ!$B$37=K711),ЦИКЛ!$H$117,IF(AND(АВР!$AD$8=ЦИКЛ!$A$107,ЦИКЛ!$I$3=M711,ЦИКЛ!$B$37=K711),ЦИКЛ!$I$117,IF(AND(АВР!$AD$8=ЦИКЛ!$A$129,ЦИКЛ!$D$3=M711,ЦИКЛ!$B$37=K711),ЦИКЛ!$D$139,IF(AND(АВР!$AD$8=ЦИКЛ!$A$129,ЦИКЛ!$E$3=M711,ЦИКЛ!$B$37=K711),ЦИКЛ!$E$139,IF(AND(АВР!$AD$8=ЦИКЛ!$A$129,ЦИКЛ!$F$3=M711,ЦИКЛ!$B$37=K711),ЦИКЛ!$F$139,IF(AND(АВР!$AD$8=ЦИКЛ!$A$129,ЦИКЛ!$G$3=M711,ЦИКЛ!$B$37=K711),ЦИКЛ!$G$139,IF(AND(АВР!$AD$8=ЦИКЛ!$A$129,ЦИКЛ!$H$3=M711,ЦИКЛ!$B$37=K711),ЦИКЛ!$H$139,IF(AND(АВР!$AD$8=ЦИКЛ!$A$129,ЦИКЛ!$I$3=M711,ЦИКЛ!$B$37=K711),ЦИКЛ!$I$139))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))',
     1, '=V711*W711*X711', '=Y711-AA711-AB711-AC711-AD711', None, None, None, None, None],
    ['=ROW()-ROW($A$46)', None, None, 'спо', 'Ловильный инструмент', 'Подъем НКТ  3 скорость', None, None, None,
     None,
     '73мм', 1200,
     '=IF(AND(L712/V712>=ЦИКЛ!$V$9,L712/V712<=ЦИКЛ!$W$9),ЦИКЛ!$U$9,IF(AND(L712/V712>=ЦИКЛ!$V$10,L712/V712<=ЦИКЛ!$W$10),ЦИКЛ!$U$10,IF(AND(L712/V712>=ЦИКЛ!$V$11,L712/V712<=ЦИКЛ!$W$11),ЦИКЛ!$U$11,IF(AND(L712/V712>=ЦИКЛ!$V$12,L712/V712<=ЦИКЛ!$W$12),ЦИКЛ!$U$12,IF(AND(L712/V712>=ЦИКЛ!$V$13,L712/V712<=ЦИКЛ!$W$13),ЦИКЛ!$U$13,IF(AND(L712/V712>=ЦИКЛ!$V$14,L712/V712<=ЦИКЛ!$W$14),ЦИКЛ!$U$14))))))',
     '=IF(AND(АВР!$AD$8=ЦИКЛ!$A$6,ЦИКЛ!$D$3=M712),ЦИКЛ!$J$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$6,ЦИКЛ!$E$3=M712),ЦИКЛ!$K$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$6,ЦИКЛ!$F$3=M712),ЦИКЛ!$L$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$6,ЦИКЛ!$G$3=M712),ЦИКЛ!$M$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$6,ЦИКЛ!$N$3=M712),ЦИКЛ!$H$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$6,ЦИКЛ!$I$3=M712),ЦИКЛ!$O$30,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$6,ЦИКЛ!$D$3=M712),ЦИКЛ!$J$30,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$6,ЦИКЛ!$E$3=M712),ЦИКЛ!$K$30,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$6,ЦИКЛ!$F$3=M712),ЦИКЛ!$L$30,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$6,ЦИКЛ!$G$3=M712),ЦИКЛ!$M$30,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$6,ЦИКЛ!$H$3=M712),ЦИКЛ!$N$30,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$6,ЦИКЛ!$I$3=M712),ЦИКЛ!$O$30,IF(AND(АВР!$AD$8=ЦИКЛ!$R$6,ЦИКЛ!$D$3=M712),ЦИКЛ!$J$30,IF(AND(АВР!$AD$8=ЦИКЛ!$R$6,ЦИКЛ!$E$3=M712),ЦИКЛ!$K$30,IF(AND(АВР!$AD$8=ЦИКЛ!$R$6,ЦИКЛ!$F$3=M712),ЦИКЛ!$L$30,IF(AND(АВР!$AD$8=ЦИКЛ!$R$6,ЦИКЛ!$G$3=M712),ЦИКЛ!$M$30,IF(AND(АВР!$AD$8=ЦИКЛ!$R$6,ЦИКЛ!$H$3=M712),ЦИКЛ!$N$30,IF(AND(АВР!$AD$8=ЦИКЛ!$R$6,ЦИКЛ!$I$3=M712),ЦИКЛ!$O$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$9,ЦИКЛ!$D$3=M712),ЦИКЛ!$J$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$9,ЦИКЛ!$E$3=M712),ЦИКЛ!$K$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$9,ЦИКЛ!$F$3=M712),ЦИКЛ!$L$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$9,ЦИКЛ!$G$3=M712),ЦИКЛ!$M$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$9,ЦИКЛ!$H$3=M712),ЦИКЛ!$N$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$9,ЦИКЛ!$I$3=M712),ЦИКЛ!$O$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$12,ЦИКЛ!$D$3=M712),ЦИКЛ!$J$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$12,ЦИКЛ!$E$3=M712),ЦИКЛ!$K$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$12,ЦИКЛ!$F$3=M712),ЦИКЛ!$L$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$12,ЦИКЛ!$G$3=M712),ЦИКЛ!$M$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$12,ЦИКЛ!$H$3=M712),ЦИКЛ!$N$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$12,ЦИКЛ!$I$3=M712),ЦИКЛ!$O$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$54,ЦИКЛ!$D$3=M712),ЦИКЛ!$J$62,IF(AND(АВР!$AD$8=ЦИКЛ!$A$54,ЦИКЛ!$E$3=M712),ЦИКЛ!$K$62,IF(AND(АВР!$AD$8=ЦИКЛ!$A$54,ЦИКЛ!$F$3=M712),ЦИКЛ!$L$62,IF(AND(АВР!$AD$8=ЦИКЛ!$A$54,ЦИКЛ!$G$3=M712),ЦИКЛ!$M$62,IF(AND(АВР!$AD$8=ЦИКЛ!$A$54,ЦИКЛ!$H$3=M712),ЦИКЛ!$N$62,IF(AND(АВР!$AD$8=ЦИКЛ!$A$54,ЦИКЛ!$I$3=M712),ЦИКЛ!$O$62,IF(AND(АВР!$AD$8=ЦИКЛ!$A$72,ЦИКЛ!$D$3=M712),ЦИКЛ!$J$80,IF(AND(АВР!$AD$8=ЦИКЛ!$A$72,ЦИКЛ!$E$3=M712),ЦИКЛ!$K$80,IF(AND(АВР!$AD$8=ЦИКЛ!$A$72,ЦИКЛ!$F$3=M712),ЦИКЛ!$L$80,IF(AND(АВР!$AD$8=ЦИКЛ!$A$72,ЦИКЛ!$G$3=M712),ЦИКЛ!$M$80,IF(AND(АВР!$AD$8=ЦИКЛ!$A$72,ЦИКЛ!$H$3=M712),ЦИКЛ!$N$80,IF(AND(АВР!$AD$8=ЦИКЛ!$A$72,ЦИКЛ!$I$3=M712),ЦИКЛ!$O$80,IF(AND(АВР!$AD$8=ЦИКЛ!$A$90,ЦИКЛ!$D$3=M712),ЦИКЛ!$J$98,IF(AND(АВР!$AD$8=ЦИКЛ!$A$90,ЦИКЛ!$E$3=M712),ЦИКЛ!$K$98,IF(AND(АВР!$AD$8=ЦИКЛ!$A$90,ЦИКЛ!$F$3=M712),ЦИКЛ!$L$98,IF(AND(АВР!$AD$8=ЦИКЛ!$A$90,ЦИКЛ!$G$3=M712),ЦИКЛ!$M$98,IF(AND(АВР!$AD$8=ЦИКЛ!$A$90,ЦИКЛ!$H$3=M712),ЦИКЛ!$N$98,IF(AND(АВР!$AD$8=ЦИКЛ!$A$90,ЦИКЛ!$I$3=M712),ЦИКЛ!$O$98,IF(AND(АВР!$AD$8=ЦИКЛ!$A$108,ЦИКЛ!$D$3=M712),ЦИКЛ!$J$118,IF(AND(АВР!$AD$8=ЦИКЛ!$A$108,ЦИКЛ!$E$3=M712),ЦИКЛ!$K$118,IF(AND(АВР!$AD$8=ЦИКЛ!$A$108,ЦИКЛ!$F$3=M712),ЦИКЛ!$L$118,IF(AND(АВР!$AD$8=ЦИКЛ!$A$108,ЦИКЛ!$G$3=M712),ЦИКЛ!$M$118,IF(AND(АВР!$AD$8=ЦИКЛ!$A$108,ЦИКЛ!$H$3=M712),ЦИКЛ!$N$118,IF(AND(АВР!$AD$8=ЦИКЛ!$A$108,ЦИКЛ!$I$3=M712),ЦИКЛ!$O$118,IF(AND(АВР!$AD$8=ЦИКЛ!$A$130,ЦИКЛ!$D$3=M712),ЦИКЛ!$J$140,IF(AND(АВР!$AD$8=ЦИКЛ!$A$130,ЦИКЛ!$E$3=M712),ЦИКЛ!$K$140,IF(AND(АВР!$AD$8=ЦИКЛ!$A$130,ЦИКЛ!$F$3=M712),ЦИКЛ!$L$140,IF(AND(АВР!$AD$8=ЦИКЛ!$A$130,ЦИКЛ!$G$3=M712),ЦИКЛ!$M$140,IF(AND(АВР!$AD$8=ЦИКЛ!$A$130,ЦИКЛ!$H$3=M712),ЦИКЛ!$N$140,IF(AND(АВР!$AD$8=ЦИКЛ!$A$130,ЦИКЛ!$I$3=M712),ЦИКЛ!$O$140))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))',
     None, None, None, None,
     '=IF($AD$8=ЦИКЛ!$A$4,ЦИКЛ!$P$4,IF($AD$8=ЦИКЛ!$A$7,ЦИКЛ!$P$7,IF($AD$8=ЦИКЛ!$A$10,ЦИКЛ!$P$7,IF($AD$8=ЦИКЛ!$A$52,ЦИКЛ!$P$52,IF($AD$8=ЦИКЛ!$A$70,ЦИКЛ!$P$70,IF($AD$8=ЦИКЛ!$A$88,ЦИКЛ!$P$88,IF($AD$8=ЦИКЛ!$A$106,ЦИКЛ!$P$106,IF($AD$8=ЦИКЛ!$A$133,ЦИКЛ!$P$133,IF($AD$8=ЦИКЛ!$Q$4,ЦИКЛ!$P$4,IF($AD$8=ЦИКЛ!$R$4,ЦИКЛ!$P$4))))))))))',
     None, 'шт', 120,
     '=IF(AND(АВР!$AD$8=ЦИКЛ!$A$6,ЦИКЛ!$D$3=M712,ЦИКЛ!$B$37=АВР!K712),ЦИКЛ!$D$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$6,ЦИКЛ!$E$3=M712,ЦИКЛ!$B$37=АВР!K712),ЦИКЛ!$E$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$6,ЦИКЛ!$F$3=M712,ЦИКЛ!$B$37=АВР!K712),ЦИКЛ!$F$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$6,ЦИКЛ!$G$3=M712,ЦИКЛ!$B$37=АВР!K712),ЦИКЛ!$G$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$6,ЦИКЛ!$H$3=M712,ЦИКЛ!$B$37=АВР!K712),ЦИКЛ!$H$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$6,ЦИКЛ!$I$3=M712,ЦИКЛ!$B$37=АВР!K712),ЦИКЛ!$I$30,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$6,ЦИКЛ!$D$3=M712,ЦИКЛ!$B$37=АВР!K712),ЦИКЛ!$D$30,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$6,ЦИКЛ!$E$3=M712,ЦИКЛ!$B$37=АВР!K712),ЦИКЛ!$E$30,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$6,ЦИКЛ!$F$3=M712,ЦИКЛ!$B$37=АВР!K712),ЦИКЛ!$F$30,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$6,ЦИКЛ!$G$3=M712,ЦИКЛ!$B$37=АВР!K712),ЦИКЛ!$G$30,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$6,ЦИКЛ!$H$3=M712,ЦИКЛ!$B$37=АВР!K712),ЦИКЛ!$H$30,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$6,ЦИКЛ!$I$3=M712,ЦИКЛ!$B$37=АВР!K712),ЦИКЛ!$I$30,IF(AND(АВР!$AD$8=ЦИКЛ!$R$6,ЦИКЛ!$D$3=M712,ЦИКЛ!$B$37=АВР!K712),ЦИКЛ!$D$30,IF(AND(АВР!$AD$8=ЦИКЛ!$R$6,ЦИКЛ!$E$3=M712,ЦИКЛ!$B$37=АВР!K712),ЦИКЛ!$E$30,IF(AND(АВР!$AD$8=ЦИКЛ!$R$6,ЦИКЛ!$F$3=M712,ЦИКЛ!$B$37=АВР!K712),ЦИКЛ!$F$30,IF(AND(АВР!$AD$8=ЦИКЛ!$R$6,ЦИКЛ!$G$3=M712,ЦИКЛ!$B$37=АВР!K712),ЦИКЛ!$G$30,IF(AND(АВР!$AD$8=ЦИКЛ!$R$6,ЦИКЛ!$H$3=M712,ЦИКЛ!$B$37=АВР!K712),ЦИКЛ!$H$30,IF(AND(АВР!$AD$8=ЦИКЛ!$R$6,ЦИКЛ!$I$3=M712,ЦИКЛ!$B$37=АВР!K712),ЦИКЛ!$I$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$9,ЦИКЛ!$D$3=M712,ЦИКЛ!$B$37=АВР!K712),ЦИКЛ!$D$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$9,ЦИКЛ!$E$3=M712,ЦИКЛ!$B$37=АВР!K712),ЦИКЛ!$E$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$9,ЦИКЛ!$F$3=M712,ЦИКЛ!$B$37=АВР!K712),ЦИКЛ!$F$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$21,ЦИКЛ!$G$3=M712,ЦИКЛ!$B$37=АВР!K712),ЦИКЛ!$G$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$9,ЦИКЛ!$H$3=M712,ЦИКЛ!$B$37=АВР!K712),ЦИКЛ!$H$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$9,ЦИКЛ!$I$3=M712,ЦИКЛ!$B$37=АВР!K712),ЦИКЛ!$I$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$12,ЦИКЛ!$D$3=M712,ЦИКЛ!$B$37=АВР!K712),ЦИКЛ!$D$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$12,ЦИКЛ!$E$3=M712,ЦИКЛ!$B$37=АВР!K712),ЦИКЛ!$E$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$12,ЦИКЛ!$F$3=M712,ЦИКЛ!$B$37=АВР!K712),ЦИКЛ!$F$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$12,ЦИКЛ!$G$3=M712,ЦИКЛ!$B$37=АВР!K712),ЦИКЛ!$G$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$12,ЦИКЛ!$H$3=M712,ЦИКЛ!$B$37=АВР!K712),ЦИКЛ!$H$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$12,ЦИКЛ!$I$3=M712,ЦИКЛ!$B$37=АВР!K712),ЦИКЛ!$I$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$54,ЦИКЛ!$D$3=M712,ЦИКЛ!$B$37=АВР!K712),ЦИКЛ!$D$62,IF(AND(АВР!$AD$8=ЦИКЛ!$A$54,ЦИКЛ!$E$3=M712,ЦИКЛ!$B$37=АВР!K712),ЦИКЛ!$E$62,IF(AND(АВР!$AD$8=ЦИКЛ!$A$54,ЦИКЛ!$F$3=M712,ЦИКЛ!$B$37=АВР!K712),ЦИКЛ!$F$62,IF(AND(АВР!$AD$8=ЦИКЛ!$A$54,ЦИКЛ!$G$3=M712,ЦИКЛ!$B$37=АВР!K712),ЦИКЛ!$G$62,IF(AND(АВР!$AD$8=ЦИКЛ!$A$54,ЦИКЛ!$H$3=M712,ЦИКЛ!$B$37=АВР!K712),ЦИКЛ!$H$62,IF(AND(АВР!$AD$8=ЦИКЛ!$A$54,ЦИКЛ!$I$3=M712,ЦИКЛ!$B$37=АВР!K712),ЦИКЛ!$I$62,IF(AND(АВР!$AD$8=ЦИКЛ!$A$72,ЦИКЛ!$D$3=M712,ЦИКЛ!$B$37=АВР!K712),ЦИКЛ!$D$80,IF(AND(АВР!$AD$8=ЦИКЛ!$A$72,ЦИКЛ!$E$3=M712,ЦИКЛ!$B$37=АВР!K712),ЦИКЛ!$E$80,IF(AND(АВР!$AD$8=ЦИКЛ!$A$72,ЦИКЛ!$F$3=M712,ЦИКЛ!$B$37=АВР!K712),ЦИКЛ!$F$80,IF(AND(АВР!$AD$8=ЦИКЛ!$A$72,ЦИКЛ!$G$3=M712,ЦИКЛ!$B$37=АВР!K712),ЦИКЛ!$G$80,IF(AND(АВР!$AD$8=ЦИКЛ!$A$72,ЦИКЛ!$H$3=M712,ЦИКЛ!$B$37=АВР!K712),ЦИКЛ!$H$80,IF(AND(АВР!$AD$8=ЦИКЛ!$A$72,ЦИКЛ!$I$3=M712,ЦИКЛ!$B$37=АВР!K712),ЦИКЛ!$I$80,IF(AND(АВР!$AD$8=ЦИКЛ!$A$90,ЦИКЛ!$D$3=M712,ЦИКЛ!$B$37=АВР!K712),ЦИКЛ!$D$98,IF(AND(АВР!$AD$8=ЦИКЛ!$A$90,ЦИКЛ!$E$3=M712,ЦИКЛ!$B$37=АВР!K712),ЦИКЛ!$E$98,IF(AND(АВР!$AD$8=ЦИКЛ!$A$90,ЦИКЛ!$F$3=M712,ЦИКЛ!$B$37=АВР!K712),ЦИКЛ!$F$98,IF(AND(АВР!$AD$8=ЦИКЛ!$A$90,ЦИКЛ!$G$3=M712,ЦИКЛ!$B$37=АВР!K712),ЦИКЛ!$G$98,IF(AND(АВР!$AD$8=ЦИКЛ!$A$90,ЦИКЛ!$H$3=M712,ЦИКЛ!$B$37=АВР!K712),ЦИКЛ!$H$98,IF(AND(АВР!$AD$8=ЦИКЛ!$A$90,ЦИКЛ!$I$3=M712,ЦИКЛ!$B$37=АВР!K712),ЦИКЛ!$I$98,IF(AND(АВР!$AD$8=ЦИКЛ!$A$113,ЦИКЛ!$D$3=M712,ЦИКЛ!$B$37=АВР!K712),ЦИКЛ!$D$118,IF(AND(АВР!$AD$8=ЦИКЛ!$A$108,ЦИКЛ!$E$3=M712,ЦИКЛ!$B$37=АВР!K712),ЦИКЛ!$E$118,IF(AND(АВР!$AD$8=ЦИКЛ!$A$113,ЦИКЛ!$F$3=M712,ЦИКЛ!$B$37=АВР!K712),ЦИКЛ!$F$118,IF(AND(АВР!$AD$8=ЦИКЛ!$A$108,ЦИКЛ!$G$3=M712,ЦИКЛ!$B$37=АВР!K712),ЦИКЛ!$G$118,IF(AND(АВР!$AD$8=ЦИКЛ!$A$113,ЦИКЛ!$H$3=M712,ЦИКЛ!$B$37=АВР!K712),ЦИКЛ!$H$118,IF(AND(АВР!$AD$8=ЦИКЛ!$A$108,ЦИКЛ!$I$3=M712,ЦИКЛ!$B$37=АВР!K712),ЦИКЛ!$I$118,IF(AND(АВР!$AD$8=ЦИКЛ!$A$135,ЦИКЛ!$D$3=M712,ЦИКЛ!$B$37=АВР!K712),ЦИКЛ!$D$140,IF(AND(АВР!$AD$8=ЦИКЛ!$A$130,ЦИКЛ!$E$3=M712,ЦИКЛ!$B$37=АВР!K712),ЦИКЛ!$E$140,IF(AND(АВР!$AD$8=ЦИКЛ!$A$135,ЦИКЛ!$F$3=M712,ЦИКЛ!$B$37=АВР!K712),ЦИКЛ!$F$140,IF(AND(АВР!$AD$8=ЦИКЛ!$A$130,ЦИКЛ!$G$3=M712,ЦИКЛ!$B$37=АВР!K712),ЦИКЛ!$G$140,IF(AND(АВР!$AD$8=ЦИКЛ!$A$135,ЦИКЛ!$H$3=M712,ЦИКЛ!$B$37=АВР!K712),ЦИКЛ!$H$140,IF(AND(АВР!$AD$8=ЦИКЛ!$A$130,ЦИКЛ!$I$3=M712,ЦИКЛ!$B$37=АВР!K712),ЦИКЛ!$I$140))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))',
     1, '=V712*W712*X712', '=Y712-AA712-AB712-AC712-AD712', None, None, None, None, None],
    ['=ROW()-ROW($A$46)', None, None, 'спо', 'Ловильный инструмент', 'Подъем НКТ  4 скорость', None, None, None,
     None,
     '73мм', 1000,
     '=IF(AND(L713/V713>=ЦИКЛ!$V$9,L713/V713<=ЦИКЛ!$W$9),ЦИКЛ!$U$9,IF(AND(L713/V713>=ЦИКЛ!$V$10,L713/V713<=ЦИКЛ!$W$10),ЦИКЛ!$U$10,IF(AND(L713/V713>=ЦИКЛ!$V$11,L713/V713<=ЦИКЛ!$W$11),ЦИКЛ!$U$11,IF(AND(L713/V713>=ЦИКЛ!$V$12,L713/V713<=ЦИКЛ!$W$12),ЦИКЛ!$U$12,IF(AND(L713/V713>=ЦИКЛ!$V$13,L713/V713<=ЦИКЛ!$W$13),ЦИКЛ!$U$13,IF(AND(L713/V713>=ЦИКЛ!$V$14,L713/V713<=ЦИКЛ!$W$14),ЦИКЛ!$U$14))))))',
     '=IF(AND(АВР!$AD$8=ЦИКЛ!$A$109,ЦИКЛ!$D$3=M713),ЦИКЛ!$J$119,IF(AND(АВР!$AD$8=ЦИКЛ!$A$109,ЦИКЛ!$E$3=M713),ЦИКЛ!$K$119,IF(AND(АВР!$AD$8=ЦИКЛ!$A$109,ЦИКЛ!$F$3=M713),ЦИКЛ!$L$119,IF(AND(АВР!$AD$8=ЦИКЛ!$A$109,ЦИКЛ!$G$3=M713),ЦИКЛ!$M$119,IF(AND(АВР!$AD$8=ЦИКЛ!$A$109,ЦИКЛ!$H$3=M713),ЦИКЛ!$N$119,IF(AND(АВР!$AD$8=ЦИКЛ!$A$109,ЦИКЛ!$I$3=M713),ЦИКЛ!$O$119,IF(AND(АВР!$AD$8=ЦИКЛ!$A$131,ЦИКЛ!$D$3=M713),ЦИКЛ!$J$141,IF(AND(АВР!$AD$8=ЦИКЛ!$A$131,ЦИКЛ!$E$3=M713),ЦИКЛ!$K$141,IF(AND(АВР!$AD$8=ЦИКЛ!$A$131,ЦИКЛ!$F$3=M713),ЦИКЛ!$L$141,IF(AND(АВР!$AD$8=ЦИКЛ!$A$131,ЦИКЛ!$G$3=M713),ЦИКЛ!$M$141,IF(AND(АВР!$AD$8=ЦИКЛ!$A$131,ЦИКЛ!$H$3=M713),ЦИКЛ!$N$141,IF(AND(АВР!$AD$8=ЦИКЛ!$A$131,ЦИКЛ!$I$3=M713),ЦИКЛ!$O$141))))))))))))',
     None, None, None, None,
     '=IF($AD$8=ЦИКЛ!$A$4,ЦИКЛ!$P$4,IF($AD$8=ЦИКЛ!$A$7,ЦИКЛ!$P$7,IF($AD$8=ЦИКЛ!$A$10,ЦИКЛ!$P$7,IF($AD$8=ЦИКЛ!$A$52,ЦИКЛ!$P$52,IF($AD$8=ЦИКЛ!$A$70,ЦИКЛ!$P$70,IF($AD$8=ЦИКЛ!$A$88,ЦИКЛ!$P$88,IF($AD$8=ЦИКЛ!$A$106,ЦИКЛ!$P$106,IF($AD$8=ЦИКЛ!$A$133,ЦИКЛ!$P$133,IF($AD$8=ЦИКЛ!$Q$4,ЦИКЛ!$P$4,IF($AD$8=ЦИКЛ!$R$4,ЦИКЛ!$P$4))))))))))',
     None, 'шт', 100,
     '=IF(AND(АВР!$AD$8=ЦИКЛ!$A$109,ЦИКЛ!$D$3=M713,ЦИКЛ!$B$37=АВР!K713),ЦИКЛ!$D$119,IF(AND(АВР!$AD$8=ЦИКЛ!$A$109,ЦИКЛ!$E$3=M713,ЦИКЛ!$B$37=АВР!K713),ЦИКЛ!$E$119,IF(AND(АВР!$AD$8=ЦИКЛ!$A$109,ЦИКЛ!$F$3=M713,ЦИКЛ!$B$37=АВР!K713),ЦИКЛ!$F$119,IF(AND(АВР!$AD$8=ЦИКЛ!$A$109,ЦИКЛ!$G$3=M713,ЦИКЛ!$B$37=АВР!K713),ЦИКЛ!$G$119,IF(AND(АВР!$AD$8=ЦИКЛ!$A$109,ЦИКЛ!$H$3=M713,ЦИКЛ!$B$37=АВР!K713),ЦИКЛ!$H$119,IF(AND(АВР!$AD$8=ЦИКЛ!$A$109,ЦИКЛ!$I$3=M713,ЦИКЛ!$B$37=АВР!K713),ЦИКЛ!$I$119,IF(AND(АВР!$AD$8=ЦИКЛ!$A$131,ЦИКЛ!$D$3=M713,ЦИКЛ!$B$37=АВР!K713),ЦИКЛ!$D$141,IF(AND(АВР!$AD$8=ЦИКЛ!$A$131,ЦИКЛ!$E$3=M713,ЦИКЛ!$B$37=АВР!K713),ЦИКЛ!$E$141,IF(AND(АВР!$AD$8=ЦИКЛ!$A$131,ЦИКЛ!$F$3=M713,ЦИКЛ!$B$37=АВР!K713),ЦИКЛ!$F$141,IF(AND(АВР!$AD$8=ЦИКЛ!$A$131,ЦИКЛ!$G$3=M713,ЦИКЛ!$B$37=АВР!K713),ЦИКЛ!$G$141,IF(AND(АВР!$AD$8=ЦИКЛ!$A$131,ЦИКЛ!$H$3=M713,ЦИКЛ!$B$37=АВР!K713),ЦИКЛ!$H$141,IF(AND(АВР!$AD$8=ЦИКЛ!$A$131,ЦИКЛ!$I$3=M713,ЦИКЛ!$B$37=АВР!K713),ЦИКЛ!$I$141))))))))))))',
     1, '=V713*W713*X713', '=Y713-AA713-AB713-AC713-AD713', None, None, None, None, None],
    ['=ROW()-ROW($A$46)', None, None, 'спо', 'Ловильный инструмент', 'Долив скважины', None, None, None, None, None,
     None, None, None, None, None, None, None, '§168разд.1', None, 'шт', '=((SUM(V710:V713))/10)', 0.003, 1,
     '=V714*W714*X714', '=Y714-AA714-AB714-AC714-AD714', None, None, None, None, None],
    ['=ROW()-ROW($A$46)', 'подъем 73мм', None, 'спо', 'Ловильный инструмент', 'Откатывание труб с 201 трубы ', None,
     None, None, None, None, None, None, None, None, None, None, None, '§40разд.1', None, 'шт',
     '=((SUM(V710:V713))-201)', 0.008, 1, '=V715*W715*X715', '=Y715-AA715-AB715-AC715-AD715', None, None, None,
     None,
     None],
    ['=ROW()-ROW($A$46)', None, None, 'спо', 'Ловильный инструмент', 'Осложнение при подъеме НКТ', None, None, None,
     None, None, None, 'Объем', 0, 'АКТ№', None, None, None, 'факт', None, 'час', 0, 1, 1, '=V716*W716*X716',
     '=Y716-AA716-AB716-AC716-AD716', None, None, None, None, None],
    ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None, 'Д/ж, м/ж спайдера', None, None, None, None, None, None,
     None, None, None, None, None, None, '§185разд.1', None, 'час', 1, 0.14, 1, '=V717*W717*X717',
     '=Y717-AA717-AB717-AC717-AD717', None, None, None, None, None],
    ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None, 'ЗР после подъема ловиля (холостая ходка)', None, None,
     None, None, None, None, None, None, None, None, None, None, '§241разд.1', None, 'шт', 1, 0.13, 1,
     '=V718*W718*X718', '=Y718-AA718-AB718-AC718-AD718', None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
     None,
     None, None, None, None, None, None, None, None, None, None, None, None],
    ['=ROW()-ROW($A$46)', None, None, 'спо', 'Ловильный инструмент',
     'Освобождение овершота, мятой трубы, щучьей пасти',
     None, None, None, None, None, None, None, None, None, None, None, None, '§242разд.1', None, 'шт', 1, 0.32, 1,
     '=V720*W720*X720', '=Y720-AA720-AB720-AC720-AD720', None, None, None, None, None],
    ['=ROW()-ROW($A$46)', None, None, 'спо', 'Ловильный инструмент', 'Освобождение колокола', None, None, None,
     None,
     None, None, None, None, None, None, None, None, '§242разд.1', None, 'шт', 1, 0.33, 1, '=V721*W721*X721',
     '=Y721-AA721-AB721-AC721-AD721', None, None, None, None, None],
    ['=ROW()-ROW($A$46)', None, None, 'спо', 'Ловильный инструмент', 'Освобождение наружней труболовки', None, None,
     None, None, None, None, None, None, None, None, None, None, '§242разд.1', None, 'шт', 1, 0.38, 1,
     '=V722*W722*X722', '=Y722-AA722-AB722-AC722-AD722', None, None, None, None, None],
    ['=ROW()-ROW($A$46)', None, None, 'спо', 'Ловильный инструмент', 'Освобождение крючка', None, None, None, None,
     None, None, None, None, None, None, None, None, '§242разд.1', None, 'шт', 1, 0.23, 1, '=V723*W723*X723',
     '=Y723-AA723-AB723-AC723-AD723', None, None, None, None, None],
    ['=ROW()-ROW($A$46)', None, None, 'спо', 'Ловильный инструмент', 'Освобождение шлипса', None, None, None, None,
     None, None, None, None, None, None, None, None, '§242разд.1', None, 'шт', 1, 0.2, 1, '=V724*W724*X724',
     '=Y724-AA724-AB724-AC724-AD724', None, None, None, None, None],
    ['=ROW()-ROW($A$46)', None, None, 'спо', 'Ловильный инструмент', 'Освобождение труболовки внутренней, метчика',
     None, None, None, None, None, None, None, None, None, None, None, None, '§242разд.1', None, 'шт', 1, 0.27, 1,
     '=V725*W725*X725', '=Y725-AA725-AB725-AC725-AD725', None, None, None, None, None]]

if __name__ == "__main__":
    # app3 = QApplication(sys.argv)

    app = QApplication(sys.argv)
    window = EmergencyWork(22, 22)
    window.show()
    sys.exit(app.exec_())
