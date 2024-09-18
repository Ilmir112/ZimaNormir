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
from normir.drilling_work import DrillingWork
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
        self.solvent_injection_label = QLabel('Закачка растворителя')
        self.nkt_is_same_label = QLabel('Кол-во НКТ на подъем совпадает со спуском')
        self.normalization_question_label = QLabel('Была ли нормализация')
        self.raid_work_text_label = QLabel('Интервалы райбирования')
        self.count_of_nkt_extensions_label = QLabel('Кол-во метров райбирования')

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

        self.nkt_label()

        self.grid.addWidget(self.complications_during_tubing_running_label, 26, 1)
        self.grid.addWidget(self.complications_during_tubing_running_combo, 27, 1)

        self.grid.addWidget(self.complications_of_failure_label, 28, 1)
        self.grid.addWidget(self.complications_of_failure_combo, 29, 1)

        self.volume_well_flush_line = QLineEdit(self)
        self.volume_well_flush_line.setValidator(self.validator_float)

        self.grid.addWidget(self.volume_well_flush_label, 30, 3)
        self.grid.addWidget(self.volume_well_flush_line, 31, 3)

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

        self.normalization_question_combo = QComboBox(self)
        self.normalization_question_combo.addItems(['Нет', 'Да'])

        self.grid.addWidget(self.normalization_question_label, 70, 1)
        self.grid.addWidget(self.normalization_question_combo, 71, 1)

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
        self.normalization_question_combo.currentTextChanged.connect(self.update_normalization_question_combo)
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

        self.drilling_ek_combo_label = QLabel('Что бурили')
        self.drilling_ek_combo = QComboBox(self)
        self.drilling_ek_combo.addItems(drilling_ek_list)

        self.grid.addWidget(self.drilling_ek_combo_label, 30, 2)
        self.grid.addWidget(self.drilling_ek_combo, 31, 2)

        self.grid.addWidget(self.count_of_nkt_extensions_label, 30, 4)
        self.grid.addWidget(self.count_of_nkt_extensions_line, 31, 4)

        self.raid_work_time_begin_label = QLabel('начало райбирования')
        self.raid_work_time_begin_date = QDateTimeEdit(self)
        self.raid_work_time_begin_date.setDisplayFormat("dd.MM.yyyy HH:mm")
        self.raid_work_time_begin_date.setDateTime(self.date_work_str)

        self.raid_work_time_end_label = QLabel('Окончание осложнения райбирования')
        self.raid_work_time_end_date = QDateTimeEdit(self)
        self.raid_work_time_end_date.setDisplayFormat("dd.MM.yyyy HH:mm")
        self.raid_work_time_end_date.setDateTime(self.date_work_str)

        self.raid_work_time_label = QLabel('затраченное время')
        self.raid_work_time_line = QLineEdit(self)
        self.raid_work_time_line.setValidator(self.validator_float)

        self.grid.addWidget(self.raid_work_time_begin_label, 30, 5)
        self.grid.addWidget(self.raid_work_time_begin_date, 31, 5)
        self.grid.addWidget(self.raid_work_time_end_label, 30, 6)
        self.grid.addWidget(self.raid_work_time_end_date, 31, 6)
        self.grid.addWidget(self.raid_work_time_label, 30, 7)
        self.grid.addWidget(self.raid_work_time_line, 31, 7)

        self.raid_work_time_end_date.dateTimeChanged.connect(self.update_date_of_raid)
        self.raid_work_time_begin_date.dateTimeChanged.connect(self.update_date_of_raid)

        self.raid_work_text_edit.editingFinished.connect(self.update_raid_work)



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


class TabWidget(QTabWidget):
    def __init__(self):
        super().__init__()
        self.addTab(TabPage_SO_Timplate(self), 'Райбер')


