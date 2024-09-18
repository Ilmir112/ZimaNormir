import sys

from datetime import datetime, timedelta

import well_data
from PyQt5.QtWidgets import QWidget, QLabel, QComboBox, QLineEdit, QGridLayout, QTabWidget, QMainWindow, QPushButton, \
    QMessageBox, QApplication, QHeaderView, QTableWidget, QTableWidgetItem, QTextEdit, QDateEdit, QDateTimeEdit
from normir.TabPageAll import TabPage, TemplateWork


class TabPage_SO_Timplate(TabPage):
    def __init__(self, parent=None):
        super().__init__()

        self.dict_nkt = well_data.dict_nkt

        self.date_work_str = datetime.strptime(self.date_work_line.text(), '%d.%m.%Y')

        self.select_work_of_third_parties_label = QLabel('Выбор оргазинации')
        self.select_work_of_third_parties = QComboBox(self)
        self.select_work_of_third_parties.addItems(
            ['', 'ГИС', 'ПВР на кабеле', 'ГИС - установка ЦЖ', 'Проведение ГРП', 'РУДНГ'])

        self.grid = QGridLayout(self)

        self.grid.addWidget(self.date_work_label, 4, 2)
        self.grid.addWidget(self.date_work_line, 5, 2)

        self.grid.addWidget(self.select_work_of_third_parties_label, 4, 3)
        self.grid.addWidget(self.select_work_of_third_parties, 5, 3)

        self.select_work_of_third_parties.currentTextChanged.connect(self.update_select_work_of_third_parties)

        self.complications_during_tubing_running_label = QLabel('Осложнение при спуске НКТ')
        self.complications_of_failure_label = QLabel('Получен ли прихват, наличие рассхаживания')
        self.complications_when_lifting_label = QLabel('Осложнения при подъеме НКТ')


        self.nkt_60_count_label = QLabel('Кол-во на спуск НКТ60')

        self.pressuar_combo_label = QLabel('Был ли опрессовка колонны после СКО для определения приемистости')

        self.definition_q_label = QLabel('Было ли определение Q после СКО')
        self.extra_work_text_label = QLabel('Текст проведения работ')
        self.depth_zumpf_paker_combo_label = QLabel('Опрессовка ЗУМПФа')
        self.depth_zumpf_paker_label = QLabel('Глубина посадки пакера ЗУМФПа')
        self.solvent_injection_label = QLabel('Закачка растворителя')
        self.nkt_is_same_label = QLabel('Кол-во НКТ на подъем совпадает со спуском')
        self.pressuar_tnkt_label = QLabel('Была ли опрессовка ТНКТ и вымыв шара')
        self.depth_paker_text_label = QLabel('Глубины посадки пакера')
        self.pressuar_ek_label = QLabel('Давление опрессовки')
        self.rezult_pressuar_combo_label = QLabel('Результат опрессовки')
        self.rezult_zumpf_pressuar_combo_label = QLabel('Результат опрессовки')
        self.determination_of_pickup_combo_label = QLabel('Было ли определение Q?')
        self.determination_of_pickup_combo_zumpf_label = QLabel('Было ли определение Q?')
        self.saturation_volume_label = QLabel('объем насыщения')
        self.determination_of_pickup_text_label = QLabel('Текст определение Q')
        self.saturation_volume_zumpf_label = QLabel('Насыщение')
        self.determination_of_pickup_zumpf_text_label = QLabel('Текст определение Q')
        self.response_text_label = QLabel('Текст реагирование')
        self.response_time_begin_label = QLabel('начало реагирования')
        self.response_time_end_label = QLabel('Окончание реагирования')
        self.roof_definition_depth_label = QLabel('Глубина спуск воронки ')
        self.count_nkt_combo_label = QLabel('Была ли допуск НКТ?')

    def update_select_work_of_third_parties(self, index):

        self.extra_work_text_line = QLineEdit(self)

        self.extra_work_time_begin_label = QLabel('начало проведения работ')
        self.extra_work_time_begin_date = QDateTimeEdit(self)
        self.extra_work_time_begin_date.setDisplayFormat("dd.MM.yyyy HH:mm")
        self.extra_work_time_begin_date.setDateTime(self.date_work_str)

        self.extra_work_time_end_label = QLabel('Окончание проведения работ')
        self.extra_work_time_end_date = QDateTimeEdit(self)
        self.extra_work_time_end_date.setDisplayFormat("dd.MM.yyyy HH:mm")
        self.extra_work_time_end_date.setDateTime(self.date_work_str)

        self.extra_work_time_label = QLabel('затраченное время')
        self.extra_work_time_line = QLineEdit(self)
        self.extra_work_time_line.setValidator(self.validator_float)

        self.grid.addWidget(self.extra_work_text_label, 52, 1)
        self.grid.addWidget(self.extra_work_text_line, 53, 1)
        self.grid.addWidget(self.extra_work_time_begin_label, 52, 2)
        self.grid.addWidget(self.extra_work_time_begin_date, 53, 2)
        self.grid.addWidget(self.extra_work_time_end_label, 52, 3)
        self.grid.addWidget(self.extra_work_time_end_date, 53, 3)
        self.grid.addWidget(self.extra_work_time_label, 52, 4)
        self.grid.addWidget(self.extra_work_time_line, 53, 4)

        self.extra_work_time_end_date.dateTimeChanged.connect(self.update_date_technological_crap)
        self.extra_work_time_begin_date.dateTimeChanged.connect(
            self.update_date_technological_crap)

        if index in ['ГИС - установка ЦЖ', 'Фондовый пакер']:
            self.extra_work_text_line.setText('ГИС - установка ЦЖ в инт. ')

            self.response_text_line = QLineEdit(self)

            self.response_time_begin_date = QDateTimeEdit(self)
            self.response_time_begin_date.setDisplayFormat("dd.MM.yyyy HH:mm")
            self.response_time_begin_date.setDateTime(self.date_work_str)

            self.response_time_end_date = QDateTimeEdit(self)
            self.response_time_end_date.setDisplayFormat("dd.MM.yyyy HH:mm")
            self.response_time_end_date.setDateTime(self.date_work_str)

            self.response_time_line_label = QLabel('Затраченное время')
            self.response_time_line = QLineEdit(self)
            if index in ['ГИС - установка ЦЖ']:
                self.pressuar_combo = QComboBox(self)
                self.pressuar_combo.addItems(['Нет', 'Да'])

                self.grid.addWidget(self.pressuar_combo_label, 62, 0)
                self.grid.addWidget(self.pressuar_combo, 63, 0)

            self.grid.addWidget(self.response_text_label, 60, 1)
            self.grid.addWidget(self.response_text_line, 61, 1)

            self.grid.addWidget(self.response_time_begin_label, 60, 2)
            self.grid.addWidget(self.response_time_begin_date, 61, 2)

            self.grid.addWidget(self.response_time_end_label, 60, 3)
            self.grid.addWidget(self.response_time_end_date, 61, 3)

            self.grid.addWidget(self.response_time_line_label, 60, 4)
            self.grid.addWidget(self.response_time_line, 61, 4)

            self.response_time_end_date.dateTimeChanged.connect(self.update_date_response)
            self.response_time_begin_date.dateTimeChanged.connect(
                self.update_date_response)

            self.response_text_line.setText('ОЗЦ')
            if index == 'Фондовый пакер':
                self.response_text_line.setText('Интерпретация данных ГИС ')

                self.extra_work_text_line.setText('ГИС - РГД ')

    def update_pressuar_combo(self, index):
        if index == 'Нет':
            self.rezult_pressuar_combo.setParent(None)
            self.pressuar_ek_line.setParent(None)
            self.pressuar_ek_label.setParent(None)
            self.rezult_pressuar_combo_label.setParent(None)

            self.depth_paker_text_edit.setParent(None)
            self.depth_paker_text_label.setParent(None)
        else:

            self.depth_paker_text_edit = QLineEdit(self)
            self.rezult_pressuar_combo = QComboBox(self)
            self.rezult_pressuar_combo.addItems(['+', '-'])

            self.pressuar_ek_line = QLineEdit(self)
            self.pressuar_ek_line.setValidator(self.validator_float)

            self.grid.addWidget(self.depth_paker_text_label, 66, 1)
            self.grid.addWidget(self.depth_paker_text_edit, 67, 1)

            self.grid.addWidget(self.pressuar_ek_label, 66, 2)
            self.grid.addWidget(self.pressuar_ek_line, 67, 2)
            self.grid.addWidget(self.rezult_pressuar_combo_label, 66, 3)
            self.grid.addWidget(self.rezult_pressuar_combo, 67, 3)

    def update_date_technological_crap(self):
        time_begin = self.extra_work_time_begin_date.dateTime()
        time_end = self.extra_work_time_end_date.dateTime()

        time_difference = self.calculate_date(time_begin, time_end)

        self.extra_work_time_line.setText(str(time_difference))

    def update_date_response(self):
        time_begin = self.response_time_begin_date.dateTime()
        time_end = self.response_time_end_date.dateTime()

        time_difference = self.calculate_date(time_begin, time_end)

        self.response_time_line.setText(str(time_difference))


