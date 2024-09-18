import sys
from datetime import datetime, timedelta

import well_data

from normir.norms import LIFTING_NORM_SUCKER_POD, DESCENT_NORM_SUCKER_POD
from PyQt5.QtGui import QIntValidator, QDoubleValidator
from PyQt5.QtWidgets import QWidget, QLabel, QComboBox, QLineEdit, QGridLayout, QTabWidget, QMainWindow, QPushButton, \
    QMessageBox, QApplication, QHeaderView, QTableWidget, QTableWidgetItem, QTextEdit, QDateTimeEdit

from normir.TabPageAll import TabPage, TemplateWork


class TabPage_SO_Lifting_Shgn(TabPage):
    def __init__(self, parent=None):
        super().__init__()

        self.grid = QGridLayout(self)

        self.grid.addWidget(self.date_work_label, 4, 2)
        self.grid.addWidget(self.date_work_line, 5, 2)

        self.actual_work_label = QLabel('Наличие работ при переезде')
        self.actual_work_combo = QComboBox(self)
        self.actual_work_combo.addItems(['Нет', 'Да'])
        self.actual_work_combo.currentTextChanged.connect(self.update_complications_of_failure)

        self.actual_work_combo.setCurrentIndex(1)

        self.grid.addWidget(self.actual_work_label, 14, 2)
        self.grid.addWidget(self.actual_work_combo, 15, 2)

    def update_date_actual_work(self):
        time_begin = self.actual_work_time_begin_date.dateTime()
        time_end = self.actual_work_time_end_date.dateTime()

        time_difference = self.calculate_date(time_begin, time_end)
        self.actual_work_time_line.setText(str(time_difference))


class TabWidget(QTabWidget):
    def __init__(self):
        super().__init__()
        self.addTab(TabPage_SO_Lifting_Shgn(self), '')


class ActualWork(TemplateWork):
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

    def add_work(self):

        current_widget = self.tabWidget.currentWidget()

        self.date_work_line = current_widget.date_work_line.text()

        self.actual_work_combo = current_widget.actual_work_combo.currentText()

        if self.actual_work_combo == 'Да':
            read_data = self.read_complications_of_failure(current_widget)
            if read_data is None:
                return

        work_list = []

        if self.actual_work_combo == 'Да':
            work_list.extend(self.actual_work_def())

        well_data.date_work = self.date_work_line

        self.populate_row(self.ins_ind, work_list, self.table_widget)
        well_data.pause = False
        self.close()

    def actual_work_def(self):
        work_list = [[
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
             f'{self.complications_of_failure_text_line} {self.complications_of_failure_time_begin_date}-'
             f'{self.complications_of_failure_time_end_date}', None, None, None, None, None, None, None, None,
             'АКТ№', None, None, None, 'факт', None, 'час', self.complications_of_failure_time_line - 0.15, 1, 1,
             '=V138*W138*X138', '=Y138-AA138-AB138-AC138-AD138',
             None, None, None, None, None]]]
        return work_list


if __name__ == "__main__":
    # app3 = QApplication(sys.argv)

    app = QApplication(sys.argv)
    window = ActualWork(22, 22)
    window.show()
    sys.exit(app.exec_())
