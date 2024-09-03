import sys
from datetime import datetime, timedelta

import well_data

from normir.norms import LIFTING_NORM_SUCKER_POD
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
        self.addTab(TabPage_SO_Lifting_Shgn(self), 'Подьем ШГН')


class LiftingShgnWindow(QMainWindow):
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

        self.date_work_line = current_widget.date_work_line.text()

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
            asssd = self.complications_of_failure_time_line

            if self.complications_of_failure_time_line == '':
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

                if self.complications_when_lifting_time_end_date == self.complications_when_lifting_time_begin_date:
                    QMessageBox.warning(self, 'Даты совпадают', 'Даты совпадают')
                    return

                if self.complications_when_lifting_text_line == '':
                    QMessageBox.warning(self, 'Ошибка', f'Не введены текст осложнения при подьеме штанг')
                    return
                if self.complications_when_lifting_time_line == '':
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

            self.complications_during_disassembly_time_line = \
                current_widget.complications_during_disassembly_time_line.text()
            if self.complications_during_disassembly_time_line != '':
                self.complications_during_disassembly_time_line = round(
                    float(self.complications_during_disassembly_time_line), 1)
            else:
                QMessageBox.warning(self, 'Ошибка', f'Не введены время осложнения при демонтаже ПШ')

            if self.complications_during_disassembly_time_line <= 0:
                QMessageBox.warning(self, 'Ошибка', f'Затраченное время при демонтаже ПШ не может быть отрицательным')
                return

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
        from normir.rod_head_work import LiftingRodHeadWindow

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
             'АКТ№', None, None, None, 'факт', None, 'час', self.complications_of_failure_time_line - 0.15, 1, 1,
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
                                 'АКТ№', None, None, None, 'факт', None, 'час',
                                 self.complications_during_disassembly_time_line, 1, 1,
                                 '=V138*W138*X138', '=Y138-AA138-AB138-AC138-AD138',
                                 None, None, None, None, None])
            self.date_work_line = self.complications_during_disassembly_q_time_end_date.split(' ')[1]
        # нормирование штанг
        work_list.extend(LiftingRodHeadWindow.lifting_sucker_pod(self, self.dict_sucker_pod, 'ШТАНГИ'))

        if self.complications_when_lifting_combo == 'Да':
            work_list.append(
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', 'ШТАНГИ',
                 f'{self.complications_when_lifting_text_line} {self.complications_when_lifting_time_begin_date}- {self.complications_when_lifting_time_end_date}',
                 None,
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




if __name__ == "__main__":
    # app3 = QApplication(sys.argv)

    app = QApplication(sys.argv)
    window = LiftingShgnWindow(22, 22)
    window.show()
    sys.exit(app.exec_())


def lifting_shgn(self):
    work_list = [
        ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None, 'ПЗР.Опрессовка ГНО на Р=40атм (+)', None, None, None,
         None, None, None, None, None, "'АКТ №1'!A1", None, None, None, '§150-152разд.1', None, 'шт', 1, 0.67, 1,
         '=V133*W133*X133', '=Y133-AA133-AB133-AC133-AD133', None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None, 'демонтаж АУШГН', None,
         None, None, None, None, None, None, None, None, None, None, None, '§54разд.1', None, 'шт', 1, 0.67, 1,
         '=V134*W134*X134', '=Y134-AA134-AB134-AC134-AD134', None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None,
         'Определение веса к/штанг. Пробный вызов подачи с ПА(-). ', None, None, None, None, None, None, None, None,
         'АКТ№', None, None, None, '§200разд.1', None, 'шт', 1, 0.57, 1, '=V135*W135*X135',
         '=ROUNDUP(Y135-AA135-AB135-AC135-AD135,2)', None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None, 'Срыв НВ-32', None, None, None, None, None, None, None,
         None, "'АКТ №1'!A1", None, None, None, '§301разд.1', None, 'шт', 1, 0.15, 1, '=V136*W136*X136',
         '=Y136-AA136-AB136-AC136-AD136', None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None, 'Искусственный наворот (-)', None, None, None, None,
         None, None, None, None, "'АКТ №1'!A1", None, None, None, 'факт', None, 'шт', 1, 0.15, 1, '=V137*W137*X137',
         '=Y137-AA137-AB137-AC137-AD137', None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None,
         'Расхаживание с пост.увеличением веса до 10т (-)  (ВРЕМЯ)', None, None, None, None, None, None, None, None,
         'АКТ№', None, None, None, 'факт', None, 'час', 1, 1, 1, '=V138*W138*X138', '=Y138-AA138-AB138-AC138-AD138',
         None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'ПР.перед.ремонтом', None, 'Монтаж ГКШ-1200', None, None, None, None, None,
         None, None, None, None, None, None, None, '§184разд.1', None, 'шт', 1, 0.33, 1, '=V139*W139*X139',
         '=Y139-AA139-AB139-AC139-AD139', None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'ПР.перед.ремонтом', None, 'Монтаж СПГ', None, None, None, None, None, None,
         None, None, None, None, None, None, '§185разд.1', None, 'шт', 1, 0.07, 1, '=V140*W140*X140',
         '=Y140-AA140-AB140-AC140-AD140', None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None, 'Устройство  рабочей площадки', None, None, None, None,
         None, None, None, None, None, None, None, None, '§54разд.1', None, 'шт', 1, 0.83, 1, '=V141*W141*X141',
         '=Y141-AA141-AB141-AC141-AD141', None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'ПР.перед.ремонтом', None, 'Монтаж ГКШ-300', None, None, None, None, None,
         None, None, None, "'АКТ №1'!A1", None, None, None, '§184разд.1', None, 'шт', 1, 0.33, 1, '=V142*W142*X142',
         '=Y142-AA142-AB142-AC142-AD142', None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None, 'Монтаж штангового превентора', None, None, None, None,
         None, None, None, None, None, None, None, None, '§120разд.1', None, 'шт', 1, 0.35, 1, '=V143*W143*X143',
         '=Y143-AA143-AB143-AC143-AD143', None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'ПР.перед.ремонтом', None, 'Опрессовка ПШМ', None, None, None, None, None,
         None, None, None, None, None, None, None, '§112,разд.1', None, 'шт', 1, 0.62, 1, '=V144*W144*X144',
         '=Y144-AA144-AB144-AC144-AD144', None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'спо', 'Штанги', 'ПЗР СПО перед подъемом штанг', None, None, None, None, None,
         None, None, None, None, None, None, None, '§191разд.1', None, 'шт', 1, 0.73, 1, '=V145*W145*X145',
         '=Y145-AA145-AB145-AC145-AD145', None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'спо', 'Штанги', 'Подъем штанг  19мм (L=8м )', None, None, None, None, None,
         None, None,
         '=IF($AD$8=ЦИКЛ!$A$210,ЦИКЛ!$E$210,IF($AD$8=ЦИКЛ!$A$211,ЦИКЛ!$E$210,IF($AD$8=ЦИКЛ!$A$212,ЦИКЛ!$E$210,IF($AD$8=ЦИКЛ!$G$210,ЦИКЛ!$E$210,IF($AD$8=ЦИКЛ!$H$210,ЦИКЛ!$E$210,IF($AD$8=ЦИКЛ!$A$217,ЦИКЛ!$E$217,IF($AD$8=ЦИКЛ!$A$224,ЦИКЛ!$E$224,IF($AD$8=ЦИКЛ!$I$210,ЦИКЛ!$M$210,IF($AD$8=ЦИКЛ!$I$217,ЦИКЛ!$M$217,IF($AD$8=ЦИКЛ!$I$224,ЦИКЛ!$M$224))))))))))',
         None, None, None, None,
         '=IF($AD$8=ЦИКЛ!$A$210,ЦИКЛ!$F$210,IF($AD$8=ЦИКЛ!$A$211,ЦИКЛ!$F$211,IF($AD$8=ЦИКЛ!$A$212,ЦИКЛ!$F$212,IF($AD$8=ЦИКЛ!$A$217,ЦИКЛ!$F$217,IF($AD$8=ЦИКЛ!$A$224,ЦИКЛ!$F$224,IF($AD$8=ЦИКЛ!$I$210,ЦИКЛ!$N$210,IF($AD$8=ЦИКЛ!$I$217,ЦИКЛ!$N$217,IF($AD$8=ЦИКЛ!$I$224,ЦИКЛ!$N$224,IF($AD$8=ЦИКЛ!$G$210,ЦИКЛ!$F$210,IF($AD$8=ЦИКЛ!$H$210,ЦИКЛ!$F$210))))))))))',
         None, 'шт', 49,
         '=IF($AD$8=ЦИКЛ!$A$210,ЦИКЛ!$D$210,IF($AD$8=ЦИКЛ!$A$211,ЦИКЛ!$D$210,IF($AD$8=ЦИКЛ!$A$212,ЦИКЛ!$D$210,IF($AD$8=ЦИКЛ!$G$210,ЦИКЛ!$D$210,IF($AD$8=ЦИКЛ!$H$210,ЦИКЛ!$D$210,IF($AD$8=ЦИКЛ!$A$217,ЦИКЛ!$D$217,IF($AD$8=ЦИКЛ!$A$224,ЦИКЛ!$D$224,IF($AD$8=ЦИКЛ!$I$210,ЦИКЛ!$L$210,IF($AD$8=ЦИКЛ!$I$217,ЦИКЛ!$L$217,IF($AD$8=ЦИКЛ!$I$224,ЦИКЛ!$L$224))))))))))',
         1, '=V146*W146*X146', '=Y146-AA146-AB146-AC146-AD146', None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'спо', 'Штанги', 'Подъем штанг  22мм  (L=8м )', None, None, None, None, None,
         None, None,
         '=IF($AD$8=ЦИКЛ!$A$210,ЦИКЛ!$E$211,IF($AD$8=ЦИКЛ!$A$211,ЦИКЛ!$E$211,IF($AD$8=ЦИКЛ!$A$212,ЦИКЛ!$E$211,IF($AD$8=ЦИКЛ!$G$210,ЦИКЛ!$E$211,IF($AD$8=ЦИКЛ!$H$210,ЦИКЛ!$E$211,IF($AD$8=ЦИКЛ!$A$217,ЦИКЛ!$E$218,IF($AD$8=ЦИКЛ!$A$224,ЦИКЛ!$E$225,IF($AD$8=ЦИКЛ!$I$210,ЦИКЛ!$M$211,IF($AD$8=ЦИКЛ!$I$217,ЦИКЛ!$M$218,IF($AD$8=ЦИКЛ!$I$224,ЦИКЛ!$M$225))))))))))',
         None, None, None, None,
         '=IF($AD$8=ЦИКЛ!$A$210,ЦИКЛ!$F$210,IF($AD$8=ЦИКЛ!$A$211,ЦИКЛ!$F$211,IF($AD$8=ЦИКЛ!$A$212,ЦИКЛ!$F$212,IF($AD$8=ЦИКЛ!$A$217,ЦИКЛ!$F$217,IF($AD$8=ЦИКЛ!$A$224,ЦИКЛ!$F$224,IF($AD$8=ЦИКЛ!$I$210,ЦИКЛ!$N$210,IF($AD$8=ЦИКЛ!$I$217,ЦИКЛ!$N$217,IF($AD$8=ЦИКЛ!$I$224,ЦИКЛ!$N$224,IF($AD$8=ЦИКЛ!$G$210,ЦИКЛ!$F$210,IF($AD$8=ЦИКЛ!$H$210,ЦИКЛ!$F$210))))))))))',
         None, 'шт', 90,
         '=IF($AD$8=ЦИКЛ!$A$210,ЦИКЛ!$D$211,IF($AD$8=ЦИКЛ!$A$211,ЦИКЛ!$D$211,IF($AD$8=ЦИКЛ!$A$212,ЦИКЛ!$D$211,IF($AD$8=ЦИКЛ!$G$210,ЦИКЛ!$D$211,IF($AD$8=ЦИКЛ!$H$210,ЦИКЛ!$D$211,IF($AD$8=ЦИКЛ!$A$217,ЦИКЛ!$D$218,IF($AD$8=ЦИКЛ!$A$224,ЦИКЛ!$D$225,IF($AD$8=ЦИКЛ!$I$210,ЦИКЛ!$L$211,IF($AD$8=ЦИКЛ!$I$217,ЦИКЛ!$L$218,IF($AD$8=ЦИКЛ!$I$224,ЦИКЛ!$L$226))))))))))',
         1, '=V147*W147*X147', '=Y147-AA147-AB147-AC147-AD147', None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'спо', 'Штанги', 'Подъем штанг  25мм  (L=8м )', None, None, None, None, None,
         None, None,
         '=IF($AD$8=ЦИКЛ!$A$210,ЦИКЛ!$E$212,IF($AD$8=ЦИКЛ!$A$211,ЦИКЛ!$E$212,IF($AD$8=ЦИКЛ!$A$212,ЦИКЛ!$E$212,IF($AD$8=ЦИКЛ!$G$210,ЦИКЛ!$E$212,IF($AD$8=ЦИКЛ!$H$210,ЦИКЛ!$E$212,IF($AD$8=ЦИКЛ!$A$217,ЦИКЛ!$E$219,IF($AD$8=ЦИКЛ!$A$224,ЦИКЛ!$E$226,IF($AD$8=ЦИКЛ!$I$210,ЦИКЛ!$M$212,IF($AD$8=ЦИКЛ!$I$217,ЦИКЛ!$M$219,IF($AD$8=ЦИКЛ!$I$224,ЦИКЛ!$M$226))))))))))',
         None, None, None, None,
         '=IF($AD$8=ЦИКЛ!$A$210,ЦИКЛ!$F$210,IF($AD$8=ЦИКЛ!$A$211,ЦИКЛ!$F$211,IF($AD$8=ЦИКЛ!$A$212,ЦИКЛ!$F$212,IF($AD$8=ЦИКЛ!$A$217,ЦИКЛ!$F$217,IF($AD$8=ЦИКЛ!$A$224,ЦИКЛ!$F$224,IF($AD$8=ЦИКЛ!$I$210,ЦИКЛ!$N$210,IF($AD$8=ЦИКЛ!$I$217,ЦИКЛ!$N$217,IF($AD$8=ЦИКЛ!$I$224,ЦИКЛ!$N$224,IF($AD$8=ЦИКЛ!$G$210,ЦИКЛ!$F$210,IF($AD$8=ЦИКЛ!$H$210,ЦИКЛ!$F$210))))))))))',
         None, 'шт', 100,
         '=IF($AD$8=ЦИКЛ!$A$210,ЦИКЛ!$D$211,IF($AD$8=ЦИКЛ!$A$211,ЦИКЛ!$D$211,IF($AD$8=ЦИКЛ!$A$212,ЦИКЛ!$D$211,IF($AD$8=ЦИКЛ!$G$210,ЦИКЛ!$D$211,IF($AD$8=ЦИКЛ!$H$210,ЦИКЛ!$D$211,IF($AD$8=ЦИКЛ!$A$217,ЦИКЛ!$D$218,IF($AD$8=ЦИКЛ!$A$224,ЦИКЛ!$D$225,IF($AD$8=ЦИКЛ!$I$210,ЦИКЛ!$L$211,IF($AD$8=ЦИКЛ!$I$217,ЦИКЛ!$L$218,IF($AD$8=ЦИКЛ!$I$224,ЦИКЛ!$L$226))))))))))',
         1, '=V148*W148*X148', '=Y148-AA148-AB148-AC148-AD148', None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'спо', 'Штанги', 'Очистка штанг от окалини солей (АСПО)(акт ревизии)', None,
         None, None, None, None, None, None, None, None, None, None, None, '§9разд.1', None, 'час', '=V146+V147+V148',
         0.017, 1, '=V149*W149*X149', '=Y149-AA149-AB149-AC149-AD149', None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'спо', 'Штанги', 'Осложнение при подъеме штанг (АСПО)', None, None, None,
         None, None, None, 'Объем', None, None, None, None, None, '§9разд.1', None, 'час', 10, 0.017, 1, 10,
         '=Y150-AA150-AB150-AC150-AD150', None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None, 'Демонтаж ГКШ-300 ', None, None, None, None, None, None,
         None, None, None, None, None, None, '§184разд.1', None, 'шт', 1, 0.12, 1, '=V151*W151*X151',
         '=Y151-AA151-AB151-AC151-AD151', None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None, 'Демонтаж ПШМ', None, None, None, None, None, None,
         None, None, None, None, None, None, '§120разд.1', None, 'шт', 1, 0.25, 1, '=V152*W152*X152',
         '=Y152-AA152-AB152-AC152-AD152', None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None, 'Разборка  рабочей площадки частично', None, None, None,
         None, None, None, None, None, None, None, None, None, '§55разд.1', None, 'шт', 1, 0.3, 1, '=V153*W153*X153',
         '=Y153-AA153-AB153-AC153-AD153', None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None, 'Ревизия ГНО ', None, None, None, None, None, None,
         None, None, 'АКТ№', None, None, None, 'факт', None, 'час', 0.5, 1, 1, '=V154*W154*X154',
         '=Y154-AA154-AB154-AC154-AD154', None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None, None, None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, None, None, 'ШТАНГОЛОВКА', None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'спо', 'Ловильный инструмент', 'ПЗР СПО при спуске штанг', None, None, None,
         None, None, None, None, None, None, None, None, None, '§196,199разд.1', None, 'шт', 1, 0.74, 1,
         '=V157*W157*X157', '=Y157-AA157-AB157-AC157-AD157', None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'спо', 'Ловильный инструмент', 'Спуск штанг  19мм (L=8м )', None, None, None,
         None, None, None, None, None, None, None, None, None, 'п.1.1 раздел 2', None, 'шт', 35, 0.012, 1,
         '=V158*W158*X158', '=Y158-AA158-AB158-AC158-AD158', None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'спо', 'Ловильный инструмент', 'Спуск штанг  22мм  (L=8м )', None, None, None,
         None, None, None, None, None, None, None, None, None, 'п.1.1 раздел 2', None, 'шт', 97, 0.013, 1,
         '=V159*W159*X159', '=Y159-AA159-AB159-AC159-AD159', None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'спо', 'Ловильный инструмент', 'Спуск штанг  25мм  (L=8м )', None, None, None,
         None, None, None, None, None, None, None, None, None, 'п.1.1 раздел 2', None, 'шт', 100, 0.013, 1,
         '=V160*W160*X160', '=Y160-AA160-AB160-AC160-AD160', None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None, 'Ловильные работы (+)', None, None, None, None, None,
         None, None, None, None, None, None, None, '§254разд.1', None, 'шт', 1, 0.33, 1, '=V161*W161*X161',
         '=Y161-AA161-AB161-AC161-AD161', None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None,
         'Расхаживание с пост.увеличением веса до 10т (-)  (ВРЕМЯ)', None, None, None, None, None, None, None, None,
         'АКТ№', None, None, None, 'факт', None, 'час', 1, 1, 1, '=V162*W162*X162', '=Y162-AA162-AB162-AC162-AD162',
         None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None, 'Срыв НВ-32', None, None, None, None, None, None, None,
         None, "'АКТ №1'!A1", None, None, None, '§301разд.1', None, 'шт', 1, 0.15, 1, '=V163*W163*X163',
         '=Y163-AA163-AB163-AC163-AD163', None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'спо', 'Ловильный инструмент', 'Подъем штанг  19мм (L=8м )', None, None, None,
         None, None, None, None, 429, None, None, None, None, 'п.1.1 раздел 2', None, 'шт', 49, 0.012, 1,
         '=V164*W164*X164', '=Y164-AA164-AB164-AC164-AD164', None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'спо', 'Ловильный инструмент', 'Подъем штанг  22мм  (L=8м )', None, None,
         None, None, None, None, None, 347, None, None, None, None, 'п.1.1 раздел 2', None, 'шт', 90, 0.013, 1,
         '=V165*W165*X165', '=Y165-AA165-AB165-AC165-AD165', None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'спо', 'Ловильный инструмент', 'Подъем штанг  25мм  (L=8м )', None, None,
         None, None, None, None, None, 307, None, None, None, None, 'п.1.1 раздел 2', None, 'шт', 100, 0.013, 1,
         '=V166*W166*X166', '=Y166-AA166-AB166-AC166-AD166', None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None, 'Демонтаж ПШМ', None, None, None, None, None, None,
         None, None, None, None, None, None, '§120разд.1', None, 'шт', 1, 0.25, 1, '=V167*W167*X167',
         '=Y167-AA167-AB167-AC167-AD167', None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None, None, None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, None, None, 'Начало работ при ШГН', None, None, None, None, None, None, None,
         None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None,
         'Разборка устьевого оборудования с тугим отворотом  (ВРЕМЯ)', None, None, None, None, None, None, None, None,
         'АКТ№', None, None, None, 'факт', None, 'час', 1, 1, 1, '=V171*W171*X171', '=Y171-AA171-AB171-AC171-AD171',
         None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None, 'Демонтаж фонтанной арматуры (ШГН)', None, None, None,
         None, None, None, None, None, None, None, None, None, '§100разд.1', None, 'шт', 1, 0.67, 1, '=V172*W172*X172',
         '=Y172-AA172-AB172-AC172-AD172', None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None, 'Демонтаж планшайбы с устья скважины(+срыв)', None,
         None, None, None, None, None, None, None, None, None, None, None, '§107разд.1', None, 'шт', 1, 0.32, 1,
         '=V173*W173*X173', '=Y173-AA173-AB173-AC173-AD173', None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None, 'Демонтаж крестовины', None, None, None, None, None,
         None, None, None, None, None, None, None, '§300разд.1', None, 'шт', 1, 0.45, 1, '=V174*W174*X174',
         '=Y174-AA174-AB174-AC174-AD174', None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None, 'Демонтаж ф.крестовины (тугой отворот)  (ВРЕМЯ)', None,
         None, None, None, None, None, None, None, 'АКТ№', None, None, None, 'факт', None, 'час', 1, 1, 1,
         '=V175*W175*X175', '=Y175-AA175-AB175-AC175-AD175', None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None, 'Установить заглушку на коллектор', None, None, None,
         None, None, None, None, None, None, None, None, None, '§28разд.1', None, 'шт', 1, 0.1, 1, '=V176*W176*X176',
         '=Y176-AA176-AB176-AC176-AD176', None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None, 'Монтаж превентора  ПМТ ', None, None, None, None, None,
         None, None, None, None, None, None, None, '§109разд.1', None, 'шт', 1, 0.67, 1, '=V177*W177*X177',
         '=Y177-AA177-AB177-AC177-AD177', None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None,
         'Поднести тяги,штурвалы,присоеденить их к превентору,установить стойки под тяги и защитные щиты.(ПВО 2 КАТ)',
         None, None, None, None, None, None, None, None, None, None, None, None, '§110расд.1', None, 'шт', 1, 0.23, 1,
         '=V178*W178*X178', '=Y178-AA178-AB178-AC178-AD178', None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None, 'Монтаж выкидной линии', None, None, None, None, None,
         None, None, None, None, None, None, None, '§301разд.1', None, 'раз', 1, 0.3, 1, '=V179*W179*X179',
         '=Y179-AA179-AB179-AC179-AD179', None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None, 'Демонтаж выкидной линии', None, None, None, None, None,
         None, None, None, None, None, None, None, '§300разд.1', None, 'раз', 1, 0.167, 1, '=V180*W180*X180',
         '=Y180-AA180-AB180-AC180-AD180', None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None, 'Опрессовка превентора Р=80атм (+)', None, None, None,
         None, None, None, None, None, 'АКТ№', None, None, None, '§115разд.1', None, 'шт', 1, 0.92, 1, 0,
         '=Y181-AA181-AB181-AC181-AD181', None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None, 'Устройство  рабочей площадки частично', None, None,
         None, None, None, None, None, None, None, None, None, None, '§55разд.1', None, 'шт', 1, 0.32, 1,
         '=V182*W182*X182', '=Y182-AA182-AB182-AC182-AD182', None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'ПР.перед.ремонтом', None, 'Монтаж ГКШ-1200', None, None, None, None, None,
         None, None, None, None, None, None, None, '§184разд.1', None, 'шт', 1, 0.33, 1, '=V183*W183*X183',
         '=Y183-AA183-AB183-AC183-AD183', None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'ПР.перед.ремонтом', None, 'Монтаж СПГ', None, None, None, None, None, None,
         None, None, None, None, None, None, '§185разд.1', None, 'шт', 1, 0.07, 1, '=V184*W184*X184',
         '=Y184-AA184-AB184-AC184-AD184', None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'спо', 'Пакер', 'ПЗР СПО пакера', None, None, None, None, None, None, None,
         None, None, None, None, None, '§136разд.1', None, 'шт', 1, 0.48, 1, 0, '=Y185-AA185-AB185-AC185-AD185', None,
         None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'спо', 'Пакер', 'Спуск НКТ компоновка ', None, None, None, None, None, '73мм',
         30,
         '=IF(AND(M186/V186>=ЦИКЛ!$V$9,M186/V186<=ЦИКЛ!$W$9),ЦИКЛ!$U$9,IF(AND(M186/V186>=ЦИКЛ!$V$10,M186/V186<=ЦИКЛ!$W$10),ЦИКЛ!$U$10,IF(AND(M186/V186>=ЦИКЛ!$V$11,M186/V186<=ЦИКЛ!$W$11),ЦИКЛ!$U$11,IF(AND(M186/V186>=ЦИКЛ!$V$12,M186/V186<=ЦИКЛ!$W$12),ЦИКЛ!$U$12,IF(AND(M186/V186>=ЦИКЛ!$V$13,M186/V186<=ЦИКЛ!$W$13),ЦИКЛ!$U$13,IF(AND(M186/V186>=ЦИКЛ!$V$14,M186/V186<=ЦИКЛ!$W$14),ЦИКЛ!$U$14))))))',
         None, None, None, None,
         '=IF($AD$8=ЦИКЛ!$A$4,ЦИКЛ!$P$4,IF($AD$8=ЦИКЛ!$A$7,ЦИКЛ!$P$7,IF($AD$8=ЦИКЛ!$A$10,ЦИКЛ!$P$7,IF($AD$8=ЦИКЛ!$A$52,ЦИКЛ!$P$52,IF($AD$8=ЦИКЛ!$A$70,ЦИКЛ!$P$70,IF($AD$8=ЦИКЛ!$A$88,ЦИКЛ!$P$88,IF($AD$8=ЦИКЛ!$A$106,ЦИКЛ!$P$106,IF($AD$8=ЦИКЛ!$A$133,ЦИКЛ!$P$133,IF($AD$8=ЦИКЛ!$Q$4,ЦИКЛ!$P$4,IF($AD$8=ЦИКЛ!$R$4,ЦИКЛ!$P$4))))))))))',
         None, 'шт', 3,
         '=IF(AND($AD$8=ЦИКЛ!$A$4,ЦИКЛ!$D$3=N186,ЦИКЛ!$B$37=АВР!L186),ЦИКЛ!$D$37,IF(AND($AD$8=ЦИКЛ!$A$4,ЦИКЛ!$E$3=N186,ЦИКЛ!$B$37=АВР!L186),ЦИКЛ!$E$37,IF(AND($AD$8=ЦИКЛ!$A$4,ЦИКЛ!$F$3=N186,ЦИКЛ!$B$37=АВР!L186),ЦИКЛ!$F$37,IF(AND($AD$8=ЦИКЛ!$A$4,ЦИКЛ!$G$3=N186,ЦИКЛ!$B$37=АВР!L186),ЦИКЛ!$G$37,IF(AND($AD$8=ЦИКЛ!$A$4,ЦИКЛ!$H$3=N186,ЦИКЛ!$B$37=АВР!L186),ЦИКЛ!$H$37,IF(AND($AD$8=ЦИКЛ!$A$4,ЦИКЛ!$I$3=N186,ЦИКЛ!$B$37=АВР!L186),ЦИКЛ!$I$37,IF(AND($AD$8=ЦИКЛ!$Q$4,ЦИКЛ!$D$3=N186,ЦИКЛ!$B$37=АВР!L186),ЦИКЛ!$D$37,IF(AND($AD$8=ЦИКЛ!$Q$4,ЦИКЛ!$E$3=N186,ЦИКЛ!$B$37=АВР!L186),ЦИКЛ!$E$37,IF(AND($AD$8=ЦИКЛ!$Q$4,ЦИКЛ!$F$3=N186,ЦИКЛ!$B$37=АВР!L186),ЦИКЛ!$F$37,IF(AND($AD$8=ЦИКЛ!$Q$4,ЦИКЛ!$G$3=N186,ЦИКЛ!$B$37=АВР!L186),ЦИКЛ!$G$37,IF(AND($AD$8=ЦИКЛ!$Q$4,ЦИКЛ!$H$3=N186,ЦИКЛ!$B$37=АВР!L186),ЦИКЛ!$H$37,IF(AND($AD$8=ЦИКЛ!$Q$4,ЦИКЛ!$I$3=N186,ЦИКЛ!$B$37=АВР!L186),ЦИКЛ!$I$37,IF(AND($AD$8=ЦИКЛ!$R$4,ЦИКЛ!$D$3=N186,ЦИКЛ!$B$37=АВР!L186),ЦИКЛ!$D$37,IF(AND($AD$8=ЦИКЛ!$R$4,ЦИКЛ!$E$3=N186,ЦИКЛ!$B$37=АВР!L186),ЦИКЛ!$E$37,IF(AND($AD$8=ЦИКЛ!$R$4,ЦИКЛ!$F$3=N186,ЦИКЛ!$B$37=АВР!L186),ЦИКЛ!$F$37,IF(AND($AD$8=ЦИКЛ!$R$4,ЦИКЛ!$G$3=N186,ЦИКЛ!$B$37=АВР!L186),ЦИКЛ!$G$37,IF(AND($AD$8=ЦИКЛ!$R$4,ЦИКЛ!$H$3=N186,ЦИКЛ!$B$37=АВР!L186),ЦИКЛ!$H$37,IF(AND($AD$8=ЦИКЛ!$R$4,ЦИКЛ!$I$3=N186,ЦИКЛ!$B$37=АВР!L186),ЦИКЛ!$I$37,IF(AND($AD$8=ЦИКЛ!$A$7,ЦИКЛ!$D$3=N186,ЦИКЛ!$B$37=АВР!L186),ЦИКЛ!$D$37,IF(AND($AD$8=ЦИКЛ!$A$7,ЦИКЛ!$E$3=N186,ЦИКЛ!$B$37=АВР!L186),ЦИКЛ!$E$37,IF(AND($AD$8=ЦИКЛ!$A$7,ЦИКЛ!$F$3=N186,ЦИКЛ!$B$37=АВР!L186),ЦИКЛ!$F$37,IF(AND($AD$8=ЦИКЛ!$A$7,ЦИКЛ!$G$3=N186,ЦИКЛ!$B$37=АВР!L186),ЦИКЛ!$G$37,IF(AND($AD$8=ЦИКЛ!$A$7,ЦИКЛ!$H$3=N186,ЦИКЛ!$B$37=АВР!L186),ЦИКЛ!$H$37,IF(AND($AD$8=ЦИКЛ!$A$7,ЦИКЛ!$I$3=N186,ЦИКЛ!$B$37=АВР!L186),ЦИКЛ!$I$37,IF(AND($AD$8=ЦИКЛ!$A$10,ЦИКЛ!$D$3=N186,ЦИКЛ!$B$37=АВР!L186),ЦИКЛ!$D$37,IF(AND($AD$8=ЦИКЛ!$A$10,ЦИКЛ!$E$3=N186,ЦИКЛ!$B$37=АВР!L186),ЦИКЛ!$E$37,IF(AND($AD$8=ЦИКЛ!$A$10,ЦИКЛ!$F$3=N186,ЦИКЛ!$B$37=АВР!L186),ЦИКЛ!$F$37,IF(AND($AD$8=ЦИКЛ!$A$10,ЦИКЛ!$G$3=N186,ЦИКЛ!$B$37=АВР!L186),ЦИКЛ!$G$37,IF(AND($AD$8=ЦИКЛ!$A$10,ЦИКЛ!$H$3=N186,ЦИКЛ!$B$37=АВР!L186),ЦИКЛ!$H$37,IF(AND($AD$8=ЦИКЛ!$A$10,ЦИКЛ!$I$3=N186,ЦИКЛ!$B$37=АВР!L186),ЦИКЛ!$I$37,IF(AND($AD$8=ЦИКЛ!$A$52,ЦИКЛ!$D$3=N186,ЦИКЛ!$B$37=АВР!L186),ЦИКЛ!$D$63,IF(AND($AD$8=ЦИКЛ!$A$52,ЦИКЛ!$E$3=N186,ЦИКЛ!$B$37=АВР!L186),ЦИКЛ!$E$63,IF(AND($AD$8=ЦИКЛ!$A$52,ЦИКЛ!$F$3=N186,ЦИКЛ!$B$37=АВР!L186),ЦИКЛ!$F$63,IF(AND($AD$8=ЦИКЛ!$A$52,ЦИКЛ!$G$3=N186,ЦИКЛ!$B$37=АВР!L186),ЦИКЛ!$G$63,IF(AND($AD$8=ЦИКЛ!$A$52,ЦИКЛ!$H$3=N186,ЦИКЛ!$B$37=АВР!L186),ЦИКЛ!$H$63,IF(AND($AD$8=ЦИКЛ!$A$52,ЦИКЛ!$I$3=N186,ЦИКЛ!$B$37=АВР!L186),ЦИКЛ!$I$63,IF(AND($AD$8=ЦИКЛ!$A$70,ЦИКЛ!$D$3=N186,ЦИКЛ!$B$37=АВР!L186),ЦИКЛ!$D$81,IF(AND($AD$8=ЦИКЛ!$A$70,ЦИКЛ!$E$3=N186,ЦИКЛ!$B$37=АВР!L186),ЦИКЛ!$E$81,IF(AND($AD$8=ЦИКЛ!$A$70,ЦИКЛ!$F$3=N186,ЦИКЛ!$B$37=АВР!L186),ЦИКЛ!$F$81,IF(AND($AD$8=ЦИКЛ!$A$70,ЦИКЛ!$G$3=N186,ЦИКЛ!$B$37=АВР!L186),ЦИКЛ!$G$81,IF(AND($AD$8=ЦИКЛ!$A$70,ЦИКЛ!$H$3=N186,ЦИКЛ!$B$37=АВР!L186),ЦИКЛ!$H$81,IF(AND($AD$8=ЦИКЛ!$A$70,ЦИКЛ!$I$3=N186,ЦИКЛ!$B$37=АВР!L186),ЦИКЛ!$I$81,IF(AND($AD$8=ЦИКЛ!$A$88,ЦИКЛ!$D$3=N186,ЦИКЛ!$B$37=АВР!L186),ЦИКЛ!$D$99,IF(AND($AD$8=ЦИКЛ!$A$88,ЦИКЛ!$E$3=N186,ЦИКЛ!$B$37=АВР!L186),ЦИКЛ!$E$99,IF(AND($AD$8=ЦИКЛ!$A$88,ЦИКЛ!$F$3=N186,ЦИКЛ!$B$37=АВР!L186),ЦИКЛ!$F$99,IF(AND($AD$8=ЦИКЛ!$A$88,ЦИКЛ!$G$3=N186,ЦИКЛ!$B$37=АВР!L186),ЦИКЛ!$G$99,IF(AND($AD$8=ЦИКЛ!$A$88,ЦИКЛ!$H$3=N186,ЦИКЛ!$B$37=АВР!L186),ЦИКЛ!$H$99,IF(AND($AD$8=ЦИКЛ!$A$88,ЦИКЛ!$I$3=N186,ЦИКЛ!$B$37=АВР!L186),ЦИКЛ!$I$99,IF(AND($AD$8=ЦИКЛ!$A$106,ЦИКЛ!$D$3=N186,ЦИКЛ!$B$37=АВР!L186),ЦИКЛ!$D$120,IF(AND($AD$8=ЦИКЛ!$A$106,ЦИКЛ!$E$3=N186,ЦИКЛ!$B$37=АВР!L186),ЦИКЛ!$E$120,IF(AND($AD$8=ЦИКЛ!$A$106,ЦИКЛ!$F$3=N186,ЦИКЛ!$B$37=АВР!L186),ЦИКЛ!$F$120,IF(AND($AD$8=ЦИКЛ!$A$106,ЦИКЛ!$G$3=N186,ЦИКЛ!$B$37=АВР!L186),ЦИКЛ!$G$120,IF(AND($AD$8=ЦИКЛ!$A$106,ЦИКЛ!$H$3=N186,ЦИКЛ!$B$37=АВР!L186),ЦИКЛ!$H$120,IF(AND($AD$8=ЦИКЛ!$A$106,ЦИКЛ!$I$3=N186,ЦИКЛ!$B$37=АВР!L186),ЦИКЛ!$I$120,IF(AND($AD$8=ЦИКЛ!$A$128,ЦИКЛ!$D$3=N186,ЦИКЛ!$B$37=АВР!L186),ЦИКЛ!$D$142,IF(AND($AD$8=ЦИКЛ!$A$128,ЦИКЛ!$E$3=N186,ЦИКЛ!$B$37=АВР!L186),ЦИКЛ!$E$142,IF(AND($AD$8=ЦИКЛ!$A$128,ЦИКЛ!$F$3=N186,ЦИКЛ!$B$37=АВР!L186),ЦИКЛ!$F$142,IF(AND($AD$8=ЦИКЛ!$A$128,ЦИКЛ!$G$3=N186,ЦИКЛ!$B$37=АВР!L186),ЦИКЛ!$G$142,IF(AND($AD$8=ЦИКЛ!$A$128,ЦИКЛ!$H$3=N186,ЦИКЛ!$B$37=АВР!L186),ЦИКЛ!$H$142,IF(AND(АВР!$AD$8=ЦИКЛ!$A$128,ЦИКЛ!$I$3=N186,ЦИКЛ!$B$37=АВР!L186),ЦИКЛ!$I$142))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))',
         1.2, 0, '=Y186-AA186-AB186-AC186-AD186', None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'спо', 'Пакер', 'Навернуть/отвернуть предохранительное кольцо', None, None,
         None, None, None, None, None, None, None, None, None, None, '§300разд.1', None, 'шт', '=SUM(V186)', 0.003, 1,
         0, '=Y187-AA187-AB187-AC187-AD187', None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None, 'Посадка пакера', None, None, None, None, None, None,
         None, None, None, None, None, None, '§138разд.1', None, 'шт', 1, 0.23, 1, 0, '=Y188-AA188-AB188-AC188-AD188',
         None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None, 'Опрессовка превентора ', None, None, None, None, None,
         None, None, None, None, None, None, None, '§115разд.1', None, 'шт', 1, 0.92, 1, 0,
         '=Y189-AA189-AB189-AC189-AD189', None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None, 'Срыв пакера в эксплуатационной колонне', None, None,
         None, None, None, None, None, None, None, None, None, None, '§146разд.1', None, 'шт', 1, 0.15, 1, 0,
         '=Y190-AA190-AB190-AC190-AD190', None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'спо', 'Пакер', 'Подъем НКТ  3 скорость', None, None, None, None, '73мм',
         1000,
         '=IF(AND(L191/V191>=ЦИКЛ!$V$9,L191/V191<=ЦИКЛ!$W$9),ЦИКЛ!$U$9,IF(AND(L191/V191>=ЦИКЛ!$V$10,L191/V191<=ЦИКЛ!$W$10),ЦИКЛ!$U$10,IF(AND(L191/V191>=ЦИКЛ!$V$11,L191/V191<=ЦИКЛ!$W$11),ЦИКЛ!$U$11,IF(AND(L191/V191>=ЦИКЛ!$V$12,L191/V191<=ЦИКЛ!$W$12),ЦИКЛ!$U$12,IF(AND(L191/V191>=ЦИКЛ!$V$13,L191/V191<=ЦИКЛ!$W$13),ЦИКЛ!$U$13,IF(AND(L191/V191>=ЦИКЛ!$V$14,L191/V191<=ЦИКЛ!$W$14),ЦИКЛ!$U$14))))))',
         '=IF(AND(АВР!$AD$8=ЦИКЛ!$A$6,ЦИКЛ!$D$3=M191),ЦИКЛ!$J$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$6,ЦИКЛ!$E$3=M191),ЦИКЛ!$K$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$6,ЦИКЛ!$F$3=M191),ЦИКЛ!$L$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$6,ЦИКЛ!$G$3=M191),ЦИКЛ!$M$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$6,ЦИКЛ!$N$3=M191),ЦИКЛ!$H$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$6,ЦИКЛ!$I$3=M191),ЦИКЛ!$O$30,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$6,ЦИКЛ!$D$3=M191),ЦИКЛ!$J$30,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$6,ЦИКЛ!$E$3=M191),ЦИКЛ!$K$30,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$6,ЦИКЛ!$F$3=M191),ЦИКЛ!$L$30,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$6,ЦИКЛ!$G$3=M191),ЦИКЛ!$M$30,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$6,ЦИКЛ!$H$3=M191),ЦИКЛ!$N$30,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$6,ЦИКЛ!$I$3=M191),ЦИКЛ!$O$30,IF(AND(АВР!$AD$8=ЦИКЛ!$R$6,ЦИКЛ!$D$3=M191),ЦИКЛ!$J$30,IF(AND(АВР!$AD$8=ЦИКЛ!$R$6,ЦИКЛ!$E$3=M191),ЦИКЛ!$K$30,IF(AND(АВР!$AD$8=ЦИКЛ!$R$6,ЦИКЛ!$F$3=M191),ЦИКЛ!$L$30,IF(AND(АВР!$AD$8=ЦИКЛ!$R$6,ЦИКЛ!$G$3=M191),ЦИКЛ!$M$30,IF(AND(АВР!$AD$8=ЦИКЛ!$R$6,ЦИКЛ!$H$3=M191),ЦИКЛ!$N$30,IF(AND(АВР!$AD$8=ЦИКЛ!$R$6,ЦИКЛ!$I$3=M191),ЦИКЛ!$O$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$9,ЦИКЛ!$D$3=M191),ЦИКЛ!$J$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$9,ЦИКЛ!$E$3=M191),ЦИКЛ!$K$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$9,ЦИКЛ!$F$3=M191),ЦИКЛ!$L$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$9,ЦИКЛ!$G$3=M191),ЦИКЛ!$M$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$9,ЦИКЛ!$H$3=M191),ЦИКЛ!$N$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$9,ЦИКЛ!$I$3=M191),ЦИКЛ!$O$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$12,ЦИКЛ!$D$3=M191),ЦИКЛ!$J$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$12,ЦИКЛ!$E$3=M191),ЦИКЛ!$K$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$12,ЦИКЛ!$F$3=M191),ЦИКЛ!$L$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$12,ЦИКЛ!$G$3=M191),ЦИКЛ!$M$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$12,ЦИКЛ!$H$3=M191),ЦИКЛ!$N$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$12,ЦИКЛ!$I$3=M191),ЦИКЛ!$O$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$54,ЦИКЛ!$D$3=M191),ЦИКЛ!$J$62,IF(AND(АВР!$AD$8=ЦИКЛ!$A$54,ЦИКЛ!$E$3=M191),ЦИКЛ!$K$62,IF(AND(АВР!$AD$8=ЦИКЛ!$A$54,ЦИКЛ!$F$3=M191),ЦИКЛ!$L$62,IF(AND(АВР!$AD$8=ЦИКЛ!$A$54,ЦИКЛ!$G$3=M191),ЦИКЛ!$M$62,IF(AND(АВР!$AD$8=ЦИКЛ!$A$54,ЦИКЛ!$H$3=M191),ЦИКЛ!$N$62,IF(AND(АВР!$AD$8=ЦИКЛ!$A$54,ЦИКЛ!$I$3=M191),ЦИКЛ!$O$62,IF(AND(АВР!$AD$8=ЦИКЛ!$A$72,ЦИКЛ!$D$3=M191),ЦИКЛ!$J$80,IF(AND(АВР!$AD$8=ЦИКЛ!$A$72,ЦИКЛ!$E$3=M191),ЦИКЛ!$K$80,IF(AND(АВР!$AD$8=ЦИКЛ!$A$72,ЦИКЛ!$F$3=M191),ЦИКЛ!$L$80,IF(AND(АВР!$AD$8=ЦИКЛ!$A$72,ЦИКЛ!$G$3=M191),ЦИКЛ!$M$80,IF(AND(АВР!$AD$8=ЦИКЛ!$A$72,ЦИКЛ!$H$3=M191),ЦИКЛ!$N$80,IF(AND(АВР!$AD$8=ЦИКЛ!$A$72,ЦИКЛ!$I$3=M191),ЦИКЛ!$O$80,IF(AND(АВР!$AD$8=ЦИКЛ!$A$90,ЦИКЛ!$D$3=M191),ЦИКЛ!$J$98,IF(AND(АВР!$AD$8=ЦИКЛ!$A$90,ЦИКЛ!$E$3=M191),ЦИКЛ!$K$98,IF(AND(АВР!$AD$8=ЦИКЛ!$A$90,ЦИКЛ!$F$3=M191),ЦИКЛ!$L$98,IF(AND(АВР!$AD$8=ЦИКЛ!$A$90,ЦИКЛ!$G$3=M191),ЦИКЛ!$M$98,IF(AND(АВР!$AD$8=ЦИКЛ!$A$90,ЦИКЛ!$H$3=M191),ЦИКЛ!$N$98,IF(AND(АВР!$AD$8=ЦИКЛ!$A$90,ЦИКЛ!$I$3=M191),ЦИКЛ!$O$98,IF(AND(АВР!$AD$8=ЦИКЛ!$A$108,ЦИКЛ!$D$3=M191),ЦИКЛ!$J$118,IF(AND(АВР!$AD$8=ЦИКЛ!$A$108,ЦИКЛ!$E$3=M191),ЦИКЛ!$K$118,IF(AND(АВР!$AD$8=ЦИКЛ!$A$108,ЦИКЛ!$F$3=M191),ЦИКЛ!$L$118,IF(AND(АВР!$AD$8=ЦИКЛ!$A$108,ЦИКЛ!$G$3=M191),ЦИКЛ!$M$118,IF(AND(АВР!$AD$8=ЦИКЛ!$A$108,ЦИКЛ!$H$3=M191),ЦИКЛ!$N$118,IF(AND(АВР!$AD$8=ЦИКЛ!$A$108,ЦИКЛ!$I$3=M191),ЦИКЛ!$O$118,IF(AND(АВР!$AD$8=ЦИКЛ!$A$130,ЦИКЛ!$D$3=M191),ЦИКЛ!$J$140,IF(AND(АВР!$AD$8=ЦИКЛ!$A$130,ЦИКЛ!$E$3=M191),ЦИКЛ!$K$140,IF(AND(АВР!$AD$8=ЦИКЛ!$A$130,ЦИКЛ!$F$3=M191),ЦИКЛ!$L$140,IF(AND(АВР!$AD$8=ЦИКЛ!$A$130,ЦИКЛ!$G$3=M191),ЦИКЛ!$M$140,IF(AND(АВР!$AD$8=ЦИКЛ!$A$130,ЦИКЛ!$H$3=M191),ЦИКЛ!$N$140,IF(AND(АВР!$AD$8=ЦИКЛ!$A$130,ЦИКЛ!$I$3=M191),ЦИКЛ!$O$140))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))',
         None, None, None, None,
         '=IF($AD$8=ЦИКЛ!$A$4,ЦИКЛ!$P$4,IF($AD$8=ЦИКЛ!$A$7,ЦИКЛ!$P$7,IF($AD$8=ЦИКЛ!$A$10,ЦИКЛ!$P$7,IF($AD$8=ЦИКЛ!$A$52,ЦИКЛ!$P$52,IF($AD$8=ЦИКЛ!$A$70,ЦИКЛ!$P$70,IF($AD$8=ЦИКЛ!$A$88,ЦИКЛ!$P$88,IF($AD$8=ЦИКЛ!$A$106,ЦИКЛ!$P$106,IF($AD$8=ЦИКЛ!$A$133,ЦИКЛ!$P$133,IF($AD$8=ЦИКЛ!$Q$4,ЦИКЛ!$P$4,IF($AD$8=ЦИКЛ!$R$4,ЦИКЛ!$P$4))))))))))',
         None, 'шт', 100,
         '=IF(AND(АВР!$AD$8=ЦИКЛ!$A$6,ЦИКЛ!$D$3=M191,ЦИКЛ!$B$37=АВР!K191),ЦИКЛ!$D$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$6,ЦИКЛ!$E$3=M191,ЦИКЛ!$B$37=АВР!K191),ЦИКЛ!$E$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$6,ЦИКЛ!$F$3=M191,ЦИКЛ!$B$37=АВР!K191),ЦИКЛ!$F$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$6,ЦИКЛ!$G$3=M191,ЦИКЛ!$B$37=АВР!K191),ЦИКЛ!$G$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$6,ЦИКЛ!$H$3=M191,ЦИКЛ!$B$37=АВР!K191),ЦИКЛ!$H$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$6,ЦИКЛ!$I$3=M191,ЦИКЛ!$B$37=АВР!K191),ЦИКЛ!$I$30,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$6,ЦИКЛ!$D$3=M191,ЦИКЛ!$B$37=АВР!K191),ЦИКЛ!$D$30,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$6,ЦИКЛ!$E$3=M191,ЦИКЛ!$B$37=АВР!K191),ЦИКЛ!$E$30,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$6,ЦИКЛ!$F$3=M191,ЦИКЛ!$B$37=АВР!K191),ЦИКЛ!$F$30,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$6,ЦИКЛ!$G$3=M191,ЦИКЛ!$B$37=АВР!K191),ЦИКЛ!$G$30,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$6,ЦИКЛ!$H$3=M191,ЦИКЛ!$B$37=АВР!K191),ЦИКЛ!$H$30,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$6,ЦИКЛ!$I$3=M191,ЦИКЛ!$B$37=АВР!K191),ЦИКЛ!$I$30,IF(AND(АВР!$AD$8=ЦИКЛ!$R$6,ЦИКЛ!$D$3=M191,ЦИКЛ!$B$37=АВР!K191),ЦИКЛ!$D$30,IF(AND(АВР!$AD$8=ЦИКЛ!$R$6,ЦИКЛ!$E$3=M191,ЦИКЛ!$B$37=АВР!K191),ЦИКЛ!$E$30,IF(AND(АВР!$AD$8=ЦИКЛ!$R$6,ЦИКЛ!$F$3=M191,ЦИКЛ!$B$37=АВР!K191),ЦИКЛ!$F$30,IF(AND(АВР!$AD$8=ЦИКЛ!$R$6,ЦИКЛ!$G$3=M191,ЦИКЛ!$B$37=АВР!K191),ЦИКЛ!$G$30,IF(AND(АВР!$AD$8=ЦИКЛ!$R$6,ЦИКЛ!$H$3=M191,ЦИКЛ!$B$37=АВР!K191),ЦИКЛ!$H$30,IF(AND(АВР!$AD$8=ЦИКЛ!$R$6,ЦИКЛ!$I$3=M191,ЦИКЛ!$B$37=АВР!K191),ЦИКЛ!$I$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$9,ЦИКЛ!$D$3=M191,ЦИКЛ!$B$37=АВР!K191),ЦИКЛ!$D$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$9,ЦИКЛ!$E$3=M191,ЦИКЛ!$B$37=АВР!K191),ЦИКЛ!$E$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$9,ЦИКЛ!$F$3=M191,ЦИКЛ!$B$37=АВР!K191),ЦИКЛ!$F$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$21,ЦИКЛ!$G$3=M191,ЦИКЛ!$B$37=АВР!K191),ЦИКЛ!$G$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$9,ЦИКЛ!$H$3=M191,ЦИКЛ!$B$37=АВР!K191),ЦИКЛ!$H$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$9,ЦИКЛ!$I$3=M191,ЦИКЛ!$B$37=АВР!K191),ЦИКЛ!$I$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$12,ЦИКЛ!$D$3=M191,ЦИКЛ!$B$37=АВР!K191),ЦИКЛ!$D$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$12,ЦИКЛ!$E$3=M191,ЦИКЛ!$B$37=АВР!K191),ЦИКЛ!$E$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$12,ЦИКЛ!$F$3=M191,ЦИКЛ!$B$37=АВР!K191),ЦИКЛ!$F$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$12,ЦИКЛ!$G$3=M191,ЦИКЛ!$B$37=АВР!K191),ЦИКЛ!$G$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$12,ЦИКЛ!$H$3=M191,ЦИКЛ!$B$37=АВР!K191),ЦИКЛ!$H$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$12,ЦИКЛ!$I$3=M191,ЦИКЛ!$B$37=АВР!K191),ЦИКЛ!$I$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$54,ЦИКЛ!$D$3=M191,ЦИКЛ!$B$37=АВР!K191),ЦИКЛ!$D$62,IF(AND(АВР!$AD$8=ЦИКЛ!$A$54,ЦИКЛ!$E$3=M191,ЦИКЛ!$B$37=АВР!K191),ЦИКЛ!$E$62,IF(AND(АВР!$AD$8=ЦИКЛ!$A$54,ЦИКЛ!$F$3=M191,ЦИКЛ!$B$37=АВР!K191),ЦИКЛ!$F$62,IF(AND(АВР!$AD$8=ЦИКЛ!$A$54,ЦИКЛ!$G$3=M191,ЦИКЛ!$B$37=АВР!K191),ЦИКЛ!$G$62,IF(AND(АВР!$AD$8=ЦИКЛ!$A$54,ЦИКЛ!$H$3=M191,ЦИКЛ!$B$37=АВР!K191),ЦИКЛ!$H$62,IF(AND(АВР!$AD$8=ЦИКЛ!$A$54,ЦИКЛ!$I$3=M191,ЦИКЛ!$B$37=АВР!K191),ЦИКЛ!$I$62,IF(AND(АВР!$AD$8=ЦИКЛ!$A$72,ЦИКЛ!$D$3=M191,ЦИКЛ!$B$37=АВР!K191),ЦИКЛ!$D$80,IF(AND(АВР!$AD$8=ЦИКЛ!$A$72,ЦИКЛ!$E$3=M191,ЦИКЛ!$B$37=АВР!K191),ЦИКЛ!$E$80,IF(AND(АВР!$AD$8=ЦИКЛ!$A$72,ЦИКЛ!$F$3=M191,ЦИКЛ!$B$37=АВР!K191),ЦИКЛ!$F$80,IF(AND(АВР!$AD$8=ЦИКЛ!$A$72,ЦИКЛ!$G$3=M191,ЦИКЛ!$B$37=АВР!K191),ЦИКЛ!$G$80,IF(AND(АВР!$AD$8=ЦИКЛ!$A$72,ЦИКЛ!$H$3=M191,ЦИКЛ!$B$37=АВР!K191),ЦИКЛ!$H$80,IF(AND(АВР!$AD$8=ЦИКЛ!$A$72,ЦИКЛ!$I$3=M191,ЦИКЛ!$B$37=АВР!K191),ЦИКЛ!$I$80,IF(AND(АВР!$AD$8=ЦИКЛ!$A$90,ЦИКЛ!$D$3=M191,ЦИКЛ!$B$37=АВР!K191),ЦИКЛ!$D$98,IF(AND(АВР!$AD$8=ЦИКЛ!$A$90,ЦИКЛ!$E$3=M191,ЦИКЛ!$B$37=АВР!K191),ЦИКЛ!$E$98,IF(AND(АВР!$AD$8=ЦИКЛ!$A$90,ЦИКЛ!$F$3=M191,ЦИКЛ!$B$37=АВР!K191),ЦИКЛ!$F$98,IF(AND(АВР!$AD$8=ЦИКЛ!$A$90,ЦИКЛ!$G$3=M191,ЦИКЛ!$B$37=АВР!K191),ЦИКЛ!$G$98,IF(AND(АВР!$AD$8=ЦИКЛ!$A$90,ЦИКЛ!$H$3=M191,ЦИКЛ!$B$37=АВР!K191),ЦИКЛ!$H$98,IF(AND(АВР!$AD$8=ЦИКЛ!$A$90,ЦИКЛ!$I$3=M191,ЦИКЛ!$B$37=АВР!K191),ЦИКЛ!$I$98,IF(AND(АВР!$AD$8=ЦИКЛ!$A$113,ЦИКЛ!$D$3=M191,ЦИКЛ!$B$37=АВР!K191),ЦИКЛ!$D$118,IF(AND(АВР!$AD$8=ЦИКЛ!$A$108,ЦИКЛ!$E$3=M191,ЦИКЛ!$B$37=АВР!K191),ЦИКЛ!$E$118,IF(AND(АВР!$AD$8=ЦИКЛ!$A$113,ЦИКЛ!$F$3=M191,ЦИКЛ!$B$37=АВР!K191),ЦИКЛ!$F$118,IF(AND(АВР!$AD$8=ЦИКЛ!$A$108,ЦИКЛ!$G$3=M191,ЦИКЛ!$B$37=АВР!K191),ЦИКЛ!$G$118,IF(AND(АВР!$AD$8=ЦИКЛ!$A$113,ЦИКЛ!$H$3=M191,ЦИКЛ!$B$37=АВР!K191),ЦИКЛ!$H$118,IF(AND(АВР!$AD$8=ЦИКЛ!$A$108,ЦИКЛ!$I$3=M191,ЦИКЛ!$B$37=АВР!K191),ЦИКЛ!$I$118,IF(AND(АВР!$AD$8=ЦИКЛ!$A$135,ЦИКЛ!$D$3=M191,ЦИКЛ!$B$37=АВР!K191),ЦИКЛ!$D$140,IF(AND(АВР!$AD$8=ЦИКЛ!$A$130,ЦИКЛ!$E$3=M191,ЦИКЛ!$B$37=АВР!K191),ЦИКЛ!$E$140,IF(AND(АВР!$AD$8=ЦИКЛ!$A$135,ЦИКЛ!$F$3=M191,ЦИКЛ!$B$37=АВР!K191),ЦИКЛ!$F$140,IF(AND(АВР!$AD$8=ЦИКЛ!$A$130,ЦИКЛ!$G$3=M191,ЦИКЛ!$B$37=АВР!K191),ЦИКЛ!$G$140,IF(AND(АВР!$AD$8=ЦИКЛ!$A$135,ЦИКЛ!$H$3=M191,ЦИКЛ!$B$37=АВР!K191),ЦИКЛ!$H$140,IF(AND(АВР!$AD$8=ЦИКЛ!$A$130,ЦИКЛ!$I$3=M191,ЦИКЛ!$B$37=АВР!K191),ЦИКЛ!$I$140))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))',
         1.2, 0, '=Y191-AA191-AB191-AC191-AD191', None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'спо', 'Пакер', 'Подъем НКТ  4 скорость', None, None, None, None, '73мм', 30,
         '=IF(AND(L192/V192>=ЦИКЛ!$V$9,L192/V192<=ЦИКЛ!$W$9),ЦИКЛ!$U$9,IF(AND(L192/V192>=ЦИКЛ!$V$10,L192/V192<=ЦИКЛ!$W$10),ЦИКЛ!$U$10,IF(AND(L192/V192>=ЦИКЛ!$V$11,L192/V192<=ЦИКЛ!$W$11),ЦИКЛ!$U$11,IF(AND(L192/V192>=ЦИКЛ!$V$12,L192/V192<=ЦИКЛ!$W$12),ЦИКЛ!$U$12,IF(AND(L192/V192>=ЦИКЛ!$V$13,L192/V192<=ЦИКЛ!$W$13),ЦИКЛ!$U$13,IF(AND(L192/V192>=ЦИКЛ!$V$14,L192/V192<=ЦИКЛ!$W$14),ЦИКЛ!$U$14))))))',
         '=IF(AND(АВР!$AD$8=ЦИКЛ!$A$109,ЦИКЛ!$D$3=M192),ЦИКЛ!$J$119,IF(AND(АВР!$AD$8=ЦИКЛ!$A$109,ЦИКЛ!$E$3=M192),ЦИКЛ!$K$119,IF(AND(АВР!$AD$8=ЦИКЛ!$A$109,ЦИКЛ!$F$3=M192),ЦИКЛ!$L$119,IF(AND(АВР!$AD$8=ЦИКЛ!$A$109,ЦИКЛ!$G$3=M192),ЦИКЛ!$M$119,IF(AND(АВР!$AD$8=ЦИКЛ!$A$109,ЦИКЛ!$H$3=M192),ЦИКЛ!$N$119,IF(AND(АВР!$AD$8=ЦИКЛ!$A$109,ЦИКЛ!$I$3=M192),ЦИКЛ!$O$119,IF(AND(АВР!$AD$8=ЦИКЛ!$A$131,ЦИКЛ!$D$3=M192),ЦИКЛ!$J$141,IF(AND(АВР!$AD$8=ЦИКЛ!$A$131,ЦИКЛ!$E$3=M192),ЦИКЛ!$K$141,IF(AND(АВР!$AD$8=ЦИКЛ!$A$131,ЦИКЛ!$F$3=M192),ЦИКЛ!$L$141,IF(AND(АВР!$AD$8=ЦИКЛ!$A$131,ЦИКЛ!$G$3=M192),ЦИКЛ!$M$141,IF(AND(АВР!$AD$8=ЦИКЛ!$A$131,ЦИКЛ!$H$3=M192),ЦИКЛ!$N$141,IF(AND(АВР!$AD$8=ЦИКЛ!$A$131,ЦИКЛ!$I$3=M192),ЦИКЛ!$O$141))))))))))))',
         None, None, None, None,
         '=IF($AD$8=ЦИКЛ!$A$4,ЦИКЛ!$P$4,IF($AD$8=ЦИКЛ!$A$7,ЦИКЛ!$P$7,IF($AD$8=ЦИКЛ!$A$10,ЦИКЛ!$P$7,IF($AD$8=ЦИКЛ!$A$52,ЦИКЛ!$P$52,IF($AD$8=ЦИКЛ!$A$70,ЦИКЛ!$P$70,IF($AD$8=ЦИКЛ!$A$88,ЦИКЛ!$P$88,IF($AD$8=ЦИКЛ!$A$106,ЦИКЛ!$P$106,IF($AD$8=ЦИКЛ!$A$133,ЦИКЛ!$P$133,IF($AD$8=ЦИКЛ!$Q$4,ЦИКЛ!$P$4,IF($AD$8=ЦИКЛ!$R$4,ЦИКЛ!$P$4))))))))))',
         None, 'шт', 3,
         '=IF(AND(АВР!$AD$8=ЦИКЛ!$A$109,ЦИКЛ!$D$3=M192,ЦИКЛ!$B$37=АВР!K192),ЦИКЛ!$D$119,IF(AND(АВР!$AD$8=ЦИКЛ!$A$109,ЦИКЛ!$E$3=M192,ЦИКЛ!$B$37=АВР!K192),ЦИКЛ!$E$119,IF(AND(АВР!$AD$8=ЦИКЛ!$A$109,ЦИКЛ!$F$3=M192,ЦИКЛ!$B$37=АВР!K192),ЦИКЛ!$F$119,IF(AND(АВР!$AD$8=ЦИКЛ!$A$109,ЦИКЛ!$G$3=M192,ЦИКЛ!$B$37=АВР!K192),ЦИКЛ!$G$119,IF(AND(АВР!$AD$8=ЦИКЛ!$A$109,ЦИКЛ!$H$3=M192,ЦИКЛ!$B$37=АВР!K192),ЦИКЛ!$H$119,IF(AND(АВР!$AD$8=ЦИКЛ!$A$109,ЦИКЛ!$I$3=M192,ЦИКЛ!$B$37=АВР!K192),ЦИКЛ!$I$119,IF(AND(АВР!$AD$8=ЦИКЛ!$A$131,ЦИКЛ!$D$3=M192,ЦИКЛ!$B$37=АВР!K192),ЦИКЛ!$D$141,IF(AND(АВР!$AD$8=ЦИКЛ!$A$131,ЦИКЛ!$E$3=M192,ЦИКЛ!$B$37=АВР!K192),ЦИКЛ!$E$141,IF(AND(АВР!$AD$8=ЦИКЛ!$A$131,ЦИКЛ!$F$3=M192,ЦИКЛ!$B$37=АВР!K192),ЦИКЛ!$F$141,IF(AND(АВР!$AD$8=ЦИКЛ!$A$131,ЦИКЛ!$G$3=M192,ЦИКЛ!$B$37=АВР!K192),ЦИКЛ!$G$141,IF(AND(АВР!$AD$8=ЦИКЛ!$A$131,ЦИКЛ!$H$3=M192,ЦИКЛ!$B$37=АВР!K192),ЦИКЛ!$H$141,IF(AND(АВР!$AD$8=ЦИКЛ!$A$131,ЦИКЛ!$I$3=M192,ЦИКЛ!$B$37=АВР!K192),ЦИКЛ!$I$141))))))))))))',
         1.2, 0, '=Y192-AA192-AB192-AC192-AD192', None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'спо', 'Пакер', 'Навернуть/отвернуть предохранительное кольцо', None, None,
         None, None, None, None, None, None, None, None, None, None, '§300разд.1', None, 'шт', '=SUM(V191:V192)', 0.003,
         1, 0, '=Y193-AA193-AB193-AC193-AD193', None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, '$Q$4', None, None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'первая.категория', '30м',
         'Монтаж линии дросселирования и глушения.Опрессовка линии 1 схема', None, None, None, None, None, None, None,
         None, None, None, None, None, '§23разд.1', None, 'шт', 1, 2.43, 1, '=V195*W195*X195',
         '=Y195-AA195-AB195-AC195-AD195', None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'первая.категория', '30м', 'дополнительное затраченое время на мж категории',
         None, None, None, None, None, None, None, None, None, None, None, None, 'факт', None, 'час', 1, 1, 1,
         '=V196*W196*X196', '=Y196-AA196-AB196-AC196-AD196', None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None, None, None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'спо', 'ЗО', 'ПЗР СПО перед подъемом труб из скважины', None, None, None,
         None, None, None, None, None, None, None, None, None, '§207разд.1', None, 'шт', 1, 0.07, 1, '=V199*W199*X199',
         '=Y199-AA199-AB199-AC199-AD199', None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'спо', 'ЗО', 'Подъем НКТ  1 скорость ', None, None, None, None, '73мм', 1000,
         '=IF(AND(L200/V200>=ЦИКЛ!$V$9,L200/V200<=ЦИКЛ!$W$9),ЦИКЛ!$U$9,IF(AND(L200/V200>=ЦИКЛ!$V$10,L200/V200<=ЦИКЛ!$W$10),ЦИКЛ!$U$10,IF(AND(L200/V200>=ЦИКЛ!$V$11,L200/V200<=ЦИКЛ!$W$11),ЦИКЛ!$U$11,IF(AND(L200/V200>=ЦИКЛ!$V$12,L200/V200<=ЦИКЛ!$W$12),ЦИКЛ!$U$12,IF(AND(L200/V200>=ЦИКЛ!$V$13,L200/V200<=ЦИКЛ!$W$13),ЦИКЛ!$U$13,IF(AND(L200/V200>=ЦИКЛ!$V$14,L200/V200<=ЦИКЛ!$W$14),ЦИКЛ!$U$14))))))',
         '=IF(AND(АВР!$AD$8=ЦИКЛ!$A$4,ЦИКЛ!$D$3=M200),ЦИКЛ!$J$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$4,ЦИКЛ!$E$3=M200),ЦИКЛ!$K$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$4,ЦИКЛ!$F$3=M200),ЦИКЛ!$L$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$4,ЦИКЛ!$M$3=M200),ЦИКЛ!$M$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$4,ЦИКЛ!$H$3=M200),ЦИКЛ!$N$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$4,ЦИКЛ!$I$3=M200),ЦИКЛ!$O$28,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$4,ЦИКЛ!$D$3=M200),ЦИКЛ!$J$28,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$4,ЦИКЛ!$E$3=M200),ЦИКЛ!$K$28,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$4,ЦИКЛ!$F$3=M200),ЦИКЛ!$L$28,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$4,ЦИКЛ!$G$3=M200),ЦИКЛ!$M$28,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$4,ЦИКЛ!$H$3=M200),ЦИКЛ!$N$28,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$4,ЦИКЛ!$O$3=M200),ЦИКЛ!$I$28,IF(AND(АВР!$AD$8=ЦИКЛ!$R$4,ЦИКЛ!$D$3=M200),ЦИКЛ!$J$28,IF(AND(АВР!$AD$8=ЦИКЛ!$R$4,ЦИКЛ!$E$3=M200),ЦИКЛ!$K$28,IF(AND(АВР!$AD$8=ЦИКЛ!$R$4,ЦИКЛ!$F$3=M200),ЦИКЛ!$L$28,IF(AND(АВР!$AD$8=ЦИКЛ!$R$4,ЦИКЛ!$G$3=M200),ЦИКЛ!$M$28,IF(AND(АВР!$AD$8=ЦИКЛ!$R$4,ЦИКЛ!$N$3=M200),ЦИКЛ!$H$28,IF(AND(АВР!$AD$8=ЦИКЛ!$R$4,ЦИКЛ!$I$3=M200),ЦИКЛ!$O$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$7,ЦИКЛ!$D$3=M200),ЦИКЛ!$J$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$7,ЦИКЛ!$E$3=M200),ЦИКЛ!$K$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$7,ЦИКЛ!$F$3=M200),ЦИКЛ!$L$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$7,ЦИКЛ!$G$3=M200),ЦИКЛ!$M$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$7,ЦИКЛ!$N$3=M200),ЦИКЛ!$H$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$7,ЦИКЛ!$I$3=M200),ЦИКЛ!$O$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$10,ЦИКЛ!$D$3=M200),ЦИКЛ!$J$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$10,ЦИКЛ!$E$3=M200),ЦИКЛ!$K$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$10,ЦИКЛ!$F$3=M200),ЦИКЛ!$L$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$10,ЦИКЛ!$G$3=M200),ЦИКЛ!$M$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$10,ЦИКЛ!$H$3=M200),ЦИКЛ!$N$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$10,ЦИКЛ!$I$3=M200),ЦИКЛ!$O$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$52,ЦИКЛ!$D$3=M200),ЦИКЛ!$J$60,IF(AND(АВР!$AD$8=ЦИКЛ!$A$52,ЦИКЛ!$E$3=M200),ЦИКЛ!$K$60,IF(AND(АВР!$AD$8=ЦИКЛ!$A$52,ЦИКЛ!$F$3=M200),ЦИКЛ!$L$60,IF(AND(АВР!$AD$8=ЦИКЛ!$A$52,ЦИКЛ!$G$3=M200),ЦИКЛ!$M$60,IF(AND(АВР!$AD$8=ЦИКЛ!$A$52,ЦИКЛ!$H$3=M200),ЦИКЛ!$N$60,IF(AND(АВР!$AD$8=ЦИКЛ!$A$52,ЦИКЛ!$I$3=M200),ЦИКЛ!$O$60,IF(AND(АВР!$AD$8=ЦИКЛ!$A$70,ЦИКЛ!$D$3=M200),ЦИКЛ!$J$78,IF(AND(АВР!$AD$8=ЦИКЛ!$A$70,ЦИКЛ!$E$3=M200),ЦИКЛ!$K$78,IF(AND(АВР!$AD$8=ЦИКЛ!$A$70,ЦИКЛ!$F$3=M200),ЦИКЛ!$L$78,IF(AND(АВР!$AD$8=ЦИКЛ!$A$70,ЦИКЛ!$G$3=M200),ЦИКЛ!$M$78,IF(AND(АВР!$AD$8=ЦИКЛ!$A$70,ЦИКЛ!$H$3=M200),ЦИКЛ!$N$78,IF(AND(АВР!$AD$8=ЦИКЛ!$A$70,ЦИКЛ!$I$3=M200),ЦИКЛ!$O$78,IF(AND(АВР!$AD$8=ЦИКЛ!$A$88,ЦИКЛ!$D$3=M200),ЦИКЛ!$J$96,IF(AND(АВР!$AD$8=ЦИКЛ!$A$88,ЦИКЛ!$E$3=M200),ЦИКЛ!$K$96,IF(AND(АВР!$AD$8=ЦИКЛ!$A$88,ЦИКЛ!$F$3=M200),ЦИКЛ!$L$96,IF(AND(АВР!$AD$8=ЦИКЛ!$A$88,ЦИКЛ!$G$3=M200),ЦИКЛ!$M$96,IF(AND(АВР!$AD$8=ЦИКЛ!$A$88,ЦИКЛ!$H$3=M200),ЦИКЛ!$N$96,IF(AND(АВР!$AD$8=ЦИКЛ!$A$88,ЦИКЛ!$I$3=M200),ЦИКЛ!$O$96,IF(AND(АВР!$AD$8=ЦИКЛ!$A$116,ЦИКЛ!$D$3=M200),ЦИКЛ!$J$116,IF(AND(АВР!$AD$8=ЦИКЛ!$A$116,ЦИКЛ!$E$3=M200),ЦИКЛ!$K$116,IF(AND(АВР!$AD$8=ЦИКЛ!$A$116,ЦИКЛ!$F$3=M200),ЦИКЛ!$L$116,IF(AND(АВР!$AD$8=ЦИКЛ!$A$116,ЦИКЛ!$G$3=M200),ЦИКЛ!$M$116,IF(AND(АВР!$AD$8=ЦИКЛ!$A$116,ЦИКЛ!$H$3=M200),ЦИКЛ!$N$116,IF(AND(АВР!$AD$8=ЦИКЛ!$A$116,ЦИКЛ!$I$3=M200),ЦИКЛ!$O$116,IF(AND(АВР!$AD$8=ЦИКЛ!$A$128,ЦИКЛ!$D$3=M200),ЦИКЛ!$J$138,IF(AND(АВР!$AD$8=ЦИКЛ!$A$128,ЦИКЛ!$E$3=M200),ЦИКЛ!$K$138,IF(AND(АВР!$AD$8=ЦИКЛ!$A$128,ЦИКЛ!$F$3=M200),ЦИКЛ!$L$138,IF(AND(АВР!$AD$8=ЦИКЛ!$A$128,ЦИКЛ!$G$3=M200),ЦИКЛ!$M$138,IF(AND(АВР!$AD$8=ЦИКЛ!$A$128,ЦИКЛ!$H$3=M200),ЦИКЛ!$N$138,IF(AND(АВР!$AD$8=ЦИКЛ!$A$128,ЦИКЛ!$I$3=M200),ЦИКЛ!$O$138))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))',
         None, None, None, None,
         '=IF($AD$8=ЦИКЛ!$A$4,ЦИКЛ!$P$4,IF($AD$8=ЦИКЛ!$A$7,ЦИКЛ!$P$7,IF($AD$8=ЦИКЛ!$A$10,ЦИКЛ!$P$7,IF($AD$8=ЦИКЛ!$A$52,ЦИКЛ!$P$52,IF($AD$8=ЦИКЛ!$A$70,ЦИКЛ!$P$70,IF($AD$8=ЦИКЛ!$A$88,ЦИКЛ!$P$88,IF($AD$8=ЦИКЛ!$A$106,ЦИКЛ!$P$106,IF($AD$8=ЦИКЛ!$A$133,ЦИКЛ!$P$133,IF($AD$8=ЦИКЛ!$Q$4,ЦИКЛ!$P$4,IF($AD$8=ЦИКЛ!$R$4,ЦИКЛ!$P$4))))))))))',
         None, 'шт', 100,
         '=IF(AND(АВР!$AD$8=ЦИКЛ!$A$4,ЦИКЛ!$D$3=M200,ЦИКЛ!$B$37=АВР!K200),ЦИКЛ!$D$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$4,ЦИКЛ!$E$3=M200,ЦИКЛ!$B$37=АВР!K200),ЦИКЛ!$E$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$4,ЦИКЛ!$F$3=M200,ЦИКЛ!$B$37=АВР!K200),ЦИКЛ!$F$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$4,ЦИКЛ!$G$3=M200,ЦИКЛ!$B$37=АВР!K200),ЦИКЛ!$G$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$4,ЦИКЛ!$H$3=M200,ЦИКЛ!$B$37=АВР!K200),ЦИКЛ!$H$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$4,ЦИКЛ!$I$3=M200,ЦИКЛ!$B$37=АВР!K200),ЦИКЛ!$I$28,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$4,ЦИКЛ!$D$3=M200,ЦИКЛ!$B$37=АВР!K200),ЦИКЛ!$D$28,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$4,ЦИКЛ!$E$3=M200,ЦИКЛ!$B$37=АВР!K200),ЦИКЛ!$E$28,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$4,ЦИКЛ!$F$3=M200,ЦИКЛ!$B$37=АВР!K200),ЦИКЛ!$F$28,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$4,ЦИКЛ!$G$3=M200,ЦИКЛ!$B$37=АВР!K200),ЦИКЛ!$G$28,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$4,ЦИКЛ!$H$3=M200,ЦИКЛ!$B$37=АВР!K200),ЦИКЛ!$H$28,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$4,ЦИКЛ!$I$3=M200,ЦИКЛ!$B$37=АВР!K200),ЦИКЛ!$I$28,IF(AND(АВР!$AD$8=ЦИКЛ!$R$4,ЦИКЛ!$D$3=M200,ЦИКЛ!$B$37=АВР!K200),ЦИКЛ!$D$28,IF(AND(АВР!$AD$8=ЦИКЛ!$R$4,ЦИКЛ!$E$3=M200,ЦИКЛ!$B$37=АВР!K200),ЦИКЛ!$E$28,IF(AND(АВР!$AD$8=ЦИКЛ!$R$4,ЦИКЛ!$F$3=M200,ЦИКЛ!$B$37=АВР!K200),ЦИКЛ!$F$28,IF(AND(АВР!$AD$8=ЦИКЛ!$R$4,ЦИКЛ!$G$3=M200,ЦИКЛ!$B$37=АВР!K200),ЦИКЛ!$G$28,IF(AND(АВР!$AD$8=ЦИКЛ!$R$4,ЦИКЛ!$H$3=M200,ЦИКЛ!$B$37=АВР!K200),ЦИКЛ!$H$28,IF(AND(АВР!$AD$8=ЦИКЛ!$R$4,ЦИКЛ!$I$3=M200,ЦИКЛ!$B$37=АВР!K200),ЦИКЛ!$I$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$7,ЦИКЛ!$D$3=M200,ЦИКЛ!$B$37=АВР!K200),ЦИКЛ!$D$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$7,ЦИКЛ!$E$3=M200,ЦИКЛ!$B$37=АВР!K200),ЦИКЛ!$E$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$7,ЦИКЛ!$F$3=M200,ЦИКЛ!$B$37=АВР!K200),ЦИКЛ!$F$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$7,ЦИКЛ!$G$3=M200,ЦИКЛ!$B$37=АВР!K200),ЦИКЛ!$G$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$7,ЦИКЛ!$H$3=M200,ЦИКЛ!$B$37=АВР!K200),ЦИКЛ!$H$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$7,ЦИКЛ!$I$3=M200,ЦИКЛ!$B$37=АВР!K200),ЦИКЛ!$I$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$10,ЦИКЛ!$D$3=M200,ЦИКЛ!$B$37=АВР!K200),ЦИКЛ!$D$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$10,ЦИКЛ!$E$3=M200,ЦИКЛ!$B$37=АВР!K200),ЦИКЛ!$E$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$10,ЦИКЛ!$F$3=M200,ЦИКЛ!$B$37=АВР!K200),ЦИКЛ!$F$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$10,ЦИКЛ!$G$3=M200,ЦИКЛ!$B$37=АВР!K200),ЦИКЛ!$G$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$10,ЦИКЛ!$H$3=M200,ЦИКЛ!$B$37=АВР!K200),ЦИКЛ!$H$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$10,ЦИКЛ!$I$3=M200,ЦИКЛ!$B$37=АВР!K200),ЦИКЛ!$I$28,IF(AND(АВР!$AD$8=ЦИКЛ!$A$52,ЦИКЛ!$D$3=M200,ЦИКЛ!$B$37=АВР!K200),ЦИКЛ!$D$60,IF(AND(АВР!$AD$8=ЦИКЛ!$A$52,ЦИКЛ!$E$3=M200,ЦИКЛ!$B$37=АВР!K200),ЦИКЛ!$E$60,IF(AND(АВР!$AD$8=ЦИКЛ!$A$52,ЦИКЛ!$F$3=M200,ЦИКЛ!$B$37=АВР!K200),ЦИКЛ!$F$60,IF(AND(АВР!$AD$8=ЦИКЛ!$A$52,ЦИКЛ!$G$3=M200,ЦИКЛ!$B$37=АВР!K200),ЦИКЛ!$G$60,IF(AND(АВР!$AD$8=ЦИКЛ!$A$52,ЦИКЛ!$H$3=M200,ЦИКЛ!$B$37=АВР!K200),ЦИКЛ!$H$60,IF(AND(АВР!$AD$8=ЦИКЛ!$A$52,ЦИКЛ!$I$3=M200,ЦИКЛ!$B$37=АВР!K200),ЦИКЛ!$I$60,IF(AND(АВР!$AD$8=ЦИКЛ!$A$70,ЦИКЛ!$D$3=M200,ЦИКЛ!$B$37=АВР!K200),ЦИКЛ!$D$78,IF(AND(АВР!$AD$8=ЦИКЛ!$A$70,ЦИКЛ!$E$3=M200,ЦИКЛ!$B$37=АВР!K200),ЦИКЛ!$E$78,IF(AND(АВР!$AD$8=ЦИКЛ!$A$70,ЦИКЛ!$F$3=M200,ЦИКЛ!$B$37=АВР!K200),ЦИКЛ!$F$78,IF(AND(АВР!$AD$8=ЦИКЛ!$A$70,ЦИКЛ!$G$3=M200,ЦИКЛ!$B$37=АВР!K200),ЦИКЛ!$G$78,IF(AND(АВР!$AD$8=ЦИКЛ!$A$70,ЦИКЛ!$H$3=M200,ЦИКЛ!$B$37=АВР!K200),ЦИКЛ!$H$78,IF(AND(АВР!$AD$8=ЦИКЛ!$A$70,ЦИКЛ!$I$3=M200,ЦИКЛ!$B$37=АВР!K200),ЦИКЛ!$I$78,IF(AND(АВР!$AD$8=ЦИКЛ!$A$88,ЦИКЛ!$D$3=M200,ЦИКЛ!$B$37=АВР!K200),ЦИКЛ!$D$96,IF(AND(АВР!$AD$8=ЦИКЛ!$A$88,ЦИКЛ!$E$3=M200,ЦИКЛ!$B$37=АВР!K200),ЦИКЛ!$E$96,IF(AND(АВР!$AD$8=ЦИКЛ!$A$88,ЦИКЛ!$F$3=M200,ЦИКЛ!$B$37=АВР!K200),ЦИКЛ!$F$96,IF(AND(АВР!$AD$8=ЦИКЛ!$A$88,ЦИКЛ!$G$3=M200,ЦИКЛ!$B$37=АВР!K200),ЦИКЛ!$G$96,IF(AND(АВР!$AD$8=ЦИКЛ!$A$88,ЦИКЛ!$H$3=M200,ЦИКЛ!$B$37=АВР!K200),ЦИКЛ!$H$96,IF(AND(АВР!$AD$8=ЦИКЛ!$A$88,ЦИКЛ!$I$3=M200,ЦИКЛ!$B$37=АВР!K200),ЦИКЛ!$I$96,IF(AND(АВР!$AD$8=ЦИКЛ!$A$106,ЦИКЛ!$D$3=M200,ЦИКЛ!$B$37=АВР!K200),ЦИКЛ!$D$116,IF(AND(АВР!$AD$8=ЦИКЛ!$A$106,ЦИКЛ!$E$3=M200,ЦИКЛ!$B$37=АВР!K200),ЦИКЛ!$E$116,IF(AND(АВР!$AD$8=ЦИКЛ!$A$106,ЦИКЛ!$F$3=M200,ЦИКЛ!$B$37=АВР!K200),ЦИКЛ!$F$116,IF(AND(АВР!$AD$8=ЦИКЛ!$A$106,ЦИКЛ!$G$3=M200,ЦИКЛ!$B$37=АВР!K200),ЦИКЛ!$G$116,IF(AND(АВР!$AD$8=ЦИКЛ!$A$106,ЦИКЛ!$H$3=M200,ЦИКЛ!$B$37=АВР!K200),ЦИКЛ!$H$116,IF(AND(АВР!$AD$8=ЦИКЛ!$A$106,ЦИКЛ!$I$3=M200,ЦИКЛ!$B$37=АВР!K200),ЦИКЛ!$I$116,IF(AND(АВР!$AD$8=ЦИКЛ!$A$128,ЦИКЛ!$D$3=M200,ЦИКЛ!$B$37=АВР!K200),ЦИКЛ!$D$138,IF(AND(АВР!$AD$8=ЦИКЛ!$A$128,ЦИКЛ!$E$3=M200,ЦИКЛ!$B$37=АВР!K200),ЦИКЛ!$E$138,IF(AND(АВР!$AD$8=ЦИКЛ!$A$128,ЦИКЛ!$F$3=M200,ЦИКЛ!$B$37=АВР!K200),ЦИКЛ!$F$138,IF(AND(АВР!$AD$8=ЦИКЛ!$A$128,ЦИКЛ!$G$3=M200,ЦИКЛ!$B$37=АВР!K200),ЦИКЛ!$G$138,IF(AND(АВР!$AD$8=ЦИКЛ!$A$128,ЦИКЛ!$H$3=M200,ЦИКЛ!$B$37=АВР!K200),ЦИКЛ!$H$138,IF(AND(АВР!$AD$8=ЦИКЛ!$A$128,ЦИКЛ!$I$3=M200,ЦИКЛ!$B$37=АВР!K200),ЦИКЛ!$I$138))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))',
         1, '=V200*W200*X200', '=Y200-AA200-AB200-AC200-AD200', None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'спо', 'ЗО', 'Подъем НКТ  2 скорость', None, None, None, None, '73мм', 1000,
         '=IF(AND(L201/V201>=ЦИКЛ!$V$9,L201/V201<=ЦИКЛ!$W$9),ЦИКЛ!$U$9,IF(AND(L201/V201>=ЦИКЛ!$V$10,L201/V201<=ЦИКЛ!$W$10),ЦИКЛ!$U$10,IF(AND(L201/V201>=ЦИКЛ!$V$11,L201/V201<=ЦИКЛ!$W$11),ЦИКЛ!$U$11,IF(AND(L201/V201>=ЦИКЛ!$V$12,L201/V201<=ЦИКЛ!$W$12),ЦИКЛ!$U$12,IF(AND(L201/V201>=ЦИКЛ!$V$13,L201/V201<=ЦИКЛ!$W$13),ЦИКЛ!$U$13,IF(AND(L201/V201>=ЦИКЛ!$V$14,L201/V201<=ЦИКЛ!$W$14),ЦИКЛ!$U$14))))))',
         '=IF(AND(АВР!$AD$8=ЦИКЛ!$A$5,ЦИКЛ!$D$3=M201),ЦИКЛ!$J$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$5,ЦИКЛ!$E$3=M201),ЦИКЛ!$K$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$5,ЦИКЛ!$F$3=M201),ЦИКЛ!$L$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$5,ЦИКЛ!$G$3=M201),ЦИКЛ!$M$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$5,ЦИКЛ!$H$3=M201),ЦИКЛ!$N$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$5,ЦИКЛ!$I$3=M201),ЦИКЛ!$O$29,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$5,ЦИКЛ!$D$3=M201),ЦИКЛ!$J$29,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$5,ЦИКЛ!$E$3=M201),ЦИКЛ!$K$29,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$5,ЦИКЛ!$F$3=M201),ЦИКЛ!$L$29,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$5,ЦИКЛ!$G$3=M201),ЦИКЛ!$M$29,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$5,ЦИКЛ!$H$3=M201),ЦИКЛ!$N$29,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$5,ЦИКЛ!$I$3=M201),ЦИКЛ!$O$29,IF(AND(АВР!$AD$8=ЦИКЛ!$R$5,ЦИКЛ!$D$3=M201),ЦИКЛ!$J$29,IF(AND(АВР!$AD$8=ЦИКЛ!$R$5,ЦИКЛ!$E$3=M201),ЦИКЛ!$K$29,IF(AND(АВР!$AD$8=ЦИКЛ!$R$5,ЦИКЛ!$F$3=M201),ЦИКЛ!$L$29,IF(AND(АВР!$AD$8=ЦИКЛ!$R$5,ЦИКЛ!$G$3=M201),ЦИКЛ!$M$29,IF(AND(АВР!$AD$8=ЦИКЛ!$R$5,ЦИКЛ!$H$3=M201),ЦИКЛ!$N$29,IF(AND(АВР!$AD$8=ЦИКЛ!$R$5,ЦИКЛ!$I$3=M201),ЦИКЛ!$O$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$8,ЦИКЛ!$D$3=M201),ЦИКЛ!$J$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$8,ЦИКЛ!$E$3=M201),ЦИКЛ!$K$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$8,ЦИКЛ!$F$3=M201),ЦИКЛ!$L$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$8,ЦИКЛ!$G$3=M201),ЦИКЛ!$M$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$8,ЦИКЛ!$H$3=M201),ЦИКЛ!$N$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$8,ЦИКЛ!$I$3=M201),ЦИКЛ!$O$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$11,ЦИКЛ!$D$3=M201),ЦИКЛ!$J$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$11,ЦИКЛ!$E$3=M201),ЦИКЛ!$K$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$11,ЦИКЛ!$F$3=M201),ЦИКЛ!$L$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$11,ЦИКЛ!$G$3=M201),ЦИКЛ!$M$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$11,ЦИКЛ!$H$3=M201),ЦИКЛ!$N$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$11,ЦИКЛ!$I$3=M201),ЦИКЛ!$O$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$53,ЦИКЛ!$D$3=M201),ЦИКЛ!#REF!,IF(AND(АВР!$AD$8=ЦИКЛ!$A$53,ЦИКЛ!$E$3=M201),ЦИКЛ!$K$61,IF(AND(АВР!$AD$8=ЦИКЛ!$A$53,ЦИКЛ!$F$3=M201),ЦИКЛ!$L$61,IF(AND(АВР!$AD$8=ЦИКЛ!$A$53,ЦИКЛ!$G$3=M201),ЦИКЛ!$M$61,IF(AND(АВР!$AD$8=ЦИКЛ!$A$53,ЦИКЛ!$H$3=M201),ЦИКЛ!$N$61,IF(AND(АВР!$AD$8=ЦИКЛ!$A$53,ЦИКЛ!$I$3=M201),ЦИКЛ!$O$61,IF(AND(АВР!$AD$8=ЦИКЛ!$A$71,ЦИКЛ!$D$3=M201),ЦИКЛ!$J$79,IF(AND(АВР!$AD$8=ЦИКЛ!$A$71,ЦИКЛ!$E$3=M201),ЦИКЛ!$K$79,IF(AND(АВР!$AD$8=ЦИКЛ!$A$71,ЦИКЛ!$F$3=M201),ЦИКЛ!$L$79,IF(AND(АВР!$AD$8=ЦИКЛ!$A$71,ЦИКЛ!$G$3=M201),ЦИКЛ!$M$79,IF(AND(АВР!$AD$8=ЦИКЛ!$A$71,ЦИКЛ!$H$3=M201),ЦИКЛ!$N$79,IF(AND(АВР!$AD$8=ЦИКЛ!$A$71,ЦИКЛ!$I$3=M201),ЦИКЛ!$O$79,IF(AND(АВР!$AD$8=ЦИКЛ!$A$89,ЦИКЛ!$D$3=M201),ЦИКЛ!$J$97,IF(AND(АВР!$AD$8=ЦИКЛ!$A$89,ЦИКЛ!$E$3=M201),ЦИКЛ!$K$97,IF(AND(АВР!$AD$8=ЦИКЛ!$A$89,ЦИКЛ!$F$3=M201),ЦИКЛ!$L$97,IF(AND(АВР!$AD$8=ЦИКЛ!$A$89,ЦИКЛ!$G$3=M201),ЦИКЛ!$M$97,IF(AND(АВР!$AD$8=ЦИКЛ!$A$89,ЦИКЛ!$H$3=M201),ЦИКЛ!$N$97,IF(AND(АВР!$AD$8=ЦИКЛ!$A$89,ЦИКЛ!$I$3=M201),ЦИКЛ!$O$97,IF(AND(АВР!$AD$8=ЦИКЛ!$A$107,ЦИКЛ!$D$3=M201),ЦИКЛ!$J$117,IF(AND(АВР!$AD$8=ЦИКЛ!$A$107,ЦИКЛ!$E$3=M201),ЦИКЛ!$K$117,IF(AND(АВР!$AD$8=ЦИКЛ!$A$107,ЦИКЛ!$F$3=M201),ЦИКЛ!$L$117,IF(AND(АВР!$AD$8=ЦИКЛ!$A$107,ЦИКЛ!$G$3=M201),ЦИКЛ!$M$117,IF(AND(АВР!$AD$8=ЦИКЛ!$A$107,ЦИКЛ!$H$3=M201),ЦИКЛ!$N$117,IF(AND(АВР!$AD$8=ЦИКЛ!$A$107,ЦИКЛ!$I$3=M201),ЦИКЛ!$O$117,IF(AND(АВР!$AD$8=ЦИКЛ!$A$129,ЦИКЛ!$D$3=M201),ЦИКЛ!$J$139,IF(AND(АВР!$AD$8=ЦИКЛ!$A$129,ЦИКЛ!$E$3=M201),ЦИКЛ!$K$139,IF(AND(АВР!$AD$8=ЦИКЛ!$A$129,ЦИКЛ!$F$3=M201),ЦИКЛ!$L$139,IF(AND(АВР!$AD$8=ЦИКЛ!$A$129,ЦИКЛ!$G$3=M201),ЦИКЛ!$M$139,IF(AND(АВР!$AD$8=ЦИКЛ!$A$129,ЦИКЛ!$H$3=M201),ЦИКЛ!$N$139,IF(AND(АВР!$AD$8=ЦИКЛ!$A$129,ЦИКЛ!$I$3=M201),ЦИКЛ!$O$139))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))',
         None, None, None, None,
         '=IF($AD$8=ЦИКЛ!$A$4,ЦИКЛ!$P$4,IF($AD$8=ЦИКЛ!$A$7,ЦИКЛ!$P$7,IF($AD$8=ЦИКЛ!$A$10,ЦИКЛ!$P$7,IF($AD$8=ЦИКЛ!$A$52,ЦИКЛ!$P$52,IF($AD$8=ЦИКЛ!$A$70,ЦИКЛ!$P$70,IF($AD$8=ЦИКЛ!$A$88,ЦИКЛ!$P$88,IF($AD$8=ЦИКЛ!$A$106,ЦИКЛ!$P$106,IF($AD$8=ЦИКЛ!$A$133,ЦИКЛ!$P$133,IF($AD$8=ЦИКЛ!$Q$4,ЦИКЛ!$P$4,IF($AD$8=ЦИКЛ!$R$4,ЦИКЛ!$P$4))))))))))',
         None, 'шт', 100,
         '=IF(AND(АВР!$AD$8=ЦИКЛ!$A$5,ЦИКЛ!$D$3=M201,ЦИКЛ!$B$37=АВР!K201),ЦИКЛ!$D$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$5,ЦИКЛ!$E$3=M201,ЦИКЛ!$B$37=АВР!K201),ЦИКЛ!$E$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$5,ЦИКЛ!$F$3=M201,ЦИКЛ!$B$37=АВР!K201),ЦИКЛ!$F$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$5,ЦИКЛ!$G$3=M201,ЦИКЛ!$B$37=АВР!K201),ЦИКЛ!$G$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$5,ЦИКЛ!$H$3=M201,ЦИКЛ!$B$37=АВР!K201),ЦИКЛ!$H$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$5,ЦИКЛ!$I$3=M201,ЦИКЛ!$B$37=K201),ЦИКЛ!$I$29,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$5,ЦИКЛ!$D$3=M201,ЦИКЛ!$B$37=K201),ЦИКЛ!$D$29,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$5,ЦИКЛ!$E$3=M201,ЦИКЛ!$B$37=K201),ЦИКЛ!$E$29,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$5,ЦИКЛ!$F$3=M201,ЦИКЛ!$B$37=K201),ЦИКЛ!$F$29,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$5,ЦИКЛ!$G$3=M201,ЦИКЛ!$B$37=K201),ЦИКЛ!$G$29,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$5,ЦИКЛ!$H$3=M201,ЦИКЛ!$B$37=K201),ЦИКЛ!$H$29,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$5,ЦИКЛ!$I$3=M201,ЦИКЛ!$B$37=K201),ЦИКЛ!$I$29,IF(AND(АВР!$AD$8=ЦИКЛ!$R$5,ЦИКЛ!$D$3=M201,ЦИКЛ!$B$37=K201),ЦИКЛ!$D$29,IF(AND(АВР!$AD$8=ЦИКЛ!$R$5,ЦИКЛ!$E$3=M201,ЦИКЛ!$B$37=K201),ЦИКЛ!$E$29,IF(AND(АВР!$AD$8=ЦИКЛ!$R$5,ЦИКЛ!$F$3=M201,ЦИКЛ!$B$37=K201),ЦИКЛ!$F$29,IF(AND(АВР!$AD$8=ЦИКЛ!$R$5,ЦИКЛ!$G$3=M201,ЦИКЛ!$B$37=K201),ЦИКЛ!$G$29,IF(AND(АВР!$AD$8=ЦИКЛ!$R$5,ЦИКЛ!$H$3=M201,ЦИКЛ!$B$37=K201),ЦИКЛ!$H$29,IF(AND(АВР!$AD$8=ЦИКЛ!$R$5,ЦИКЛ!$I$3=M201,ЦИКЛ!$B$37=K201),ЦИКЛ!$I$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$8,ЦИКЛ!$D$3=M201,ЦИКЛ!$B$37=K201),ЦИКЛ!$D$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$8,ЦИКЛ!$E$3=M201,ЦИКЛ!$B$37=K201),ЦИКЛ!$E$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$8,ЦИКЛ!$F$3=M201,ЦИКЛ!$B$37=K201),ЦИКЛ!$F$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$8,ЦИКЛ!$G$3=M201,ЦИКЛ!$B$37=K201),ЦИКЛ!$G$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$8,ЦИКЛ!$H$3=M201,ЦИКЛ!$B$37=K201),ЦИКЛ!$H$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$8,ЦИКЛ!$I$3=M201,ЦИКЛ!$B$37=K201),ЦИКЛ!$I$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$11,ЦИКЛ!$D$3=M201,,ЦИКЛ!$B$37=K201),ЦИКЛ!$D$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$11,ЦИКЛ!$E$3=M201,ЦИКЛ!$B$37=K201),ЦИКЛ!$E$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$11,ЦИКЛ!$F$3=M201,ЦИКЛ!$B$37=K201),ЦИКЛ!$F$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$11,ЦИКЛ!$G$3=M201,ЦИКЛ!$B$37=K201),ЦИКЛ!$G$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$11,ЦИКЛ!$H$3=M201,ЦИКЛ!$B$37=K201),ЦИКЛ!$H$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$11,ЦИКЛ!$I$3=M201,ЦИКЛ!$B$37=K201),ЦИКЛ!$I$29,IF(AND(АВР!$AD$8=ЦИКЛ!$A$53,ЦИКЛ!$D$3=M201,ЦИКЛ!$B$37=K201),ЦИКЛ!$D$61,IF(AND(АВР!$AD$8=ЦИКЛ!$A$53,ЦИКЛ!$E$3=M201,ЦИКЛ!$B$37=K201),ЦИКЛ!$E$61,IF(AND(АВР!$AD$8=ЦИКЛ!$A$53,ЦИКЛ!$F$3=M201,ЦИКЛ!$B$37=K201),ЦИКЛ!$F$61,IF(AND(АВР!$AD$8=ЦИКЛ!$A$53,ЦИКЛ!$G$3=M201,ЦИКЛ!$B$37=K201),ЦИКЛ!$G$61,IF(AND(АВР!$AD$8=ЦИКЛ!$A$53,ЦИКЛ!$H$3=M201,ЦИКЛ!$B$37=K201),ЦИКЛ!$H$61,IF(AND(АВР!$AD$8=ЦИКЛ!$A$53,ЦИКЛ!$I$3=M201,ЦИКЛ!$B$37=K201),ЦИКЛ!$I$61,IF(AND(АВР!$AD$8=ЦИКЛ!$A$71,ЦИКЛ!$D$3=M201,ЦИКЛ!$B$37=K201),ЦИКЛ!$D$79,IF(AND(АВР!$AD$8=ЦИКЛ!$A$71,ЦИКЛ!$E$3=M201,ЦИКЛ!$B$37=K201),ЦИКЛ!$E$79,IF(AND(АВР!$AD$8=ЦИКЛ!$A$71,ЦИКЛ!$F$3=M201,ЦИКЛ!$B$37=K201),ЦИКЛ!$F$79,IF(AND(АВР!$AD$8=ЦИКЛ!$A$71,ЦИКЛ!$G$3=M201,ЦИКЛ!$B$37=K201),ЦИКЛ!$G$79,IF(AND(АВР!$AD$8=ЦИКЛ!$A$71,ЦИКЛ!$H$3=M201,ЦИКЛ!$B$37=K201),ЦИКЛ!$H$79,IF(AND(АВР!$AD$8=ЦИКЛ!$A$71,ЦИКЛ!$I$3=M201,ЦИКЛ!$B$37=K201),ЦИКЛ!$I$79,IF(AND(АВР!$AD$8=ЦИКЛ!$A$89,ЦИКЛ!$D$3=M201,ЦИКЛ!$B$37=K201),ЦИКЛ!$D$97,IF(AND(АВР!$AD$8=ЦИКЛ!$A$89,ЦИКЛ!$E$3=M201,ЦИКЛ!$B$37=K201),ЦИКЛ!$E$97,IF(AND(АВР!$AD$8=ЦИКЛ!$A$89,ЦИКЛ!$F$3=M201,ЦИКЛ!$B$37=K201),ЦИКЛ!$F$97,IF(AND(АВР!$AD$8=ЦИКЛ!$A$89,ЦИКЛ!$G$3=M201,ЦИКЛ!$B$37=K201),ЦИКЛ!$G$97,IF(AND(АВР!$AD$8=ЦИКЛ!$A$89,ЦИКЛ!$H$3=M201,ЦИКЛ!$B$37=K201),ЦИКЛ!$H$97,IF(AND(АВР!$AD$8=ЦИКЛ!$A$89,ЦИКЛ!$I$3=M201,ЦИКЛ!$B$37=K201),ЦИКЛ!$I$97,IF(AND(АВР!$AD$8=ЦИКЛ!$A$107,ЦИКЛ!$D$3=M201,ЦИКЛ!$B$37=K201),ЦИКЛ!$D$117,IF(AND(АВР!$AD$8=ЦИКЛ!$A$107,ЦИКЛ!$E$3=M201,ЦИКЛ!$B$37=K201),ЦИКЛ!$E$117,IF(AND(АВР!$AD$8=ЦИКЛ!$A$107,ЦИКЛ!$F$3=M201,ЦИКЛ!$B$37=K201),ЦИКЛ!$F$117,IF(AND(АВР!$AD$8=ЦИКЛ!$A$107,ЦИКЛ!$G$3=M201,ЦИКЛ!$B$37=K201),ЦИКЛ!$G$117,IF(AND(АВР!$AD$8=ЦИКЛ!$A$107,ЦИКЛ!$H$3=M201,ЦИКЛ!$B$37=K201),ЦИКЛ!$H$117,IF(AND(АВР!$AD$8=ЦИКЛ!$A$107,ЦИКЛ!$I$3=M201,ЦИКЛ!$B$37=K201),ЦИКЛ!$I$117,IF(AND(АВР!$AD$8=ЦИКЛ!$A$129,ЦИКЛ!$D$3=M201,ЦИКЛ!$B$37=K201),ЦИКЛ!$D$139,IF(AND(АВР!$AD$8=ЦИКЛ!$A$129,ЦИКЛ!$E$3=M201,ЦИКЛ!$B$37=K201),ЦИКЛ!$E$139,IF(AND(АВР!$AD$8=ЦИКЛ!$A$129,ЦИКЛ!$F$3=M201,ЦИКЛ!$B$37=K201),ЦИКЛ!$F$139,IF(AND(АВР!$AD$8=ЦИКЛ!$A$129,ЦИКЛ!$G$3=M201,ЦИКЛ!$B$37=K201),ЦИКЛ!$G$139,IF(AND(АВР!$AD$8=ЦИКЛ!$A$129,ЦИКЛ!$H$3=M201,ЦИКЛ!$B$37=K201),ЦИКЛ!$H$139,IF(AND(АВР!$AD$8=ЦИКЛ!$A$129,ЦИКЛ!$I$3=M201,ЦИКЛ!$B$37=K201),ЦИКЛ!$I$139))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))',
         1, '=V201*W201*X201', '=Y201-AA201-AB201-AC201-AD201', None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'спо', 'ЗО', 'Подъем НКТ  3 скорость', None, None, None, None, '73мм',
         '=(1121/110)*V202',
         '=IF(AND(L202/V202>=ЦИКЛ!$V$9,L202/V202<=ЦИКЛ!$W$9),ЦИКЛ!$U$9,IF(AND(L202/V202>=ЦИКЛ!$V$10,L202/V202<=ЦИКЛ!$W$10),ЦИКЛ!$U$10,IF(AND(L202/V202>=ЦИКЛ!$V$11,L202/V202<=ЦИКЛ!$W$11),ЦИКЛ!$U$11,IF(AND(L202/V202>=ЦИКЛ!$V$12,L202/V202<=ЦИКЛ!$W$12),ЦИКЛ!$U$12,IF(AND(L202/V202>=ЦИКЛ!$V$13,L202/V202<=ЦИКЛ!$W$13),ЦИКЛ!$U$13,IF(AND(L202/V202>=ЦИКЛ!$V$14,L202/V202<=ЦИКЛ!$W$14),ЦИКЛ!$U$14))))))',
         '=IF(AND(АВР!$AD$8=ЦИКЛ!$A$6,ЦИКЛ!$D$3=M202),ЦИКЛ!$J$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$6,ЦИКЛ!$E$3=M202),ЦИКЛ!$K$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$6,ЦИКЛ!$F$3=M202),ЦИКЛ!$L$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$6,ЦИКЛ!$G$3=M202),ЦИКЛ!$M$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$6,ЦИКЛ!$N$3=M202),ЦИКЛ!$H$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$6,ЦИКЛ!$I$3=M202),ЦИКЛ!$O$30,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$6,ЦИКЛ!$D$3=M202),ЦИКЛ!$J$30,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$6,ЦИКЛ!$E$3=M202),ЦИКЛ!$K$30,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$6,ЦИКЛ!$F$3=M202),ЦИКЛ!$L$30,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$6,ЦИКЛ!$G$3=M202),ЦИКЛ!$M$30,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$6,ЦИКЛ!$H$3=M202),ЦИКЛ!$N$30,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$6,ЦИКЛ!$I$3=M202),ЦИКЛ!$O$30,IF(AND(АВР!$AD$8=ЦИКЛ!$R$6,ЦИКЛ!$D$3=M202),ЦИКЛ!$J$30,IF(AND(АВР!$AD$8=ЦИКЛ!$R$6,ЦИКЛ!$E$3=M202),ЦИКЛ!$K$30,IF(AND(АВР!$AD$8=ЦИКЛ!$R$6,ЦИКЛ!$F$3=M202),ЦИКЛ!$L$30,IF(AND(АВР!$AD$8=ЦИКЛ!$R$6,ЦИКЛ!$G$3=M202),ЦИКЛ!$M$30,IF(AND(АВР!$AD$8=ЦИКЛ!$R$6,ЦИКЛ!$H$3=M202),ЦИКЛ!$N$30,IF(AND(АВР!$AD$8=ЦИКЛ!$R$6,ЦИКЛ!$I$3=M202),ЦИКЛ!$O$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$9,ЦИКЛ!$D$3=M202),ЦИКЛ!$J$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$9,ЦИКЛ!$E$3=M202),ЦИКЛ!$K$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$9,ЦИКЛ!$F$3=M202),ЦИКЛ!$L$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$9,ЦИКЛ!$G$3=M202),ЦИКЛ!$M$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$9,ЦИКЛ!$H$3=M202),ЦИКЛ!$N$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$9,ЦИКЛ!$I$3=M202),ЦИКЛ!$O$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$12,ЦИКЛ!$D$3=M202),ЦИКЛ!$J$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$12,ЦИКЛ!$E$3=M202),ЦИКЛ!$K$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$12,ЦИКЛ!$F$3=M202),ЦИКЛ!$L$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$12,ЦИКЛ!$G$3=M202),ЦИКЛ!$M$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$12,ЦИКЛ!$H$3=M202),ЦИКЛ!$N$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$12,ЦИКЛ!$I$3=M202),ЦИКЛ!$O$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$54,ЦИКЛ!$D$3=M202),ЦИКЛ!$J$62,IF(AND(АВР!$AD$8=ЦИКЛ!$A$54,ЦИКЛ!$E$3=M202),ЦИКЛ!$K$62,IF(AND(АВР!$AD$8=ЦИКЛ!$A$54,ЦИКЛ!$F$3=M202),ЦИКЛ!$L$62,IF(AND(АВР!$AD$8=ЦИКЛ!$A$54,ЦИКЛ!$G$3=M202),ЦИКЛ!$M$62,IF(AND(АВР!$AD$8=ЦИКЛ!$A$54,ЦИКЛ!$H$3=M202),ЦИКЛ!$N$62,IF(AND(АВР!$AD$8=ЦИКЛ!$A$54,ЦИКЛ!$I$3=M202),ЦИКЛ!$O$62,IF(AND(АВР!$AD$8=ЦИКЛ!$A$72,ЦИКЛ!$D$3=M202),ЦИКЛ!$J$80,IF(AND(АВР!$AD$8=ЦИКЛ!$A$72,ЦИКЛ!$E$3=M202),ЦИКЛ!$K$80,IF(AND(АВР!$AD$8=ЦИКЛ!$A$72,ЦИКЛ!$F$3=M202),ЦИКЛ!$L$80,IF(AND(АВР!$AD$8=ЦИКЛ!$A$72,ЦИКЛ!$G$3=M202),ЦИКЛ!$M$80,IF(AND(АВР!$AD$8=ЦИКЛ!$A$72,ЦИКЛ!$H$3=M202),ЦИКЛ!$N$80,IF(AND(АВР!$AD$8=ЦИКЛ!$A$72,ЦИКЛ!$I$3=M202),ЦИКЛ!$O$80,IF(AND(АВР!$AD$8=ЦИКЛ!$A$90,ЦИКЛ!$D$3=M202),ЦИКЛ!$J$98,IF(AND(АВР!$AD$8=ЦИКЛ!$A$90,ЦИКЛ!$E$3=M202),ЦИКЛ!$K$98,IF(AND(АВР!$AD$8=ЦИКЛ!$A$90,ЦИКЛ!$F$3=M202),ЦИКЛ!$L$98,IF(AND(АВР!$AD$8=ЦИКЛ!$A$90,ЦИКЛ!$G$3=M202),ЦИКЛ!$M$98,IF(AND(АВР!$AD$8=ЦИКЛ!$A$90,ЦИКЛ!$H$3=M202),ЦИКЛ!$N$98,IF(AND(АВР!$AD$8=ЦИКЛ!$A$90,ЦИКЛ!$I$3=M202),ЦИКЛ!$O$98,IF(AND(АВР!$AD$8=ЦИКЛ!$A$108,ЦИКЛ!$D$3=M202),ЦИКЛ!$J$118,IF(AND(АВР!$AD$8=ЦИКЛ!$A$108,ЦИКЛ!$E$3=M202),ЦИКЛ!$K$118,IF(AND(АВР!$AD$8=ЦИКЛ!$A$108,ЦИКЛ!$F$3=M202),ЦИКЛ!$L$118,IF(AND(АВР!$AD$8=ЦИКЛ!$A$108,ЦИКЛ!$G$3=M202),ЦИКЛ!$M$118,IF(AND(АВР!$AD$8=ЦИКЛ!$A$108,ЦИКЛ!$H$3=M202),ЦИКЛ!$N$118,IF(AND(АВР!$AD$8=ЦИКЛ!$A$108,ЦИКЛ!$I$3=M202),ЦИКЛ!$O$118,IF(AND(АВР!$AD$8=ЦИКЛ!$A$130,ЦИКЛ!$D$3=M202),ЦИКЛ!$J$140,IF(AND(АВР!$AD$8=ЦИКЛ!$A$130,ЦИКЛ!$E$3=M202),ЦИКЛ!$K$140,IF(AND(АВР!$AD$8=ЦИКЛ!$A$130,ЦИКЛ!$F$3=M202),ЦИКЛ!$L$140,IF(AND(АВР!$AD$8=ЦИКЛ!$A$130,ЦИКЛ!$G$3=M202),ЦИКЛ!$M$140,IF(AND(АВР!$AD$8=ЦИКЛ!$A$130,ЦИКЛ!$H$3=M202),ЦИКЛ!$N$140,IF(AND(АВР!$AD$8=ЦИКЛ!$A$130,ЦИКЛ!$I$3=M202),ЦИКЛ!$O$140))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))',
         None, None, None, None,
         '=IF($AD$8=ЦИКЛ!$A$4,ЦИКЛ!$P$4,IF($AD$8=ЦИКЛ!$A$7,ЦИКЛ!$P$7,IF($AD$8=ЦИКЛ!$A$10,ЦИКЛ!$P$7,IF($AD$8=ЦИКЛ!$A$52,ЦИКЛ!$P$52,IF($AD$8=ЦИКЛ!$A$70,ЦИКЛ!$P$70,IF($AD$8=ЦИКЛ!$A$88,ЦИКЛ!$P$88,IF($AD$8=ЦИКЛ!$A$106,ЦИКЛ!$P$106,IF($AD$8=ЦИКЛ!$A$133,ЦИКЛ!$P$133,IF($AD$8=ЦИКЛ!$Q$4,ЦИКЛ!$P$4,IF($AD$8=ЦИКЛ!$R$4,ЦИКЛ!$P$4))))))))))',
         None, 'шт', 120,
         '=IF(AND(АВР!$AD$8=ЦИКЛ!$A$6,ЦИКЛ!$D$3=M202,ЦИКЛ!$B$37=АВР!K202),ЦИКЛ!$D$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$6,ЦИКЛ!$E$3=M202,ЦИКЛ!$B$37=АВР!K202),ЦИКЛ!$E$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$6,ЦИКЛ!$F$3=M202,ЦИКЛ!$B$37=АВР!K202),ЦИКЛ!$F$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$6,ЦИКЛ!$G$3=M202,ЦИКЛ!$B$37=АВР!K202),ЦИКЛ!$G$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$6,ЦИКЛ!$H$3=M202,ЦИКЛ!$B$37=АВР!K202),ЦИКЛ!$H$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$6,ЦИКЛ!$I$3=M202,ЦИКЛ!$B$37=АВР!K202),ЦИКЛ!$I$30,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$6,ЦИКЛ!$D$3=M202,ЦИКЛ!$B$37=АВР!K202),ЦИКЛ!$D$30,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$6,ЦИКЛ!$E$3=M202,ЦИКЛ!$B$37=АВР!K202),ЦИКЛ!$E$30,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$6,ЦИКЛ!$F$3=M202,ЦИКЛ!$B$37=АВР!K202),ЦИКЛ!$F$30,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$6,ЦИКЛ!$G$3=M202,ЦИКЛ!$B$37=АВР!K202),ЦИКЛ!$G$30,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$6,ЦИКЛ!$H$3=M202,ЦИКЛ!$B$37=АВР!K202),ЦИКЛ!$H$30,IF(AND(АВР!$AD$8=ЦИКЛ!$Q$6,ЦИКЛ!$I$3=M202,ЦИКЛ!$B$37=АВР!K202),ЦИКЛ!$I$30,IF(AND(АВР!$AD$8=ЦИКЛ!$R$6,ЦИКЛ!$D$3=M202,ЦИКЛ!$B$37=АВР!K202),ЦИКЛ!$D$30,IF(AND(АВР!$AD$8=ЦИКЛ!$R$6,ЦИКЛ!$E$3=M202,ЦИКЛ!$B$37=АВР!K202),ЦИКЛ!$E$30,IF(AND(АВР!$AD$8=ЦИКЛ!$R$6,ЦИКЛ!$F$3=M202,ЦИКЛ!$B$37=АВР!K202),ЦИКЛ!$F$30,IF(AND(АВР!$AD$8=ЦИКЛ!$R$6,ЦИКЛ!$G$3=M202,ЦИКЛ!$B$37=АВР!K202),ЦИКЛ!$G$30,IF(AND(АВР!$AD$8=ЦИКЛ!$R$6,ЦИКЛ!$H$3=M202,ЦИКЛ!$B$37=АВР!K202),ЦИКЛ!$H$30,IF(AND(АВР!$AD$8=ЦИКЛ!$R$6,ЦИКЛ!$I$3=M202,ЦИКЛ!$B$37=АВР!K202),ЦИКЛ!$I$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$9,ЦИКЛ!$D$3=M202,ЦИКЛ!$B$37=АВР!K202),ЦИКЛ!$D$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$9,ЦИКЛ!$E$3=M202,ЦИКЛ!$B$37=АВР!K202),ЦИКЛ!$E$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$9,ЦИКЛ!$F$3=M202,ЦИКЛ!$B$37=АВР!K202),ЦИКЛ!$F$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$21,ЦИКЛ!$G$3=M202,ЦИКЛ!$B$37=АВР!K202),ЦИКЛ!$G$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$9,ЦИКЛ!$H$3=M202,ЦИКЛ!$B$37=АВР!K202),ЦИКЛ!$H$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$9,ЦИКЛ!$I$3=M202,ЦИКЛ!$B$37=АВР!K202),ЦИКЛ!$I$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$12,ЦИКЛ!$D$3=M202,ЦИКЛ!$B$37=АВР!K202),ЦИКЛ!$D$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$12,ЦИКЛ!$E$3=M202,ЦИКЛ!$B$37=АВР!K202),ЦИКЛ!$E$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$12,ЦИКЛ!$F$3=M202,ЦИКЛ!$B$37=АВР!K202),ЦИКЛ!$F$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$12,ЦИКЛ!$G$3=M202,ЦИКЛ!$B$37=АВР!K202),ЦИКЛ!$G$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$12,ЦИКЛ!$H$3=M202,ЦИКЛ!$B$37=АВР!K202),ЦИКЛ!$H$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$12,ЦИКЛ!$I$3=M202,ЦИКЛ!$B$37=АВР!K202),ЦИКЛ!$I$30,IF(AND(АВР!$AD$8=ЦИКЛ!$A$54,ЦИКЛ!$D$3=M202,ЦИКЛ!$B$37=АВР!K202),ЦИКЛ!$D$62,IF(AND(АВР!$AD$8=ЦИКЛ!$A$54,ЦИКЛ!$E$3=M202,ЦИКЛ!$B$37=АВР!K202),ЦИКЛ!$E$62,IF(AND(АВР!$AD$8=ЦИКЛ!$A$54,ЦИКЛ!$F$3=M202,ЦИКЛ!$B$37=АВР!K202),ЦИКЛ!$F$62,IF(AND(АВР!$AD$8=ЦИКЛ!$A$54,ЦИКЛ!$G$3=M202,ЦИКЛ!$B$37=АВР!K202),ЦИКЛ!$G$62,IF(AND(АВР!$AD$8=ЦИКЛ!$A$54,ЦИКЛ!$H$3=M202,ЦИКЛ!$B$37=АВР!K202),ЦИКЛ!$H$62,IF(AND(АВР!$AD$8=ЦИКЛ!$A$54,ЦИКЛ!$I$3=M202,ЦИКЛ!$B$37=АВР!K202),ЦИКЛ!$I$62,IF(AND(АВР!$AD$8=ЦИКЛ!$A$72,ЦИКЛ!$D$3=M202,ЦИКЛ!$B$37=АВР!K202),ЦИКЛ!$D$80,IF(AND(АВР!$AD$8=ЦИКЛ!$A$72,ЦИКЛ!$E$3=M202,ЦИКЛ!$B$37=АВР!K202),ЦИКЛ!$E$80,IF(AND(АВР!$AD$8=ЦИКЛ!$A$72,ЦИКЛ!$F$3=M202,ЦИКЛ!$B$37=АВР!K202),ЦИКЛ!$F$80,IF(AND(АВР!$AD$8=ЦИКЛ!$A$72,ЦИКЛ!$G$3=M202,ЦИКЛ!$B$37=АВР!K202),ЦИКЛ!$G$80,IF(AND(АВР!$AD$8=ЦИКЛ!$A$72,ЦИКЛ!$H$3=M202,ЦИКЛ!$B$37=АВР!K202),ЦИКЛ!$H$80,IF(AND(АВР!$AD$8=ЦИКЛ!$A$72,ЦИКЛ!$I$3=M202,ЦИКЛ!$B$37=АВР!K202),ЦИКЛ!$I$80,IF(AND(АВР!$AD$8=ЦИКЛ!$A$90,ЦИКЛ!$D$3=M202,ЦИКЛ!$B$37=АВР!K202),ЦИКЛ!$D$98,IF(AND(АВР!$AD$8=ЦИКЛ!$A$90,ЦИКЛ!$E$3=M202,ЦИКЛ!$B$37=АВР!K202),ЦИКЛ!$E$98,IF(AND(АВР!$AD$8=ЦИКЛ!$A$90,ЦИКЛ!$F$3=M202,ЦИКЛ!$B$37=АВР!K202),ЦИКЛ!$F$98,IF(AND(АВР!$AD$8=ЦИКЛ!$A$90,ЦИКЛ!$G$3=M202,ЦИКЛ!$B$37=АВР!K202),ЦИКЛ!$G$98,IF(AND(АВР!$AD$8=ЦИКЛ!$A$90,ЦИКЛ!$H$3=M202,ЦИКЛ!$B$37=АВР!K202),ЦИКЛ!$H$98,IF(AND(АВР!$AD$8=ЦИКЛ!$A$90,ЦИКЛ!$I$3=M202,ЦИКЛ!$B$37=АВР!K202),ЦИКЛ!$I$98,IF(AND(АВР!$AD$8=ЦИКЛ!$A$113,ЦИКЛ!$D$3=M202,ЦИКЛ!$B$37=АВР!K202),ЦИКЛ!$D$118,IF(AND(АВР!$AD$8=ЦИКЛ!$A$108,ЦИКЛ!$E$3=M202,ЦИКЛ!$B$37=АВР!K202),ЦИКЛ!$E$118,IF(AND(АВР!$AD$8=ЦИКЛ!$A$113,ЦИКЛ!$F$3=M202,ЦИКЛ!$B$37=АВР!K202),ЦИКЛ!$F$118,IF(AND(АВР!$AD$8=ЦИКЛ!$A$108,ЦИКЛ!$G$3=M202,ЦИКЛ!$B$37=АВР!K202),ЦИКЛ!$G$118,IF(AND(АВР!$AD$8=ЦИКЛ!$A$113,ЦИКЛ!$H$3=M202,ЦИКЛ!$B$37=АВР!K202),ЦИКЛ!$H$118,IF(AND(АВР!$AD$8=ЦИКЛ!$A$108,ЦИКЛ!$I$3=M202,ЦИКЛ!$B$37=АВР!K202),ЦИКЛ!$I$118,IF(AND(АВР!$AD$8=ЦИКЛ!$A$135,ЦИКЛ!$D$3=M202,ЦИКЛ!$B$37=АВР!K202),ЦИКЛ!$D$140,IF(AND(АВР!$AD$8=ЦИКЛ!$A$130,ЦИКЛ!$E$3=M202,ЦИКЛ!$B$37=АВР!K202),ЦИКЛ!$E$140,IF(AND(АВР!$AD$8=ЦИКЛ!$A$135,ЦИКЛ!$F$3=M202,ЦИКЛ!$B$37=АВР!K202),ЦИКЛ!$F$140,IF(AND(АВР!$AD$8=ЦИКЛ!$A$130,ЦИКЛ!$G$3=M202,ЦИКЛ!$B$37=АВР!K202),ЦИКЛ!$G$140,IF(AND(АВР!$AD$8=ЦИКЛ!$A$135,ЦИКЛ!$H$3=M202,ЦИКЛ!$B$37=АВР!K202),ЦИКЛ!$H$140,IF(AND(АВР!$AD$8=ЦИКЛ!$A$130,ЦИКЛ!$I$3=M202,ЦИКЛ!$B$37=АВР!K202),ЦИКЛ!$I$140))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))',
         1, '=V202*W202*X202', '=Y202-AA202-AB202-AC202-AD202', None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'спо', 'ЗО', 'Подъем НКТ  4 скорость', None, None, None, None, '73мм',
         '=(955/100)',
         '=IF(AND(L203/V203>=ЦИКЛ!$V$9,L203/V203<=ЦИКЛ!$W$9),ЦИКЛ!$U$9,IF(AND(L203/V203>=ЦИКЛ!$V$10,L203/V203<=ЦИКЛ!$W$10),ЦИКЛ!$U$10,IF(AND(L203/V203>=ЦИКЛ!$V$11,L203/V203<=ЦИКЛ!$W$11),ЦИКЛ!$U$11,IF(AND(L203/V203>=ЦИКЛ!$V$12,L203/V203<=ЦИКЛ!$W$12),ЦИКЛ!$U$12,IF(AND(L203/V203>=ЦИКЛ!$V$13,L203/V203<=ЦИКЛ!$W$13),ЦИКЛ!$U$13,IF(AND(L203/V203>=ЦИКЛ!$V$14,L203/V203<=ЦИКЛ!$W$14),ЦИКЛ!$U$14))))))',
         '=IF(AND(АВР!$AD$8=ЦИКЛ!$A$109,ЦИКЛ!$D$3=M203),ЦИКЛ!$J$119,IF(AND(АВР!$AD$8=ЦИКЛ!$A$109,ЦИКЛ!$E$3=M203),ЦИКЛ!$K$119,IF(AND(АВР!$AD$8=ЦИКЛ!$A$109,ЦИКЛ!$F$3=M203),ЦИКЛ!$L$119,IF(AND(АВР!$AD$8=ЦИКЛ!$A$109,ЦИКЛ!$G$3=M203),ЦИКЛ!$M$119,IF(AND(АВР!$AD$8=ЦИКЛ!$A$109,ЦИКЛ!$H$3=M203),ЦИКЛ!$N$119,IF(AND(АВР!$AD$8=ЦИКЛ!$A$109,ЦИКЛ!$I$3=M203),ЦИКЛ!$O$119,IF(AND(АВР!$AD$8=ЦИКЛ!$A$131,ЦИКЛ!$D$3=M203),ЦИКЛ!$J$141,IF(AND(АВР!$AD$8=ЦИКЛ!$A$131,ЦИКЛ!$E$3=M203),ЦИКЛ!$K$141,IF(AND(АВР!$AD$8=ЦИКЛ!$A$131,ЦИКЛ!$F$3=M203),ЦИКЛ!$L$141,IF(AND(АВР!$AD$8=ЦИКЛ!$A$131,ЦИКЛ!$G$3=M203),ЦИКЛ!$M$141,IF(AND(АВР!$AD$8=ЦИКЛ!$A$131,ЦИКЛ!$H$3=M203),ЦИКЛ!$N$141,IF(AND(АВР!$AD$8=ЦИКЛ!$A$131,ЦИКЛ!$I$3=M203),ЦИКЛ!$O$141))))))))))))',
         None, None, None, None,
         '=IF($AD$8=ЦИКЛ!$A$4,ЦИКЛ!$P$4,IF($AD$8=ЦИКЛ!$A$7,ЦИКЛ!$P$7,IF($AD$8=ЦИКЛ!$A$10,ЦИКЛ!$P$7,IF($AD$8=ЦИКЛ!$A$52,ЦИКЛ!$P$52,IF($AD$8=ЦИКЛ!$A$70,ЦИКЛ!$P$70,IF($AD$8=ЦИКЛ!$A$88,ЦИКЛ!$P$88,IF($AD$8=ЦИКЛ!$A$106,ЦИКЛ!$P$106,IF($AD$8=ЦИКЛ!$A$133,ЦИКЛ!$P$133,IF($AD$8=ЦИКЛ!$Q$4,ЦИКЛ!$P$4,IF($AD$8=ЦИКЛ!$R$4,ЦИКЛ!$P$4))))))))))',
         None, 'шт', 100,
         '=IF(AND(АВР!$AD$8=ЦИКЛ!$A$109,ЦИКЛ!$D$3=M203,ЦИКЛ!$B$37=АВР!K203),ЦИКЛ!$D$119,IF(AND(АВР!$AD$8=ЦИКЛ!$A$109,ЦИКЛ!$E$3=M203,ЦИКЛ!$B$37=АВР!K203),ЦИКЛ!$E$119,IF(AND(АВР!$AD$8=ЦИКЛ!$A$109,ЦИКЛ!$F$3=M203,ЦИКЛ!$B$37=АВР!K203),ЦИКЛ!$F$119,IF(AND(АВР!$AD$8=ЦИКЛ!$A$109,ЦИКЛ!$G$3=M203,ЦИКЛ!$B$37=АВР!K203),ЦИКЛ!$G$119,IF(AND(АВР!$AD$8=ЦИКЛ!$A$109,ЦИКЛ!$H$3=M203,ЦИКЛ!$B$37=АВР!K203),ЦИКЛ!$H$119,IF(AND(АВР!$AD$8=ЦИКЛ!$A$109,ЦИКЛ!$I$3=M203,ЦИКЛ!$B$37=АВР!K203),ЦИКЛ!$I$119,IF(AND(АВР!$AD$8=ЦИКЛ!$A$131,ЦИКЛ!$D$3=M203,ЦИКЛ!$B$37=АВР!K203),ЦИКЛ!$D$141,IF(AND(АВР!$AD$8=ЦИКЛ!$A$131,ЦИКЛ!$E$3=M203,ЦИКЛ!$B$37=АВР!K203),ЦИКЛ!$E$141,IF(AND(АВР!$AD$8=ЦИКЛ!$A$131,ЦИКЛ!$F$3=M203,ЦИКЛ!$B$37=АВР!K203),ЦИКЛ!$F$141,IF(AND(АВР!$AD$8=ЦИКЛ!$A$131,ЦИКЛ!$G$3=M203,ЦИКЛ!$B$37=АВР!K203),ЦИКЛ!$G$141,IF(AND(АВР!$AD$8=ЦИКЛ!$A$131,ЦИКЛ!$H$3=M203,ЦИКЛ!$B$37=АВР!K203),ЦИКЛ!$H$141,IF(AND(АВР!$AD$8=ЦИКЛ!$A$131,ЦИКЛ!$I$3=M203,ЦИКЛ!$B$37=АВР!K203),ЦИКЛ!$I$141))))))))))))',
         1, '=V203*W203*X203', '=Y203-AA203-AB203-AC203-AD203', None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'спо', 'ЗО', 'Долив скважины', None, None, None, None, None, None, None, None,
         None, None, None, None, '§168разд.1', None, 'шт', '=V205/10', 0.003, 1, '=V204*W204*X204',
         '=Y204-AA204-AB204-AC204-AD204', None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'спо', 'ЗО', 'Навернуть/отвернуть предохранительное кольцо', None, None, None,
         None, None, None, None, None, None, None, None, None, '§300разд.1', None, 'шт', '=SUM(V200:V202)', 0.003, 1,
         '=V205*W205*X205', '=Y205-AA205-AB205-AC205-AD205', None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'спо', 'ЗО', 'Осложнение при подъеме НКТ', None, None, None, None, None, None,
         'Объем', 0, None, None, None, None, 'факт', None, 'час', 0, 1, 1, '=V206*W206*X206',
         '=Y206-AA206-AB206-AC206-AD206', None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'спо', 'ЗО', 'Замер НКТ ', None, None, None, None, None, None, None, None,
         None, None, None, None, '§47разд.1', None, 'шт', '=V205', 0.008, 1, '=V207*W207*X207',
         '=Y207-AA207-AB207-AC207-AD207', None, None, None, None, None],
        ['=ROW()-ROW($A$46)', 'подъем 73мм', None, 'спо', 'ЗО', 'Откатывание труб с 201 трубы ', None, None, None, None,
         None, None, None, None, None, None, None, None, '§40разд.1', None, 'шт', '=V205-201', 0.008, 1,
         '=V208*W208*X208', '=Y208-AA208-AB208-AC208-AD208', None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None, 'Очистка от замазученности', None, None, None, None,
         None, None, None, None, 'АКТ№', None, None, None, 'факт', None, 'шт', 1, 0.67, 1, '=V209*W209*X209',
         '=Y209-AA209-AB209-AC209-AD209', None, None, None, None, None],
        ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None, 'Ревизия ГНО ', None, None, None, None, None, None,
         None, None, 'АКТ№', None, None, None, 'факт', None, 'час', 0.5, 1, 1, '=V210*W210*X210',
         '=Y210-AA210-AB210-AC210-AD210', None, None, None, None, None]]