class TabWidget(QTabWidget):
    def __init__(self):
        super().__init__()
        self.addTab(TabPage_SO_Timplate(self), 'пакер')


class WorkOfThirdPaties(TemplateWork):
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
        self.pressuar_ek_line = None

        self.volume_of_finishing_line = None
        self.volume_flush_line = None

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
        self.select_work_of_third_parties = current_widget.select_work_of_third_parties.currentText()

        if self.select_work_of_third_parties == '':
            return

        elif self.select_work_of_third_parties in ['ГИС - установка ЦЖ']:

            self.pressuar_combo = current_widget.pressuar_combo.currentText()
            if self.pressuar_combo == 'Да':
                self.depth_paker_text_edit = current_widget.depth_paker_text_edit.text()

                self.pressuar_ek_line = current_widget.pressuar_ek_line.text()
                if self.pressuar_ek_line != '':
                    self.pressuar_ek_line = int(self.pressuar_ek_line)
                else:
                    question = QMessageBox.question(self, 'Давление', 'Не указано давление опрессовки?')
                    if question == QMessageBox.StandardButton.No:
                        return

                self.rezult_pressuar_combo = current_widget.rezult_pressuar_combo.currentText()

            read_data = self.read_responce(current_widget)
            if read_data is None:
                read_data

        read_data = self.read_extra_work(current_widget)
        if read_data is None:
            read_data

        work_list = self.depth_paker_work()

        well_data.date_work = self.date_work_line

        self.populate_row(self.ins_ind, work_list, self.table_widget)
        well_data.pause = False
        self.close()

    def depth_paker_work(self):
        work_list = []
        if self.select_work_of_third_parties in ['ГИС - установка ЦЖ']:
            work_list.extend(self.install_zh())
        elif self.select_work_of_third_parties in ['ПВР на кабеле']:
            work_list.extend((self.perforation_work()))
        elif self.select_work_of_third_parties in ['Проведение ГРП', 'РУДНГ']:
            work_list.extend((self.work_grp()))
        elif self.select_work_of_third_parties in ['ГИС']:
            work_list.extend((self.work_gis()))

        return work_list

    def work_gis(self):
        work_list = [
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'ГИС', 'ГК ЛМ', 'ПЗР работы перед ГФИ', None, None, None, None, None,
             None, None, None, None, None, None, None, '§307разд.1', None, 'раз', 1, 1.4, 1, '=V347*W347*X347',
             '=Y347-AA347-AB347-AC347-AD347', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
             f'{self.extra_work_text_line} {self.extra_work_time_begin_date}-{self.extra_work_time_end_date}',
             None, None, None,
             None, None, None, None, None, 'АКТ№', None, None, None, 'Простои', 'Тех. ожидание', 'час',
             self.extra_work_time_line, 1, 1, '=V391*W391*X391', '=Y391-AA391-AB391-AC391-AD391',
             None, None, None, None, None]
        ]
        return work_list

    def perforation_work(self):
        work_list = [
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'ГИС', 'ГК ЛМ', 'ПЗР работы перед ГФИ', None, None, None, None, None,
             None, None, None, None, None, None, None, '§307разд.1', None, 'раз', 1, 1.4, 1, '=V347*W347*X347',
             '=Y347-AA347-AB347-AC347-AD347', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'ГИС', 'ПВР',
             f'{self.extra_work_text_line} {self.extra_work_time_begin_date}-{self.extra_work_time_end_date}',
             None, None, None, None, None, None,
             None, None, 'АКТ№', None, None, None, 'Факт', None, 'час', self.extra_work_time_line, 1, 1,
             '=V350*W350*X350',
             '=Y350-AA350-AB350-AC350-AD350', None, None, None, None, None],
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
             'Д/ж и м/ж спайдера', None, None, None, None, None, None, None,
             None, None, None, None, None, '§185разд.1', None, 'раз', 1, 0.14, 1, '=X351*W351*V351',
             '=Y351-AA351-AB351-AC351-AD351', None, None, None, None, None]
        ]
        return work_list

    def work_grp(self):
        work_list = [
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
             f'{self.extra_work_text_line} {self.extra_work_time_begin_date}-{self.extra_work_time_end_date}',
             None, None, None,
             None, None, None, None, None, 'АКТ№', None, None, None, 'Простои', 'Тех. ожидание', 'час',
             self.extra_work_time_line, 1, 1, '=V391*W391*X391', '=Y391-AA391-AB391-AC391-AD391',
             None, None, None, None, None]]
        return work_list

    def install_zh(self):
        work_list = [
            ['=ROW()-ROW($A$46)', self.date_work_line, None, 'ГИС', 'Прочие',
             f'{self.extra_work_text_line} {self.extra_work_time_begin_date}-{self.extra_work_time_end_date}',
             None, None, None, None, None, None, None, None, 'АКТ№', 'ЦЕМЕНТ', 'Цемент', 0.2, 'Факт', None, 'час',
             5, 1, 1, '=V353*W353*X353', '=Y353-AA353-AB353-AC353-AD353', None, None, None, None, None]
        ]
        work_list.extend([['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
                           'Д/ж и м/ж спайдера', None, None, None, None, None, None, None,
                           None, None, None, None, None, '§185разд.1', None, 'раз', 1, 0.14, 1, '=X351*W351*V351',
                           '=Y351-AA351-AB351-AC351-AD351', None, None, None, None, None]])
        if self.response_text_line != '':
            work_list.extend(
                [['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', 'ОЗЦ',
                  f'{self.response_text_line} ({self.response_time_begin_date}-{self.response_time_end_date})', None,
                  None, None, None, None, None,
                  None, None, None, None, None, None, 'Простои', 'Тех. ожидание', 'час', self.response_time_line, 1, 1,
                  '=V389*W389*X389',
                  '=Y389-AA389-AB389-AC389-AD389', None, None, None, None, None]])

        if self.pressuar_combo == 'Да':
            pressuar_list = [
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'ПЗР перед опрессовкой ', None, None, None,
                 None,
                 None, None, None, None, None, None, None, None, '§150/152 разд.1 ', None, 'шт', 1, 0.43, 1,
                 '=V394*W394*X394', '=Y394-AA394-AB394-AC394-AD394', None, None, None, None, None],
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
                 f'Опрессовка по НКТ на Р={self.pressuar_ek_line}атм {self.rezult_pressuar_combo}', None, None,
                 None,
                 None, None, None, None, None, 'АКТ№', None, None, None, '§151 разд.1', None, 'шт', 1, 0.25, 1,
                 '=V395*W395*X395', '=Y395-AA395-AB395-AC395-AD395', None, None, None, None, None],
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
                 'Опрессовка нагнетательной линии ',
                 None, None, None, None, None, None, None, None, None, None, None, None, '§113 разд.1 ', None, 'раз', 1,
                 '=8/60', 1, '=V396*W396*X396', '=Y396-AA396-AB396-AC396-AD396', None, None, None, None, None]]

            work_list.extend(pressuar_list)

        return work_list

    def pressuar_ek_rir(self):
        work_list = []
        if self.count_nkt_combo == 'Да':
            work_list = [
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
                 f'Определение кровли на гл. {self.depth_paker_text_edit}м', None, None, None,
                 None, None, None, None, None, 'АКТ№', None, None, None, '§289разд.1', None, 'шт', 1, 0.17, 1,
                 '=V404*W404*X404', '=Y404-AA404-AB404-AC404-AD404', None, None, None, None, None]]
        if self.pressuar_combo == 'Да':
            pressuar_list = [
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None, 'ПЗР перед опрессовкой ', None, None, None,
                 None,
                 None, None, None, None, None, None, None, None, '§150/152 разд.1 ', None, 'шт', 1, 0.43, 1,
                 '=V394*W394*X394', '=Y394-AA394-AB394-AC394-AD394', None, None, None, None, None],
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
                 f'Опрессовка по НКТ Р={self.pressuar_ek_line}атм {self.rezult_pressuar_combo}', None, None,
                 None,
                 None, None, None, None, None, 'АКТ№', None, None, None, '§151 разд.1', None, 'шт', 1, 0.25, 1,
                 '=V395*W395*X395', '=Y395-AA395-AB395-AC395-AD395', None, None, None, None, None],
                ['=ROW()-ROW($A$46)', self.date_work_line, None, 'Тех.операции', None,
                 'Опрессовка нагнетательной линии',
                 None, None, None, None, None, None, None, None, None, None, None, None, '§113 разд.1 ', None, 'раз', 1,
                 '=8/60', 1, '=V396*W396*X396', '=Y396-AA396-AB396-AC396-AD396', None, None, None, None, None]
            ]

            work_list.extend(pressuar_list)
        return work_list


if __name__ == "__main__":
    # app3 = QApplication(sys.argv)

    app = QApplication(sys.argv)
    window = WorkOfThirdPaties(22, 22)
    window.show()
    sys.exit(app.exec_())
