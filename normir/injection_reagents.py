import sys
from datetime import datetime, timedelta

import well_data

from collections import namedtuple
from normir.files_with_list import cause_presence_of_jamming
from normir.norms import LIFTING_NORM_NKT, DESCENT_NORM_NKT
from PyQt5.QtGui import QIntValidator, QDoubleValidator
from PyQt5.QtWidgets import QWidget, QLabel, QComboBox, QLineEdit, QGridLayout, QTabWidget, QMainWindow, QPushButton, \
    QMessageBox, QApplication, QHeaderView, QTableWidget, QTableWidgetItem, QTextEdit, QDateEdit, QDateTimeEdit
from PyQt5.QtCore import Qt

from normir.relocation_brigade import TextEditTableWidgetItem
from normir.spo_pakera import TabPage_SO_Timplate
from normir.spo_pakera import SpoPakerAction
from normir.TabPageAll import TabPage, TemplateWork


class TabPage_SO_inijection(TabPage):
    def __init__(self, parent=None):
        super().__init__()



        self.select_type_combo_label = QLabel('Выбор реагента')
        self.select_type_combo = QComboBox(self)
        self.select_type_combo.addItems(['', 'СКВ', 'СКО', 'растворитель', 'ПДК', 'Блок-пачка',
                                         'НЕЗАМЕРЗ.ЖИДКОСТЬ', 'ИНГИБИТОР КОРРОЗИИ'])

        self.grid = QGridLayout(self)

        self.grid.addWidget(self.date_work_label, 4, 2)
        self.grid.addWidget(self.date_work_line, 5, 2)

        self.grid.addWidget(self.select_type_combo_label, 4, 3)
        self.grid.addWidget(self.select_type_combo, 5, 3)

        self.select_type_combo.currentTextChanged.connect(self.update_select_type_combo)



    def update_select_type_combo(self, index):

        self.information = QLabel('НУЖНО Указать количество спущенных НКТ перед закачкой')

        self.grid.addWidget(self.information, 18, 1, 1, 5)

        self.select_type_nkt_combo = QComboBox(self)
        self.select_type_nkt_combo.addItems(['', 'ПСШ', 'шаблон', 'перо', 'воронка', 'пакер'])

        self.grid.addWidget(self.select_type_nkt_combo_label, 20, 1)
        self.grid.addWidget(self.select_type_nkt_combo, 21, 1)

        self.select_type_nkt_combo.currentTextChanged.connect(self.update_select_type_nkt_combo)

        if index in ['СКО', 'СКВ', 'растворитель']:
            self.solvent_injection_combo = QComboBox(self)
            self.solvent_injection_combo.addItems(['Нет', 'Да'])

            self.grid.addWidget(self.solvent_injection_label, 32, 1)
            self.grid.addWidget(self.solvent_injection_combo, 33, 1)

            self.solvent_injection_combo.currentTextChanged.connect(self.update_solvent_injection_combo)
            self.solvent_injection_combo.setCurrentIndex(1)

            self.solvent_volume_text_label.setText(f'Объем {index}')
            self.solvent_injection_label.setText(f'{index}')

            self.volume_flush_line_combo_label = QLabel(f'Была ли промывка после {index}')
            self.volume_flush_line_combo = QComboBox(self)
            self.volume_flush_line_combo.addItems(['Нет', 'Да'])

            self.grid.addWidget(self.volume_flush_line_combo_label, 64, 1)
            self.grid.addWidget(self.volume_flush_line_combo, 65, 1)

            self.volume_flush_line_combo.currentTextChanged.connect(self.update_volume_flush_line_combo)
            self.volume_flush_line_sko_label = QLabel(f'Объем промывки после {index}')

            self.response_combo_label = QLabel('Реагирование')
            self.response_combo = QComboBox(self)
            self.response_combo.addItems(['Нет', 'Да'])

            self.grid.addWidget(self.response_combo_label, 62, 1)
            self.grid.addWidget(self.response_combo, 63, 1)
            self.response_combo.currentTextChanged.connect(self.update_sko_combo)
            self.response_combo.setCurrentIndex(1)

            self.determination_of_pickup_sko_combo_label = QLabel('Было ли определение Q после СКО')
            self.determination_of_pickup_sko_combo = QComboBox(self)
            self.determination_of_pickup_sko_combo.addItems(['Нет', 'Да'])

            self.grid.addWidget(self.determination_of_pickup_sko_combo_label, 66, 1)
            self.grid.addWidget(self.determination_of_pickup_sko_combo, 67, 1)

            self.determination_of_pickup_sko_combo.currentTextChanged.connect(
                self.update_determination_of_pickup_sko_combo)

        self.normalization_question_combo = QComboBox(self)
        self.normalization_question_combo.addItems(['Нет', 'Да'])

        self.grid.addWidget(self.normalization_question_label, 70, 1)
        self.grid.addWidget(self.normalization_question_combo, 71, 1)

        # self.equipment_audit_combo.currentTextChanged.connect(self.update_equipment_audit_combo)
        # self.pressuar_gno_combo.currentTextChanged.connect(self.update_pressuar_gno_combo)
        # self.technological_crap_question_combo.currentTextChanged.connect(self.update_technological_crap_question_combo)
        # self.select_type_combo.currentTextChanged.connect(self.update_solvent_injection_combo)
        # self.pressuar_gno_combo.currentTextChanged.connect(self.update_pressuar_gno_combo)
        self.normalization_question_combo.currentTextChanged.connect(self.update_normalization_question_combo)


