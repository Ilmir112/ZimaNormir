import json
import well_data

from PyQt5 import QtCore,  QtWidgets
from PyQt5.Qt import *



class TabPageSO(QWidget):
    selected_region = None
    podpis_dict = None

    def __init__(self, parent=None):
        super().__init__(parent)

        # Открытие JSON файла и чтение данных
        with open(f'{well_data.path_image}podpisant.json', 'r', encoding='utf-8') as file:
            self.podpis_dict = json.load(file)
        TabPageSO.podpis_dict = self.podpis_dict

        self.productLavelLabel = QLabel("Заказчик", self)
        self.productLavelType = QComboBox(self)
        self.productLavelType.addItems(["ООО Башнефть_добыча"])

        self.regionLabel = QLabel("Регион", self)
        self.regioncomboBox = QComboBox(self)
        self.region_list = well_data.region_list
        self.regioncomboBox.addItems(self.region_list)
        self.regioncomboBox.currentIndexChanged.connect(self.update_line_edit)

        if 'Ойл' in well_data.contractor and 'Ойл' not in self.productLavelType.currentText():
            self.productLavelType.addItems(['Ойл'])
        elif 'РН' in well_data.contractor and 'РН' not in self.productLavelType.currentText():
            self.productLavelType.addItems(['РН'])

        self.region_select = self.regioncomboBox.currentText()

        self.title_job_Label = QLabel("Должность", self)
        self.surname_Label = QLabel("Фамилия И.О.", self)

        self.chief_Label = QLabel("Руководители региона", self)
        self.head_of_orm_Label = QLabel("Сектор разработки", self)
        self.head_of_gtm_Label = QLabel("Сектор Анализа ГТМ", self)
        self.head_of_go_Label = QLabel("Сектор геологический и ВНС", self)
        self.head_of_grr_Label = QLabel("Сектор геолого-разведки", self)
        self.head_of_usrsist_Label = QLabel("Сектор супервайзерской службы", self)

        self.chief_engineer_edit_type = QLineEdit(self)
        self.chief_engineer_name_edit_type = QLineEdit(self)

        self.chief_geologist_edit_type = QLineEdit(self)
        self.chief_geologist_name_edit_type = QLineEdit(self)

        self.head_of_orm_edit_type = QLineEdit(self)
        self.head_of_orm_name_edit_type = QLineEdit(self)

        self.representative_of_orm_edit_type = QLineEdit(self)
        self.representative_of_orm_name_edit_type = QLineEdit(self)

        self.head_of_gtm_edit_type = QLineEdit(self)
        self.head_of_gtm_name_edit_type = QLineEdit(self)

        self.representative_of_gtm_edit_type = QLineEdit(self)
        self.representative_of_gtm_name_edit_type = QLineEdit(self)

        self.representative_of_go_edit_type = QLineEdit(self)
        self.representative_of_go_name_edit_type = QLineEdit(self)

        self.head_of_usrsist_edit_type = QLineEdit(self)
        self.head_of_usrsist_name_edit_type = QLineEdit(self)

        self.representative_of_grr_edit_type = QLineEdit(self)
        self.representative_of_grr_name_edit_type = QLineEdit(self)

        grid = QGridLayout(self)

        grid.addWidget(self.productLavelLabel, 0, 0)
        grid.addWidget(self.productLavelType, 0, 1)

        grid.addWidget(self.regionLabel, 1, 0)
        grid.addWidget(self.regioncomboBox, 1, 1)

        grid.addWidget(self.chief_Label, 2, 1)
        grid.addWidget(self.title_job_Label, 3, 0)
        grid.addWidget(self.surname_Label, 3, 2)
        grid.addWidget(self.chief_engineer_edit_type, 4, 0)
        grid.addWidget(self.chief_engineer_name_edit_type, 4, 2)
        grid.addWidget(self.chief_geologist_edit_type, 6, 0)
        grid.addWidget(self.chief_geologist_name_edit_type, 6, 2)

        grid.addWidget(self.head_of_orm_Label, 7, 1)

        grid.addWidget(self.head_of_orm_edit_type, 9, 0)
        grid.addWidget(self.head_of_orm_name_edit_type, 9, 2)
        grid.addWidget(self.representative_of_orm_edit_type, 10, 0)
        grid.addWidget(self.representative_of_orm_name_edit_type, 10, 2)

        grid.addWidget(self.head_of_gtm_Label, 11, 1)

        grid.addWidget(self.head_of_gtm_edit_type, 13, 0)
        grid.addWidget(self.head_of_gtm_name_edit_type, 13, 2)
        grid.addWidget(self.representative_of_gtm_edit_type, 14, 0)
        grid.addWidget(self.representative_of_gtm_name_edit_type, 14, 2)

        grid.addWidget(self.head_of_go_Label, 15, 1)

        grid.addWidget(self.representative_of_go_edit_type, 17, 0)
        grid.addWidget(self.representative_of_go_name_edit_type, 17, 2)

        grid.addWidget(self.head_of_grr_Label, 18, 1)

        grid.addWidget(self.representative_of_grr_edit_type, 20, 0)
        grid.addWidget(self.representative_of_grr_name_edit_type, 20, 2)

        grid.addWidget(self.head_of_usrsist_Label, 21, 1)

        grid.addWidget(self.head_of_usrsist_edit_type, 23, 0)
        grid.addWidget(self.head_of_usrsist_name_edit_type, 23, 2)

    def update_line_edit(self):
        selected_region = self.regioncomboBox.currentText()
        TabPageSO.selected_region = selected_region

        self.chief_engineer_edit_type.setText(self.podpis_dict['регион'][selected_region]['gi']['post'])
        self.chief_engineer_name_edit_type.setText(self.podpis_dict['регион'][selected_region]['gi']["surname"])

        self.chief_geologist_edit_type.setText(self.podpis_dict['регион'][selected_region]['gg']['post'])
        self.chief_geologist_name_edit_type.setText(self.podpis_dict['регион'][selected_region]['gg']['surname'])

        self.head_of_orm_edit_type.setText(self.podpis_dict['регион'][selected_region]["ruk_orm"]['post'])
        self.head_of_orm_name_edit_type.setText(self.podpis_dict['регион'][selected_region]["ruk_orm"]['surname'])

        self.representative_of_orm_edit_type.setText(self.podpis_dict['регион'][selected_region]["ved_orm"]['post'])
        self.representative_of_orm_name_edit_type.setText(
            self.podpis_dict['регион'][selected_region]["ved_orm"]['surname'])

        self.head_of_gtm_edit_type.setText(self.podpis_dict['регион'][selected_region]["ruk_gtm"]['post'])
        self.head_of_gtm_name_edit_type.setText(self.podpis_dict['регион'][selected_region]["ruk_gtm"]['surname'])

        self.representative_of_gtm_edit_type.setText(self.podpis_dict['регион'][selected_region]["ved_gtm"]['post'])
        self.representative_of_gtm_name_edit_type.setText(
            self.podpis_dict['регион'][selected_region]["ved_gtm"]['surname'])

        self.representative_of_go_edit_type.setText(self.podpis_dict['регион'][selected_region]["go"]['post'])
        self.representative_of_go_name_edit_type.setText(self.podpis_dict['регион'][selected_region]["go"]['surname'])

        self.head_of_usrsist_edit_type.setText(self.podpis_dict['регион'][selected_region]["usrs"]['post'])
        self.head_of_usrsist_name_edit_type.setText(self.podpis_dict['регион'][selected_region]["usrs"]['surname'])

        self.representative_of_grr_edit_type.setText(self.podpis_dict['регион'][selected_region]["grr"]['post'])
        self.representative_of_grr_name_edit_type.setText(self.podpis_dict['регион'][selected_region]["grr"]['surname'])


