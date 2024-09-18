from datetime import datetime
import sys
import re

from PyQt5.QtCore import QDate

import well_data
from normir.files_with_list import cause_presence_of_jamming, cause_discharge_list, count_jamming_list, \
    contractor_zhgs_list, technological_expectation_list, cause_jamming_first_list, cause_jamming_second_list, \
    cause_jamming_three_list

from PyQt5.QtGui import QIntValidator, QDoubleValidator
from PyQt5.QtWidgets import QWidget, QLabel, QComboBox, QLineEdit, QGridLayout, QTabWidget, QMainWindow, QPushButton, \
    QMessageBox, QApplication, QHeaderView, QTableWidget, QTableWidgetItem, QTextEdit, QDateTimeEdit

from normir.lifting_gno import TabPage_SO_Lifting_gno, LiftingWindow

from normir.TabPageAll import TabPage, TemplateWork


class TabPage_SO_Jamming(TabPage):

    def __init__(self, parent=None):
        super().__init__()

        self.validator_int = QIntValidator(0, 600)
        self.validator_float = QDoubleValidator(0.2, 1000, 1)

        self.count_jamming_label = QLabel("Счет глушения", self)
        self.count_jamming_combo = QComboBox(self)

        self.count_jamming_combo.addItems(count_jamming_list)

        self.grid = QGridLayout(self)

        self.grid.addWidget(self.date_work_label, 4, 2)
        self.grid.addWidget(self.date_work_line, 5, 2)

        self.grid.addWidget(self.count_jamming_label, 4, 3)
        self.grid.addWidget(self.count_jamming_combo, 5, 3)

        self.count_jamming_combo.currentTextChanged.connect(self.update_select_gno)

    def update_select_gno(self, index):

        if index in ['1ый подход глушения', '2ой подход глушения', '3ий подход глушения']:

            self.determination_of_pickup_sko_combo_label = QLabel('Было ли определение Q перед Разрядкой')
            self.determination_of_pickup_sko_combo = QComboBox(self)
            self.determination_of_pickup_sko_combo.addItems(['Нет', 'Да'])

            self.grid.addWidget(self.determination_of_pickup_sko_combo_label, 6, 1)
            self.grid.addWidget(self.determination_of_pickup_sko_combo, 7, 1)

            self.determination_of_pickup_sko_combo.currentTextChanged.connect(
                self.update_determination_of_pickup_sko_combo)

            self.need_well_discharge_label = QLabel('Была ли разрядка ли до глушения?')
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

            self.need_well_discharge_after_label = QLabel('Была ли разрядка ли после глушения?')
            self.need_well_discharge_after_combo = QComboBox(self)
            self.need_well_discharge_after_combo.addItems(['Нет', 'Да'])

            self.grid.addWidget(self.need_well_discharge_label, 16, 1)
            self.grid.addWidget(self.need_well_discharge_combo, 17, 1)

            self.grid.addWidget(self.need_well_discharge_after_label, 26, 1)
            self.grid.addWidget(self.need_well_discharge_after_combo, 27, 1)

            self.grid.addWidget(self.expectation_label, 20, 1)
            self.grid.addWidget(self.expectation_combo, 21, 1)
            self.grid.addWidget(self.volume_jamming_label, 20, 2)
            self.grid.addWidget(self.volume_jamming_line, 21, 2)
            self.grid.addWidget(self.fluid_well_label, 20, 3)
            self.grid.addWidget(self.fluid_well_line, 21, 3)
            self.grid.addWidget(self.time_work_label, 20, 4)
            self.grid.addWidget(self.time_work_line, 21, 4)
            self.grid.addWidget(self.source_of_work_label, 20, 5)
            self.grid.addWidget(self.source_of_work_combo, 21, 5)
            self.grid.addWidget(self.cause_of_work_label, 20, 6)
            self.grid.addWidget(self.cause_of_work_combo, 21, 6)

        else:
            self.need_well_discharge_label.setParent(None)
            self.need_well_discharge_combo.setParent(None)

        self.need_well_discharge_after_combo.currentTextChanged.connect(
            self.update_need_well_discharge_after_combo)

        self.need_well_discharge_combo.currentTextChanged.connect(
            self.update_need_well_discharge_combo)

        self.insert_date_in_ois()

    def update_time_well_discharge_time(self):

        time_end = self.time_well_discharge_end_date.dateTime()
        time_begin = self.time_well_discharge_begin_date.dateTime()

        time_difference = self.calculate_date(time_begin, time_end)
        self.time_well_discharge_line.setText(str(time_difference))
        if float(self.time_well_discharge_line.text()) > 2:
            self.need_well_discharge_more_combo.setCurrentIndex(1)
        else:
            self.need_well_discharge_more_combo.setCurrentIndex(0)

    def update_time_well_discharge_after_time(self):

        time_end = self.time_well_discharge_end_after_date.dateTime()
        time_begin = self.time_well_discharge_begin_after_date.dateTime()

        time_difference = self.calculate_date(time_begin, time_end)
        self.time_well_discharge_after_line.setText(str(time_difference))
        if float(self.time_well_discharge_after_line.text()) > 2:
            self.need_well_discharge_more_after_combo.setCurrentIndex(1)
        else:
            self.need_well_discharge_more_after_combo.setCurrentIndex(0)

    def insert_date_in_ois(self):
        for datа_day, data_work, _, _ in well_data.work_list_in_ois[1:]:

            day, month, year = list(map(int, datа_day.split('\n')[0].split('.')))
            day1, month1, year1 = list(map(int, well_data.date_work.split('.')))
            input_date = QDate(year1, month1, day1 + 3)
            comparison_date = QDate(year, month, day)
            if input_date >= comparison_date:
                if 'разрядка' in data_work.lower():
                    self.need_well_discharge_combo.setCurrentIndex(1)
                    self.need_well_discharge_after_combo.setCurrentIndex(1)
                elif 'насыщение' in data_work.lower():
                    self.determination_of_pickup_sko_combo.setCurrentIndex(1)