class TabWidget(QTabWidget):
    def __init__(self):
        super().__init__()
        self.addTab(TabPage_SO_inijection(self), 'Шаблон')


class TemplateWithoutSKM(TemplateWork):
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

        self.dict_nkt = {}
        self.count_nkt_line = None

    def add_work(self):
        from main import MyWindow

        current_widget = self.tabWidget.currentWidget()

        self.date_work_line = current_widget.date_work_line.text()
        self.select_type_combo = current_widget.select_type_combo.currentText()
        self.select_type_nkt_combo = current_widget.select_type_nkt_combo.currentText()

        if self.select_type_combo == '':
            return

        if self.select_type_nkt_combo == '':
            question = QMessageBox.question(self, 'Ошибка', 'Работа без НКТ в скважине?')
            if question == QMessageBox.StandardButton.No:
                return
        else:
            read_data = self.read_nkt_up(current_widget)
        if read_data is None:
            return

        if self.select_type_nkt_combo == 'пакер':
            self.type_equipment = 'пакер'
            self.coefficient_lifting = 1.2


        elif self.select_type_nkt_combo in ['ПСШ', 'шаблон', ]:
            self.type_equipment = 'Шаблон'
            self.coefficient_lifting = 1.15
            if self.select_type_combo in ['ПСШ']:
                if self.select_type_combo in ['ПСШ']:
                    self.type_equipment = 'ПСШ'


        elif self.select_type_combo in ['Заглушка']:
            self.coefficient_lifting = 1
            self.type_equipment = 'Заглушка'
        elif self.select_type_combo in ['перо', 'воронка']:
            self.type_equipment = 'Перо, воронка'
            self.coefficient_lifting = 1

        self.normalization_question_combo = current_widget.normalization_question_combo.currentText()

        if self.normalization_question_combo == 'Да':
            self.read_normalization_question(current_widget)

        self.solvent_injection_combo = current_widget.solvent_injection_combo.currentText()
        if self.solvent_injection_combo == 'Да':
            self.read_solvent_volume(current_widget)

        self.response_combo = current_widget.response_combo.currentText()
        if self.response_combo == 'Да':
            self.read_responce(current_widget)

        self.volume_flush_line_combo = current_widget.volume_flush_line_combo.currentText()
        if self.volume_flush_line_combo == 'Да':
            self.read_volume_after_sko(current_widget)

            self.count_nkt_combo = current_widget.count_nkt_combo.currentText()
            if self.count_nkt_combo == 'Да':
                self.read_count_nkt_combo(current_widget)

        self.determination_of_pickup_sko_combo = current_widget.determination_of_pickup_sko_combo.currentText()
        if self.determination_of_pickup_sko_combo == 'Да':
            self.read_determination_of_pickup_sko_combo(current_widget)



        work_list = self.template_with_skm()

        well_data.date_work = self.date_work_line

        self.populate_row(self.ins_ind, work_list, self.table_widget)
        well_data.pause = False
        self.close()

    def print_work(self):
        work_list = [
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'работа печати', 'ПЗР при промывке скважины', None,
             None, None, None, None, None, None, None, None, None, None, None, '§159,161разд.1', None, 'шт', 1, 1, 1,
             '=V649*W649*X649', '=Y649-AA649-AB649-AC649', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'работа печати', 'Опрессовка нагнетательной линии', None,
             None, None, None, None, None, None, None, None, None, None, None, '§113разд.1', None, 'раз', 1, 0.13, 1,
             '=X650*W650*V650', '=Y650-AA650-AB650-AC650', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'работа печати',
             self.interval_skm_text_edit, None, None, None, None, None, None, None, None, 'АКТ№',
             None, None, None, '§269разд.1', None, 'раз', self.count_of_nkt_extensions_line, 0.75, 1,
             '=V651*W651*X651', '=Y651-AA651-AB651-AC651-AD651', None, None, None, None, None]]
        return work_list

    def lifting_nkt(self):

        middle_nkt = '9.6-10.5'
        count_nkt = 0
        for nkt_key, nkt_value in self.dict_nkt_up.items():
            if count_nkt > 1:
                work_list.extend([
                    ['=ROW()-ROW($A$46)', '73мм-60мм', None, 'Тех.операции', None, 'Смена захвата ЭТА', None, None,
                     None, None, None, None, None, None, None, None, None, None, '§301разд.1 п.141', None, 'раз',
                     1, 0.07, 1, '=V361*W361*X361', '=Y361-AA361-AB361-AC361-AD361', None, None, None, None, None]])
            middle_nkt_value = nkt_value[0] / nkt_value[1]
            nkt_lenght = nkt_value[0]
            nkt_count = nkt_value[1]

            if 6.5 <= middle_nkt_value <= 7.6:
                middle_nkt = '6.5-7.5'
            elif 7.6 <= middle_nkt_value <= 8.6:
                middle_nkt = '7.6-8.5'
            elif 8.6 <= middle_nkt_value <= 9.6:
                middle_nkt = '8.6-9.5'
            elif 9.6 <= middle_nkt_value <= 10.6:
                middle_nkt = '9.6-10.5'
            elif 10.6 <= middle_nkt_value <= 11.6:
                middle_nkt = '10.6-11.5'
            elif 11.6 <= middle_nkt_value <= 12.6:
                middle_nkt = '11.6-12.5'

            max_count_3 = LIFTING_NORM_NKT[well_data.lifting_unit_combo][nkt_key]['III'][middle_nkt][1]
            koef_norm_3 = LIFTING_NORM_NKT[well_data.lifting_unit_combo][nkt_key]['III'][middle_nkt][0]
            razdel_3 = LIFTING_NORM_NKT[well_data.lifting_unit_combo][nkt_key]['III']['раздел']

            if max_count_3 > nkt_lenght:
                nkt_count_3 = nkt_count
            else:
                nkt_count_3 = max_count_3

            lenght_nkt_3 = int(middle_nkt_value * nkt_count_3)

            work_list = [
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', self.type_equipment,
                 'ПЗР СПО перед подъемом труб из скважины',
                 None, None, None,
                 None, None, None, None, None, None, None, None, None, '§207разд.1', None, 'шт', 1, 0.07, 1,
                 '=V199*W199*X199', '=Y199-AA199-AB199-AC199-AD199', None, None, None, None, None]]

            podien_3_list = ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', self.type_equipment,
                             'Подъем НКТ  3 скорость',
                             None, None, None, None, nkt_key, lenght_nkt_3, middle_nkt, max_count_3,
                             None, None, None, None, razdel_3, None, 'шт', nkt_count_3, koef_norm_3,
                             self.coefficient_lifting, '=V202*W202*X202', '=Y202-AA202-AB202-AC202-AD202',
                             None, None, None, None, None]

            work_list.append(podien_3_list)

            nkt_count -= max_count_3

            if nkt_count > 0:
                max_count_2 = LIFTING_NORM_NKT[well_data.lifting_unit_combo][nkt_key]['II'][middle_nkt][1]
                koef_norm_2 = LIFTING_NORM_NKT[well_data.lifting_unit_combo][nkt_key]['II'][middle_nkt][0]
                razdel_2 = LIFTING_NORM_NKT[well_data.lifting_unit_combo][nkt_key]['II']['раздел']
                if max_count_2 > nkt_count:
                    nkt_count_2 = nkt_count
                else:
                    nkt_count_2 = max_count_2
                lenght_nkt_2 = int(middle_nkt_value * nkt_count_2)
                podiem_list_2 = ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', self.type_equipment,
                                 'Подъем НКТ  2 скорость',
                                 None, None, None, None, nkt_key, lenght_nkt_2, middle_nkt, max_count_2,
                                 None, None, None, None, razdel_2, None, 'шт', nkt_count_2, koef_norm_2,
                                 self.coefficient_lifting, '=V202*W202*X202', '=Y202-AA202-AB202-AC202-AD202', None,
                                 None, None, None, None]
                nkt_count -= max_count_2
                work_list.insert(1, podiem_list_2)

            if nkt_count > 0:
                max_count_1 = LIFTING_NORM_NKT[well_data.lifting_unit_combo][nkt_key]['I'][middle_nkt][1]
                koef_norm_1 = LIFTING_NORM_NKT[well_data.lifting_unit_combo][nkt_key]['I'][middle_nkt][0]
                razdel_1 = LIFTING_NORM_NKT[well_data.lifting_unit_combo][nkt_key]['I']['раздел']

                lenght_nkt_1 = int(middle_nkt_value * nkt_count)
                podiem_list_1 = [
                    '=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', self.type_equipment,
                    'Подъем НКТ  1 скорость',
                    None, None, None, None, nkt_key, lenght_nkt_1, middle_nkt, max_count_1,
                    None, None, None, None, razdel_1, None, 'шт', nkt_count, koef_norm_1,
                    self.coefficient_lifting, '=V202*W202*X202', '=Y202-AA202-AB202-AC202-AD202', None, None, None,
                    None, None]
                nkt_count -= max_count_1
                work_list.insert(1, podiem_list_1)

        nkt_sum = sum(list(map(lambda x: x[1], self.dict_nkt_up.values())))

        work_list.extend([
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', self.type_equipment, 'Долив скважины', None, None,
             None, None,
             None, None, None,
             None, None, None, None, None, '§168разд.1', None, 'шт', nkt_sum / 10, 0.003, 1, '=V204*W204*X204',
             '=Y204-AA204-AB204-AC204-AD204', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', self.type_equipment,
             'Навернуть/отвернуть предохранительное кольцо', None, None,
             None, None, None, None, None, None, None, None, None, None, '§300разд.1', None, 'шт',
             nkt_sum,
             0.003, 1, '=V205*W205*X205', '=Y205-AA205-AB205-AC205-AD205', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', self.type_equipment, 'Замер НКТ ', None, None, None,
             None, None,
             None, None, None,
             None, None, None, None, '§47разд.1', None, 'шт', nkt_sum, 0.008, 1,
             '=V207*W207*X207',
             '=Y207-AA207-AB207-AC207-AD207', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'д/ж спайдера',
             None, None, None, None,
             None, None, None, None, None, None, None, None, '§185разд.1', None, 'шт', 1, 0.07, 1, '=V209*W209*X209',
             '=Y209-AA209-AB209-AC209-AD209', None, None, None, None, None],
        ])

        if self.complications_when_lifting_combo == 'Да':
            work_list.insert(-4, ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', self.type_equipment,
                                  f'{self.complications_when_lifting_text_line} '
                                  f'{self.complications_when_lifting_time_begin_date}'
                                  f'{self.complications_when_lifting_time_end_date}',
                                  None, None,
                                  None, None, None,
                                  None, 'Объем', 0, None, None, None, None, 'факт', None,
                                  'час', self.complications_when_lifting_time_end_date, 1, 1, '=V206*W206*X206',
                                  '=Y206-AA206-AB206-AC206-AD206', None, None, None, None, None])
        if nkt_sum > 201:
            work_list.insert(-3, ['=ROW()-ROW($A$46)', 'подъем НКТ', None, 'спо', self.type_equipment,
                                  'Откатывание труб с 201 трубы ',
                                  None, None, None,
                                  None, None, None, None, None, None, None, None, None, '§40разд.1', None, 'шт',
                                  nkt_sum - 201, 0.008, 1,
                                  '=V208*W208*X208', '=Y208-AA208-AB208-AC208-AD208', None, None, None, None, None])

        return work_list

    def deinstallation_of_washing_equipment(self):
        work_list = [
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'Д/ж спайдера', None, None, None,
             None,
             None, None, None, None, None, None, None, None, '§185разд.1', None, 'час', 1, 0.07, 1,
             '=V469*W469*X469', '=Y469-AA469-AB469-AC469-AD469', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'Демонтаж КГОМ', None, None, None,
             None,
             None, None, None, None, None, None, None, None, '§301разд.1', None, 'час', 1, 0.17, 1,
             '=V470*W470*X470', '=Y470-AA470-AB470-AC470-AD470', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'М/ж спайдера', None, None, None,
             None,
             None, None, None, None, None, None, None, None, '§185разд.1', None, 'час', 1, 0.07, 1,
             '=V471*W471*X471', '=Y471-AA471-AB471-AC471-AD471', None, None, None, None, None]]
        return work_list

    def installation_of_washing_equipment(self):
        work_list = [
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'Д/ж спайдера', None, None, None,
             None,
             None, None, None, None, None, None, None, None, '§185разд.1', None, 'час', 1, 0.07, 1,
             '=V453*W453*X453', '=Y453-AA453-AB453-AC453-AD453', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'Монтаж КГОМ', None, None, None,
             None,
             None, None, None, None, None, None, None, None, '§301разд.1', None, 'час', '=SUM(V453)', 0.17, 1,
             '=V454*W454*X454', '=Y454-AA454-AB454-AC454-AD454', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'М/ж спайдера', None, None, None,
             None,
             None, None, None, None, None, None, None, None, '§185разд.1', None, 'час', 1, 0.07, 1,
             '=V455*W455*X455', '=Y455-AA455-AB455-AC455-AD455', None, None, None, None, None]]
        return work_list

    def skm_work(self):
        work_list = self.installation_of_washing_equipment()
        if self.interval_skm_text_edit != '':
            skm_list = [
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
                 'Подготовительные работы перед скреперованием', None, None, None, None, None, None, None, None,
                 None, None, None, None, '§178разд.1', None, 'шт', 1, 1.02, 1, '=V456*W456*X456',
                 '=Y456-AA456-AB456-AC456-AD456', None, None, None, None, None],
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
                 f'Проработка мех.скрепером в инт.{self.interval_skm_text_edit}м', None,
                 None, None, None, None, None, None, None, None, None, None, None, '§179разд.1', None, 'м',
                 self.count_of_nkt_extensions_line,
                 0.012, 1, '=V457*W457*X457', '=Y457-AA457-AB457-AC457-AD457', None, None, None, None, None],
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'Наращивание', None, None, None,
                 None,
                 None, None, None, None, None, None, None, None, '§300разд.1', None, 'шт',
                 int(self.count_of_nkt_extensions_line / 10), 0.17, 1,
                 '=V458*W458*X458', '=Y458-AA458-AB458-AC458-AD458', None, None, None, None, None],
            ]
            work_list.extend(skm_list)

        return work_list

    def gvzh_work(self):
        work_list = [
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'ПЗР при промывке скважины', None, None, None, None,
             None, None, None, None, None, None, None, None, '§159,161разд.1', None, 'шт', 1, 1, 1, '=V865*W865*X865',
             '=Y865-AA865-AB865-AC865', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'Опрессовка нагнетательной линии', None, None, None,
             None, None, None, None, None, None, None, None, None, '§113разд.1', None, 'раз', 1, 0.13, 1,
             '=X866*W866*V866', '=Y866-AA866-AB866-AC866', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'Отбивка уровня жидкости в скважинах (эхолотом)',
             None, None, None, None, None, None, None, None, None, None, None, None, '§182разд.1', None, 'шт', 1, 0.22,
             1, '=V867*W867*X867', '=Y867-AA867-AB867-AC867-AD867', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'Посадка гидрожелонки', None, None, None, None,
             None, None, None, None, None, None, None, None, '§252разд.1', None, 'шт', 1, 0.33, 1, '=V868*W868*X868',
             '=Y868-AA868-AB868-AC868-AD868', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'Набор жидкости в гидрожелонку в скважине', None,
             None, None, None, None, None, None, None, None, None, None, None, '§253разд.1', None, 'раз', 1, 0.05, 1,
             '=V869*W869*X869', '=Y869-AA869-AB869-AC869-AD869', None, None, None, None, None]]
        return work_list

    def kot_work(self):
        work_list = [
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'ПЗР при промывке скважины', None, None, None, None,
             None, None, None, None, None, None, None, None, '§159,161разд.1', None, 'шт', 1, 1, 1, '=V865*W865*X865',
             '=Y865-AA865-AB865-AC865', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'Опрессовка нагнетательной линии', None, None, None,
             None, None, None, None, None, None, None, None, None, '§113разд.1', None, 'раз', 1, 0.13, 1,
             '=X866*W866*V866', '=Y866-AA866-AB866-AC866', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'Отбивка уровня жидкости в скважинах (эхолотом)',
             None, None, None, None, None, None, None, None, None, None, None, None, '§182разд.1', None, 'шт', 1, 0.22,
             1, '=V867*W867*X867', '=Y867-AA867-AB867-AC867-AD867', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'Посадка КОТ', None, None, None, None,
             None, None, None, None, None, None, None, None, '§252разд.1', None, 'шт', 1, 0.33, 1, '=V868*W868*X868',
             '=Y868-AA868-AB868-AC868-AD868', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'Набор жидкости в гидрожелонку в скважине', None,
             None, None, None, None, None, None, None, None, None, None, None, '§253разд.1', None, 'раз', 1, 0.05, 1,
             '=V869*W869*X869', '=Y869-AA869-AB869-AC869-AD869', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'Набор жидкости в гидрожелонку в скважине', None,
             None, None, None, None, None, None, None, None, None, None, None, '§253разд.1', None, 'раз', 1, 0.05, 1,
             '=V869*W869*X869', '=Y869-AA869-AB869-AC869-AD869', None, None, None, None, None]
        ]
        return work_list

    def template_with_skm(self):
        complications_of_failure_list = []
        complications_during_disassembly_list = []
        if self.select_type_combo in ['СКВ', 'СКО', 'растворитель']:
            if self.select_type_combo in ['СКВ']:
                work_list = self.skv_work()
            elif self.select_type_combo in ['СКО']:
                work_list = self.sko_work()
            elif self.select_type_combo in ['растворитель']:
                work_list = self.solvent_work()


            if self.response_combo == 'Да':
                work_list.append(self.response_sko())

            if self.normalization_question_combo == 'Да':
                work_list.extend(self.drinirovanie())

            if self.volume_flush_line_combo == 'Да':
                if self.count_nkt_combo == 'Да':
                    work_list.extend(self.count_nkt_down())
                work_list.extend(self.volume_after_sko_work())

            if self.determination_of_pickup_sko_combo == 'Да':
                work_list.extend(self.determination_of_pickup_work(
                    self.saturation_volume_sko_line, self.determination_of_pickup_sko_text_line))

        return work_list

    def solvent_work(self):
        work_list = self.solvent_injection_work()
        return work_list

    def nkt_vn(self):
        nkt_vn = 0
        for nkt_key, nkt_value in self.dict_nkt.items():
            if '60' in nkt_key:
                nkt_vn += nkt_value[0] * 2 / 1000
            elif '73' in nkt_key:
                nkt_vn += nkt_value[0] * 3 / 1000
            elif '89' in nkt_key:
                nkt_vn += nkt_value[0] * 4 / 1000
        return nkt_vn

    def sko_work(self):
        volume_sko = self.solvent_volume_text_line
        nkt_vn = self.nkt_vn()

        work_list = [
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'ОПЗ', 'Подготовительные работы, выполняемые ', None,
             None,
             None, 'ПО ТКРС', None, None, 'перед началом работ на скважине', None, None, 'КИСЛОТА',
             'Соляная кислота ингибированная ', None, '§227,229разд.1', None, 'шт', 1, 0.96, 1, '=V572*W572*X572',
             '=Y572-AA572-AB572-AC572-AD572', None, None, None, None, None]
        ]
        skv_list, time_skv_norm = self.sko_download(volume_sko, nkt_vn)
        work_list.extend(skv_list)
        if len(self.dict_nkt) > 0:
            if nkt_vn > self.solvent_volume_text_line:

                nkt_list = self.dovodka(time_skv_norm)
                work_list.extend(nkt_list)

                if self.select_type_nkt_combo == 'пакер':
                    work_list.extend([
                        ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'ОПЗ', f'Посадка пакера', None, None, None,
                         None,
                         None, None, None, None, None, None, None, None, '§138разд.1', None, 'шт', 1, 0.23, 1,
                         '=V584*W584*X584',
                         '=Y584-AA584-AB584-AC584-AD584', None, None, None, None, None]])
                else:
                    work_list.extend([
                        ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'Открытие закрытие скв',
                         'Открытие закрытие скв', None, None, None, None, None, None, None, None, None,
                         None, None, None, '§300разд.1', None, 'шт', 1, 0.18, 1, '=V1252*W1252*X1252',
                         '=Y1252-AA1252-AB1252-AC1252-AD1252', None, None, None, None, None]])
                work_list.extend([
                        ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'ОПЗ', 'Продавка кислоты тех.водой в пласт ',
                         None, None,
                         None, None, None, None, None, None, None, None, None, None, '§228разд.1', None, 'м3',
                         self.volume_of_finishing_line,
                         0.07, 1,
                         '=V577*W577*X577', '=Y577-AA577-AB577-AC577-AD577', None, None, None, None, None]
                    ])
            else:

                work_list.extend([
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'ОПЗ', 'Продавка кислоты кислотой в пласт ', None,
                 None,
                 None, None, None, None, None, None, None, None, None, None, '§228разд.1', None, 'м3',
                 self.solvent_volume_text_line - nkt_vn, 0.07, 1,
                 '=V576*W576*X576', '=Y576-AA576-AB576-AC576-AD576', None, None, None, None, None],
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'ОПЗ', 'Продавка кислоты тех.водой в пласт ',
                 None, None,
                 None, None, None, None, None, None, None, None, None, None, '§228разд.1', None, 'м3',
                 self.volume_of_finishing_line,
                 0.07, 1,
                 '=V577*W577*X577', '=Y577-AA577-AB577-AC577-AD577', None, None, None, None, None]
            ])

        if time_skv_norm < self.solvent_volume_time_line:
            skv_list = [['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'ОПЗ',
                         f'Проведение СКО {self.solvent_volume_time_begin_date}-{self.solvent_volume_time_end_date}',
                         None, None, None,
                         None, None, None, None, None, 'АКТ№', None, None, None, 'факт', None, 'час',
                         self.solvent_volume_time_line - time_skv_norm, 1,
                         1,
                         '=V583*W583*X583', '=Y583-AA583-AB583-AC583-AD583', None, None, None, None, None]]
            work_list.extend(skv_list)

        return work_list

    def drinirovanie(self):
        work_list = [
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'ОПЗ',
             f'{self.normalization_question_text_line} '
             f'{self.normalization_question_time_begin_date}-{self.normalization_question_time_end_date}', None,
             None, None, None, None, None, None, None, 'АКТ№', None, None, None, 'простои', 'Тех. ожидание', 'час',
             self.normalization_question_time_line,
             1, 1, '=V586*W586*X586', '=Y586-AA586-AB586-AC586-AD586', None, None, None, None, None]]
        return work_list

    def sko_download(self, volume_skv, nkt_vn):
        work_list = []
        if volume_skv > 1:

            work_list.extend([
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'ОПЗ',
                 f'Закачка кислоты первого 1м3', None, None, None,
                 None, None, None, None, None, 'АКТ№', None, None, None, '§228разд.1', None, 'м3',
                 1, 0.2, 1,
                 '=V582*W582*X582', '=Y582-AA582-AB582-AC582-AD582', None, None, None, None, None]])
            if self.solvent_volume_text_line > nkt_vn:
                work_list.extend([
                    ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'ОПЗ',
                 f'Закачка кислоты следующего {round(nkt_vn - 1, 1)}м3',
                 None, None, None,
                 None, None, None, None, None, 'АКТ№', None, None, None, '§228разд.1', None, 'м3',
                 round(nkt_vn - 1, 1), 0.1,
                 1,
                 '=V583*W583*X583', '=Y583-AA583-AB583-AC583-AD583', None, None, None, None, None]])
            else:
                work_list.extend([
                    ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'ОПЗ',
                     f'Закачка кислоты следующего {self.solvent_volume_text_line - 1}м3',
                     None, None, None,
                     None, None, None, None, None, 'АКТ№', None, None, None, '§228разд.1', None, 'м3',
                     round(self.solvent_volume_text_line - 1, 1), 0.1,
                     1,
                     '=V583*W583*X583', '=Y583-AA583-AB583-AC583-AD583', None, None, None, None, None]])

            time_skv_norm = (nkt_vn -1) * 0.1 + 0.2 + 1.17

        else:
            work_list.extend([['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'ОПЗ',
                               f'Закачка кислоты первого {volume_skv}м3', None, None, None,
                               None, None, None, None, None, 'АКТ№', None, None, None, '§228разд.1', None, 'м3',
                               volume_skv, 0.2, 1,
                               '=V582*W582*X582', '=Y582-AA582-AB582-AC582-AD582', None, None, None, None, None]])
            time_skv_norm = (volume_skv) * 0.2 + 1.17

        return work_list, time_skv_norm

    def skv_work(self):
        volume_skv = self.solvent_volume_text_line
        nkt_vn = self.nkt_vn()

        work_list = [
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'ОПЗ', 'Подготовительные работы, выполняемые ', None,
             None, None, 'ПО ТКРС', None, None, 'перед началом работ на скважине', None, None, 'КИСЛОТА',
             'Соляная кислота ингибированная ', None, '§232,233разд.1', None, 'шт', 1, 1.167, 1, '=V581*W581*X581',
             '=Y581-AA581-AB581-AC581-AD581', None, None, None, None, None]]
        nkt_vn
        skv_list, time_skv_norm = self.sko_download(volume_skv, nkt_vn)
        work_list.extend(skv_list)

        if len(self.dict_nkt) > 0:
            nkt_list = self.dovodka(time_skv_norm)
            work_list.extend(nkt_list)

        if time_skv_norm < self.solvent_volume_time_line:
            skv_list = [['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'ОПЗ',
                         f'Проведение СКВ {self.solvent_volume_time_begin_date}-{self.solvent_volume_time_end_date}',
                         None, None, None,
                         None, None, None, None, None, 'АКТ№', None, None, None, 'факт', None, 'час',
                         self.solvent_volume_time_line - time_skv_norm, 1,
                         1,
                         '=V583*W583*X583', '=Y583-AA583-AB583-AC583-AD583', None, None, None, None, None]]
            work_list.extend(skv_list)

        if self.select_type_nkt_combo == 'пакер':
            work_list.append(
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'ОПЗ', 'Посадка пакера', None, None, None,
                 None,
                 None, None, None, None, None, None, None, None, '§138разд.1', None, 'шт', 1, 0.23, 1,
                 '=V584*W584*X584',
                 '=Y584-AA584-AB584-AC584-AD584', None, None, None, None, None])

        return work_list

    def volume_well_work(self):
        work_list = []

        volume_list = [
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'Промывка',
             'ПЗР при промывке скважины ',
             None, None, None, None, None, None, None, None, None, None, None, None, '§156,160р.1', None, 'шт',
             1, 1, 1, '=V462*W462*X462', '=Y462-AA462-AB462-AC462-AD462', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'Промывка',
             'Переход на обратную промывку',
             None, None, None, None, None, None, None, None, None, None, None, None, '§162разд.1', None, 'раз',
             1, 0.15, 1, '=V463*W463*X463', '=Y463-AA463-AB463-AC463-AD463', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'Промывка', 'Промывка ',
             None, None, None, None, None, None, None, None, None, None, None, None, '§300разд.1', None, 'м3',
             self.volume_well_flush_line, 0.033, 1,
             '=V464*W464*X464', '=Y464-AA464-AB464-AC464-AD464', None, None, None, None, None]
        ]
        work_list.extend(volume_list)
        return work_list

    def solvent_injection_work(self):
        work_list = [
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'ОПЗ', 'Подготовительные работы, выполняемые ', None,
             None, None, 'ПО ТКРС', None, None, 'перед началом работ на скважине', None, None, 'РАСТВОРИТЕЛЬ',
             'Растворитель АСПО Реком 7125 серия 4, КР-4Р', None, '§227,229разд.1', None, 'шт', 1, 0.96, 1,
             '=V589*W589*X589', '=Y589-AA589-AB589-AC589-AD589', None, None, None, None, None]]
        if self.solvent_volume_text_line > 1:
            solvent_volume_list = [
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'ОПЗ', f'Закачка растворителя первого 1м3',
                 None, None, None, None, None, None, None, None, 'АКТ№', None, None, None, '§228разд.1', None, 'м3',
                 1,
                 0.2,
                 1, '=V590*W590*X590', '=Y590-AA590-AB590-AC590-AD590', None, None, None, None, None],
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'ОПЗ',
                 f'Закачка растворителя следующего {self.solvent_volume_text_line - 1}м3', None, None,
                 None, None, None, None, None, None, 'АКТ№', None, None, None, '§228разд.1', None, 'м3', 1, 0.1,
                 1, '=V591*W591*X591', '=Y591-AA591-AB591-AC591-AD591', None, None, None, None, None]]
        else:
            solvent_volume_list = [
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'ОПЗ',
                 f'Закачка растворителя первого {self.solvent_volume_text_line}м3', None,
                 None, None, None, None, None, None, None, 'АКТ№', None, None, None, '§228разд.1', None, 'м3', 1,
                 0.2,
                 1, '=V590*W590*X590', '=Y590-AA590-AB590-AC590-AD590', None, None, None, None, None],
            ]
        work_list.extend(solvent_volume_list)
        volume_list = [
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'ОПЗ',
             f'Доводка растворителя в объеме {self.volume_of_finishing_line}', None, None, None, None,
             None, None, None, None, None, None, None, None, '§228разд.1', None, 'м3',
             self.volume_of_finishing_line,
             0.033, 1, '=V592*W592*X592',
             '=Y592-AA592-AB592-AC592-AD592', None, None, None, None, None],
            ]
        work_list.extend(volume_list)
        return work_list

    def descent_nkt_work(self):
        sum_nkt = sum(list(map(lambda x: x[1], list(self.dict_nkt.values()))))
        work_list = []
        middle_nkt = '9.6-10.5'
        for nkt_key, nkt_value in self.dict_nkt.items():

            middle_nkt_value = nkt_value[0] / nkt_value[1]
            nkt_lenght = nkt_value[0]
            nkt_count = nkt_value[1]
            if 6.5 <= middle_nkt_value <= 7.6:
                middle_nkt = '6.5-7.5'
            elif 7.6 < middle_nkt_value <= 8.6:
                middle_nkt = '7.6-8.5'
            elif 8.6 < middle_nkt_value <= 9.6:
                middle_nkt = '8.6-9.5'
            elif 9.6 < middle_nkt_value <= 10.6:
                middle_nkt = '9.6-10.5'
            elif 10.6 < middle_nkt_value <= 11.6:
                middle_nkt = '10.6-11.5'
            elif 11.6 < middle_nkt_value <= 12.5:
                middle_nkt = '11.6-12.5'

            aaaa = DESCENT_NORM_NKT[well_data.lifting_unit_combo]
            koef_norm_down = DESCENT_NORM_NKT[well_data.lifting_unit_combo][nkt_key][middle_nkt]
            razdel_2_down = DESCENT_NORM_NKT[well_data.lifting_unit_combo][nkt_key]['раздел']

            work_list.extend([
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', self.type_equipment,
                 f'Спуск НКТ компоновка {nkt_key}', None,
                 None, None, None,
                 None, nkt_key, nkt_lenght,
                 middle_nkt, None, None, None, None,
                 razdel_2_down, None, 'шт', nkt_count,
                 koef_norm_down, self.coefficient_lifting, '=V448*W448*X448', '=Y448-AA448-AB448-AC448-AD448', None,
                 None,
                 None, None, None]])

            work_list.extend([
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', self.type_equipment,
                 'Навернуть/отвернуть предохранительное кольцо',
                 None, None, None, None, None, None, None, None, None, None, None, None, '§300разд.1',
                 None, 'шт',
                 sum_nkt, 0.003, 1, '=V449*W449*X449', '=Y449-AA449-AB449-AC449-AD449', None,
                 None, None,
                 None, None],
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', self.type_equipment, 'Замер НКТ ', None,
                 None,
                 None, None, None, None,
                 None, None, None, None, None, None, '§47разд.1', None, 'шт', sum_nkt, 0.008, 1,
                 '=V450*W450*X450',
                 '=Y450-AA450-AB450-AC450-AD450', None, None, None, None, None]])
            if sum_nkt > 201:
                work_list.append([
                    '=ROW()-ROW($A$46)', 'спуск 73мм', None, 'спо', self.type_equipment,
                    'Подкатывание труб с 201 трубы ', None,
                    None, None, None, None, None, None, None, None, None, None, None, '§40разд.1', None, 'шт',
                    sum_nkt - 201, 0.008, 1, '=V451*W451*X451', '=Y451-AA451-AB451-AC451-AD451', None, None, None,
                    None,
                    None])

        return work_list

if __name__ == "__main__":
    # app3 = QApplication(sys.argv)

    app = QApplication(sys.argv)
    window = TemplateWithoutSKM(22, 22)
    window.show()
    sys.exit(app.exec_())
