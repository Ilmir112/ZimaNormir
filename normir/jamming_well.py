from datetime import datetime
import sys

import well_data
from normir.files_with_list import cause_presence_of_jamming, cause_discharge_list, count_jamming_list, \
    contractor_zhgs_list, technological_expectation_list, cause_jamming_first_list, cause_jamming_second_list, \
    cause_jamming_three_list

from PyQt5.QtGui import QIntValidator, QDoubleValidator
from PyQt5.QtWidgets import QWidget, QLabel, QComboBox, QLineEdit, QGridLayout, QTabWidget, QMainWindow, QPushButton, \
    QMessageBox, QApplication, QHeaderView, QTableWidget, QTableWidgetItem, QTextEdit, QDateTimeEdit

from normir.lifting_gno import TabPage_SO_Lifting_gno, LiftingWindow


class TabPage_SO_Jamming(QWidget):

    def __init__(self, parent=None):
        super().__init__()

        self.validator_int = QIntValidator(0, 600)
        self.validator_float = QDoubleValidator(0.2, 1000, 1)

        self.date_work_label = QLabel('Дата работы')
        self.date_work_line = QLineEdit(self)
        self.date_work_line.setText(f'{well_data.date_work}')

        self.date_work_str = datetime.strptime(self.date_work_line.text(), '%d.%m.%Y')


        self.count_jamming_label = QLabel("Счет глушения", self)
        self.count_jamming_combo = QComboBox(self)

        self.count_jamming_combo.addItems(count_jamming_list)

        self.grid = QGridLayout(self)

        if well_data.date_work != '':
            self.date_work_line.setText(well_data.date_work)

        self.grid.addWidget(self.date_work_label, 4, 2)
        self.grid.addWidget(self.date_work_line, 5, 2)

        self.grid.addWidget(self.count_jamming_label, 4, 3)
        self.grid.addWidget(self.count_jamming_combo, 5, 3)

        self.count_jamming_combo.currentTextChanged.connect(self.update_select_gno)

    def update_select_gno(self, index):

        if index in ['1ый подход глушения', '2ой подход глушения', '3ий подход глушения']:

            self.need_well_discharge_label = QLabel('Была разрядка ли?')
            self.need_well_discharge_combo = QComboBox(self)
            self.need_well_discharge_combo.addItems(['Нет', 'Да'])

            self.volume_jamming_label = QLabel('Объем глушения')
            self.volume_jamming_line = QLineEdit(self)
            self.volume_jamming_line.setValidator(self.validator_float)

            self.fluid_well_label = QLabel('удельный вес')
            self.fluid_well_line = QLineEdit(self)
            self.fluid_well_line.setText(f"{str(well_data.fluid_work)[:4]}")

            self.time_work_label = QLabel('Время работ')
            self.time_work_line = QLineEdit(self)
            self.time_work_line.setValidator(self.validator_float)

            self.source_of_work_label = QLabel('Источник работ')
            self.source_of_work_combo = QComboBox(self)
            self.source_of_work_combo.addItems(contractor_zhgs_list)

            self.cause_of_work_label = QLabel('Причины глушения')
            self.cause_of_work_combo = QComboBox(self)
            if index == '1ый подход глушения':
                self.cause_of_work_combo.addItems(cause_jamming_first_list)
            elif index == '2ой подход глушения':
                self.cause_of_work_combo.addItems(cause_jamming_second_list)
            elif index == '3ий подход глушения':
                self.cause_of_work_combo.addItems(cause_jamming_three_list)


            self.expectation_label = QLabel('технологическое ожидание')
            self.expectation_combo = QComboBox(self)
            self.expectation_combo.addItems(technological_expectation_list)
            self.expectation_combo.setCurrentIndex(5)

            self.grid.addWidget(self.need_well_discharge_label, 6, 1)
            self.grid.addWidget(self.need_well_discharge_combo, 7, 1)

            self.grid.addWidget(self.expectation_label, 10, 1)
            self.grid.addWidget(self.expectation_combo, 11, 1)
            self.grid.addWidget(self.volume_jamming_label, 10, 2)
            self.grid.addWidget(self.volume_jamming_line, 11, 2)
            self.grid.addWidget(self.fluid_well_label, 10, 3)
            self.grid.addWidget(self.fluid_well_line, 11, 3)
            self.grid.addWidget(self.time_work_label, 10, 4)
            self.grid.addWidget(self.time_work_line, 11, 4)
            self.grid.addWidget(self.source_of_work_label, 10, 5)
            self.grid.addWidget(self.source_of_work_combo, 11, 5)
            self.grid.addWidget(self.cause_of_work_label, 10, 6)
            self.grid.addWidget(self.cause_of_work_combo, 11, 6)

        else:
            self.need_well_discharge_label.setParent(None)
            self.need_well_discharge_combo.setParent(None)

        self.need_well_discharge_combo.currentTextChanged.connect(
            self.update_need_well_discharge_combo)

    def update_need_well_discharge_combo(self, index):
        if index == 'Нет':
            self.need_well_discharge_more_label.setParent(None)
            self.need_well_discharge_more_combo.setParent(None)

            self.need_well_discharge_more_text_label.setParent(None)
            self.need_well_discharge_more_text_line.setParent(None)

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

            self.time_well_discharge_begin_label = QLabel('начало демонтажа')
            self.time_well_discharge_begin_date = QDateTimeEdit(self)
            self.time_well_discharge_begin_date.setDisplayFormat("dd.MM.yyyy HH:mm")
            self.time_well_discharge_begin_date.setDateTime(self.date_work_str)

            self.time_well_discharge_end_label = QLabel('Окончание демонтажа')
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

            self.grid.addWidget(self.volume_well_discharge_label, 6, 2)
            self.grid.addWidget(self.volume_well_discharge_line, 7, 2)
            self.grid.addWidget(self.time_well_discharge_begin_label, 6, 3)
            self.grid.addWidget(self.time_well_discharge_begin_date, 7, 3)
            self.grid.addWidget(self.time_well_discharge_end_label, 6, 4)
            self.grid.addWidget(self.time_well_discharge_end_date, 7, 4)
            self.grid.addWidget(self.time_well_discharge_label, 6, 5)
            self.grid.addWidget(self.time_well_discharge_line, 7, 5)
            self.grid.addWidget(self.cause_discharge_label, 6, 6)
            self.grid.addWidget(self.cause_discharge_combo, 7, 6)
            self.grid.addWidget(self.need_well_discharge_more_label, 8, 1)
            self.grid.addWidget(self.need_well_discharge_more_combo, 9, 1)

            self.need_well_discharge_more_combo.currentTextChanged.connect(self.update_need_well_discharge_more_combo)

            self.time_well_discharge_begin_date.dateTimeChanged.connect(
                self.update_time_well_discharge_time)
            self.time_well_discharge_end_date.dateTimeChanged.connect(
                self.update_time_well_discharge_time)


    def update_time_well_discharge_time(self):

        time_end = self.time_well_discharge_end_date.dateTime()
        time_begin = self.time_well_discharge_begin_date.dateTime()

        time_difference = TabPage_SO_Lifting_gno.calculate_date(self, time_begin, time_end)
        self.time_well_discharge_line.setText(str(time_difference))
        if float(self.time_well_discharge_line.text()) > 2:
            self.need_well_discharge_more_combo.setCurrentIndex(1)
        else:
            self.need_well_discharge_more_combo.setCurrentIndex(0)
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

            self.grid.addWidget(self.need_well_discharge_more_text_label, 8, 2, 1, 2)
            self.grid.addWidget(self.need_well_discharge_more_text_line, 9, 2, 1, 2)

            self.grid.addWidget(self.cause_discharge_more_label, 8, 4)
            self.grid.addWidget(self.cause_discharge_more_combo, 9, 4)


