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

        self.loading_work_label = QLabel('Вид оборудования')
        self.loading_work_combo = QComboBox(self)
        self.loading_work_combo.addItems(['', 'Погрузка и вывоз НКТ', 'Погрузка и вывоз штанг',
                                          'Завоз и разгрузка НКТ', 'Погрузка и вывоз НКТ', 'Завоз и разгрузка НШ',
                                          'Переукладка фНКТ с доп.стеллажей ', 'Переукладка фНКТ73мм на доп.стеллажи',
                                          'Погрузка и вывоз СБТ', 'Завоз и разгрузка СБТ'])

        self.loading_work_combo.currentTextChanged.connect(self.update_complications_of_failure)
        self.loading_work_combo.currentTextChanged.connect(self.update_loading_work_combo)


        self.loading_work_combo.setCurrentIndex(1)

        self.grid.addWidget(self.loading_work_label, 14, 2)
        self.grid.addWidget(self.loading_work_combo, 15, 2)

    def update_count_nkt_loading(self):
        index = self.loading_work_combo.currentText()
        if index == 'Погрузка и вывоз НКТ':
            self.complications_of_failure_text_line.setText(
                f'Погрузка и вывоз НКТ {self.count_nkt_loading_line.text()}шт')
        elif index == 'Погрузка и вывоз штанг':
            self.complications_of_failure_text_line.setText(
                f'Погрузка и вывоз штанг {self.count_nkt_loading_line.text()}шт')
        elif index == 'Завоз и разгрузка НКТ':
            self.complications_of_failure_text_line.setText(
                f'Завоз и разгрузка НКТ {self.count_nkt_loading_line.text()}шт')
        elif index == 'Завоз и разгрузка НШ':
            self.complications_of_failure_text_line.setText(
                f'Завоз и разгрузка НШ {self.count_nkt_loading_line.text()}шт')
        elif index == 'Погрузка и вывоз НКТ  ':
            self.complications_of_failure_text_line.setText(
                f'Погрузка и вывоз НКТ {self.count_nkt_loading_line.text()}шт')
        elif index == 'Завоз и разгрузка СБТ':
            self.complications_of_failure_text_line.setText(
                f'Завоз и разгрузка СБТ {self.count_nkt_loading_line.text()}шт')
        elif index == 'Погрузка и вывоз СБТ':
            self.complications_of_failure_text_line.setText(
                f'Погрузка и вывоз СБТ {self.count_nkt_loading_line.text()}шт')
        elif index == 'Переукладка фНКТ с доп.стеллажей ':
            self.complications_of_failure_text_line.setText(
                f'Переукладка НКТ с доп.стеллажей {self.count_nkt_loading_line.text()}')

    def update_loading_work_combo(self, index):

        self.count_nkt_loading_label = QLabel('Кол-во, шт')
        self.count_nkt_loading_line = QLineEdit(self)
        self.count_nkt_loading_line.textChanged.connect(self.update_count_nkt_loading)

        self.grid.addWidget(self.count_nkt_loading_label, 14, 4)
        self.grid.addWidget(self.count_nkt_loading_line, 15, 4)



    def update_date_loading_work(self):
        time_begin = self.loading_work_time_begin_date.dateTime()
        time_end = self.loading_work_time_end_date.dateTime()

        time_difference = self.calculate_date(time_begin, time_end)
        self.loading_work_time_line.setText(str(time_difference))


class TabWidget(QTabWidget):
    def __init__(self):
        super().__init__()
        self.addTab(TabPage_SO_Lifting_Shgn(self), '')


