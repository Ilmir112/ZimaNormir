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
from normir.TabPageAll import TabPage, TemplateWork


class TabPage_SO_Timplate(TabPage):
    def __init__(self, parent=None):
        super().__init__()

        self.select_type_combo_label = QLabel('Выбор компоновки спуска')
        self.select_type_combo = QComboBox(self)
        self.select_type_combo.addItems(['', 'ПСШ', 'шаблон', 'перо', 'воронка', 'печать', 'магнит',
                                         'КОТ', 'Заглушка', 'Гидрожелонка'])

        self.grid = QGridLayout(self)

        self.grid.addWidget(self.date_work_label, 4, 2)
        self.grid.addWidget(self.date_work_line, 5, 2)

        self.grid.addWidget(self.select_type_combo_label, 4, 3)
        self.grid.addWidget(self.select_type_combo, 5, 3)

        self.select_type_combo.currentTextChanged.connect(self.update_select_type_combo)

        self.complications_during_tubing_running_label = QLabel('Осложнение при спуске НКТ')
        self.complications_of_failure_label = QLabel('Получен ли прихват, наличие рассхаживания')
        self.complications_when_lifting_label = QLabel('Осложнения при подъеме НКТ')
        self.nkt_48_lenght_label = QLabel('Длина на спуск НКТ48')
        self.nkt_48_count_label = QLabel('Кол-во на спуск НКТ48')
        self.nkt_60_lenght_label = QLabel('Длина на спуск НКТ60')
        self.technological_crap_question_label = QLabel('Был ли тех. отстой')
        self.nkt_60_count_label = QLabel('Кол-во на спуск НКТ60')
        self.nkt_73_lenght_label = QLabel('Длина НКТ73')
        self.nkt_73_count_label = QLabel('Кол-во НКТ73')
        self.nkt_89_lenght_label = QLabel('Длина НКТ89-102')
        self.nkt_89_count_label = QLabel('Кол-во НКТ89-102')
        self.volume_well_flush_label = QLabel('Объем промывки')
        self.solvent_injection_label = QLabel('Закачка растворителя')
        self.nkt_is_same_label = QLabel('Кол-во НКТ на подъем совпадает со спуском')
        self.normalization_question_label = QLabel('Была ли нормализация')
        self.interval_skm_text_label = QLabel('Интервалы скреперования')
        self.count_of_nkt_extensions_label = QLabel('Кол-во метров скреперования')

    def update_select_type_combo(self, index):

        self.complications_during_tubing_running_combo = QComboBox(self)
        self.complications_during_tubing_running_combo.addItems(['Нет', 'Да'])

        self.complications_of_failure_combo = QComboBox(self)
        self.complications_of_failure_combo.addItems(['Нет', 'Да'])

        self.complications_when_lifting_combo = QComboBox(self)
        self.complications_when_lifting_combo.addItems(['Нет', 'Да'])

        # self.grid.addWidget(self.complications_of_failure_label, 10, 1)
        # self.grid.addWidget(self.complications_of_failure_combo, 11, 1)

        self.nkt_label()

        self.grid.addWidget(self.complications_during_tubing_running_label, 26, 1)
        self.grid.addWidget(self.complications_during_tubing_running_combo, 27, 1)

        self.grid.addWidget(self.complications_of_failure_label, 28, 1)
        self.grid.addWidget(self.complications_of_failure_combo, 29, 1)



        self.grid.addWidget(self.complications_when_lifting_label, 46, 1)
        self.grid.addWidget(self.complications_when_lifting_combo, 47, 1)

        self.solvent_injection_combo = QComboBox(self)
        self.solvent_injection_combo.addItems(['Нет', 'Да'])

        self.grid.addWidget(self.solvent_injection_label, 32, 1)
        self.grid.addWidget(self.solvent_injection_combo, 33, 1)

        self.nkt_is_same_combo = QComboBox(self)
        self.nkt_is_same_combo.addItems(['Да', 'Нет'])

        self.grid.addWidget(self.nkt_is_same_label, 34, 1)
        self.grid.addWidget(self.nkt_is_same_combo, 35, 1)

        self.normalization_question_combo = QComboBox(self)
        self.normalization_question_combo.addItems(['Нет', 'Да'])

        self.grid.addWidget(self.normalization_question_label, 70, 1)
        self.grid.addWidget(self.normalization_question_combo, 71, 1)

        self.technological_crap_question_combo = QComboBox(self)
        self.technological_crap_question_combo.addItems(['Нет', 'Да'])

        self.grid.addWidget(self.technological_crap_question_label, 52, 1)
        self.grid.addWidget(self.technological_crap_question_combo, 53, 1)

        self.equipment_audit_label = QLabel('Была ли ревизия')
        self.equipment_audit_combo = QComboBox(self)
        self.equipment_audit_combo.addItems(['Нет', 'Да'])

        self.grid.addWidget(self.equipment_audit_label, 94, 1)
        self.grid.addWidget(self.equipment_audit_combo, 95, 1)

        self.equipment_audit_combo.currentTextChanged.connect(self.update_equipment_audit_combo)
        # self.pressuar_gno_combo.currentTextChanged.connect(self.update_pressuar_gno_combo)
        self.technological_crap_question_combo.currentTextChanged.connect(self.update_technological_crap_question_combo)
        self.solvent_injection_combo.currentTextChanged.connect(self.update_solvent_injection_combo)
        # self.pressuar_gno_combo.currentTextChanged.connect(self.update_pressuar_gno_combo)
        self.normalization_question_combo.currentTextChanged.connect(self.update_normalization_question_combo)
        self.complications_of_failure_combo.currentTextChanged.connect(self.update_complications_of_failure)
        self.complications_when_lifting_combo.currentTextChanged.connect(self.update_complications_when_lifting)

        self.complications_during_tubing_running_combo.currentTextChanged.connect(
            self.update_complications_during_tubing_running_combo)
        self.nkt_is_same_combo.currentTextChanged.connect(self.update_nkt_is_same_combo)
        self.interval_skm_text_edit = QLineEdit(self)

        self.count_of_nkt_extensions_line = QLineEdit(self)
        self.count_of_nkt_extensions_line.setValidator(self.validator_float)

        if index in ['ПСШ', 'печать', 'магнит', 'КОТ', 'Гидрожелонка']:

            self.grid.addWidget(self.interval_skm_text_label, 30, 1)
            self.grid.addWidget(self.interval_skm_text_edit, 31, 1)

            self.grid.addWidget(self.count_of_nkt_extensions_label, 30, 2)
            self.grid.addWidget(self.count_of_nkt_extensions_line, 31, 2)

            self.volume_well_flush_line = QLineEdit(self)
            self.volume_well_flush_line.setValidator(self.validator_float)

            self.grid.addWidget(self.volume_well_flush_label, 30, 3)
            self.grid.addWidget(self.volume_well_flush_line, 31, 3)

            if index == 'ПСШ':
                self.interval_skm_text_edit.editingFinished.connect(self.update_interval_skm)
            elif index in ['печать', 'магнит']:
                self.interval_skm_text_label.setText('текст работы печатью или магнитом')
                self.count_of_nkt_extensions_label.setText('Кол-во раз работы')
                self.count_of_nkt_extensions_line.setText('1')
            elif index in ['КОТ']:
                self.interval_skm_text_label.setText('текст работы КОТ или ГВЖ')
                self.count_of_nkt_extensions_label.setText('Кол-во раз работы')
                self.count_of_nkt_extensions_line.setText('1')



        else:
            try:
                self.interval_skm_text_label.setParent(None)
                self.interval_skm_text_edit.setParent(None)
                self.count_of_nkt_extensions_label.setParent(None)
                self.count_of_nkt_extensions_line.setParent(None)
            except:
                pass

    def update_interval_skm(self):
        text = self.interval_skm_text_edit.text()
        count_skm = 0
        if ',' in text and '-' in text:
            for interval in text.split(','):
                if len(interval.split('-')) == 2:
                    roof, sole = list(map(int, interval.split('-')))
                    count_skm += (sole - roof)
        elif '-' in text:
            if len(text.split('-')) == 2:
                roof, sole = list(map(int, text.split('-')))
                count_skm += int((sole - roof))

        self.count_of_nkt_extensions_line.setText(str(count_skm))

    def update_date_when_lifting(self):
        time_begin = self.complications_when_lifting_time_begin_date.dateTime()
        time_end = self.complications_when_lifting_time_end_date.dateTime()

        time_difference = self.calculate_date(time_begin, time_end)
        self.complications_when_lifting_time_line.setText(str(time_difference))

    def update_esp_dismantling_time(self):
        time_end = self.esp_dismantling_time_end_date.dateTime()
        time_begin = self.esp_dismantling_time_begin_date.dateTime()

        time_difference = self.calculate_date(time_begin, time_end)
        self.esp_dismantling_time_line.setText(str(time_difference))

    def update_date_during_disassembly_q(self):
        time_begin = self.complications_during_disassembly_q_time_begin_date.dateTime()
        time_end = self.complications_during_disassembly_q_time_end_date.dateTime()

        time_difference = self.calculate_date(time_begin, time_end)
        self.complications_during_disassembly_time_line.setText(str(time_difference))

    def update_date_of_normalization(self):
        time_begin = self.normalization_question_time_begin_date.dateTime()
        time_end = self.normalization_question_time_end_date.dateTime()

        time_difference = self.calculate_date(time_begin, time_end)
        self.normalization_question_time_line.setText(str(time_difference))

    def update_date_technological_crap(self):
        time_begin = self.technological_crap_question_time_begin_date.dateTime()
        time_end = self.technological_crap_question_time_end_date.dateTime()

        time_difference = self.calculate_date(time_begin, time_end)

        self.technological_crap_question_time_line.setText(str(time_difference))

    def update_date_of_failure(self):
        time_begin = self.complications_of_failure_time_begin_date.dateTime()
        time_end = self.complications_of_failure_time_end_date.dateTime()

        time_difference = self.calculate_date(time_begin, time_end)
        self.complications_of_failure_time_line.setText(str(time_difference))

    def update_date_tubing_running(self):
        time_begin = self.complications_during_tubing_running_time_begin_date.dateTime()
        time_end = self.complications_during_tubing_running_time_end_date.dateTime()

        time_difference = self.calculate_date(time_begin, time_end)
        self.complications_during_tubing_running_time_line.setText(str(time_difference))

    def update_date_solvent_volume(self):
        time_begin = self.solvent_volume_time_begin_date.dateTime()
        time_end = self.solvent_volume_time_end_date.dateTime()

        time_difference = self.calculate_date(time_begin, time_end)
        self.solvent_volume_time_line.setText(str(time_difference))


