import sys
from datetime import datetime, timedelta

import well_data

from normir.norms import LIFTING_NORM_SUCKER_POD
from PyQt5.QtGui import QIntValidator, QDoubleValidator
from PyQt5.QtWidgets import QWidget, QLabel, QComboBox, QLineEdit, QGridLayout, QTabWidget, QMainWindow, QPushButton, \
    QMessageBox, QApplication, QHeaderView, QTableWidget, QTableWidgetItem, QTextEdit, QDateTimeEdit

from normir.descent_gno import TabPage_SO_Lifting_gno


class TabPage_SO_Descent_Shgn(QWidget):
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

        self.lift_installation_combo.currentTextChanged.connect(TabPage_SO_Lifting_gno.update_lifting)

        self.complications_of_failure_label = QLabel('осложнения при срыве ПШ')
        self.complications_of_failure_combo = QComboBox(self)
        self.complications_of_failure_combo.addItems(['Нет', 'Да'])

        self.complications_during_disassembly_label = QLabel('осложнения при ')
        self.complications_during_disassembly_combo = QComboBox(self)
        self.complications_during_disassembly_combo.addItems(['Нет', 'Да'])

        self.complications_when_lifting_label = QLabel('Осложнения при спуске штанг')
        self.complications_when_lifting_combo = QComboBox(self)
        self.complications_when_lifting_combo.addItems(['Нет', 'Да'])

        self.grid.addWidget(self.complications_of_failure_label, 28, 1)
        self.grid.addWidget(self.complications_of_failure_combo, 29, 1)

        # self.grid.addWidget(self.complications_of_failure_label, 10, 1)
        # self.grid.addWidget(self.complications_of_failure_combo, 11, 1)

        self.grid.addWidget(self.complications_during_disassembly_label, 30, 1)
        self.grid.addWidget(self.complications_during_disassembly_combo, 31, 1)

        self.grid.addWidget(self.complications_when_lifting_label, 22, 1)
        self.grid.addWidget(self.complications_when_lifting_combo, 23, 1)

        self.complications_of_failure_label.setText('Рассхаживание')
        self.complications_during_disassembly_label.setText('Осложнения при монтаже')

        self.pressuar_gno_label = QLabel('Опрессовка ГНО')
        self.pressuar_gno_combo = QComboBox(self)
        self.pressuar_gno_combo.addItems(['Нет', 'Да'])

        # self.determination_of_the_weight_text_label = QLabel('Определение веса штанг')
        # self.determination_of_the_weight_text_line = QLineEdit(self)

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

        self.grid.addWidget(self.pressuar_gno_label, 26, 1)
        self.grid.addWidget(self.pressuar_gno_combo, 27, 1)

        # self.grid.addWidget(self.determination_of_the_weight_text_label, 6, 3)
        # self.grid.addWidget(self.determination_of_the_weight_text_line, 7, 3)

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
            self.pressuar_gno_text_line.setText('ПЗР. Опрессовка ГНО при Р-40атм (+)')
            self.grid.addWidget(self.pressuar_gno_text_label, 26, 2)
            self.grid.addWidget(self.pressuar_gno_text_line, 27, 2)

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
            self.grid.addWidget(self.complications_when_lifting_text_label, 22, 2)
            self.grid.addWidget(self.complications_when_lifting_text_line, 23, 2)

            self.grid.addWidget(self.complications_when_lifting_time_begin_label, 22, 3)
            self.grid.addWidget(self.complications_when_lifting_time_begin_date, 23, 3)

            self.grid.addWidget(self.complications_when_lifting_time_end_label, 22, 4)
            self.grid.addWidget(self.complications_when_lifting_time_end_date, 23, 4)

            self.grid.addWidget(self.complications_when_lifting_time_label, 22, 5)
            self.grid.addWidget(self.complications_when_lifting_time_line, 23, 5)

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
            self.grid.addWidget(self.complications_during_disassembly_q_label, 30, 2)
            self.grid.addWidget(self.complications_during_disassembly_q_line, 31, 2)

            self.grid.addWidget(self.complications_during_disassembly_q_time_begin_label, 30, 3)
            self.grid.addWidget(self.complications_during_disassembly_q_time_begin_date, 31, 3)

            self.grid.addWidget(self.complications_during_disassembly_q_time_begin_label, 30, 4)
            self.grid.addWidget(self.complications_during_disassembly_q_time_end_date, 31, 4)

            self.grid.addWidget(self.complications_during_disassembly_time_label, 30, 5)
            self.grid.addWidget(self.complications_during_disassembly_time_line, 31, 5)

            self.complications_during_disassembly_q_time_end_date.dateTimeChanged.connect(
                self.update_date_during_disassembly_q)
            self.complications_during_disassembly_q_time_begin_date.dateTimeChanged.connect(
                self.update_date_during_disassembly_q)


