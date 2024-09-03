import sys
from datetime import datetime, timedelta

import well_data

from normir.norms import LIFTING_NORM_SUCKER_POD, DESCENT_NORM_SUCKER_POD
from PyQt5.QtGui import QIntValidator, QDoubleValidator
from PyQt5.QtWidgets import QWidget, QLabel, QComboBox, QLineEdit, QGridLayout, QTabWidget, QMainWindow, QPushButton, \
    QMessageBox, QApplication, QHeaderView, QTableWidget, QTableWidgetItem, QTextEdit, QDateTimeEdit


class TabPage_SO_Lifting_Shgn(QWidget):
    def __init__(self, parent=None):
        super().__init__()

        self.validator_int = QIntValidator(0, 600)
        self.validator_float = QDoubleValidator(0.02, 1000, 1)

        self.date_work_label = QLabel('Дата работы')
        self.date_work_line = QLineEdit(self)
        self.date_work_line.setText(f'{well_data.date_work}')
        self.date_work_str = datetime.strptime(self.date_work_line.text(), '%d.%m.%Y')

        self.grid = QGridLayout(self)

        if well_data.date_work != '':
            self.date_work_line.setText(well_data.date_work)

        self.grid.addWidget(self.date_work_label, 4, 2)
        self.grid.addWidget(self.date_work_line, 5, 2)

        self.complications_of_failure_label = QLabel('Рассхаживание')
        self.complications_of_failure_combo = QComboBox(self)
        self.complications_of_failure_combo.addItems(['Нет', 'Да'])

        self.complications_when_lifting_label = QLabel('Осложнения при подьеме штанг')
        self.complications_when_lifting_combo = QComboBox(self)
        self.complications_when_lifting_combo.addItems(['Нет', 'Да'])

        self.grid.addWidget(self.complications_of_failure_label, 8, 1)
        self.grid.addWidget(self.complications_of_failure_combo, 9, 1)

        self.grid.addWidget(self.complications_when_lifting_label, 49, 1)
        self.grid.addWidget(self.complications_when_lifting_combo, 50, 1)

        self.fishing_works_label = QLabel('Ловильные работы')
        self.fishing_works_line = QLineEdit(self)

        self.sucker_pod_19_lenght_label = QLabel('Длина штанг на спуск 19мм')
        self.sucker_pod_22_lenght_label = QLabel('Длина штанг на спуск 22мм')
        self.sucker_pod_25_lenght_label = QLabel('Длина штанг на спуск 25мм')

        self.sucker_pod_19_lenght_edit = QLineEdit(self)
        self.sucker_pod_19_lenght_edit.setValidator(self.validator_float)
        self.sucker_pod_19_lenght_edit.setText('8')

        self.sucker_pod_19_count_label = QLabel('Кол-во штанг 19мм')
        self.sucker_pod_19_count_edit = QLineEdit(self)
        self.sucker_pod_19_count_edit.setValidator(self.validator_float)

        self.sucker_pod_22_lenght_edit = QLineEdit(self)
        self.sucker_pod_22_lenght_edit.setText('8')
        self.sucker_pod_22_lenght_edit.setValidator(self.validator_float)

        self.sucker_pod_22_count_label = QLabel('Кол-во штанг 22мм')
        self.sucker_pod_22_count_edit = QLineEdit(self)
        self.sucker_pod_22_count_edit.setValidator(self.validator_float)

        self.sucker_pod_25_lenght_edit = QLineEdit(self)
        self.sucker_pod_25_lenght_edit.setText('8')
        self.sucker_pod_25_lenght_edit.setValidator(self.validator_float)

        self.sucker_pod_25_count_label = QLabel('Кол-во штанг 25мм')
        self.sucker_pod_25_count_edit = QLineEdit(self)
        self.sucker_pod_25_count_edit.setValidator(self.validator_float)

        self.count_rods_is_same_label = QLabel('Кол-во штанг на подьем совпадает')
        self.count_rods_is_same_combo = QComboBox(self)
        self.count_rods_is_same_combo.addItems(['Да', 'Нет'])

        self.grid.addWidget(self.sucker_pod_19_lenght_label, 34, 1)
        self.grid.addWidget(self.sucker_pod_19_lenght_edit, 35, 1)

        self.grid.addWidget(self.sucker_pod_22_lenght_label, 34, 2)
        self.grid.addWidget(self.sucker_pod_22_lenght_edit, 35, 2)

        self.grid.addWidget(self.sucker_pod_25_lenght_label, 34, 3)
        self.grid.addWidget(self.sucker_pod_25_lenght_edit, 35, 3)

        self.grid.addWidget(self.sucker_pod_19_count_label, 36, 1)
        self.grid.addWidget(self.sucker_pod_19_count_edit, 37, 1)

        self.grid.addWidget(self.sucker_pod_22_count_label, 36, 2)
        self.grid.addWidget(self.sucker_pod_22_count_edit, 37, 2)

        self.grid.addWidget(self.sucker_pod_25_count_label, 36, 3)
        self.grid.addWidget(self.sucker_pod_25_count_edit, 37, 3)

        self.grid.addWidget(self.fishing_works_label, 38, 1, 1, 3)
        self.grid.addWidget(self.fishing_works_line, 39, 1, 1, 3)

        self.grid.addWidget(self.count_rods_is_same_label, 40, 1)
        self.grid.addWidget(self.count_rods_is_same_combo, 41, 1)

        self.complications_of_failure_combo.currentTextChanged.connect(self.update_complications_of_failure)
        self.complications_when_lifting_combo.currentTextChanged.connect(self.update_complications_when_lifting)

        self.count_rods_is_same_combo.currentTextChanged.connect(self.update_count_rods_is_same_combo)

    def update_count_rods_is_same_combo(self, index):
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

            self.complications_when_lifting_time_label = QLabel('затраченное время')
            self.complications_when_lifting_time_line = QLineEdit(self)

            self.complications_when_lifting_time_line.setValidator(self.validator_float)

            self.grid.addWidget(self.complications_when_lifting_text_label, 49, 2)
            self.grid.addWidget(self.complications_when_lifting_text_line, 50, 2)

            self.grid.addWidget(self.complications_when_lifting_time_begin_label, 49, 3)
            self.grid.addWidget(self.complications_when_lifting_time_begin_date, 50, 3)

            self.grid.addWidget(self.complications_when_lifting_time_end_label, 49, 4)
            self.grid.addWidget(self.complications_when_lifting_time_end_date, 50, 4)

            self.grid.addWidget(self.complications_when_lifting_time_label, 49, 5)
            self.grid.addWidget(self.complications_when_lifting_time_line, 50, 5)

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

            self.complications_during_disassembly_q_time_end_date.dateTimeChanged.connect(
                self.update_date_during_disassembly_q)
            self.complications_during_disassembly_q_time_begin_date.dateTimeChanged.connect(
                self.update_date_during_disassembly_q)


