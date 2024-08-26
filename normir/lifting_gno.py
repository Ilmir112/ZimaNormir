
import sys
from datetime import datetime, timedelta

import well_data

from collections import namedtuple
from normir.files_with_list import cause_presence_of_jamming
from normir.norms import LIFTING_NORM_NKT, LIFTING_NORM_SUCKER_POD
from PyQt5.QtGui import QIntValidator, QDoubleValidator
from PyQt5.QtWidgets import QWidget, QLabel, QComboBox, QLineEdit, QGridLayout, QTabWidget, QMainWindow, QPushButton, \
    QMessageBox, QApplication, QHeaderView, QTableWidget, QTableWidgetItem, QTextEdit, QDateEdit, QDateTimeEdit
from PyQt5.QtCore import Qt

from normir.relocation_brigade import TextEditTableWidgetItem


class TabPage_SO_Lifting_gno(QWidget):
    def __init__(self, parent=None):
        super().__init__()

        self.validator_int = QIntValidator(0, 600)
        self.validator_float = QDoubleValidator(0.2, 1000, 1)

        self.date_work_label = QLabel('Дата работы')
        self.date_work_line = QLineEdit(self)
        self.date_work_line.setText(f'{well_data.date_work}')
        self.date_work_str = datetime.strptime(self.date_work_line.text(), '%d.%m.%Y')

        self.gno_label = QLabel("вид поднимаемого ГНО", self)
        self.gno_combo = QComboBox(self)
        gno_list = ['', 'пакер', 'ОРЗ', 'ОРД', 'воронка', 'НН с пакером', 'НВ с пакером',
                    'ЭЦН с пакером', 'ЭЦН', 'НВ', 'НН']  # 'ЭЦН с автономными пакерами'
        self.gno_combo.addItems(gno_list)

        self.grid = QGridLayout(self)

        if well_data.date_work != '':
            self.date_work_line.setText(well_data.date_work)

        self.grid.addWidget(self.date_work_label, 4, 2)
        self.grid.addWidget(self.date_work_line, 5, 2)

        self.grid.addWidget(self.gno_label, 4, 3)
        self.grid.addWidget(self.gno_combo, 5, 3)

        self.gno_combo.currentTextChanged.connect(self.update_select_gno)

    def update_select_gno(self, index):

        self.complications_of_failure_label = QLabel('осложнения при срыве ПШ')
        self.complications_of_failure_combo = QComboBox(self)
        self.complications_of_failure_combo.addItems(['Нет', 'Да'])

        self.complications_during_disassembly_label = QLabel('осложнения при демонтаже')
        self.complications_during_disassembly_combo = QComboBox(self)
        self.complications_during_disassembly_combo.addItems(['Нет', 'Да'])

        self.complications_when_lifting_label = QLabel('Осложнения при подьеме штанг')
        self.complications_when_lifting_combo = QComboBox(self)
        self.complications_when_lifting_combo.addItems(['Нет', 'Да'])

        self.grid.addWidget(self.complications_of_failure_label, 8, 1)
        self.grid.addWidget(self.complications_of_failure_combo, 9, 1)

        # self.grid.addWidget(self.complications_of_failure_label, 10, 1)
        # self.grid.addWidget(self.complications_of_failure_combo, 11, 1)

        self.grid.addWidget(self.complications_during_disassembly_label, 20, 1)
        self.grid.addWidget(self.complications_during_disassembly_combo, 21, 1)

        self.grid.addWidget(self.complications_when_lifting_label, 36, 1)
        self.grid.addWidget(self.complications_when_lifting_combo, 37, 1)

        if index == 'пакер':
            self.complications_when_lifting_label.setText('Осложнения при подьеме НКТ')

            self.nkt_48_lenght_label = QLabel('Длина НКТ48')
            self.nkt_48_lenght_edit = QLineEdit(self)

            self.nkt_48_count_label = QLabel('Кол-во НКТ48')
            self.nkt_48_count_edit = QLineEdit(self)

            self.nkt_60_lenght_label = QLabel('Длина НКТ60')
            self.nkt_60_lenght_edit = QLineEdit(self)

            self.nkt_60_count_label = QLabel('Кол-во НКТ60')
            self.nkt_60_count_edit = QLineEdit(self)

            self.nkt_73_lenght_label = QLabel('Длина НКТ73')
            self.nkt_73_lenght_edit = QLineEdit(self)

            self.nkt_73_count_label = QLabel('Кол-во НКТ73')
            self.nkt_73_count_edit = QLineEdit(self)

            self.nkt_89_lenght_label = QLabel('Длина НКТ89-102')
            self.nkt_89_lenght_edit = QLineEdit(self)

            self.nkt_89_count_label = QLabel('Кол-во НКТ89-102')
            self.nkt_89_count_edit = QLineEdit(self)

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
            try:
                self.pressuar_gno_label.setParent(None)
                self.pressuar_gno_combo.setParent(None)
            except:
                pass

        elif index == 'НВ':

            self.complications_of_failure_label.setText('Рассхаживание')
            self.complications_during_disassembly_label.setText('Осложнения при демонтаже')

            self.pressuar_gno_label = QLabel('Опрессовка ГНО')
            self.pressuar_gno_combo = QComboBox(self)
            self.pressuar_gno_combo.addItems(['Нет', 'Да'])

            self.determination_of_the_weight_text_label = QLabel('Определение веса штанг')
            self.determination_of_the_weight_text_line = QLineEdit(self)

            self.sucker_pod_19_lenght_label = QLabel('Длина штанги 19мм')
            self.sucker_pod_22_lenght_label = QLabel('Длина штанги 22мм')
            self.sucker_pod_25_lenght_label = QLabel('Длина штанги 25мм')

            self.sucker_pod_19_lenght_edit = QLineEdit(self)
            self.sucker_pod_19_lenght_edit.setValidator(self.validator_float)
            self.sucker_pod_19_lenght_edit.setText('8')

            self.sucker_pod_19_count_label = QLabel('Кол-во штанги 19мм')
            self.sucker_pod_19_count_edit = QLineEdit(self)
            self.sucker_pod_19_count_edit.setValidator(self.validator_float)

            self.sucker_pod_22_lenght_edit = QLineEdit(self)
            self.sucker_pod_22_lenght_edit.setText('8')
            self.sucker_pod_22_lenght_edit.setValidator(self.validator_float)

            self.sucker_pod_22_count_label = QLabel('Кол-во штанги 22мм')
            self.sucker_pod_22_count_edit = QLineEdit(self)
            self.sucker_pod_22_count_edit.setValidator(self.validator_float)

            self.sucker_pod_25_lenght_edit = QLineEdit(self)
            self.sucker_pod_25_lenght_edit.setText('8')
            self.sucker_pod_25_lenght_edit.setValidator(self.validator_float)

            self.sucker_pod_25_count_label = QLabel('Кол-во штанги 25мм')
            self.sucker_pod_25_count_edit = QLineEdit(self)
            self.sucker_pod_25_count_edit.setValidator(self.validator_float)

            self.grid.addWidget(self.sucker_pod_19_lenght_label, 26, 1)
            self.grid.addWidget(self.sucker_pod_19_lenght_edit, 27, 1)

            self.grid.addWidget(self.sucker_pod_22_lenght_label, 26, 2)
            self.grid.addWidget(self.sucker_pod_22_lenght_edit, 27, 2)

            self.grid.addWidget(self.sucker_pod_25_lenght_label, 26, 3)
            self.grid.addWidget(self.sucker_pod_25_lenght_edit, 27, 3)

            self.grid.addWidget(self.sucker_pod_19_count_label, 28, 1)
            self.grid.addWidget(self.sucker_pod_19_count_edit, 29, 1)

            self.grid.addWidget(self.sucker_pod_22_count_label, 28, 2)
            self.grid.addWidget(self.sucker_pod_22_count_edit, 29, 2)

            self.grid.addWidget(self.sucker_pod_25_count_label, 28, 3)
            self.grid.addWidget(self.sucker_pod_25_count_edit, 29, 3)

            self.grid.addWidget(self.pressuar_gno_label, 6, 1)
            self.grid.addWidget(self.pressuar_gno_combo, 7, 1)

            self.grid.addWidget(self.determination_of_the_weight_text_label, 6, 3)
            self.grid.addWidget(self.determination_of_the_weight_text_line, 7, 3)

            self.pressuar_gno_combo.currentTextChanged.connect(self.update_pressuar_gno_combo)
        self.complications_during_disassembly_combo.currentTextChanged.connect(
            self.update_complications_during_disassembly)
        self.complications_of_failure_combo.currentTextChanged.connect(self.update_complications_of_failure)
        self.complications_when_lifting_combo.currentTextChanged.connect(self.update_complications_when_lifting)


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
        if self.gno_combo.currentText() in ['НВ', 'НН']:
            self.complications_of_failure_text_label.setText(None)
            self.complications_of_failure_text_label.setText('Текст рассхаживания')

    def update_date_when_lifting(self):
        time_begin = self.complications_when_lifting_time_begin_date.dateTime()
        time_end = self.complications_when_lifting_time_end_date.dateTime()

        time_difference = self.calculate_date(time_begin, time_end)
        self.complications_when_lifting_time_line.setText(str(time_difference))

    def update_date_during_disassembly_q(self):
        time_begin = self.complications_during_disassembly_q_time_begin_date.dateTime()
        time_end = self.complications_during_disassembly_q_time_end_date.dateTime()

        time_difference = self.calculate_date(time_begin, time_end)
        self.complications_during_disassembly_time_line.setText(str(time_difference))

    def update_date_of_failure(self):
        time_begin = self.complications_of_failure_time_begin_date.dateTime()
        time_end = self.complications_of_failure_time_end_date.dateTime()

        time_difference = self.calculate_date(time_begin, time_end)
        self.complications_of_failure_time_line.setText(str(time_difference))


    def calculate_date(self,  time_begin, time_end):
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

            self.complications_when_lifting_time_label = QLabel('затраченное время')
            self.complications_when_lifting_time_line = QLineEdit(self)

            self.complications_when_lifting_time_line.setValidator(self.validator_float)
            self.grid.addWidget(self.complications_when_lifting_text_label, 36, 2)
            self.grid.addWidget(self.complications_when_lifting_text_line, 37, 2)

            self.grid.addWidget(self.complications_when_lifting_time_begin_label, 36, 3)
            self.grid.addWidget(self.complications_when_lifting_time_begin_date, 37, 3)

            self.grid.addWidget(self.complications_when_lifting_time_end_label, 36, 4)
            self.grid.addWidget(self.complications_when_lifting_time_end_date, 37, 4)

            self.grid.addWidget(self.complications_when_lifting_time_label, 36, 5)
            self.grid.addWidget(self.complications_when_lifting_time_line, 37, 5)

            self.complications_when_lifting_time_end_date.dateTimeChanged.connect(self.update_date_when_lifting)
            self.complications_when_lifting_time_begin_date.dateTimeChanged.connect(self.update_date_when_lifting)

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


            self.complications_during_disassembly_q_time_end_label = QLabel('Окончание осложнения')
            self.complications_during_disassembly_q_time_end_date
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
            self.grid.addWidget(self.complications_during_disassembly_q_label, 20, 2)
            self.grid.addWidget(self.complications_during_disassembly_q_line, 21, 2)

            self.grid.addWidget(self.complications_during_disassembly_q_time_begin_label, 20, 3)
            self.grid.addWidget(self.complications_during_disassembly_q_time_begin_date, 21, 3)

            self.grid.addWidget(self.complications_during_disassembly_q_time_begin_label, 20, 4)
            self.grid.addWidget(self.complications_during_disassembly_q_time_end_date, 21, 4)

            self.grid.addWidget(self.complications_during_disassembly_time_label, 20, 5)
            self.grid.addWidget(self.complications_during_disassembly_time_line, 21, 5)

            self.complications_during_disassembly_q_time_end_date.dateTimeChanged.connect(self.update_date_during_disassembly_q)
            self.complications_during_disassembly_q_time_begin_date.dateTimeChanged.connect(self.update_date_during_disassembly_q)