class TabWidget(QTabWidget):
    def __init__(self):
        super().__init__()
        self.addTab(TabPage_SO_Descent_Shgn(self), 'Спуск ШГН')


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
        # self.determination_of_the_weight_text_line = None
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
        self.type_equipment = 'Штанги'
        # self.determination_of_the_weight_text_line = current_widget.determination_of_the_weight_text_line.text()
        # if self.determination_of_the_weight_text_line == '':
        #     QMessageBox.warning(self, 'Ошибка', f'Не введены текст опрессовки ГНО')
        #     return
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
        self.lift_installation_combo = current_widget.lift_installation_combo.currentText()
        self.anchor_lifts_combo = current_widget.anchor_lifts_combo.currentText()
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

                self.complications_when_lifting_time_line = \
                    current_widget.complications_when_lifting_time_line.text()

                if self.complications_when_lifting_time_end_date == self.complications_when_lifting_time_begin_date:
                    QMessageBox.warning(self, 'Даты совпадают', 'Даты совпадают')
                    return

                if self.complications_when_lifting_text_line == '':
                    QMessageBox.warning(self, 'Ошибка', f'Не введены текст осложнения при спуске штанг')
                    return
                if self.complications_when_lifting_time_line == '':
                    QMessageBox.warning(self, 'Ошибка', f'Не введены время осложнения при спуске штанг')
                    return
                else:
                    aaa = self.complications_when_lifting_time_line
                    self.complications_when_lifting_time_line = round(float(self.complications_when_lifting_time_line),
                                                                      1)
                if self.complications_when_lifting_time_line <= 0:
                    QMessageBox.warning(self, 'Ошибка',
                                        f'Затраченное время при спуске штанг не может быть отрицательным')
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


        if len(self.dict_sucker_pod) == 0:
            question = QMessageBox.question(self, 'Ошибка', f'НКТ отсутствуют?')
            if question == QMessageBox.StandardButton.No:
                return

        work_list = self.descent_sucker_pod_work()

        well_data.date_work = self.date_work_line

        MyWindow.populate_row(self, self.ins_ind, work_list, self.table_widget)
        well_data.pause = False
        self.close()

    def change_string_in_date(self, date_str):
        # Преобразуем строку в объект datetime

        formatted_date = date_str.strftime("%d.%m.%Y %H:%M")
        return formatted_date

    def descent_sucker_pod_work(self):
        from normir.rod_head_work import LiftingRodHeadWindow
        from normir.descent_gno import DescentGnoWindow

        work_list = [
            ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None, 'Монтаж планшайбы на устье скважины', None, None,
             None, None, None, None, None, None, None, None, None, None, '§106разд.1', None, 'шт', 1, 0.37, 1,
             '=V1081*W1081*X1081', '=Y1081-AA1081-AB1081-AC1081-AD1081', None, None, None, None, None],

            ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None, 'Монтаж штангового превентора', None, None, None,
             None, None, None, None, None, None, None, None, None, '§120разд.1', None, 'шт', 1, 0.35, 1,
             '=V1083*W1083*X1083', '=Y1083-AA1083-AB1083-AC1083-AD1083', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None, 'Опрессовка ПШМ', None, None, None, None, None,
             None, None, None, None, None, None, None, '§112,разд.1', None, 'шт', 1, 0.62, 1, '=V1084*W1084*X1084',
             '=Y1084-AA1084-AB1084-AC1084-AD1084', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None, 'Устройство  рабочей площадки частично', None, None,
             None, None, None, None, None, None, None, None, None, None, '§55разд.1', None, 'шт', 1, 0.32, 1,
             '=V1085*W1085*X1085', '=Y1085-AA1085-AB1085-AC1085-AD1085', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', None, None, 'Тех.операции', None, 'Монтаж гидравлических ключей штанговых(ГШК-300)',
             None, None, None, None, None, None, None, None, None, None, None, None, '§184разд.1', None, 'шт', 1, 0.33,
             1, '=V1086*W1086*X1086', '=Y1086-AA1086-AB1086-AC1086-AD1086', None, None, None, None, None],
            ]

        work_list.extend(LiftingRodHeadWindow.descent_sucker_pod(self, self.dict_sucker_pod, self.type_equipment))

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
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, f'Подгонка НВ-32 (+)', None, None, None,
             None, None, None,
             None, None, 'АКТ№', None, None, None, 'факт', None, 'час', 0.5, 1, 1, '=V154*W154*X154',
             '=Y154-AA154-AB154-AC154-AD154', None, None, None, None, None],
            ['=ROW()-ROW($A$56)', None, None, 'Тех.операции', None, 'Монтаж СУСГ', None, None, None, None, None, None,
             None, None, None, None, None, None, '§199разд.1', None, 'шт', 1, 0.23, 1, '=V1096*W1096*X1096',
             '=Y1096-AA1096-AB1096-AC1096-AD1096', None, None, None, None, None],
            ['=ROW()-ROW($A$56)', None, None, 'Тех.операции', None,
             'Заполнить колонны труб водой для проверки работы глубинного насоса на 100м', None, None, None, None, None,
             None, None, None, None, None, None, None, '§202разд.1', None, 'м', '=M1064', 1, 1,
             '=ROUNDUP(SUM((V1097*0.00058)+0.06),2)', '=ROUNDUP(Y1097-AA1097-AB1097-AC1097-AD1097,2)', None, None, None,
             None, None],
            ['=ROW()-ROW($A$56)', None, None, 'Тех.операции', None, 'Набивка сальника', None, None, None, None, None,
             None,
             None, None, None, None, None, None, '§211разд.1', None, 'шт', 1, 0.48, 1, '=V1098*W1098*X1098',
             '=Y1098-AA1098-AB1098-AC1098-AD1098', None, None, None, None, None],
            ['=ROW()-ROW($A$56)', None, None, 'Тех.операции', None,
             'Одновременно подгонка полированного штока и проверка входа плунжера в насос ', None, None, None, None,
             None,
             None, None, None, None, None, None, None, '§206разд.1', None, 'шт', 1, 0.25, 1, '=V1099*W1099*X1099',
             '=Y1099-AA1099-AB1099-AC1099-AD1099', None, None, None, None, None],
            ['=ROW()-ROW($A$56)', None, None, 'Тех.операции', None, 'Вызов подачи (+)', None, None, None, None, None,
             None,
             None, None, 'АКТ№', None, None, None, '§200разд.1', None, 'шт', 1, 0.57, 1, '=V1100*W1100*X1100',
             '=Y1100-AA1100-AB1100-AC1100-AD1100', None, None, None, None, None],
            ['=ROW()-ROW($A$56)', None, None, 'Тех.операции', None, f'{self.pressuar_gno_text_line}', None, None,
             None, None, None, None, None, None, 'АКТ№', None, None, None, '§150-152разд.1', None, 'шт', 1, 0.67, 1,
             '=V1101*W1101*X1101', '=Y1101-AA1101-AB1101-AC1101-AD1101', None, None, None, None, None],
            ['=ROW()-ROW($A$56)', None, None, 'Тех.операции', None, 'Закидывание головки СКН', None, None, None, None,
             None, None, None, None, 'АКТ№', None, None, None, 'факт', None, 'час', 0.5, 1, 1, '=V1102*W1102*X1102',
             '=Y1102-AA1102-AB1102-AC1102-AD1102', None, None, None, None, None],
            ['=ROW()-ROW($A$56)', None, None, 'Тех.операции', None, 'Монтаж фонтанной арматуры (ШГН)', None, None, None,
             None, None, None, None, None, None, None, None, None, '§101разд.1', None, 'шт', 1, 0.67, 1,
             '=V1103*W1103*X1103', '=Y1103-AA1103-AB1103-AC1103-AD1103', None, None, None, None, None]
        ]

        work_list.extend(list_end)


        work_list.extend(DescentGnoWindow.dismantling_lifting(self))

        work_list.extend(DescentGnoWindow.finish_krs(self))




        return work_list


if __name__ == "__main__":
    # app3 = QApplication(sys.argv)

    app = QApplication(sys.argv)
    window = LiftingShgnWindow(22, 22)
    window.show()
    sys.exit(app.exec_())

