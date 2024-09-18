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

        self.presence_of_downtime_label = QLabel('Наличие простоя')
        self.presence_of_downtime_combo = QComboBox(self)
        self.presence_of_downtime_combo.addItems(['Нет', 'Да'])
        self.presence_of_downtime_combo.currentTextChanged.connect(self.update_presence_of_downtime_combo)

        self.presence_of_downtime_combo.setCurrentIndex(1)

        self.grid.addWidget(self.presence_of_downtime_label, 14, 2)
        self.grid.addWidget(self.presence_of_downtime_combo, 15, 2)

    def update_date_presence_of_downtime(self):
        time_begin = self.presence_of_downtime_time_begin_date.dateTime()
        time_end = self.presence_of_downtime_time_end_date.dateTime()

        time_difference = self.calculate_date(time_begin, time_end)
        self.presence_of_downtime_time_line.setText(str(time_difference))


class TabWidget(QTabWidget):
    def __init__(self):
        super().__init__()
        self.addTab(TabPage_SO_Lifting_Shgn(self), 'СПО штанголовки')


class SimpleWork(TemplateWork):
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

        self.presence_of_downtime_combo = current_widget.presence_of_downtime_combo.currentText()

        if self.presence_of_downtime_combo == 'Да':
            self.read_presence_of_downtime(current_widget)

        work_list = []

        if self.presence_of_downtime_combo == 'Да':
            work_list.extend(self.presence_of_downtime_def())

        well_data.date_work = self.date_work_line

        self.populate_row(self.ins_ind, work_list, self.table_widget)
        well_data.pause = False
        self.close()


if __name__ == "__main__":
    # app3 = QApplication(sys.argv)

    app = QApplication(sys.argv)
    window = SimpleWork(22, 22)
    window.show()
    sys.exit(app.exec_())