class LoadingWork(TemplateWork):
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

        self.loading_work_combo = current_widget.loading_work_combo.currentText()

        if self.loading_work_combo != '':
            read_data = self.read_complications_of_failure(current_widget)
            if read_data is None:
                return
            self.count_nkt_loading_line = current_widget.count_nkt_loading_line.text()
            if self.count_nkt_loading_line == '':
                QMessageBox.warning(self, 'Ошибка', 'Нужно ввести кол-во')
                return
            else:
                self.count_nkt_loading_line = int(float(self.count_nkt_loading_line))

            work_list = []

            work_list.extend(self.loading_work_def())

            well_data.date_work = self.date_work_line

            self.populate_row(self.ins_ind, work_list, self.table_widget)
            well_data.pause = False
            self.close()

    def loading_work_def(self):
        work_list = [
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'ПР.перед.ремонтом', None, 'Монтаж и демонтаж автокрана ',
             None, None,
             None,
             None, None, None, None, None, None, None, None, None, '§32разд.1', None, 'шт', 1, '=16/60', 1,
             '=V378*W378*X378', '=Y378-AA378-AB378-AC378-AD378', None, None, None, None, None], ]
        if self.loading_work_combo == 'Погрузка и вывоз НКТ':
            nkt_all = self.count_nkt_loading_line * 0.004
            work_list.extend([
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
                 f'Погрузка и вывоз НКТ  {self.count_nkt_loading_line}шт', None,
                 None, None, None, None,
                 None, None, None, None, None, None, None, '§39разд.1', None, 'шт',
                 self.count_nkt_loading_line, 0.004, 1, '=V381*W381*X381',
                 '=Y381-AA381-AB381-AC381-AD381', None, None, None, None, None]])
        elif self.loading_work_combo == 'Погрузка и вывоз СБТ':
            nkt_all = self.count_nkt_loading_line * 0.004
            work_list.extend([
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
                 f'Погрузка и вывоз СБТ {self.count_nkt_loading_line}шт', None,
                 None, None, None, None,
                 None, None, None, None, None, None, None, '§39разд.1', None, 'шт',
                 self.count_nkt_loading_line, 0.004, 1, '=V381*W381*X381',
                 '=Y381-AA381-AB381-AC381-AD381', None, None, None, None, None]])
        elif self.loading_work_combo == 'Погрузка и вывоз штанг':
            nkt_all = self.count_nkt_loading_line * 0.003
            work_list.extend([
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
                 f'Погрузка и вывоз штанг {self.count_nkt_loading_line}шт', None,
                 None, None, None, None,
                 None, None, None, None, None, None, None, '§39разд.1', None, 'шт',
                 self.count_nkt_loading_line, 0.003, 1, '=V382*W382*X382',
                 '=Y382-AA382-AB382-AC382-AD382', None, None, None, None, None]])
        elif self.loading_work_combo == 'Завоз и разгрузка НКТ':
            nkt_all = self.count_nkt_loading_line * 0.008
            work_list.extend([
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
                 f'Завоз и разгрузка НКТ {self.count_nkt_loading_line}шт', None,
                 None, None, None, None,
                 None, None, None, None, None, None, None, '§39разд.1', None, 'шт',
                 self.count_nkt_loading_line, 0.008, 1, '=V383*W383*X383',
                 '=Y383-AA383-AB383-AC383-AD383', None, None, None, None, None]])

        elif self.loading_work_combo == 'Завоз и разгрузка СБТ':
            nkt_all = self.count_nkt_loading_line * 0.008
            work_list.extend([
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
                 f'Завоз и разгрузка СБТ {self.count_nkt_loading_line}шт', None,
                 None, None, None, None,
                 None, None, None, None, None, None, None, '§39разд.1', None, 'шт',
                 self.count_nkt_loading_line, 0.008, 1, '=V383*W383*X383',
                 '=Y383-AA383-AB383-AC383-AD383', None, None, None, None, None]])

        elif self.loading_work_combo == 'Завоз и разгрузка НШ':
            nkt_all = self.count_nkt_loading_line * 0.008
            work_list.extend([
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
                 f'Завоз и разгрузка НШ {self.count_nkt_loading_line}шт', None,
                 None, None, None, None,
                 None, None, None, None, None, None, None, '§39разд.1', None, 'шт', self.count_nkt_loading_line, 0.008,
                 1,
                 '=V384*W384*X384',
                 '=Y384-AA384-AB384-AC384-AD384', None, None, None, None, None]])

        elif self.loading_work_combo == 'Переукладка фНКТ73мм с доп.стеллажей ':
            nkt_all = self.count_nkt_loading_line * 0.003
            work_list.extend([
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
                 f'Переукладка фНКТ73мм с доп.стеллажей {self.count_nkt_loading_line}шт', None, None,
                 None, None, None, None, None, None, None, None, None, None, '§39разд.1', None, 'шт',
                 self.count_nkt_loading_line,
                 0.003, 1,
                 '=V385*W385*X385', '=Y385-AA385-AB385-AC385-AD385', None, None, None, None, None]])
        elif self.loading_work_combo == 'Переукладка фНКТ73мм на доп.стеллажи':
            nkt_all = self.count_nkt_loading_line * 0.004
            work_list.extend([
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
                 'Переукладка фНКТ73мм на доп.стеллажи', None, None,
                 None, None, None, None, None, None, None, None, None, None, '§39разд.1', None, 'шт',
                 self.count_nkt_loading_line,
                 0.004, 1,
                 '=V386*W386*X386', '=Y386-AA386-AB386-AC386-AD386', None, None, None, None, None]])
        if self.complications_of_failure_time_line - nkt_all > 0:
            work_list.append([
                '=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
                f'{self.complications_of_failure_text_line} {self.complications_of_failure_time_begin_date}-'
                f'{self.complications_of_failure_time_end_date}', None, None, None, None, None, None, None,
                None,
                'АКТ№', None, None, None, 'факт', None, 'час',
                self.complications_of_failure_time_line - nkt_all, 1, 1,
                '=V138*W138*X138', '=Y138-AA138-AB138-AC138-AD138',
                None, None, None, None, None])

        return work_list


if __name__ == "__main__":
    # app3 = QApplication(sys.argv)

    app = QApplication(sys.argv)
    window = LoadingWork(22, 22)
    window.show()
    sys.exit(app.exec_())
