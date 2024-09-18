import sys
from datetime import datetime, timedelta

import well_data

from normir.norms import LIFTING_NORM_SUCKER_POD
from PyQt5.QtGui import QIntValidator, QDoubleValidator
from PyQt5.QtWidgets import QWidget, QLabel, QComboBox, QLineEdit, QGridLayout, QTabWidget, QMainWindow, QPushButton, \
    QMessageBox, QApplication, QHeaderView, QTableWidget, QTableWidgetItem, QTextEdit, QDateTimeEdit

from normir.descent_gno import TabPage_SO_Lifting_gno
from normir.TabPageAll import TabPage, TemplateWork


class TabPage_SO_Descent_Shgn(TabPage):
    def __init__(self, parent=None):
        super().__init__()

        self.grid = QGridLayout(self)

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

        self.lift_installation_combo.currentTextChanged.connect(self.update_lifting)

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

        self.grid.addWidget(self.complications_when_lifting_label, 46, 1)
        self.grid.addWidget(self.complications_when_lifting_combo, 47, 1)

        self.complications_of_failure_label.setText('Рассхаживание при срыве')
        self.complications_during_disassembly_label.setText('Осложнения при монтаже')

        self.pressuar_gno_label = QLabel('Опрессовка ГНО')
        self.pressuar_gno_combo = QComboBox(self)
        self.pressuar_gno_combo.addItems(['Нет', 'Да'])

        self.grid.addWidget(self.pressuar_gno_label, 26, 1)
        self.grid.addWidget(self.pressuar_gno_combo, 27, 1)

        # self.determination_of_the_weight_text_label = QLabel('Определение веса штанг')
        # self.determination_of_the_weight_text_line = QLineEdit(self)

        self.sucker_up()



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
        self.addTab(TabPage_SO_Descent_Shgn(self), 'Спуск ШГН')


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
            self.read_sucker_up(current_widget)
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
            read_data = self.read_complications_of_failure(current_widget)
            if read_data is None:
                return

        if self.complications_when_lifting_combo == 'Да':
            read_data = self.read_complications_when_lifting(current_widget)
            if read_data is None:
                return

        if self.complications_during_disassembly_combo == 'Да':
            read_data = self.read_complications_during_disassembly_combo(current_widget)
            if read_data is None:
                return


        if len(self.dict_sucker_pod) == 0:
            question = QMessageBox.question(self, 'Ошибка', f'НКТ отсутствуют?')
            if question == QMessageBox.StandardButton.No:
                return

        work_list = self.descent_sucker_pod_work()

        well_data.date_work = self.date_work_line

        self.populate_row(self.ins_ind, work_list, self.table_widget)

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
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'Монтаж планшайбы на устье скважины', None, None,
             None, None, None, None, None, None, None, None, None, None, '§106разд.1', None, 'шт', 1, 0.37, 1,
             '=V1081*W1081*X1081', '=Y1081-AA1081-AB1081-AC1081-AD1081', None, None, None, None, None],

            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'Монтаж штангового превентора', None, None, None,
             None, None, None, None, None, None, None, None, None, '§120разд.1', None, 'шт', 1, 0.35, 1,
             '=V1083*W1083*X1083', '=Y1083-AA1083-AB1083-AC1083-AD1083', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'Опрессовка ПШМ', None, None, None, None, None,
             None, None, None, None, None, None, None, '§112,разд.1', None, 'шт', 1, 0.62, 1, '=V1084*W1084*X1084',
             '=Y1084-AA1084-AB1084-AC1084-AD1084', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'Устройство  рабочей площадки частично', None, None,
             None, None, None, None, None, None, None, None, None, None, '§55разд.1', None, 'шт', 1, 0.32, 1,
             '=V1085*W1085*X1085', '=Y1085-AA1085-AB1085-AC1085-AD1085', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'Монтаж гидравлических ключей штанговых(ГШК-300)',
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

