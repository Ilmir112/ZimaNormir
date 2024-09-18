import sys
from datetime import datetime, timedelta

import well_data

from normir.norms import LIFTING_NORM_SUCKER_POD
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

        self.complications_of_failure_label = QLabel('осложнения при срыве ПШ')
        self.complications_of_failure_combo = QComboBox(self)
        self.complications_of_failure_combo.addItems(['Нет', 'Да'])

        self.complications_during_disassembly_label = QLabel('осложнения при демонтаже')
        self.complications_during_disassembly_combo = QComboBox(self)
        self.complications_during_disassembly_combo.addItems(['Нет', 'Да'])

        self.complications_when_lifting_label = QLabel('Осложнения при подьеме штанг')
        self.complications_when_lifting_combo = QComboBox(self)
        self.complications_when_lifting_combo.addItems(['Нет', 'Да'])

        self.grid.addWidget(self.complications_of_failure_label, 28, 1)
        self.grid.addWidget(self.complications_of_failure_combo, 29, 1)

        # self.grid.addWidget(self.complications_of_failure_label, 10, 1)
        # self.grid.addWidget(self.complications_of_failure_combo, 11, 1)

        self.grid.addWidget(self.complications_during_disassembly_label, 30, 1)
        self.grid.addWidget(self.complications_during_disassembly_combo, 31, 1)

        self.grid.addWidget(self.complications_when_lifting_label, 46, 1)
        self.grid.addWidget(self.complications_when_lifting_combo, 47, 1)

        self.complications_of_failure_label.setText('Рассхаживание')
        self.complications_during_disassembly_label.setText('Осложнения при демонтаже')

        self.pressuar_gno_label = QLabel('Опрессовка ГНО')
        self.pressuar_gno_combo = QComboBox(self)
        self.pressuar_gno_combo.addItems(['Нет', 'Да'])

        self.determination_of_the_weight_text_label = QLabel('Определение веса штанг')
        self.determination_of_the_weight_text_line = QLineEdit(self)

        self.sucker_up()

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


class TabWidget(QTabWidget):
    def __init__(self):
        super().__init__()
        self.addTab(TabPage_SO_Lifting_Shgn(self), 'Подьем ШГН')


class LiftingShgnWindow(TemplateWork):
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

        self.dict_sucker_pod = {}

    def add_work(self):
        from main import MyWindow

        current_widget = self.tabWidget.currentWidget()

        self.date_work_line = current_widget.date_work_line.text()

        self.determination_of_the_weight_text_line = current_widget.determination_of_the_weight_text_line.text()
        if self.determination_of_the_weight_text_line == '':
            QMessageBox.warning(self, 'Ошибка', f'Не введены текст опрессовки ГНО')
            return

        self.read_sucker_up(current_widget)

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
            read_data = self.read_complications_of_failure(current_widget)
            if read_data is None:
                return

        if self.complications_when_lifting_combo == 'Да':
            read_data = self.read_complications_when_lifting(current_widget)
            if read_data is None:
                return

        if self.complications_during_disassembly_combo == 'Да':
            read_data = self.read_complications_during_tubing_running_combo(current_widget)
            if read_data is None:
                return

        work_list = self.lifting_sucker_pod_list()
        if len(self.dict_sucker_pod) == 0:
            question = QMessageBox.question(self, 'Ошибка', f'НКТ отсутствуют?')
            if question == QMessageBox.StandardButton.No:
                return

        well_data.date_work = self.date_work_line

        self.populate_row(self.ins_ind, work_list, self.table_widget)
        well_data.pause = False
        self.close()

    def lifting_sucker_pod_list(self):
        from normir.rod_head_work import LiftingRodHeadWindow
        work_list = []
        if self.pressuar_gno_combo == 'Да':
            pressuar_list = [
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, self.pressuar_gno_text_line,
                 None,
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
                 '=Y136-AA136-AB136-AC136-AD136', None, None, None, None, None]]
            work_list.extend(pressuar_list)
        if self.complications_of_failure_combo == 'Да':
            work_list.extend([
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
                 f'{self.complications_of_failure_text_line} {self.complications_of_failure_time_begin_date}-'
                 f'{self.complications_of_failure_time_end_date}', None, None, None, None, None, None, None, None,
                 'АКТ№', None, None, None, 'факт', None, 'час', self.complications_of_failure_time_line - 0.15, 1, 1,
                 '=V138*W138*X138', '=Y138-AA138-AB138-AC138-AD138',
                 None, None, None, None, None]])
        work_list.extend([
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
        ])

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
                 f'{self.complications_when_lifting_text_line} '
                 f'{self.complications_when_lifting_time_begin_date}-{self.complications_when_lifting_time_end_date}',
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