class TabWidget(QTabWidget):
    def __init__(self):
        super().__init__()
        self.addTab(TabPageSO(self), 'Изменение данных')


class CorrectSignaturesWindow(QMainWindow):

    def __init__(self):
        super(CorrectSignaturesWindow, self).__init__()

        # self.selected_region = instance.selected_region
        self.podpis_dict = TabPageSO.podpis_dict

        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.setWindowModality(QtCore.Qt.ApplicationModal)  # Устанавливаем модальность окна

        # self.selected_region = selected_region
        self.tabWidget = TabWidget()
        # self.tableWidget = QTableWidget(0, 4)
        # self.labels_nkt = labels_nkt

        self.buttonAdd = QPushButton('сохранить данные')
        self.buttonAdd.clicked.connect(self.add_row_table)

        vbox = QGridLayout(self.centralWidget)
        vbox.addWidget(self.tabWidget, 0, 0, 1, 2)
        # vbox.addWidget(self.tableWidget, 0, 0, 1, 2)
        vbox.addWidget(self.buttonAdd, 3, 0)

    def add_row_table(self):
        selected_region = TabPageSO.selected_region
        self.current_widget = self.tabWidget.currentWidget()
        

        chief_engineer_edit_type = self.current_widget.chief_engineer_edit_type.text()
        chief_engineer_name_edit_type = self.current_widget.chief_engineer_name_edit_type.text().title()
        chief_geologist_edit_type = self.current_widget.chief_geologist_edit_type.text()
        chief_geologist_name_edit_type = self.current_widget.chief_geologist_name_edit_type.text().title()
        head_of_orm_edit_type = self.current_widget.head_of_orm_edit_type.text()
        head_of_orm_name_edit_type = self.current_widget.head_of_orm_name_edit_type.text().title()
        representative_of_orm_edit_type = self.current_widget.representative_of_orm_edit_type.text()
        representative_of_orm_name_edit_type = self.current_widget.representative_of_orm_name_edit_type.text().title()
        head_of_gtm_edit_type = self.current_widget.head_of_gtm_edit_type.text()
        head_of_gtm_name_edit_type = self.current_widget.head_of_gtm_name_edit_type.text().title()
        representative_of_gtm_edit_type = self.current_widget.representative_of_gtm_edit_type.text()
        representative_of_gtm_name_edit_type = self.current_widget.representative_of_gtm_name_edit_type.text().title()
        representative_of_go_edit_type = self.current_widget.representative_of_go_edit_type.text()
        representative_of_go_name_edit_type = self.current_widget.representative_of_go_name_edit_type.text().title()
        head_of_usrsist_edit_type = self.current_widget.head_of_usrsist_edit_type.text()
        head_of_usrsist_name_edit_type = self.current_widget.head_of_usrsist_name_edit_type.text().title()
        representative_of_grr_edit_type = self.current_widget.representative_of_grr_edit_type.text()

        representative_of_grr_name_edit_type = self.current_widget.representative_of_grr_name_edit_type.text().title()

        name_list = [chief_engineer_name_edit_type, chief_geologist_name_edit_type,
                     head_of_usrsist_name_edit_type, head_of_gtm_name_edit_type, head_of_orm_name_edit_type,
                     representative_of_grr_name_edit_type, representative_of_gtm_name_edit_type,
                     representative_of_orm_name_edit_type]
        if TabPageSO.selected_region is None:
            QMessageBox.information(self, 'Внимание', 'Не все поля соответствуют значениям')
            return

        elif all([string.count('.') == 2 for string in name_list]) is False:
            # print([string.count('.') == 2 for string in name_list])
            QMessageBox.information(self, 'Внимание', 'Не корректны сокращения в фамилиях')
            return

        else:
            self.podpis_dict = TabPageSO.podpis_dict
            aaaa = self.podpis_dict
            self.podpis_dict['регион'][selected_region]['gi']['post'] = chief_engineer_edit_type
            self.podpis_dict['регион'][selected_region]['gi']["surname"] = chief_engineer_name_edit_type

            self.podpis_dict['регион'][selected_region]['gg']['post'] = chief_geologist_edit_type
            self.podpis_dict['регион'][selected_region]['gg']['surname'] = chief_geologist_name_edit_type

            self.podpis_dict['регион'][selected_region]["ruk_orm"]['post'] = head_of_orm_edit_type
            self.podpis_dict['регион'][selected_region]["ruk_orm"]['surname'] = head_of_orm_name_edit_type

            self.podpis_dict['регион'][selected_region]["ved_orm"]['post'] = representative_of_orm_edit_type
            self.podpis_dict['регион'][selected_region]["ved_orm"]['surname'] = representative_of_orm_name_edit_type

            self.podpis_dict['регион'][selected_region]["ruk_gtm"]['post'] = head_of_gtm_edit_type
            self.podpis_dict['регион'][selected_region]["ruk_gtm"]['surname'] = head_of_gtm_name_edit_type

            self.podpis_dict['регион'][selected_region]["ved_gtm"]['post'] = representative_of_gtm_edit_type
            self.podpis_dict['регион'][selected_region]["ved_gtm"]['surname'] = representative_of_gtm_name_edit_type

            self.podpis_dict['регион'][selected_region]["go"]['post'] = representative_of_go_edit_type
            self.podpis_dict['регион'][selected_region]["go"]['surname'] = representative_of_go_name_edit_type

            self.podpis_dict['регион'][selected_region]["usrs"]['post'] = head_of_usrsist_edit_type
            self.podpis_dict['регион'][selected_region]["usrs"]['surname'] = head_of_usrsist_name_edit_type

            self.podpis_dict['регион'][selected_region]["grr"]['post'] = representative_of_grr_edit_type
            self.podpis_dict['регион'][selected_region]["grr"]['surname'] = representative_of_grr_name_edit_type

            with open(f'{well_data.path_image}podpisant.json', 'w', encoding='utf-8') as json_file:
                json.dump(self.podpis_dict, json_file, indent=4, ensure_ascii=False)

            self.close()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet()
    window = CorrectSignaturesWindow()
    # window.show()
    app.exec_()