class TabWidget(QTabWidget):
    def __init__(self):
        super().__init__()
        self.addTab(TabPage_SO_Jamming(self), 'Глушение ')


class JammingWindow(QMainWindow):

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
        self.need_well_discharge_more_text_line = None
        self.cause_discharge_combo = None
        self.expectation_combo = None
        self.volume_jamming_line = None
        self.volume_well_discharge_line = ''
        self.complications_during_disassembly_text_line = None
        self.complications_during_disassembly_time_line = None
        self.fluid_well_line = None
        self.time_work_line = None
        self.source_of_work_combo = None
        self.cause_of_work_combo = None
        self.time_well_discharge_line = None
        self.volume_well_discharge_more_line = None
        self.time_well_discharge_more_line = None

        self.time_well_discharge_end_date = None

        self.time_well_discharge_begin_date = None

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

        self.count_jamming_combo = current_widget.count_jamming_combo.currentText()
        self.need_well_discharge_combo = current_widget.need_well_discharge_combo.currentText()

        self.need_well_discharge_combo = current_widget.need_well_discharge_combo.currentText()


        self.date_work_line = current_widget.date_work_line.text()
        self.volume_jamming_line = current_widget.volume_jamming_line.text()
        self.fluid_well_line = current_widget.fluid_well_line.text()
        self.time_work_line = current_widget.time_work_line.text()

        self.cause_of_work_combo = current_widget.cause_of_work_combo.currentText()
        self.expectation_combo = current_widget.expectation_combo.currentText()
        work_list = []
        if self.need_well_discharge_combo == 'Да':
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
               LiftingWindow.change_string_in_date(self.time_well_discharge_end_date)

            self.time_well_discharge_begin_date = current_widget.time_well_discharge_begin_date.dateTime().toPyDateTime()

            self.time_well_discharge_begin_date = \
                LiftingWindow.change_string_in_date(self.time_well_discharge_begin_date)


            if self.time_well_discharge_line != '':
                self.time_well_discharge_line = round(float(self.time_well_discharge_line), 1)

            else:
                QMessageBox.warning(self, 'Ошибка', f'Не введены время разрядки')
                return

            if self.time_well_discharge_line <= 0:
                QMessageBox.warning(self, 'Ошибка', f'Затраченное время разрядки не может быть отрицательным или равным нулю')
                return


            work_list.append(self.well_discharge())
            if self.need_well_discharge_more_combo == 'Да':
                try:
                    self.need_well_discharge_more_text_line = current_widget.need_well_discharge_more_text_line.text()
                    self.cause_discharge_more_combo = current_widget.cause_discharge_more_combo.currentText()
                    self.volume_well_discharge_more_line = self.volume_well_discharge_line

                    self.time_well_discharge_more_line = self.time_well_discharge_line - 2.00


                    work_list.extend(self.well_discharge_more())
                except Exception as e:
                    QMessageBox.warning(self, 'Ошибка', f'ВВедены не все значения {e}')
                    return

        if self.count_jamming_combo in ['1ый подход глушения', '2ой подход глушения', '3ий подход глушения']:
            work_list.extend(self.jamming_well_work())

        well_data.date_work = self.date_work_line

        MyWindow.populate_row(self, self.ins_ind, work_list, self.table_widget)
        well_data.pause = False
        self.close()

    def well_discharge(self):

        work_list = [
            '=ROW()-ROW($A$46)', None, None, 'Разрядка', None, 'Разрядка скважины ', None, None, None, 'Объем',
            self.volume_well_discharge_line,
            'причины рязрядки:', self.cause_discharge_combo, None, "'АКТ №1'!A1", None, None, None, '§205разд.1',
            None, 'час', self.time_well_discharge_line_2, 1, 1, '=V118*W118*X118', '=Y118-AA118-AB118-AC118-AD118',
            None,  None, None, None, None]

        return work_list

    def well_discharge_more(self):
        work_list = [
            ['=ROW()-ROW($A$46)', None, None, 'Разрядка', None, f'{self.need_well_discharge_more_text_line} '
                                                                f'{self.time_well_discharge_begin_date}-'
                                                                f'{self.time_well_discharge_end_date}', None, None,
             None, 'Объем',
             self.volume_well_discharge_more_line, 'причины рязрядки:', self.cause_discharge_more_combo,
             None, 'АКТ№', None, None, None, 'факт',
             None, 'час', self.time_well_discharge_more_line - 2, 1, 1,
             '=V121*W121*X121', '=Y121-AA121-AB121-AC121-AD121', None, None, None, None, None]]
        return work_list

    def jamming_well_work(self):
        work_list = [
            ['=ROW()-ROW($A$46)', None, None, 'Глушение', self.count_jamming_combo, 'ПЗР к глушению ', None, None,
             'источник ЖГ:', self.source_of_work_combo, None, None, None, None, "'АКТ №1'!A1", None, None, None,
             '§3разд.1',
             self.expectation_combo, 'раз', 1, 0.9, 1, '=V123*W123*X123', '=Y123-AA123-AB123-AC123-AD123', None,
             None, None, None, None],
            ['=ROW()-ROW($A$46)', None, None, 'Глушение', self.count_jamming_combo,
             f'Смена объема 1 цикл {self.volume_jamming_line}м3 {self.fluid_well_line}г/см3',
             None, None, None, None, 1.02, 'причины глушения:',
             self.cause_of_work_combo, None, 'АКТ №6', None,
             None, None, '§3разд.1', self.expectation_combo, 'м3', self.volume_jamming_line, 0.08, 1, '=V124*W124*X124',
             '=Y124-AA124-AB124-AC124-AD124', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', None, None, 'Глушение', self.count_jamming_combo, 'Стабилизация', None, None, None, None,
             None, None, None, None, "'АКТ №1'!A1", None, None, None, 'Простои', 'Тех. ожидание', 'раз', 1, 2, 1,
             '=V125*W125*X125', '=Y125-AA125-AB125-AC125-AD125', None, None, None, None, None]]

        return work_list


if __name__ == "__main__":
    # app3 = QApplication(sys.argv)

    app = QApplication(sys.argv)
    window = JammingWindow(22, 22)
    window.show()
    sys.exit(app.exec_())
