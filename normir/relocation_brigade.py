import sys
from collections import namedtuple
from normir.files_with_list import cause_presence_of_downtime_list, cause_presence_of_downtime_classifocations_list, \
    operations_of_downtimes_list

from PyQt5.QtGui import QIntValidator, QDoubleValidator
from PyQt5.QtWidgets import QWidget, QLabel, QComboBox, QLineEdit, QGridLayout, QTabWidget, QMainWindow, QPushButton, \
    QMessageBox, QApplication, QHeaderView, QTableWidget, QTableWidgetItem, QTextEdit
from PyQt5.QtCore import Qt

import well_data


class TextEditTableWidgetItem(QTableWidgetItem):
    """Класс, который использует QTextEdit для переноса текста в ячейках."""

    def __init__(self, text):
        super().__init__(text)
        # Устанавливаем флаг, чтобы ячейка не была редактируемой напрямую
        self.setFlags(Qt.ItemIsEnabled)


class TabPage_SO_Relocation(QWidget):
    def __init__(self, parent=None):
        super().__init__()

        self.validator_int = QIntValidator(0, 600)
        self.validator_float = QDoubleValidator(0, 5000, 1)

        self.old_well_label = QLabel('Старая скважина')
        self.old_well_line = QLineEdit(self)

        self.new_well_label = QLabel('Новая скважина')
        self.new_well_line = QLineEdit(self)
        self.new_well_line.setText(f'{well_data.well_number._value} {well_data.well_area._value}')

        self.satisfactory_road_true_label = QLabel('Наличие удовлетворительной дороги')
        self.satisfactory_road_true_combo = QComboBox(self)
        self.satisfactory_road_true_combo.addItems(['Нет', 'Да'])

        self.satisfactory_road_label = QLabel('Переезд по удовлетворительной дороге, км')
        self.satisfactory_road_line = QLineEdit(self)
        self.satisfactory_road_line.setValidator(self.validator_float)

        self.unsatisfactory_road_true_label = QLabel('Наличие неудовлетворительной дороги')
        self.unsatisfactory_road_true_combo = QComboBox(self)
        self.unsatisfactory_road_true_combo.addItems(['Нет', 'Да'])

        self.unsatisfactory_road_label = QLabel('Переезд по неудовлетворительной дороге, км')
        self.unsatisfactory_road_line = QLineEdit(self)
        self.unsatisfactory_road_line.setValidator(self.validator_float)

        self.count_of_equipment_label = QLabel('Кол-во техники, и рейсов')
        self.count_of_equipment_line = QLineEdit(self)

        self.usage_k_label = QLabel('Переезд с К-700, T-150')
        self.usage_k_combo = QComboBox(self)
        self.usage_k_combo.addItems(['Нет', 'Да'])

        self.usage_k_road_label = QLabel('километраж с помощью K-700, T-150, км')
        self.usage_k_road_line = QLineEdit(self)
        self.usage_k_road_line.setValidator(self.validator_float)

        self.usage_two_road_true_label = QLabel('Переезд (буксировка двойной тягой)')
        self.usage_two_road_true_combo = QComboBox(self)
        self.usage_two_road_true_combo.addItems(['Нет', 'Да'])

        self.usage_two_road_label = QLabel('фактическое время')
        self.usage_two_road_line = QLineEdit(self)
        self.usage_two_road_line.setValidator(self.validator_float)

        self.usage_buildozer_true_label = QLabel('Переезд (с помощью бульдозера)')
        self.usage_buildozer_true_combo = QComboBox(self)
        self.usage_buildozer_true_combo.addItems(['Нет', 'Да'])

        self.usage_buildozer_label = QLabel('фактическое время')
        self.usage_buildozer_line = QLineEdit(self)
        self.usage_buildozer_line.setValidator(self.validator_float)

        self.lift_installation_label = QLabel('Монтаж Подьемника')
        self.lift_installation_combo = QComboBox(self)
        self.lift_installation_combo.addItems(['', 'СУРС-40', 'АЗИНМАШ-37А (Оснастка 2×3)', 'АПРС-32 (Оснастка 2×3)',
                                               'АПРС-40 (Оснастка 2×3)', 'АПРС-40 (Оснастка 3×4)',
                                               'АПРС-50 (Оснастка 3×4)',
                                               'АПР60/80 (Оснастка 3×4)', 'УПА-60/80 (Оснастка 3×4)',
                                               'УПТ-32 (Оснастка 3×4)', 'БАРС 60/80'])
        self.lift_installation_combo.setCurrentText(well_data.lifting_unit_combo)

        self.anchor_lifts_label = QLabel('монтаж якорей')
        self.anchor_lifts_combo = QComboBox(self)
        self.anchor_lifts_combo.addItems(['Нет', 'Да'])

        self.territory_planning_label = QLabel('Планировка территории перед м/ж подъемника')
        self.territory_planning_combo = QComboBox(self)
        self.territory_planning_combo.addItems(['Нет', 'Да'])

        self.presence_of_downtime_label = QLabel('Наличие простоя при переезде')
        self.presence_of_downtime_combo = QComboBox(self)
        self.presence_of_downtime_combo.addItems(['Нет', 'Да'])



        self.grid = QGridLayout(self)

        self.date_work_label = QLabel('Дата работы')
        self.date_work_line = QLineEdit(self)

        if well_data.date_work != '':
            self.date_work_line.setText(well_data.date_work)

        self.grid.addWidget(self.date_work_label, 4, 2)
        self.grid.addWidget(self.date_work_line, 5, 2)

        self.grid.addWidget(self.old_well_label, 4, 3)
        self.grid.addWidget(self.old_well_line, 5, 3)

        self.grid.addWidget(self.new_well_label, 4, 4)
        self.grid.addWidget(self.new_well_line, 5, 4)

        self.grid.addWidget(self.satisfactory_road_true_label, 6, 2)
        self.grid.addWidget(self.satisfactory_road_true_combo, 7, 2)

        self.grid.addWidget(self.satisfactory_road_label, 6, 3)
        self.grid.addWidget(self.satisfactory_road_line, 7, 3)

        self.grid.addWidget(self.unsatisfactory_road_true_label, 6, 4)
        self.grid.addWidget(self.unsatisfactory_road_true_combo, 7, 4)

        self.grid.addWidget(self.unsatisfactory_road_label, 6, 5)
        self.grid.addWidget(self.unsatisfactory_road_line, 7, 5)

        self.grid.addWidget(self.count_of_equipment_label, 6, 6)
        self.grid.addWidget(self.count_of_equipment_line, 7, 6)

        self.grid.addWidget(self.usage_k_label, 8, 2)
        self.grid.addWidget(self.usage_k_combo, 9, 2)

        self.grid.addWidget(self.usage_k_road_label, 8, 3)
        self.grid.addWidget(self.usage_k_road_line, 9, 3)

        self.grid.addWidget(self.usage_two_road_true_label, 10, 2)
        self.grid.addWidget(self.usage_two_road_true_combo, 11, 2)

        self.grid.addWidget(self.usage_two_road_label, 10, 3)
        self.grid.addWidget(self.usage_two_road_line, 11, 3)

        self.grid.addWidget(self.usage_buildozer_true_label, 12, 2)
        self.grid.addWidget(self.usage_buildozer_true_combo, 13, 2)

        self.grid.addWidget(self.usage_buildozer_label, 12, 3)
        self.grid.addWidget(self.usage_buildozer_line, 13, 3)

        self.grid.addWidget(self.lift_installation_label, 8, 4)
        self.grid.addWidget(self.lift_installation_combo, 9, 4)

        self.grid.addWidget(self.anchor_lifts_label, 8, 5)
        self.grid.addWidget(self.anchor_lifts_combo, 9, 5)

        self.grid.addWidget(self.territory_planning_label, 8, 6)
        self.grid.addWidget(self.territory_planning_combo, 9, 6)

        self.grid.addWidget(self.presence_of_downtime_label, 14, 2)
        self.grid.addWidget(self.presence_of_downtime_combo, 15, 2)

        self.presence_of_downtime_combo.currentTextChanged.connect(self.update_presence_of_downtime_combo)


    def update_presence_of_downtime_combo(self, index):
        if index == 'Да':
            self.cause_presence_of_downtime_label = QLabel('Предварительная причина простоя')
            self.cause_presence_of_downtime_combo = QComboBox(self)

            self.cause_presence_of_downtime_combo.addItems(cause_presence_of_downtime_list)
            self.cause_presence_of_downtime_combo.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContents)

            self.cause_presence_of_downtime_text_label = QLabel('текст простоя')
            self.cause_presence_of_downtime_text_line = QLineEdit(self)

            self.cause_presence_of_downtime_classification_label = QLabel('Классификация простоя')
            self.cause_presence_of_downtime_classification_combo = QComboBox(self)

            self.cause_presence_of_downtime_classification_combo.addItems(
                cause_presence_of_downtime_classifocations_list)
            self.cause_presence_of_downtime_classification_combo.setSizeAdjustPolicy(
                QComboBox.SizeAdjustPolicy.AdjustToContents)

            self.tehnological_operation_label = QLabel('Тип простоя')
            self.tehnological_operation_combo = QComboBox(self)
            self.tehnological_operation_combo.addItems(operations_of_downtimes_list)

            self.time_presence_of_downtime_label = QLabel('Время простоя')
            self.time_presence_of_downtime_line = QLineEdit(self)
            self.time_presence_of_downtime_line.setValidator(self.validator_float)

            self.grid.addWidget(self.presence_of_downtime_label, 14, 2)
            self.grid.addWidget(self.presence_of_downtime_combo, 15, 2)
            self.grid.addWidget(self.cause_presence_of_downtime_label, 14, 3)
            self.grid.addWidget(self.cause_presence_of_downtime_combo, 15, 3)
            self.grid.addWidget(self.cause_presence_of_downtime_text_label, 14, 4)
            self.grid.addWidget(self.cause_presence_of_downtime_text_line, 15, 4)
            self.grid.addWidget(self.cause_presence_of_downtime_classification_label, 14, 5)
            self.grid.addWidget(self.cause_presence_of_downtime_classification_combo, 15, 5)
            self.grid.addWidget(self.tehnological_operation_label, 14, 6)
            self.grid.addWidget(self.tehnological_operation_combo, 15, 6)
            self.grid.addWidget(self.time_presence_of_downtime_label, 14, 7)
            self.grid.addWidget(self.time_presence_of_downtime_line, 15, 7)
        else:
            self.tehnological_operation_label.setParent(None)
            self.tehnological_operation_combo.setParent(None)
            self.cause_presence_of_downtime_label.setParent(None)
            self.cause_presence_of_downtime_combo.setParent(None)
            self.cause_presence_of_downtime_text_label.setParent(None)
            self.cause_presence_of_downtime_text_line.setParent(None)
            self.cause_presence_of_downtime_classification_label.setParent(None)
            self.cause_presence_of_downtime_classification_combo.setParent(None)
            self.cause_presence_of_downtime_classification_combo.setParent(None)
            self.tehnological_operation_label.setParent(None)
            self.tehnological_operation_combo.setParent(None)
            self.time_presence_of_downtime_label.setParent(None)
            self.time_presence_of_downtime_line.setParent(None)

    def update_lifting(self, index):
        if 'АПР60' in index or 'УПА-60' in index or 'БАРС 60/80' in index or 'А-50':
            self.anchor_lifts_combo.setCurrentIndex(1)