class TabWidget(QTabWidget):
    def __init__(self):
        super().__init__()
        self.addTab(TabPage_SO_Lifting_Shgn(self), 'СПО штанголовки')


class LiftingRodHeadWindow(QMainWindow):
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
        self.dict_sucker_pod_up = {}
        self.dict_nkt = {}
        self.need_saturation_well_text_line = None
        self.need_saturation_q_text_line = None
        self.cycle_count_combo = None
        self.volume_jamming_line = None
        self.complications_during_disassembly_text_line = None
        self.complications_during_disassembly_time_line = None
        self.complications_when_lifting_text_line = None
        self.complications_when_lifting_time_line = None
        self.fishing_works_line = None
        self.fluid_well_line = None
        self.time_work_line = None
        self.source_of_work_line = None
        self.couse_of_work_combo = None
        self.pressuar_gno_text_line = None
        self.complications_of_failure_time_line = None
        self.complications_of_failure_time_begin_date = None
        self.complications_of_failure_time_end_date = None

        self.sucker_pod_19_lenght_edit = None
        self.sucker_pod_19_count_edit = None

        self.sucker_pod_22_lenght_edit = None
        self.sucker_pod_22_count_edit = None

        self.sucker_pod_25_lenght_edit = None
        self.sucker_pod_25_count_edit = None

        self.sucker_pod_19_lenght_up_edit = None
        self.sucker_pod_19_count_up_edit = None

        self.sucker_pod_22_lenght_up_edit = None
        self.sucker_pod_22_count_up_edit = None

        self.sucker_pod_25_lenght_up_edit = None
        self.sucker_pod_25_count_up_edit = None

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

        self.fishing_works_line = current_widget.fishing_works_line.text()
        if self.fishing_works_line == '':
            QMessageBox.warning(self, 'Ошибка', f'Не введены текст ловильных работ')
            return

        self.count_rods_is_same_combo = current_widget.count_rods_is_same_combo.currentText()

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

        if self.count_rods_is_same_combo == 'Нет':
            try:
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

            except Exception as e:
                QMessageBox.warning(self, 'Ошибка', f'ВВедены не все значения {e}')
                return
        else:
            self.dict_sucker_pod_up = self.dict_sucker_pod

        self.complications_of_failure_combo = current_widget.complications_of_failure_combo.currentText()

        self.complications_when_lifting_combo = current_widget.complications_when_lifting_combo.currentText()

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

            if self.complications_of_failure_text_line in ['', None]:
                QMessageBox.warning(self, 'Ошибка', f'Не введены текст осложнения при срыве ПШ')
                return

            self.complications_of_failure_time_line = current_widget.complications_of_failure_time_line.text()

            if self.complications_of_failure_time_line in ['', None]:
                QMessageBox.warning(self, 'Ошибка', f'Не введены время осложнения при срыве ПШ')
            else:
                self.complications_of_failure_time_line = round(float(self.complications_of_failure_time_line), 1)

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

                self.complications_when_lifting_time_line = current_widget.complications_when_lifting_time_line.text()

                if self.complications_when_lifting_time_end_date == self.complications_when_lifting_time_begin_date:
                    QMessageBox.warning(self, 'Даты совпадают', 'Даты совпадают')
                    return

                if self.complications_when_lifting_time_line in ['', None]:
                    QMessageBox.warning(self, 'Ошибка', f'Не введены время осложнения при подьеме штанг')
                    return
                else:
                    self.complications_when_lifting_time_line = round(float(self.complications_when_lifting_time_line),
                                                                      1)
                if self.complications_when_lifting_time_line <= 0:
                    QMessageBox.warning(self, 'Ошибка',
                                        f'Затраченное время при подьеме штанг не может быть отрицательным')
                    return

            except Exception as e:
                QMessageBox.warning(self, 'Ошибка', f'ВВедены не все значения {e}')
                return

        work_list = self.lifting_shgn()
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

    def lifting_shgn(self):
        type_equipment = 'Ловильный инструмент'
        work_list = [
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', type_equipment, 'ПЗР СПО при спуске штанг',
             None, None,
             None, None, None, None, None, None, None, None, None, None, '§196,199разд.1', None, 'шт', 1, 0.74, 1,
             '=V157*W157*X157', '=Y157-AA157-AB157-AC157-AD157', None, None, None, None, None]]
        work_list.extend(self.descent_sucker_pod(self.dict_sucker_pod, type_equipment))

        work_list.append(
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, f'{self.fishing_works_line}', None,
             None,
             None, None,
             None, None, None, None, None, None, None, None, '§254разд.1', None, 'шт', 1, 0.33, 1, '=V161*W161*X161',
             '=Y161-AA161-AB161-AC161-AD161', None, None, None, None, None])
        if self.complications_of_failure_combo == 'Да':
            work_list.extend([['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
                               f'{self.complications_of_failure_text_line} '
                               f'{self.complications_of_failure_time_begin_date}-{self.complications_of_failure_time_end_date}',
                               None, None, None, None, None, None, None, None,
                               'АКТ№', None, None, None, 'факт', None, 'час', 1, 1, 1, '=V162*W162*X162',
                               '=Y162-AA162-AB162-AC162-AD162',
                               None, None, None, None, None],
                              ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
                               f'Срыв {well_data.dict_sucker_rod}', None, None, None, None, None, None,
                               None, None, "'АКТ №1'!A1", None, None, None, '§301разд.1', None, 'шт', 1, 0.15, 1,
                               '=V163*W163*X163',
                               '=Y163-AA163-AB163-AC163-AD163', None, None, None, None, None]])
        # нормирование штанг
        work_list.extend(self.lifting_sucker_pod(self.dict_sucker_pod_up, type_equipment))
        work_list.append(
            ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None, 'Демонтаж ПШМ', None, None, None, None, None, None,
             None, None, None, None, None, None, '§120разд.1', None, 'шт', 1, 0.25, 1, '=V167*W167*X167',
             '=Y167-AA167-AB167-AC167-AD167', None, None, None, None, None])
        return work_list

    def descent_sucker_pod(self, dict_sucker_pod, type_equipment):
        work_list = [
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', type_equipment, 'ПЗР СПО перед подъемом штанг',
             None, None, None, None, None,
             None, None, None, None, None, None, None, '§191разд.1', None, 'шт', 1, 0.74, 1, '=V145*W145*X145',
             '=Y145-AA145-AB145-AC145-AD145', None, None, None, None, None]]
        sucker_count_all = sum(map(lambda x: x[1], dict_sucker_pod.values()))
        for sucker_key, sucker in dict_sucker_pod.items():
            sucker_lenght = sucker[0]
            sucker_count = sucker[1]

            koef_norm = DESCENT_NORM_SUCKER_POD[well_data.lifting_unit_combo][sucker_key]
            razdel_3 = DESCENT_NORM_SUCKER_POD[well_data.lifting_unit_combo]['раздел']
            work_list.append(
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', type_equipment,
                 f'Спуск штанг {sucker_key}мм (L={sucker_lenght}м )',
                 None, None,
                 None, None, None, None, None, None, None, None, None, None, razdel_3, None,
                 'шт', sucker_count, koef_norm, 1,
                 '=V158*W158*X158', '=Y158-AA158-AB158-AC158-AD158', None, None, None, None, None])

        return work_list

    def lifting_sucker_pod(self, dict_sucker_pod, type_equipment):
        if type_equipment != 'ШТАНГИ':
            work_list = [
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', type_equipment, 'ПЗР СПО перед подъемом штанг',
                 None, None, None, None, None,
                 None, None, None, None, None, None, None, '§191разд.1', None, 'шт', 1, 0.74, 1, '=V145*W145*X145',
                 '=Y145-AA145-AB145-AC145-AD145', None, None, None, None, None]]
        else:
            work_list = []
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


if __name__ == "__main__":
    # app3 = QApplication(sys.argv)

    app = QApplication(sys.argv)
    window = LiftingRodHeadWindow(22, 22)
    window.show()
    sys.exit(app.exec_())