class TabWidget(QTabWidget):
    def __init__(self):
        super().__init__()
        self.addTab(TabPage_SO_Lifting_gno(self), 'Подьем ГНО')


class LiftingWindow(QMainWindow):
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
        self.complications_during_disassembly_text_line = None
        self.complications_during_disassembly_time_line = None
        self.complications_when_lifting_text_line = None
        self.complications_when_lifting_time_line = None
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
        self.sucker_pod_19_lenght_edit = None
        self.sucker_pod_19_count_edit = None

        self.sucker_pod_22_lenght_edit = None
        self.sucker_pod_22_count_edit = None

        self.sucker_pod_25_lenght_edit = None
        self.sucker_pod_25_count_edit = None

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

        self.gno_combo = current_widget.gno_combo.currentText()

        self.date_work_line = current_widget.date_work_line.text()

        if self.gno_combo in ['пакер']:
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
                QMessageBox.warning(self, 'Ошибка', f'ВВедены не все значения {e}')
                return

        if self.gno_combo in ['НВ', 'НН']:
            self.determination_of_the_weight_text_line = current_widget.determination_of_the_weight_text_line.text()
            if self.determination_of_the_weight_text_line == '':
                QMessageBox.warning(self, 'Ошибка', f'Не введены текст опрессовки ГНО')
                return
            try:
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

            except Exception as e:
                QMessageBox.warning(self, 'Ошибка', f'ВВедены не все значения {e}')
                return

        self.complications_of_failure_combo = current_widget.complications_of_failure_combo.currentText()
        self.complications_during_disassembly_combo = current_widget.complications_during_disassembly_combo.currentText()
        self.complications_when_lifting_combo = current_widget.complications_when_lifting_combo.currentText()
        self.pressuar_gno_combo = current_widget.pressuar_gno_combo.currentText()

        if self.pressuar_gno_combo == 'Да':
            self.pressuar_gno_text_line = current_widget.pressuar_gno_text_line.text()
            if self.pressuar_gno_text_line == '':
                QMessageBox.warning(self, 'Ошибка', f'Не введены текст опрессовки ГНО')
                return

        if self.complications_of_failure_combo == 'Да':
            self.complications_of_failure_text_line = current_widget.complications_of_failure_text_line.text()
            self.complications_of_failure_time_begin_date =\
                current_widget.complications_of_failure_time_begin_date.dateTime().toPyDateTime()
            self.complications_of_failure_time_begin_date = \
                self.change_string_in_date(self.complications_of_failure_time_begin_date)

            self.complications_of_failure_time_end_date =\
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
            if self.complications_of_failure_time_line == '':
                self.complications_of_failure_time_line = round(float(self.complications_of_failure_time_line), 1)
                QMessageBox.warning(self, 'Ошибка', f'Не введены время осложнения при срыве ПШ')
                return
            if self.complications_of_failure_time_line <= 0:
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

                if self.complications_when_lifting_time_end_date == self.complications_when_lifting_time_begin_date:
                    QMessageBox.warning(self, 'Даты совпадают', 'Даты совпадают')
                    return

                if self.complications_when_lifting_text_line == '':
                    QMessageBox.warning(self, 'Ошибка', f'Не введены текст осложнения при подьеме штанг')
                    return
                if self.complications_when_lifting_time_line == '':
                    self.complications_when_lifting_time_line = round(float(self.complications_when_lifting_time_line),
                                                                      1)
                    QMessageBox.warning(self, 'Ошибка', f'Не введены время осложнения при подьеме штанг')
                    return
                if self.complications_when_lifting_time_line <= 0:
                    QMessageBox.warning(self, 'Ошибка', f'Затраченное время при подьеме штанг не может быть отрицательным')
                    return

            except Exception as e:
                QMessageBox.warning(self, 'Ошибка', f'ВВедены не все значения {e}')
                return

        if self.complications_during_disassembly_combo == 'Да':
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

            self.complications_during_disassembly_time_line =\
                current_widget.complications_during_disassembly_time_line.text()
            if self.complications_during_disassembly_time_line != '':
                self.complications_during_disassembly_time_line = round(
                    float(self.complications_during_disassembly_time_line), 1)

            if self.complications_during_disassembly_time_line <= 0:
                QMessageBox.warning(self, 'Ошибка', f'Затраченное время при демонтаже ПШ не может быть отрицательным')
                return

        asd = self.gno_combo

        if self.gno_combo == 'пакер':
            work_list = self.lifting_paker_def()
            if len(self.dict_nkt) == 0:
                question = QMessageBox.question(self, 'Ошибка', f'НКТ отсутствуют?')
                if question == QMessageBox.StandardButton.No:
                    return
        elif self.gno_combo in ['НВ']:
            work_list = self.lifting_sucker_pod_list()
            if len(self.dict_sucker_pod) == 0:
                question = QMessageBox.question(self, 'Ошибка', f'НКТ отсутствуют?')
                if question == QMessageBox.StandardButton.No:
                    return

        well_data.date_work = self.date_work_line

        MyWindow.populate_row(self, self.ins_ind, work_list, self.table_widget)
        well_data.pause = False
        self.close()

    def change_string_in_date(self, date_str):
        # Преобразуем строку в объект datetime

        formatted_date = date_str.strftime("%d.%m.%Y %H:%M")
        return formatted_date

    def lifting_sucker_pod_list(self):

        work_list = [
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, self.pressuar_gno_text_line, None,
             None, None, None, None, None, None, None, "'АКТ №1'!A1", None, None, None,
             '§150-152разд.1', None, 'шт', 1, 0.67, 1,
             '=V133*W133*X133', '=Y133-AA133-AB133-AC133-AD133', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'демонтаж АУШГН', None,
             None, None, None, None, None, None, None, None, None, None, None, '§54разд.1', None, 'шт', 1, 0.67, 1,
             '=V134*W134*X134', '=Y134-AA134-AB134-AC134-AD134', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
             self.determination_of_the_weight_text_line, None, None, None, None, None, None, None, None,
             'АКТ№', None, None, None, '§200разд.1', None, 'шт', 1, 0.57, 1, '=V135*W135*X135',
             '=ROUNDUP(Y135-AA135-AB135-AC135-AD135,2)', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
             f'Срыв {well_data.dict_pump_SHGN["do"]}', None,
             None, None, None, None, None,
             None,
             None, "'АКТ №1'!A1", None, None, None, '§301разд.1', None, 'шт', 1, 0.15, 1, '=V136*W136*X136',
             '=Y136-AA136-AB136-AC136-AD136', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
             f'{self.complications_of_failure_text_line} {self.complications_of_failure_time_begin_date}-'
             f'{self.complications_of_failure_time_end_date}', None, None, None, None, None, None, None, None,
             'АКТ№', None, None, None, 'факт', None, 'час', self.complications_of_failure_time_line, 1, 1,
             '=V138*W138*X138', '=Y138-AA138-AB138-AC138-AD138',
             None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'ПР.перед.ремонтом', None, 'Монтаж ГКШ-1200', None, None,
             None, None,
             None,
             None, None, None, None, None, None, None, '§184разд.1', None, 'шт', 1, 0.33, 1, '=V139*W139*X139',
             '=Y139-AA139-AB139-AC139-AD139', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'ПР.перед.ремонтом', None, 'Монтаж СПГ', None, None, None,
             None, None,
             None,
             None, None, None, None, None, None, '§185разд.1', None, 'шт', 1, 0.07, 1, '=V140*W140*X140',
             '=Y140-AA140-AB140-AC140-AD140', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'Устройство  рабочей площадки', None,
             None, None,
             None,
             None, None, None, None, None, None, None, None, '§54разд.1', None, 'шт', 1, 0.83, 1, '=V141*W141*X141',
             '=Y141-AA141-AB141-AC141-AD141', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'ПР.перед.ремонтом', None, 'Монтаж ГКШ-300', None, None,
             None, None, None,
             None, None, None, "'АКТ №1'!A1", None, None, None, '§184разд.1', None, 'шт', 1, 0.33, 1, '=V142*W142*X142',
             '=Y142-AA142-AB142-AC142-AD142', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'Монтаж штангового превентора', None,
             None, None,
             None,
             None, None, None, None, None, None, None, None, '§120разд.1', None, 'шт', 1, 0.35, 1, '=V143*W143*X143',
             '=Y143-AA143-AB143-AC143-AD143', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'ПР.перед.ремонтом', None, 'Опрессовка ПШМ', None, None,
             None, None, None,
             None, None, None, None, None, None, None, '§112,разд.1', None, 'шт', 1, 0.62, 1, '=V144*W144*X144',
             '=Y144-AA144-AB144-AC144-AD144', None, None, None, None, None]
        ]

        if self.complications_during_disassembly_combo == 'Да':
            work_list.insert(2, ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
             f'{self.complications_during_disassembly_q_line} '
             f'{self.complications_during_disassembly_q_time_begin_date}-'
             f'{self.complications_during_disassembly_q_time_end_date}',
                                 None, None, None, None, None, None, None, None,
             'АКТ№', None, None, None, 'факт', None, 'час', self.complications_during_disassembly_time_line, 1, 1,
             '=V138*W138*X138', '=Y138-AA138-AB138-AC138-AD138',
             None, None, None, None, None])
            self.date_work_line = self.complications_during_disassembly_q_time_end_date.split(' ')[1]
        # нормирование штанг
        work_list.extend(self.lifting_sucker_pod(self.dict_sucker_pod, 'ШТАНГИ'))

        if self.complications_when_lifting_combo == 'Да':
            work_list.append(
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', 'ШТАНГИ',
                 f'{self.complications_when_lifting_text_line} {self.complications_when_lifting_time_begin_date}- {self.complications_when_lifting_time_end_date}' , None,
                 None, None,
                 None, None, None, 'Объем', None, None, None, None, None, '§9разд.1', None, 'час',
                 f'=SUM(Z{self.ins_ind}:Z{self.ins_ind + len(work_list)} - {self.complications_when_lifting_time_line}',
                 0.017, 1, 10,
                 '=Y150-AA150-AB150-AC150-AD150', None, None, None, None, None])

            self.date_work_line = self.complications_when_lifting_time_end_date.split(' ')[1]

        list_end = [
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'Демонтаж ГКШ-300 ', None, None,
             None, None, None, None,
             None, None, None, None, None, None, '§184разд.1', None, 'шт', 1, 0.12, 1, '=V151*W151*X151',
             '=Y151-AA151-AB151-AC151-AD151', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'Демонтаж ПШМ', None, None, None,
             None, None, None,
             None, None, None, None, None, None, '§120разд.1', None, 'шт', 1, 0.25, 1, '=V152*W152*X152',
             '=Y152-AA152-AB152-AC152-AD152', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
             'Разборка  рабочей площадки частично', None, None, None,
             None, None, None, None, None, None, None, None, None, '§55разд.1', None, 'шт', 1, 0.3, 1,
             '=V153*W153*X153',
             '=Y153-AA153-AB153-AC153-AD153', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'Ревизия ГНО ', None, None, None,
             None, None, None,
             None, None, 'АКТ№', None, None, None, 'факт', None, 'час', 0.5, 1, 1, '=V154*W154*X154',
             '=Y154-AA154-AB154-AC154-AD154', None, None, None, None, None]]



        work_list.extend(list_end)



        return work_list

    def lifting_sucker_pod(self, dict_sucker_pod, type_equipment):
        work_list = [
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', type_equipment, 'ПЗР СПО перед подъемом штанг',
             None, None, None, None, None,
             None, None, None, None, None, None, None, '§191разд.1', None, 'шт', 1, 0.73, 1, '=V145*W145*X145',
             '=Y145-AA145-AB145-AC145-AD145', None, None, None, None, None]]
        sucker_count_all = sum(map(lambda x: x[1], dict_sucker_pod.values()))
        for sucker_key, sucker in dict_sucker_pod.items():
            sucker_lenght = sucker[0]
            sucker_count = sucker[1]
            aderg = LIFTING_NORM_SUCKER_POD[well_data.lifting_unit_combo]
            if well_data.lifting_unit_combo not in ['УПА-60/80 (Оснастка 3×4)', 'УПТ-32 (Оснастка 3×4)']:
                max_count = LIFTING_NORM_SUCKER_POD[well_data.lifting_unit_combo][sucker_key]['III'][1]
                koef_norm = LIFTING_NORM_SUCKER_POD[well_data.lifting_unit_combo][sucker_key]['III'][0]
                razdel_3 = LIFTING_NORM_SUCKER_POD[well_data.lifting_unit_combo][sucker_key]['раздел']
            else:
                max_count = LIFTING_NORM_SUCKER_POD[well_data.lifting_unit_combo][sucker_key]['IV'][1]
                koef_norm = LIFTING_NORM_SUCKER_POD[well_data.lifting_unit_combo][sucker_key]['IV'][0]
                razdel_3 = LIFTING_NORM_SUCKER_POD[well_data.lifting_unit_combo][sucker_key]['раздел']
            work_list.append(
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', type_equipment,
                 f'Подъем штанг {sucker_key}мм (L={sucker_lenght}м )',
                 None, None,
                 None, None, None, None, None, max_count, None, None, None, None,
                 razdel_3, None, 'шт', sucker_count,
                 koef_norm, 1, '=V147*W147*X147', '=Y147-AA147-AB147-AC147-AD147', None, None, None, None, None])

        work_list.append(
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', 'ШТАНГИ',
             'Очистка штанг от окалини солей (АСПО)(акт ревизии)',
             None,
             None, None, None, None, None, None, None, None, None, None, None, '§9разд.1', None, 'час',
             sucker_count_all,
             0.017, 1, '=V149*W149*X149', '=Y149-AA149-AB149-AC149-AD149', None, None, None, None, None])

        return work_list

    def lifting_nkt(self, dict_nkt, type_equipment):

        middle_nkt = ''
        for nkt_key, nkt_value in dict_nkt.items():
            middle_nkt_value = nkt_value[0] / nkt_value[1]
            nkt_lenght = nkt_value[0]
            nkt_count = nkt_value[1]
            if 6.5 <= middle_nkt_value <= 7.5:
                middle_nkt = '6.5-7.5'
            elif 7.6 <= middle_nkt_value <= 8.5:
                middle_nkt = '7.6-8.5'
            elif 8.6 <= middle_nkt_value <= 9.5:
                middle_nkt = '8.6-9.5'
            elif 9.6 <= middle_nkt_value <= 10.5:
                middle_nkt = '9.6-10.5'
            elif 10.6 <= middle_nkt_value <= 11.5:
                middle_nkt = '10.6-11.5'
            elif 11.6 <= middle_nkt_value <= 12.5:
                middle_nkt = '11.6-12.5'

            max_count_3 = LIFTING_NORM_NKT[well_data.lifting_unit_combo][nkt_key]['III'][middle_nkt][1]
            koef_norm_3 = LIFTING_NORM_NKT[well_data.lifting_unit_combo][nkt_key]['III'][middle_nkt][0]
            razdel_3 = LIFTING_NORM_NKT[well_data.lifting_unit_combo][nkt_key]['III']['раздел']

            if max_count_3 >= nkt_lenght:
                max_count_3 = nkt_lenght

            lenght_nkt_3 = int(middle_nkt_value * max_count_3)

            work_list = [
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', type_equipment,
                 'ПЗР СПО перед подъемом труб из скважины',
                 None, None, None,
                 None, None, None, None, None, None, None, None, None, '§207разд.1', None, 'шт', 1, 0.07, 1,
                 '=V199*W199*X199', '=Y199-AA199-AB199-AC199-AD199', None, None, None, None, None]]

            podien_3_list = ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', type_equipment,
                             'Подъем НКТ  3 скорость',
                             None, None, None, None, nkt_key, lenght_nkt_3, middle_nkt, max_count_3,
                             None, None, None, None, razdel_3, None, 'шт', max_count_3, koef_norm_3,
                             1, '=V202*W202*X202', '=Y202-AA202-AB202-AC202-AD202', None, None, None, None, None]

            work_list.append(podien_3_list)

            nkt_count -= max_count_3

            if nkt_count > 0:
                max_count_2 = LIFTING_NORM_NKT[well_data.lifting_unit_combo][nkt_key]['II'][middle_nkt][1]
                koef_norm_2 = LIFTING_NORM_NKT[well_data.lifting_unit_combo][nkt_key]['II'][middle_nkt][0]
                razdel_2 = LIFTING_NORM_NKT[well_data.lifting_unit_combo][nkt_key]['II']['раздел']
                if max_count_2 >= nkt_count:
                    max_count_2 = nkt_count
                lenght_nkt_2 = int(middle_nkt_value * max_count_2)
                podiem_list_2 = ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', type_equipment,
                                 'Подъем НКТ  2 скорость',
                                 None, None, None, None, nkt_key, lenght_nkt_2, middle_nkt, max_count_2,
                                 None, None, None, None, razdel_2, None, 'шт', max_count_2, koef_norm_2,
                                 1, '=V202*W202*X202', '=Y202-AA202-AB202-AC202-AD202', None, None, None, None, None]
                nkt_count -= max_count_2
                work_list.insert(1, podiem_list_2)

            if nkt_count > 0:
                max_count_1 = LIFTING_NORM_NKT[well_data.lifting_unit_combo][nkt_key]['I'][middle_nkt][1]
                koef_norm_1 = LIFTING_NORM_NKT[well_data.lifting_unit_combo][nkt_key]['I'][middle_nkt][0]
                razdel_1 = LIFTING_NORM_NKT[well_data.lifting_unit_combo][nkt_key]['I']['раздел']

                if max_count_1 >= nkt_count:
                    max_count_1 = nkt_count

                lenght_nkt_1 = int(middle_nkt_value * max_count_1)
                podiem_list_1 = [
                    '=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', type_equipment, 'Подъем НКТ  1 скорость',
                    None, None, None, None, nkt_key, lenght_nkt_1, middle_nkt, max_count_1,
                    None, None, None, None, razdel_1, None, 'шт', max_count_1, koef_norm_1,
                    1, '=V202*W202*X202', '=Y202-AA202-AB202-AC202-AD202', None, None, None, None, None]
                nkt_count -= max_count_1
                work_list.insert(1, podiem_list_1)

            work_list.extend([
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', type_equipment, 'Долив скважины', None, None,
                 None, None,
                 None, None, None,
                 None, None, None, None, None, '§168разд.1', None, 'шт', '=V205/10', 0.003, 1, '=V204*W204*X204',
                 '=Y204-AA204-AB204-AC204-AD204', None, None, None, None, None],
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', type_equipment,
                 'Навернуть/отвернуть предохранительное кольцо', None, None,
                 None, None, None, None, None, None, None, None, None, None, '§300разд.1', None, 'шт',
                 '=SUM(V200:V202)',
                 0.003, 1, '=V205*W205*X205', '=Y205-AA205-AB205-AC205-AD205', None, None, None, None, None],
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', type_equipment, 'Осложнение при подъеме НКТ',
                 None, None,
                 None, None, None,
                 None, 'Объем', 0, None, None, None, None, 'факт', None, 'час', 0, 1, 1, '=V206*W206*X206',
                 '=Y206-AA206-AB206-AC206-AD206', None, None, None, None, None],
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', type_equipment, 'Замер НКТ ', None, None, None,
                 None, None,
                 None, None, None,
                 None, None, None, None, '§47разд.1', None, 'шт', '=V205', 0.008, 1, '=V207*W207*X207',
                 '=Y207-AA207-AB207-AC207-AD207', None, None, None, None, None],
                ['=ROW()-ROW($A$46)', 'подъем 73мм', None, 'спо', type_equipment, 'Откатывание труб с 201 трубы ',
                 None, None, None,
                 None, None, None, None, None, None, None, None, None, '§40разд.1', None, 'шт', '=V205-201', 0.008, 1,
                 '=V208*W208*X208', '=Y208-AA208-AB208-AC208-AD208', None, None, None, None, None],
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'Очистка от замазученности',
                 None, None, None,
                 None,
                 None, None, None, None, 'АКТ№', None, None, None, 'факт', None, 'шт', 1, 0.67, 1, '=V209*W209*X209',
                 '=Y209-AA209-AB209-AC209-AD209', None, None, None, None, None],
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'Ревизия ГНО ', None, None, None,
                 None, None,
                 None,
                 None, None, 'АКТ№', None, None, None, 'факт', None, 'час', 0.5, 1, 1, '=V210*W210*X210',
                 '=Y210-AA210-AB210-AC210-AD210', None, None, None, None, None]])

        return work_list

    def lifting_paker_def(self):
        complications_of_failure_list = []
        complications_during_disassembly_list = []
        work_list = []

        if self.complications_of_failure_combo == 'Да':
            complications_of_failure_list = [
                '=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
                f'{self.complications_of_failure_text_line} {self.complications_of_failure_time_begin_date}-'
             f'{self.complications_of_failure_time_end_date}', None, None, None, None, None,
                None, None, None, 'АКТ№', None, None, None, 'факт', None, 'час',
                {self.complications_of_failure_text_line}, 1, 1, '=V280*W280*X280',
                '=Y280-AA280-AB280-AC280-AD280', None, None, None, None, None]
            work_list.append(complications_of_failure_list)

        work_list.extend([
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'Демонтаж ПШ', None, None, None,
             None, None, None, None, None, None, None, None, None, '§121разд.1', None, 'шт', 1, 0.3, 1,
             '=V281*W281*X281', '=Y281-AA281-AB281-AC281-AD281', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
             'Срыв пакера в эксплуатационной колонне', None, None, None, None, None, None, None, None,
             None, None, None, None, '§146разд.1', None, 'шт', 1, 0.15, 1, '=V282*W282*X282',
             '=Y282-AA282-AB282-AC282-AD282', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
             'Демонтаж планшайбы с устья скважины', None, None, None, None, None, None, None, None, None,
             None, None, None, '§107разд.1', None, 'шт', 1, 0.32, 1, '=V283*W283*X283',
             '=Y283-AA283-AB283-AC283-AD283', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'Демонтаж АУ фонтанной арматуры',
             None, None, None, None, None, None, None, None, None, None, None, None, '§102разд.1', None,
             'раз', 1, 0.75, 1, '=V284*W284*X284', '=Y284-AA284-AB284-AC284-AD284', None, None, None,
             None, None]])

        if self.complications_during_disassembly_combo == "Да":
            complications_during_disassembly_list = ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции',
                                                     None,
                                                     f'{self.complications_during_disassembly_text_line}', None,
                                                     None, None, None, None, None,
                                                     None, None, 'АКТ№', None, None, None, 'факт', None, 'час',
                                                     self.complications_during_disassembly_time_line, 1, 1,
                                                     '=V286*W286*X286', '=Y286-AA286-AB286-AC286-AD286', None, None,
                                                     None, None, None],
            work_list.append(complications_during_disassembly_list)

        relocation_list = [
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'Демонтаж крестовины', None,
             None, None, None, None, None, None, None, None, None, None, None, '§300разд.1', None, 'шт',
             1, 0.45, 1, '=V285*W285*X285', '=Y285-AA285-AB285-AC285-AD285', None, None, None, None,
             None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'Монтаж превентора ПМТ ', None,
             None, None, None, None, None, None, None, None, None, None, None, '§109разд.1', None, 'шт',
             1, 0.67, 1, '=V287*W287*X287', '=Y287-AA287-AB287-AC287-AD287', None, None, None, None,
             None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
             'Поднести тяги,штурвалы,присоеденить их к превентору,установить стойки под тяги и защитные щиты',
             None, None, None, None, None, None, None, None, None, None, None, None,
             '§110расд.1', None, 'шт', 1, 0.23, 1, '=V288*W288*X288',
             '=Y288-AA288-AB288-AC288-AD288', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'Монтаж выкидной линии', None, None,
             None, None, None, None, None, None, None, None, None, None, '§301разд.1', None, 'раз', 1,
             0.3, 1, '=V289*W289*X289', '=Y289-AA289-AB289-AC289-AD289', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', 'ПРС', self.date_work_line, 'Тех.операции', None, 'Опрессовка превентора Р=80атм (+)',
             None, None, None, None, None, None, None, None, 'АКТ№', None, None, None, '§115разд.1',
             None, 'шт', 1, 0.92, 1, 0, '=Y290-AA290-AB290-AC290-AD290', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'Устройство  рабочей площадки', None,
             None, None, None, None, None, None, None, None, None, None, None, '§54разд.1', None, 'шт',
             1, 0.83, 1, '=V291*W291*X291', '=Y291-AA291-AB291-AC291-AD291', None, None, None, None,
             None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'ПР.перед.ремонтом', None, 'Монтаж ГКШ-1200', None, None,
             None, None, None, None, None, None, None, None, None, None, '§184разд.1', None, 'шт', 1,
             0.33, 1, '=V292*W292*X292', '=Y292-AA292-AB292-AC292-AD292', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'ПР.перед.ремонтом', None, 'Монтаж СПГ', None, None, None,
             None, None, None, None, None, None, None, None, None, '§185разд.1', None, 'шт', 1, 0.07, 1,
             '=V293*W293*X293', '=Y293-AA293-AB293-AC293-AD293', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', 'Пакер', 'ПЗР СПО пакера', None, None, None, None,
             None, None, None, None, None, None, None, None, '§136разд.1', None, 'шт', 1, 0.48, 1, 0,
             '=Y294-AA294-AB294-AC294-AD294', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
             'Срыв пакера в эксплуатационной колонне', None, None, None, None, None, None, None, None,
             None, None, None, None, '§146разд.1', None, 'шт', 1, 0.15, 1, 0,
             '=Y299-AA299-AB299-AC299-AD299', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', 'Пакер',
             'Навернуть/отвернуть предохранительное кольцо', None, None, None, None, None, None, None,
             None, None, None, None, None, '§300разд.1', None, 'шт', '=SUM(V300:V301)', 0.003, 1, 0,
             '=Y302-AA302-AB302-AC302-AD302', None, None, None, None, None]]

        if self.gno_combo == 'пакер':
            work_list = self.lifting_nkt(self.dict_nkt, 'Фондовый пакер')
        relocation_list.extend(work_list)
        return relocation_list


if __name__ == "__main__":
    # app3 = QApplication(sys.argv)

    app = QApplication(sys.argv)
    window = LiftingWindow(22, 22)
    window.show()
    sys.exit(app.exec_())