class TabWidget(QTabWidget):
    def __init__(self):
        super().__init__()
        self.addTab(TabPage_SO_Relocation(self), 'Переезд')


class Relocation_Window(QMainWindow):
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

        a = well_data.work_list_in_ois

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
        self.old_well_line = None
        self.new_well_line = None
        self.satisfactory_road_line = None
        self.unsatisfactory_road_line = None
        self.count_of_equipment_line = None
        self.unsatisfactory_road_true_combo = None
        self.usage_k_combo = None
        self.usage_k_road_line = None
        self.usage_two_road_true_combo = None
        self.usage_two_road_line = None
        self.usage_buildozer_true_combo = None
        self.usage_buildozer_line = None
        self.lift_installation_combo = None
        self.anchor_lifts_combo = None

        self.presence_of_downtime_combo = None
        self.cause_presence_of_downtime_combo = None
        self.cause_presence_of_downtime_text_line = None
        self.cause_presence_of_downtime_classification_combo = None


        self.tehnological_operation_combo = None

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
        self.presence_of_downtime_combo = current_widget.presence_of_downtime_combo.currentText()
        self.date_work_line = current_widget.date_work_line.text()
        self.old_well_line = current_widget.old_well_line.text()
        self.new_well_line = current_widget.new_well_line.text()
        self.satisfactory_road_line = current_widget.satisfactory_road_line.text()
        self.unsatisfactory_road_line = current_widget.unsatisfactory_road_line.text()
        self.count_of_equipment_line = current_widget.count_of_equipment_line.text()
        self.satisfactory_road_true_combo = current_widget.satisfactory_road_true_combo.currentText()
        self.usage_k_combo = current_widget.usage_k_combo.currentText()
        self.unsatisfactory_road_true_combo = current_widget.unsatisfactory_road_true_combo.currentText()
        self.usage_k_combo = current_widget.usage_k_combo.currentText()
        self.usage_k_road_line = current_widget.usage_k_road_line.text()
        self.usage_two_road_true_combo = current_widget.usage_two_road_true_combo.currentText()
        self.usage_two_road_line = current_widget.usage_two_road_line.text()
        self.usage_buildozer_true_combo = current_widget.usage_two_road_true_combo.currentText()
        self.usage_buildozer_line = current_widget.usage_buildozer_line.text()
        self.lift_installation_combo = current_widget.lift_installation_combo.currentText()
        self.anchor_lifts_combo = current_widget.anchor_lifts_combo.currentText()

        if '' in [self.date_work_line, self.old_well_line, self.new_well_line, self.count_of_equipment_line]:
            QMessageBox.warning(self, 'Ошибка', 'ВВедены не все значения')
            return
        if self.unsatisfactory_road_true_combo == 'Да':
            if self.unsatisfactory_road_line == '':
                QMessageBox.warning(self, 'Ошибка', 'Не указан километраж в не удовлетварительной дороге')
                return
        if self.satisfactory_road_true_combo == 'Да':
            if self.satisfactory_road_line == '':
                QMessageBox.warning(self, 'Ошибка', 'Не указан километраж в не удовлетварительной дороге')
                return
        if self.usage_k_combo == 'Да':
            if self.usage_k_road_line == '':
                QMessageBox.warning(self, 'Ошибка', 'Не указан километраж при переезда К-700')
                return
        if self.usage_two_road_true_combo == 'Да':
            if self.usage_two_road_line == '':
                QMessageBox.warning(self, 'Ошибка', 'Не указано время при двойной тяге')
                return
        if self.usage_buildozer_true_combo == 'Да':
            if self.usage_buildozer_line == '':
                QMessageBox.warning(self, 'Ошибка', 'Не указано время при двойной тяге')
                return

        work_list = self.relocation_def()
        if len(work_list) == 0:
            QMessageBox.warning(self, 'Ошибка', 'Нет данных')
            return
        if self.presence_of_downtime_combo == 'Да':
            work_list.extend(self.presence_of_downtime_def())

        work_list.extend(self.preparatory_work())

        MyWindow.populate_row(self, self.ins_ind, work_list, self.table_widget)
        well_data.pause = False
        self.close()

    def presence_of_downtime_def(self):
        current_widget = self.tabWidget.currentWidget()

        self.cause_presence_of_downtime_text_line = current_widget.cause_presence_of_downtime_text_line.text()
        self.cause_presence_of_downtime_classification_combo = current_widget.cause_presence_of_downtime_classification_combo.currentText()
        self.tehnological_operation_combo = current_widget.tehnological_operation_combo.currentText()
        self.time_presence_of_downtime_line =  current_widget.time_presence_of_downtime_line.text()

        technological_downtime_list = [[
            '=ROW()-ROW($A$46)', self.date_work_line, None, 'простои', self.cause_presence_of_downtime_text_line,
            'По отсутствию подъездных путей',
            None, None,
            None, None, 'классификация простоя', None, self.cause_presence_of_downtime_classification_combo,
            None, None, None, None, None, 'Простои',  self.tehnological_operation_combo, 'час',
            self.time_presence_of_downtime_line, 1, 1, '=V66*W66*X66',
            '=Y66-AA66-AB66-AC66-AD66', None, None, None, None, None]]
        return technological_downtime_list

    def relocation_def(self):

        relocation_list = [[
            '=ROW()-ROW($A$46)', self.date_work_line, None, 'Переезд', None,
            f'ПЗР к переезду (инструктаж (в том числе инструктаж по ТБ), уточнение маршрута транспортировки, '
            f'монтаж-демонтаж крана, выбор площадки под загрузку-разгрузку, маневрирование техники на кусту, '
            f'построение техники в колонну)',
            None, None, None, None,
            None, None, None, None, None, None, None, None, '§302разд1', None, 'опер.', 1,
            1.167, 1, '=X59*W59*V59',
            '=Y59-AA59-AB59-AC59-AD59', None, None, None, None, None]]
        satisfactory_road_list = [[
            '=ROW()-ROW($A$46)', self.date_work_line, None, 'Переезд', None,
            f'Переезд cо скв {self.old_well_line} на скв {self.new_well_line} {self.satisfactory_road_line}км '
            f'({self.count_of_equipment_line})',
            None, None, None, None,
            None, None, None, None, None, None, None, None, '§302разд1', None, 'км', self.satisfactory_road_line,
            0.028, 1, '=X59*W59*V59',
            '=Y59-AA59-AB59-AC59-AD59', None, None, None, None, None]]
        unsatisfactory_road_list = [[
            '=ROW()-ROW($A$46)', self.date_work_line, None, 'Переезд', None,
            f'Переезд (неуд.состояние дорог) cо скв {self.old_well_line} на скв '
            f'{self.new_well_line} {self.satisfactory_road_line}км '
            f'({self.count_of_equipment_line})',
            None, None, None, None, None, None, None, None, None, None, None, None, '§302разд1', None, 'км', 100,
            0.028, 1.5, '=X60*W60*V60', '=Y60-AA60-AB60-AC60-AD60', None, None, None, None, None]]

        road_fact_list = [[
            '=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
            f'Переезд (уд.состояние дорог) (ВРЕМЯ)', None,
            None, None, None, None, None, None, None, None, None, None, None, 'факт', None, 'час', 0.5, 1, 1,
            '=V61*W61*X61', '=Y61-AA61-AB61-AC61-AD61', None, None, None, None, None]]

        towing_k700_list = [[
            '=ROW()-ROW($A$46)', self.date_work_line, None, 'Переезд', None,
            'Переезд на  К-700,Т-150 (прикладывается трекер СПТ)',
            None, None, None, None, None, None, None, None, None, None, None, None, '§302разд1', None, 'км',
            self.usage_k_road_line,
            0.07, 1, '=X62*W62*V62', '=Y62-AA62-AB62-AC62-AD62', None, None, None, None, None]]
        towing_two_list = [[
            '=ROW()-ROW($A$46)', self.date_work_line, None, 'Переезд', None, 'Переезд (буксировка двойной тягой)',
            None, None,
            None, None, None, None, None, None, None, None, None, None, 'Факт', None, 'час', self.usage_two_road_line,
            1, 1,
            '=V63*W63*X63', '=Y63-AA63-AB63-AC63-AD63', None, None, None, None, None]]
        towing_bulldozer_list = [[
            '=ROW()-ROW($A$46)', self.date_work_line, None, 'Переезд', None, 'Переезд (с помощью бульдозера)', None,
            None, None,
            None, None, None, None, None, None, None, None, None, 'Факт', None, 'час', self.usage_buildozer_line, 1, 1,
            '=V64*W64*X64',
            '=Y64-AA64-AB64-AC64-AD64', None, None, None, None, None]]




        if well_data.type_working == 'КРС':
            well_data.type_working_list = [
                ['=ROW()-ROW($A$46)', 'КРС', None, 'ПР.перед.ремонтом', None, 'Работа приёмной комиссии', None, None,
                 None,
                 None, None, None, None, None, None, None, None, None, '§302разд.1', None, 'раз', 1, 1.75, 1,
                 '=V108*W108*X108', '=Y108-AA108-AB108-AC108-AD108', None, None, None, None, None]]
        else:
            well_data.type_working_list = [
                ['=ROW()-ROW($A$46)', 'ПРС', None, 'ПР.перед.ремонтом', None, 'Работа приёмной комиссии', None, None,
                 None,
                 None, None, None, None, None, None, None, None, None, '§302разд.1', None, 'раз', 1, 1.05, 1,
                 '=V109*W109*X109', '=Y109-AA109-AB109-AC109-AD109', None, None, None, None, None]]

        relocation_list.extend(satisfactory_road_list)
        aas = self.unsatisfactory_road_true_combo
        if self.unsatisfactory_road_true_combo == 'Да':
            relocation_list.extend(unsatisfactory_road_list)
        if self.usage_two_road_true_combo == 'Да':
            relocation_list.extend(towing_two_list)
        if self.usage_k_combo == 'Да':
            relocation_list.extend(towing_k700_list)
        if self.usage_buildozer_true_combo == 'Да':
            relocation_list.extend(towing_bulldozer_list)

        return relocation_list

    def select_lifting(self):
        if 'А5-40' in self.lift_installation_combo:
            lift_installation_list = [
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'ПР.перед.ремонтом', None, 'Монтаж А5-40', None, None, None, None,
                 None,
                 None, None, None, None, None, None, None, '§68разд.1', None, 'шт', 1, 1.13, 1, '=V96*W96*X96',
                 '=Y96-AA96-AB96-AC96-AD96', None, None, None, None, None]]
        elif 'СУРС-40' in self.lift_installation_combo:
            lift_installation_list = [
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'ПР.перед.ремонтом', None,
                 'Монтаж СУРС-40 при подготовленной скв.', None,
                 None, None, None, None, None, None, None, "'АКТ №1'!A1", None, None, None,
                 '§68разд.1', None, 'шт', 1, 1.13,
                 1, '=V97*W97*X97', '=Y97-AA97-AB97-AC97-AD97', None, None, None, None,
                 None]]
        elif 'УП 32/40' in self.lift_installation_combo:
            lift_installation_list = [
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'ПР.перед.ремонтом', None,
                 'Монтаж УП 32/40  при подготовленной скв. ',
                 None,
                 None, None, None, None, None, None, None, None, None, None, None, '§62разд.1', None, 'шт', 1, 1.47, 1,
                 '=V98*W98*X98', '=Y98-AA98-AB98-AC98-AD98', None, None, None, None, None]]
        elif 'АПРС-40' in self.lift_installation_combo:
            lift_installation_list = [
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'ПР.перед.ремонтом', None, 'Монтаж подъемника АПРС-40', None, None,
                 None,
                 None, None, None, None, None, None, None, None, None, '§62разд.1', None, 'раз', 1, 1.467, 1,
                 '=V99*W99*X99',
                 '=Y99-AA99-AB99-AC99-AD99', None, None, None, None, None]]
        elif 'АПРС-50' in self.lift_installation_combo:
            lift_installation_list = [
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'ПР.перед.ремонтом', None, 'Монтаж подъемника АПРС-50', None, None,
                 None,
                 None, None, None, None, None, None, None, None, None, '§70разд.1', None, 'раз', 1, 1.67, 1,
                 '=V100*W100*X100',
                 '=Y100-AA100-AB100-AC100-AD100', None, None, None, None, None]]
        elif 'АПР-60/80' in self.lift_installation_combo:
            lift_installation_list = [
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'ПР.перед.ремонтом', None, 'Монтаж подъемника АПР-60/80', None, None,
                 None,
                 None, None, None, None, None, None, None, None, None, '§86разд.1', None, 'шт', 1, 3.21, 1,
                 '=V101*W101*X101',
                 '=Y101-AA101-AB101-AC101-AD101', None, None, None, None, None]]
        elif 'УПА-60' in self.lift_installation_combo:
            lift_installation_list = [
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'ПР.перед.ремонтом', None,
                 'Монтаж подъемника УПА-60  при подготовленной скв.', None, None, None, None, None, None, None, None,
                 None,
                 None, None, None, '§82разд.1', None, 'шт', 1, 4.87, 1, '=V102*W102*X102',
                 '=Y102-AA102-AB102-AC102-AD102',
                 None, None, None, None, None]]
        elif 'А5-40' in self.lift_installation_combo:
            lift_installation_list = [
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'ПР.перед.ремонтом', None,
                 'Центрирование мачты подъемника А5-40 во время монтажа', None, None, None,
                 None, None, None, None, None, None, None, None, None, '§59разд.1', None, 'шт',
                 1, 0.67, 1, '=V103*W103*X103', '=Y103-AA103-AB103-AC103-AD103', None, None,
                 None, None, None]]
        elif 'А-50М' in self.lift_installation_combo:
            lift_installation_list = [
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'ПР.перед.ремонтом', None, 'Монтаж подъемника А-50М', None, None,
                 None,
                 None,
                 None, None, None, None, None, None, None, None, '§72 р.1', None, 'шт', 1, 3.25, 1, '=V104*W104*X104',
                 '=Y104-AA104-AB104-AC104-AD104', None, None, None, None, None]]
        elif 'БАРС-80' in self.lift_installation_combo:
            lift_installation_list = [
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'ПР.перед.ремонтом', None,
                 'Монтаж подъемника БАРС-80-полуприцеп (оснастка 3×4)', None, None, None, None, None, None, None, None,
                 None,
                 None, None, None, '§88разд.1', None, 'шт', 1, 5.85, 1, '=V105*W105*X105',
                 '=Y105-AA105-AB105-AC105-AD105',
                 None, None, None, None, None]]

        if self.anchor_lifts_combo == 'Да':
            anchor_lifts = [
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'Забурка 4-х якорей с перепусканием оттяжек (',
                 None,
                 None, None, None, None, None, None, None, 'АКТ№', 'ЦЕМЕНТ', 'Цемент', 0.5, 'факт', None, 'час', 2, 1,
                 1,
                 '=V106*W106*X106', '=Y106-AA106-AB106-AC106-AD106', None, None, None, None, None],
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Оттяжки', None, 'Установка и испытание якорей', None, None, None,
                 None,
                 None, None, None, None, 'АКТ№', 'ЦЕМЕНТ', 'Цемент', 0.5, '§29,30раз.1', None, 'шт', 4, 0.48, 1,
                 '=V107*W107*X107', '=Y107-AA107-AB107-AC107-AD107', None, None, None, None, None],
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Оттяжки', None, 'Установка и испытание якорей', None, None, None,
                 None,
                 None, None, None, None, "'АКТ №1'!A1", None, None, None, '§29,30раз.1', None, 'шт', 4, 0.48, 1,
                 '=V111*W111*X111', '=Y111-AA111-AB111-AC111-AD111', None, None, None, None, None]]
            lift_installation_list.extend(anchor_lifts)


        return lift_installation_list

    def preparatory_work(self):
        preparatory_work_list = [
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Переезд', None,
             'Отцепка-прицепка  (2 вагона, инструменталка, ЕДК, аквтонаматыватель, беспилотник)',
             None, None, None, None, None, None, None, None, None, None, None, None, '§304разд1',
             None, 'раз', 5, 0.067, 1, '=V70*W70*X70', '=Y70-AA70-AB70-AC70-AD70', None, None,
             None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'ПР.перед.ремонтом', None,
             'Расставить оборудование на кусту скважины согласно схемы ', None,
             None, None, None,
             None, None, None, None,
             None, None, None, None, '§16разд.1', None, 'раз', 5,
             0.09, 1, '=V71*W71*X71',
             '=Y71-AA71-AB71-AC71-AD71', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'ПР.перед.ремонтом', None,
             'Монтаж лестниц и перильных ограждений на вагонах и техемкостях ', None, None, None,
             None,
             None, None, None, None, None, None, None, None, '§86разд.1', None, 'шт', 5, 0.17, 1,
             '=V72*W72*X72',
             '=Y72-AA72-AB72-AC72-AD72', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'ПР.перед.ремонтом', None, 'Разгрузка оборудования',
             None, None, None, None,
             None, None, None, None, None, None, None, None, '§299разд.1', None, 'шт', 1,
             1.58, 1, '=V73*W73*X73',
             '=Y73-AA73-AB73-AC73-AD73', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'ПР.перед.ремонтом', None,
             'Установка  заземления (2 куль.будки, доливная, мостки, площадка,2 щита, ПА)(с испытанием )',
             None, None,
             None, None, None, None, None, None, None, None, None, None, '§33разд.1', None, 'шт',
             10, 0.1, 1,
             '=V74*W74*X74', '=Y74-AA74-AB74-AC74-AD74', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'Сборка линии долива', None,
             None, None, None, None,
             None, None, None, None, None, None, None, '§18разд.1', None, 'шт', 1, 0.22, 1,
             '=V75*W75*X75',
             '=Y75-AA75-AB75-AC75-AD75', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'ПР.перед.ремонтом', None,
             'Размотать электрокабель и подключить оборудование к электросети ', None, None, None,
             None, None, None, None,
             None, None, None, None, None, '§34разд.1', None, 'шт', 4, 0.12, 1,
             '=V76*W76*X76',
             '=Y76-AA76-AB76-AC76-AD76', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'ПР.перед.ремонтом', None,
             'Поднести подставки и подставить их под электрокабель  (1шт.)', None, None, None,
             None, None, None, None,
             None, None, None, None, None, '§35разд.1', None, 'раз', 10, 0.030000000000000002, 1,
             '=V77*W77*X77',
             '=Y77-AA77-AB77-AC77-AD77', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'ПР.перед.ремонтом', None, 'Подключение прожектора',
             None, None, None, None,
             None, None, None, None, None, None, None, None, '§36разд.1', None, 'шт', 1,
             0.08, 1, '=V78*W78*X78',
             '=Y78-AA78-AB78-AC78-AD78', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'ПР.перед.ремонтом', None,
             'Монтаж/демонтаж и проверка работы видеорегистратора', None, None, None, None, None,
             None, None, None, None,
             None, None, None, '§38 разд.1', None, 'раз', 1, 0.2, 1, '=V79*W79*X79',
             '=Y79-AA79-AB79-AC79-AD79', None,
             None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'ПР.перед.ремонтом', None, 'Монтаж ИВЭ-50', None,
             None, None, None, None,
             None, None, None, None, None, None, None, '§25разд.1', None, 'раз', 1, 0.17,
             1, '=V80*W80*X80',
             '=Y80-AA80-AB80-AC80-AD80', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'ПР.перед.ремонтом', None,
             'Монтаж и демонтаж автокрана ', None, None, None,
             None, None, None, None, None, None, None, None, None, '§32разд.1', None, 'шт', 1,
             0.26666666666666666, 1,
             '=V81*W81*X81', '=Y81-AA81-AB81-AC81-AD81', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'ПР.перед.ремонтом', None,
             'Разгрузка и раскатка труб на мостках ', None,
             None, None, None, None, None, None, None, None, None, None, None, '§39разд.1', None,
             'шт', 160, 0.008, 1,
             '=V82*W82*X82', '=Y82-AA82-AB82-AC82-AD82', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'ПР.перед.ремонтом', None,
             'Монтаж  дополнительных стеллажей для труб (облегченная конструкция)', None, None,
             None, None, None, None,
             None, None, None, None, None, None, '§57разд.1', None, 'раз', 3, 0.0867, 1,
             '=V83*W83*X83',
             '=Y83-AA83-AB83-AC83-AD83', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'ПР.перед.ремонтом', None,
             'Монтаж и демонтаж передвижного приемного мостка',
             None, None, None, None, None, None, None, None, None, None, None, None,
             '§58разд.1', None, 'шт', 1,
             0.92, 1, '=V84*W84*X84', '=Y84-AA84-AB84-AC84-AD84', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'ПР.перед.ремонтом', None,
             'Монтаж доп.стеллажей (если штанги)', None, None,
             None, None, None, None, None, None, None, None, None, None, '§35разд.1', None, 'шт',
             4, 0.030000000000000002,
             1, '=V85*W85*X85', '=Y85-AA85-AB85-AC85-AD85', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
             'Установить заглушку на коллектор', None, None, None,
             None, None, None, None, None, None, None, None, None, '§28разд.1', None, 'шт', 1, 0.1,
             1, '=V86*W86*X86',
             '=Y86-AA86-AB86-AC86-AD86', None, None, None, None, None]]

        if well_data.dict_pump_SHGN['do'] != '0' or well_data.dict_pump_SHGN['posle'] != '0':
            preparatory_work_list.pop(-2)
        return preparatory_work_list


if __name__ == "__main__":
    # app3 = QApplication(sys.argv)

    app = QApplication(sys.argv)
    window = Relocation_Window(22, 22)
    window.show()
    sys.exit(app.exec_())