class TabWidget(QTabWidget):
    def __init__(self):
        super().__init__()
        self.addTab(TabPage_SO_Timplate(self), 'Шаблон')


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
        self.dict_nkt_up = {}

        self.need_saturation_well_text_line = None
        self.need_saturation_q_text_line = None
        self.cycle_count_combo = None
        self.volume_jamming_line = None
        self.complications_during_disassembly_text_line = None
        self.complications_during_disassembly_time_line = None
        self.complications_when_lifting_text_line = None
        self.complications_when_lifting_time_line = None
        self.complications_when_lifting_time_begin_date = None
        self.complications_when_lifting_time_end_date = None
        self.determination_of_the_weight_text_line = None
        self.fluid_well_line = None
        self.time_work_line = None
        self.source_of_work_line = None
        self.couse_of_work_combo = None
        self.pressuar_gno_text_line = None
        self.complications_of_failure_time_line = None
        self.complications_of_failure_time_begin_date = None
        self.complications_of_failure_time_end_date = None
        self.nkt_48_lenght_edit = None
        self.nkt_48_count_edit = None
        self.nkt_60_lenght_edit = None
        self.coefficient_lifting = 1
        self.nkt_60_count_edit = None
        self.nkt_73_lenght_edit = None
        self.nkt_73_count_edit = None
        self.volume_of_finishing_line = None
        self.volume_flush_line = None
        self.nkt_89_lenght_edit = None
        self.nkt_89_count_edit = None
        self.type_equipment = None

        self.roof_definition_depth_line = None

        self.count_nkt_line = None
        self.pressuar_bop_text_line = None
        self.line_lenght_bop_line = None

        self.count_sections_esp_combo = None
        self.count_sections_ped_combo = None

        self.esp_dismantling_time_begin_date = None
        self.esp_dismantling_time_end_date = None
        self.esp_dismantling_time_line = None

    def add_work(self):
        from main import MyWindow

        current_widget = self.tabWidget.currentWidget()

        self.date_work_line = current_widget.date_work_line.text()
        self.select_type_combo = current_widget.select_type_combo.currentText()
        if self.select_type_combo == '':
            return
        elif self.select_type_combo in ['ПСШ', 'шаблон', 'печать', 'магнит']:
            self.type_equipment = 'Шаблон'
            self.coefficient_lifting = 1.15
            if self.select_type_combo in ['ПСШ', 'печать', 'магнит', 'КОТ', 'Трубный перфоратор', 'Гидрожелонка']:
                if self.select_type_combo in ['ПСШ']:
                    self.type_equipment = 'ПСШ'
                elif self.select_type_combo in ['печать']:
                    self.coefficient_lifting = 1
                    self.type_equipment = 'магнит'
                elif self.select_type_combo in ['магнит']:
                    self.coefficient_lifting = 1
                    self.type_equipment = 'магнит'

                elif self.select_type_combo in ['Гидрожелонка']:
                    self.coefficient_lifting = 1.15
                    self.type_equipment = 'ГВЖ'

                self.interval_skm_text_edit = current_widget.interval_skm_text_edit.text()

                self.count_of_nkt_extensions_line = current_widget.count_of_nkt_extensions_line.text()
                if self.count_of_nkt_extensions_line != '':
                    self.count_of_nkt_extensions_line = int(self.count_of_nkt_extensions_line)
                else:
                    question = QMessageBox.question(self, 'Скреперование', 'Скреперования не было?')
                    if question == QMessageBox.StandardButton.No:
                        return
        elif self.select_type_combo in ['Заглушка']:
            self.coefficient_lifting = 1
            self.type_equipment = 'Заглушка'
        elif self.select_type_combo in ['перо', 'воронка']:
            self.type_equipment = 'Перо, воронка'
            self.coefficient_lifting = 1

        self.nkt_is_same_combo = current_widget.nkt_is_same_combo.currentText()
        self.equipment_audit_combo = current_widget.equipment_audit_combo.currentText()
        if self.equipment_audit_combo == 'Да':
            self.equipment_audit_text_line = current_widget.equipment_audit_text_line.text()

        self.volume_well_flush_line = current_widget.volume_well_flush_line.text().replace(',', '.')
        if self.volume_well_flush_line != ['', None]:
            self.volume_well_flush_line = int(float(self.volume_well_flush_line))
        else:
            question = QMessageBox.question(self, 'Промывка', 'Промывки не было?')
            if question == QMessageBox.StandardButton.No:
                return

        read_data = self.read_nkt_up(current_widget)
        if read_data is None:
            return

        if self.nkt_is_same_combo == 'Нет':
            read_data = self.read_nkt_down(current_widget)
            if read_data is None:
                return
        else:
            self.dict_nkt_up = self.dict_nkt

        self.complications_of_failure_combo = current_widget.complications_of_failure_combo.currentText()
        self.complications_during_tubing_running_combo = current_widget.complications_during_tubing_running_combo.currentText()

        self.solvent_injection_combo = current_widget.solvent_injection_combo.currentText()
        self.technological_crap_question_combo = current_widget.technological_crap_question_combo.currentText()
        self.complications_when_lifting_combo = current_widget.complications_when_lifting_combo.currentText()

        # self.pressuar_gno_combo = current_widget.pressuar_gno_combo.currentText()
        self.normalization_question_combo = current_widget.normalization_question_combo.currentText()

        if self.normalization_question_combo == 'Да':
            self.read_normalization_question(current_widget)

        if self.solvent_injection_combo == 'Да':
            self.read_solvent_volume(current_widget)

        if self.technological_crap_question_combo == 'Да':
            read_data = self.read_technological_crap_question(current_widget)
            if read_data is None:
                return

        if self.complications_of_failure_combo == 'Да':
            read_data = self.read_complications_of_failure(current_widget)
            if read_data is None:
                return

        if self.complications_during_tubing_running_combo == 'Да':
            read_data = self.read_complications_during_tubing_running_combo(current_widget)
            if read_data is None:
                return


        if self.complications_when_lifting_combo == 'Да':
            read_data = self.read_complications_when_lifting(current_widget)
            if read_data is None:
                return


        if len(self.dict_nkt) == 0:
            question = QMessageBox.question(self, 'Ошибка', f'НКТ отсутствуют?')
            if question == QMessageBox.StandardButton.No:
                return
        if len(self.dict_nkt_up) == 0 and self.nkt_is_same_combo == 'Нет':
            question = QMessageBox.question(self, 'Ошибка', f'НКТ отсутствуют?')
            if question == QMessageBox.StandardButton.No:
                return

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
        if self.select_type_combo in ['ПСШ']:
            work_list = [
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
                 'М/ж спайдера  (установка шаблон, СКМ, шаблон + обтиратор)', None, None, None, None, None, None,
                 None, None, None, None, None, None, '§185разд.1', None, 'час', 1, 0.07, 1, '=V445*W445*X445',
                 '=Y445-AA445-AB445-AC445-AD445', None, None, None, None, None],
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', self.type_equipment, 'ПЗР СПО ПЕРО ШАБЛОН',
                 None,
                 None, None, None,
                 None, None, None, None, None, None, None, None, '§176разд.1', None, 'шт', 1, 0.52, 1,
                 '=V446*W446*X446', '=Y446-AA446-AB446-AC446-AD446', None, None, None, None, None],
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', self.type_equipment, 'ПЗР СПО ПСШ', None, None,
                 None, None, None,
                 None,
                 None, None, None, None, None, None, '§178разд.1', None, 'шт', 1, 1.27, 1, '=V447*W447*X447',
                 '=Y447-AA447-AB447-AC447-AD447', None, None, None, None, None]]
        elif self.select_type_combo in ['шаблон']:
            work_list = [
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'М/ж спайдера', None, None, None, None, None,
                 None, None, None, None, None, None, None, '§185разд.1', None, 'час', 1, 0.07, 1, '=V483*W483*X483',
                 '=Y483-AA483-AB483-AC483-AD483', None, None, None, None, None],
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', self.type_equipment, 'ПЗР СПО ПЕРО ШАБЛОН', None, None, None,
                 None, None,
                 None, None, None, None, None, None, None, '§176разд.1', None, 'шт', 1, 0.52, 1, '=V484*W484*X484',
                 '=Y484-AA484-AB484-AC484-AD484', None, None, None, None, None]]
        elif self.select_type_combo in ['перо', 'воронка', 'КОТ']:
            work_list = [
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', 'Перо,воронка', 'ПЗР СПО работы перед спуском  НКТ ',
                 None, None, None, None,
                 None, None, None, None, None, None, None, None, '§177разд.1', None, 'шт', 1, 0.17, 1,
                 '=V530*W530*X530', '=Y530-AA530-AB530-AC530-AD530', None, None, None, None, None]]
        elif self.select_type_combo in ['печать']:
            self.type_equipment = 'печать'
            work_list = [
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', 'магнит', 'ПЗР СПО НКТ с магнитом', None, None, None,
                 None, None, None, None, None, None, None, None, None, '§269разд.1', None, 'шт', 1, 0.38, 1,
                 '=V639*W639*X639', '=Y639-AA639-AB639-AC639-AD639', None, None, None, None, None]]

        elif self.select_type_combo in ['магнит']:
            self.type_equipment = 'магнит'
            work_list = [
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'спо', 'Печать', 'ПЗР СПО НКТ с печатью', None, None, None,
                 None, None, None, None, None, None, None, None, None, '§269разд.1', None, 'шт', 1, 0.38, 1,
                 '=V639*W639*X639', '=Y639-AA639-AB639-AC639-AD639', None, None, None, None, None]]

        if len(self.dict_nkt) != 0:
            work_list.extend(self.descent_nkt_work())

        if self.complications_during_tubing_running_combo == 'Да':
            complications_during_tubing_running_list = [
                '=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', self.type_equipment,
                f'{self.complications_during_tubing_running_text_line} '
                f'{self.complications_during_tubing_running_time_begin_date}-'
                f'{self.complications_during_tubing_running_time_end_date}', None, None, None, None, None,
                None, 'Объем', None, 'АКТ№', None, None, None, 'факт', None, 'час',
                self.complications_during_tubing_running_time_line - 0.3, 1, 1, '=V280*W280*X280',
                '=Y280-AA280-AB280-AC280-AD280', None, None, None, None, None]
            work_list.append(complications_during_tubing_running_list)

            self.date_work_line = self.complications_during_tubing_running_time_end_date.split(' ')[0]

        if self.complications_of_failure_combo == 'Да':
            complications_of_failure_list = [
                '=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
                f'{self.complications_of_failure_text_line} {self.complications_of_failure_time_begin_date}-'
                f'{self.complications_of_failure_time_end_date}', None, None, None, None, None,
                None, None, None, 'АКТ№', None, None, None, 'факт', None, 'час',
                self.complications_of_failure_time_line, 1, 1, '=V280*W280*X280',
                '=Y280-AA280-AB280-AC280-AD280', None, None, None, None, None]
            work_list.append(complications_of_failure_list)
            self.date_work_line = self.complications_of_failure_time_end_date.split(' ')[0]

        if self.select_type_combo in ['ПСШ']:
            if self.count_of_nkt_extensions_line != 0:
                work_list.extend(self.skm_work())

        if self.select_type_combo not in ['ПСШ']:
            work_list.extend(self.installation_of_washing_equipment())

        if self.volume_well_flush_line != '' and self.select_type_combo not in ['печать', 'магнит']:
            work_list.extend(self.volume_well_work())

        if self.select_type_combo == 'печать':
            work_list.extend(self.print_work())
        elif self.select_type_combo == 'КОТ':
            work_list.extend(self.kot_work())
        elif self.select_type_combo == 'Гидрожелонка':
            work_list.extend(self.gvzh_work())

        if self.normalization_question_combo == 'Да':
            normalization_question_list = [
                '=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
                f'{self.normalization_question_text_line} {self.normalization_question_time_begin_date}-'
                f'{self.normalization_question_time_end_date}', None, None, None, None, None,
                None, None, None, 'АКТ№', None, None, None, 'факт', None, 'час',
                self.normalization_question_time_line, 1, 1, '=V280*W280*X280',
                '=Y280-AA280-AB280-AC280-AD280', None, None, None, None, None]
            work_list.append(normalization_question_list)
            self.date_work_line = self.normalization_question_time_end_date.split(' ')[0]

        if self.solvent_injection_combo == 'Да':
            work_list.extend(self.solvent_injection_work())

        if self.technological_crap_question_combo == 'Да':
            technological_crap_question_list = self.descent_nkt_work()

            for row_index, row in enumerate(technological_crap_question_list):
                technological_crap_question_list[row_index][13] = self.count_nkt_line * 10
                technological_crap_question_list[row_index][21] = self.count_nkt_line

            technological_crap_question_list.extend([
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
                 f'{self.technological_crap_question_text_line} {self.technological_crap_question_time_begin_date}-'
                 f'{self.technological_crap_question_time_end_date}', None, None, None,
                 None, None, None,
                 None, None, 'АКТ№', None, None, None, 'простои', 'Тех. ожидание',
                 'час', self.technological_crap_question_time_line, 1, 1,
                 '=V467*W467*X467',
                 '=Y467-AA467-AB467-AC467-AD467', None, None, None, None, None],
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
                 f'Определение кровли на гл. {self.roof_definition_depth_line}м', None, None,
                 None, None, None, None, None, None, 'АКТ№', None, None, None,
                 '§289разд.1', None, 'шт', 1, 0.17, 1,
                 '=V468*W468*X468', '=Y468-AA468-AB468-AC468-AD468', None, None, None,
                 None, None]])

            work_list.extend(technological_crap_question_list)
            self.date_work_line = self.technological_crap_question_time_end_date.split(' ')[0]

        work_list.extend(self.deinstallation_of_washing_equipment())

        work_list.extend(self.lifting_nkt())
        if self.equipment_audit_combo == 'Да':
            work_list.extend([
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, f'Ревизия:{self.equipment_audit_text_line}',
                 None, None, None, None, None, None, None, None, None, None, None,
                 None, 'факт', None, 'час', 0.5, 1, 1, '=V480*W480*X480', '=Y480-AA480-AB480-AC480-AD480', None,
                 None, None, None, None]]
            )

        return work_list




if __name__ == "__main__":
    # app3 = QApplication(sys.argv)

    app = QApplication(sys.argv)
    window = TemplateWithoutSKM(22, 22)
    window.show()
    sys.exit(app.exec_())