class RaidWork(TemplateWork):
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
        elif self.select_type_combo in ['НКТ', 'СБТ']:
            self.type_equipment = 'Райбер'
            self.coefficient_lifting = 1.2

            self.raid_work_text_edit = current_widget.raid_work_text_edit.text()

            self.count_of_nkt_extensions_line = current_widget.count_of_nkt_extensions_line.text()
            if self.count_of_nkt_extensions_line != '':
                self.count_of_nkt_extensions_line = int(self.count_of_nkt_extensions_line)
            else:
                question = QMessageBox.question(self, 'райбирование', 'Райбирования не было?')
                if question == QMessageBox.StandardButton.No:
                    return

            if self.select_type_combo == 'СБТ':
                self.type_rotor_combo = current_widget.type_rotor_combo.currentText()
                self.count_spo_sbt_combo = current_widget.count_spo_sbt_combo.currentText()
                self.type_key_combo = current_widget.type_key_combo.currentText()

        self.nkt_is_same_combo = current_widget.nkt_is_same_combo.currentText()
        self.equipment_audit_combo = current_widget.equipment_audit_combo.currentText()
        self.volume_well_flush_line = current_widget.volume_well_flush_line.text()
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
            read_data = self.read_nkt_up(current_widget)
            if read_data is None:
                return
        except Exception as e:
            QMessageBox.warning(self, 'Ошибка', f'Введены не все значения {e}')
            return

        if self.nkt_is_same_combo == 'Нет':
            read_data = self.read_nkt_down(current_widget)
            if read_data is None:
                return
        else:
            self.dict_nkt_up = self.dict_nkt

        self.complications_of_failure_combo = current_widget.complications_of_failure_combo.currentText()
        self.complications_during_tubing_running_combo = current_widget.complications_during_tubing_running_combo.currentText()
        self.normalization_question_combo = current_widget.normalization_question_combo.currentText()
        self.solvent_injection_combo = current_widget.solvent_injection_combo.currentText()
        self.technological_crap_question_combo = current_widget.technological_crap_question_combo.currentText()
        self.complications_when_lifting_combo = current_widget.complications_when_lifting_combo.currentText()
        self.drilling_ek_combo = current_widget.drilling_ek_combo.currentText()
        if self.drilling_ek_combo == '':
            QMessageBox.warning(self, 'Нужно выбрать что бурили')
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

            self.read_solvent_volume(current_widget)

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
                 None, None, None, None, None, 'что бурили:', self.drilling_ek_combo, 'АКТ№', None, None, None,
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
                 None, None, None, 'АКТ№', None, None, None, '§301разд.1', None, 'м3', self.volume_well_flush_line,
                 0.033,
                 1, '=V746*W746*X746',
                 '=Y746-AA746-AB746-AC746-AD746', None, None, None, None, None]]

            work_list.extend(raid_list)

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
                work_list.extend(DrillingWork.descent_SBT(self))

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
            work_list.extend(DrillingWork.drilling_with_sbt_work(self))

        if self.count_of_nkt_extensions_line != 0:
            work_list.extend(self.skm_work())

        if self.select_type_combo == 'СБТ':
            work_list.extend(DrillingWork.drilling_with_sbt_work_up(self))

        # if self.volume_well_flush_line != '':
        #     work_list.extend(self.volume_well_work())

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
            work_list.extend(DrillingWork.lifting_SBT(self))

        if self.equipment_audit_combo == 'Да':
            work_list.extend([
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
                 f'Ревизия:{self.equipment_audit_text_line}',
                 None, None, None, None, None, None, None, None, None, None, None,
                 None, 'факт', None, 'час', 0.5, 1, 1, '=V480*W480*X480', '=Y480-AA480-AB480-AC480-AD480', None,
                 None, None, None, None]]
            )

        return work_list




if __name__ == "__main__":
    # app3 = QApplication(sys.argv)

    app = QApplication(sys.argv)
    window = RaidWork(22, 22)
    window.show()
    sys.exit(app.exec_())