class TabWidget(QTabWidget):
    def __init__(self):
        super().__init__()
        self.addTab(TabPage_SO_Jamming(self), 'Глушение ')


class JammingWindow(TemplateWork):

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

    def add_work(self):
        from main import MyWindow

        current_widget = self.tabWidget.currentWidget()

        self.count_jamming_combo = current_widget.count_jamming_combo.currentText()
        self.need_well_discharge_combo = current_widget.need_well_discharge_combo.currentText()
        self.need_well_discharge_after_combo = current_widget.need_well_discharge_after_combo.currentText()

        self.date_work_line = current_widget.date_work_line.text()
        self.volume_jamming_line = current_widget.volume_jamming_line.text()
        self.fluid_well_line = current_widget.fluid_well_line.text()
        self.time_work_line = current_widget.time_work_line.text()
        self.determination_of_pickup_sko_combo = current_widget.determination_of_pickup_sko_combo.currentText()
        if self.determination_of_pickup_sko_combo == 'Да':
            read_data = self.read_determination_of_pickup_sko_combo(current_widget)
            if read_data is None:
                re

        self.cause_of_work_combo = current_widget.cause_of_work_combo.currentText()
        self.expectation_combo = current_widget.expectation_combo.currentText()
        work_list = []
        if self.determination_of_pickup_sko_combo == 'Да':
            work_list.extend(self.determination_of_pickup_work(
                self.saturation_volume_sko_line, self.determination_of_pickup_sko_text_line))
        if self.need_well_discharge_combo == 'Да':
            self.read_need_well_discharge_combo(current_widget)

            work_list.append(self.well_discharge(self.volume_well_discharge_line,
                                                 self.cause_discharge_combo, self.time_well_discharge_line_2))
            if self.need_well_discharge_more_combo == 'Да':
                work_list.extend(self.well_discharge_more(self.need_well_discharge_more_text_line,
                                                          self.time_well_discharge_begin_date,
                                                          self.time_well_discharge_end_date,
                                                          self.volume_well_discharge_more_line,
                                                          self.cause_discharge_more_combo,
                                                          self.time_well_discharge_more_line))

        if self.count_jamming_combo in ['1ый подход глушения', '2ой подход глушения', '3ий подход глушения']:
            work_list.extend(self.jamming_well_work())

        if self.need_well_discharge_after_combo == 'Да':
            self.read_need_well_discharge_after_combo(current_widget)

            work_list.append(self.well_discharge(self.volume_well_discharge_after_line,
                                                 self.cause_discharge_after_combo, self.time_well_discharge_after_line_2))
            if self.need_well_discharge_more_after_combo == 'Да':
                work_list.extend(self.well_discharge_more(
                    self.need_well_discharge_more_text_after_line,
                    self.time_well_discharge_begin_after_date,
                    self.time_well_discharge_end_after_date, self.volume_well_discharge_more_after_line,
                    self.cause_discharge_more_after_combo,
                    self.time_well_discharge_more_after_line))

        well_data.date_work = self.date_work_line

        self.populate_row(self.ins_ind, work_list, self.table_widget)
        well_data.pause = False
        self.close()

    def well_discharge(self, volume_well_discharge_line, cause_discharge_combo, time_well_discharge_line_2):

        work_list = [
            '=ROW()-ROW($A$46)', self.date_work_line, None, 'Разрядка', None, 'Разрядка скважины ', None, None, None, 'Объем',
            volume_well_discharge_line,
            'причины рязрядки:', cause_discharge_combo, None, "'АКТ №1'!A1", None, None, None, '§205разд.1',
            None, 'час', time_well_discharge_line_2, 1, 1, '=V118*W118*X118', '=Y118-AA118-AB118-AC118-AD118',
            None, None, None, None, None]

        return work_list

    def well_discharge_more(self,
                            need_well_discharge_more_text_line, time_well_discharge_begin_date,
                            time_well_discharge_end_date, volume_well_discharge_more_line, cause_discharge_more_combo,
                            time_well_discharge_more_line):
        work_list = [
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Разрядка', None, f'{need_well_discharge_more_text_line} '
                                                                f'{time_well_discharge_begin_date}-'
                                                                f'{time_well_discharge_end_date}', None, None,
             None, 'Объем',
             volume_well_discharge_more_line, 'причины рязрядки:', cause_discharge_more_combo,
             None, 'АКТ№', None, None, None, 'факт',
             None, 'час', time_well_discharge_more_line - 2, 1, 1,
             '=V121*W121*X121', '=Y121-AA121-AB121-AC121-AD121', None, None, None, None, None]]
        return work_list

    def jamming_well_work(self):
        work_list = [
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Глушение', self.count_jamming_combo, 'ПЗР к глушению ', None, None,
             'источник ЖГ:', self.source_of_work_combo, None, None, None, None, "'АКТ №1'!A1", None, None, None,
             '§3разд.1',
             self.expectation_combo, 'раз', 1, 0.9, 1, '=V123*W123*X123', '=Y123-AA123-AB123-AC123-AD123', None,
             None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Глушение', self.count_jamming_combo,
             f'Смена объема 1 цикл {self.volume_jamming_line}м3 {self.fluid_well_line}г/см3',
             None, None, None, None, 1.02, 'причины глушения:',
             self.cause_of_work_combo, None, 'АКТ №6', None,
             None, None, '§3разд.1', self.expectation_combo, 'м3', self.volume_jamming_line, 0.08, 1, '=V124*W124*X124',
             '=Y124-AA124-AB124-AC124-AD124', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Глушение', self.count_jamming_combo, 'Стабилизация',
             None, None, None,
             None,
             None, None, None, None, "'АКТ №1'!A1", None, None, None, 'Простои', 'Тех. ожидание', 'раз', 1, 2, 1,
             '=V125*W125*X125', '=Y125-AA125-AB125-AC125-AD125', None, None, None, None, None]]

        return work_list


if __name__ == "__main__":
    # app3 = QApplication(sys.argv)

    app = QApplication(sys.argv)
    window = JammingWindow(22, 22)
    window.show()
    sys.exit(app.exec_())
