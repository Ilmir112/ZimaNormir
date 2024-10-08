import sys
from collections import namedtuple
from normir.files_with_list import cause_presence_of_downtime_list, cause_presence_of_downtime_classifocations_list, \
    operations_of_downtimes_list

from PyQt5.QtGui import QIntValidator, QDoubleValidator
from PyQt5.QtWidgets import QWidget, QLabel, QComboBox, QLineEdit, QGridLayout, QTabWidget, QMainWindow, QPushButton, \
    QMessageBox, QApplication, QHeaderView, QTableWidget, QTableWidgetItem, QTextEdit
from PyQt5.QtCore import Qt

import well_data

from normir.TabPageAll import TabPage, TemplateWork

class TabPage_SO_Earthwork(TabPage):
    def __init__(self, parent=None):
        super().__init__()



        self.earthwork_label = QLabel('Текст Копки шахты')
        self.earthwork_line = QLineEdit(self)

        self.earthwork_volume_label = QLabel('Объем земли')
        self.earthwork_volume_line = QLineEdit(self)
        self.earthwork_volume_line.setValidator(self.validator_float)

        self.opressovka_mkp_true_label = QLabel('Необходимость опрессовки МКП')
        self.opressovka_mkp_true_combo = QComboBox(self)
        self.opressovka_mkp_true_combo.addItems(['Нет', 'Да'])

        self.opressovka_mkp_text_label = QLabel('Текст опрессовки МКП')
        self.opressovka_mkp_text_line = QLineEdit(self)

        self.grid = QGridLayout(self)

        self.grid.addWidget(self.date_work_label, 4, 2)
        self.grid.addWidget(self.date_work_line, 5, 2)

        self.grid.addWidget(self.earthwork_label, 4, 3)
        self.grid.addWidget(self.earthwork_line, 5, 3)

        self.grid.addWidget(self.earthwork_volume_label, 4, 4)
        self.grid.addWidget(self.earthwork_volume_line, 5, 4)

        self.grid.addWidget(self.opressovka_mkp_true_label, 6, 2)
        self.grid.addWidget(self.opressovka_mkp_true_combo, 7, 2)
        self.grid.addWidget(self.opressovka_mkp_text_label, 6, 3)
        self.grid.addWidget(self.opressovka_mkp_text_line, 7, 3)


class TabWidget(QTabWidget):
    def __init__(self):
        super().__init__()
        self.addTab(TabPage_SO_Earthwork(self), 'Земляные работы')


class Earthwor_Window(TemplateWork):
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
        self.earthwork_line = None
        self.earthwork_volume_line = None


    def add_work(self):
        from main import MyWindow

        current_widget = self.tabWidget.currentWidget()

        self.opressovka_mkp_true_combo = current_widget.opressovka_mkp_true_combo.currentText()

        self.date_work_line = current_widget.date_work_line.text()
        self.earthwork_line = current_widget.earthwork_line.text()
        self.earthwork_volume_line = current_widget.earthwork_volume_line.text()
        if self.opressovka_mkp_true_combo == 'Да':
            self.opressovka_mkp_text_line = current_widget.opressovka_mkp_text_line.text()
        value_list = [self.date_work_line, self.earthwork_line, self.earthwork_volume_line]
        if '' in value_list:
            QMessageBox.warning(self, 'Ошибка', 'ВВедены не все значения')
            return
        well_data.date_work = self.date_work_line
        work_list = self.earthwork_def()

        self.populate_row(self.ins_ind, work_list, self.table_widget)
        well_data.pause = False
        self.close()

    def earthwork_def(self):

        relocation_list = [
            ['=ROW()-ROW($A$56)', self.date_work_line, None, 'Тех.операции', 'Земляные работы',
             self.earthwork_line, None, None, None, None, None, None, None,
             None, None, None, None, None, '§301разд.1', None, 'раз', self.earthwork_volume_line, 1.9, 1,
             '=V1137*W1137*X1137',
             '=Y1137-AA1137-AB1137-AC1137-AD1137', None, None, None, None, None]]
        if self.opressovka_mkp_true_combo == 'Да':
            opressovka_list = [
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'ПЗР перед опрессовкой ', None, None, None,
                 None, None, None, None, None, None, None, None, None, '§150/152 разд.1 ', None, 'шт', 1, 0.43, 1,
                 '=V541*W541*X541', '=Y541-AA541-AB541-AC541-AD541', None, None, None, None, None],
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, self.opressovka_mkp_text_line, None, None,
                 None, None, None, None, None, None, 'АКТ№', None, None, None, '§151 разд.1', None, 'шт', 1, 0.25, 1,
                 '=V542*W542*X542', '=Y542-AA542-AB542-AC542-AD542', None, None, None, None, None]]

            relocation_list.extend(opressovka_list)

        return relocation_list


if __name__ == "__main__":
    # app3 = QApplication(sys.argv)

    app = QApplication(sys.argv)
    window = Earthwor_Window(22, 22)
    window.show()
    sys.exit(app.exec_())
