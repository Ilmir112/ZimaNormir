import well_data
import re
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *
from PyQt5.QtGui import QRegExpValidator, QColor, QPalette
from normir.alone_oreration import definition_plast_work


class FloatLineEdit(QLineEdit):
    def __init__(self, parent=None):
        super(FloatLineEdit, self).__init__(parent)

        # Устанавливаем валидатор для проверки на float


        reg = QRegExp("[0-9.]*")
        pValidator = QRegExpValidator(self)
        pValidator.setRegExp(reg)
        self.setValidator(pValidator)

    def focusOutEvent(self, event):
        # При потере фокуса проверяем, является ли текст float
        if self.validator().validate(self.text(), 0)[0] != QValidator.Acceptable:
            # Если текст не является числом, меняем цвет фона на красный
            palette = self.palette()
            palette.setColor(QPalette.Base, QColor(Qt.red))
            self.setPalette(palette)
        else:
            # Если текст является числом, возвращаем цвет фона по умолчанию
            self.setPalette(self.parentWidget().palette())


class TabPage_SO(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
       

        self.labels_plast = {}
        self.dict_perforation = well_data.dict_perforation
        self.dict_perforation_project = well_data.dict_perforation_project

        self.plast_label = QLabel("пласта")
        self.roof_label = QLabel("Кровля")
        self.sole_label = QLabel("Подошва")
        self.plast_status_label = QLabel("Статус пласта")
        self.template_status_label = QLabel("Прошаблонировано")
        self.raiding_status_label = QLabel("Отрайбировано")

        grid = QGridLayout(self)
        grid.addWidget(self.plast_label, 0, 0)
        grid.addWidget(self.roof_label, 0, 1)
        grid.addWidget(self.sole_label, 0, 2)
        grid.addWidget(self.plast_status_label, 0, 3)
        grid.addWidget(self.template_status_label, 0, 4)
        grid.addWidget(self.raiding_status_label, 0, 5)



        plast_all = list(self.dict_perforation.keys())
        plast_projects = list(self.dict_perforation_project.keys())

        index_interval = 1
        for plast in plast_all:
            for index, (roof, sole) in enumerate(list(sorted(self.dict_perforation[plast]["интервал"],
                                                             key=lambda x:x[0]))):

                plast_edit = QLineEdit(self)
                plast_edit.setText(plast)

                roof_edit = QLineEdit(self)
                roof_edit.setText(str(roof))

                sole_edit = QLineEdit(self)
                sole_edit.setText(str(sole))

                plast_status_ComboBox = QComboBox(self)
                plast_status_ComboBox.addItems(['отключен', 'вскрыт', 'проект', 'отсутствует'])
                plast_status_ComboBox.setCurrentIndex(self.check_plast_status(plast))

                template_status_ComboBox = QComboBox(self)
                template_status_ComboBox.addItems(['Прошаблонировано', 'Не прошаблонировано'])
                # template_status_ComboBox.setText('Прошаблонировано')
                template_status_ComboBox.setCurrentIndex(self.check_template_status(plast))

                raiding_status_ComboBox = QComboBox(self)
                raiding_status_ComboBox.addItems(['отрайбировано', 'Не отрайбировано'])
                # raiding_status_ComboBox.setText('отрайбировано')
                raiding_status_ComboBox.setCurrentIndex(self.check_raiding_status(plast))

                grid.addWidget(plast_edit, index_interval, 0)
                grid.addWidget(roof_edit, index_interval, 1)
                grid.addWidget(sole_edit, index_interval, 2)
                grid.addWidget(plast_status_ComboBox, index_interval, 3)
                grid.addWidget(template_status_ComboBox, index_interval, 4)
                grid.addWidget(raiding_status_ComboBox, index_interval, 5)

                # Переименование атрибута
                setattr(self, f"plast_{index_interval}_edit", plast_edit)
                setattr(self, f"roof_{index_interval}_edit", roof_edit)
                setattr(self, f"sole_{index_interval}_edit", sole_edit)
                setattr(self, f"plast_status_{index_interval}_edit", plast_status_ComboBox)
                setattr(self, f"template_status_{index_interval}_edit", template_status_ComboBox)
                setattr(self, f"raiding_status_{index_interval}_edit", raiding_status_ComboBox)

                self.labels_plast[index_interval] = (plast_edit, roof_edit, sole_edit, plast_status_ComboBox,
                                          template_status_ComboBox, raiding_status_ComboBox)
                index_interval += 1
        if len(well_data.dict_perforation) != 0:
            for plast in plast_projects:
                for index, (roof, sole) in enumerate(list(sorted(self.dict_perforation_project[plast]["интервал"],
                                                                 key=lambda x: x[0]))):
                    plast_edit = QLineEdit(self)
                    plast_edit.setText(plast)

                    roof_edit = QLineEdit(self)
                    roof_edit.setText(str(roof))

                    sole_edit = QLineEdit(self)
                    sole_edit.setText(str(sole))

                    plast_status_ComboBox = QComboBox(self)
                    plast_status_ComboBox.addItems(['отключен', 'вскрыт', 'проект', 'отсутствует'])
                    plast_status_ComboBox.setCurrentIndex(2)

                    template_status_ComboBox = QComboBox(self)
                    template_status_ComboBox.addItems(['Прошаблонировано', 'Не прошаблонировано'])
                    # template_status_ComboBox.setText('Прошаблонировано')
                    template_status_ComboBox.setCurrentIndex(1)

                    raiding_status_ComboBox = QComboBox(self)
                    raiding_status_ComboBox.addItems(['отрайбировано', 'Не отрайбировано'])
                    # raiding_status_ComboBox.setText('отрайбировано')
                    raiding_status_ComboBox.setCurrentIndex(1)

                    grid.addWidget(plast_edit, index_interval, 0)
                    grid.addWidget(roof_edit, index_interval, 1)
                    grid.addWidget(sole_edit, index_interval, 2)
                    grid.addWidget(plast_status_ComboBox, index_interval, 3)
                    grid.addWidget(template_status_ComboBox, index_interval, 4)
                    grid.addWidget(raiding_status_ComboBox, index_interval, 5)

                    # Переименование атрибута
                    setattr(self, f"plast_{index_interval}_edit", plast_edit)
                    setattr(self, f"roof_{index_interval}_edit", roof_edit)
                    setattr(self, f"sole_{index_interval}_edit", sole_edit)
                    setattr(self, f"plast_status_{index_interval}_edit", plast_status_ComboBox)
                    setattr(self, f"template_status_{index_interval}_edit", template_status_ComboBox)
                    setattr(self, f"raiding_status_{index_interval}_edit", raiding_status_ComboBox)

                    self.labels_plast[index_interval] = (plast_edit, roof_edit, sole_edit, plast_status_ComboBox,
                                                         template_status_ComboBox, raiding_status_ComboBox)
                    index_interval += 1

    def check_plast_status(self, plast):
        return 0 if self.dict_perforation[plast]['отключение'] else 1

    def check_template_status(self, plast):
        # print(self.dict_perforation[plast].keys())
        return 0 if self.dict_perforation[plast]['Прошаблонировано'] else 1

    def check_raiding_status(self, plast):
        return 0 if self.dict_perforation[plast]['отрайбировано'] else 1


class TabWidget(QTabWidget):
    def __init__(self):
        super().__init__()
        self.addTab(TabPage_SO(self), 'Проверка корректности данных перфорации')


class PerforationCorrect(QMainWindow):

    def __init__(self, parent=None):
        super(PerforationCorrect, self).__init__()

        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.setWindowModality(QtCore.Qt.ApplicationModal) # Устанавливаем модальность окна

        self.tabWidget = TabWidget()

        self.buttonAdd = QPushButton('сохранить данные')
        self.buttonAdd.clicked.connect(self.add_row_table)

        vbox = QGridLayout(self.centralWidget)
        vbox.addWidget(self.tabWidget, 0, 0, 1, 2)
        # vbox.addWidget(self.tableWidget, 0, 0, 1, 2)
        vbox.addWidget(self.buttonAdd, 3, 0)

    def add_row_table(self):

        self.dict_perforation = well_data.dict_perforation
        plast_all = self.tabWidget.currentWidget().labels_plast
        self.dict_perforation_project = {}

        plast_list = []
        plast_oktl = []
        plast_templ = []
        plast_raid = []
        plast_project = []
        plast_del = []

        for index, plast_dict in plast_all.items():
            plast = plast_dict[0].text()
            roof = plast_dict[1].text()
            sole = plast_dict[2].text()
            plast_status = plast_dict[3].currentText()
            template = plast_dict[4].currentText()
            raid = plast_dict[5].currentText()
            if plast not in plast_list:
                plast_oktl = []
                plast_templ = []
                plast_raid = []
                plast_project = []


            if plast_status == 'отключен':
                plast_oktl.append(True)
            elif plast_status == 'вскрыт':
                plast_oktl.append(False)
            elif plast_status == 'проект':
                plast_project.append(plast)
            elif plast_status == 'отсутствует':
                plast_del.append(plast)

            if template == 'Прошаблонировано':
                plast_templ.append(True)
            else:
                plast_templ.append(False)

            if raid == 'отрайбировано':
                plast_raid.append(True)
            else:
                plast_raid.append(False)

            if len(plast_project) > 0:
                plast_project_list = list(well_data.dict_perforation_project.keys())
                if plast_project[0] not in plast_project_list:
                    well_data.dict_perforation_project.setdefault(
                        plast, {}).setdefault('интервал', []).append((float(roof), float(sole)))
                else:
                    well_data.dict_perforation_project[plast]['интервал'] = (float(roof), float(sole))
            else:
                if all([oktl is True for oktl in plast_oktl]):
                    well_data.dict_perforation_short[plast]['отключение'] = True
                    well_data.dict_perforation[plast]["отключение"] = True
                else:
                    well_data.dict_perforation_short[plast]['отключение'] = False
                    well_data.dict_perforation[plast]['отключение'] = False
                if all([oktl is True for oktl in plast_templ]):
                    well_data.dict_perforation[plast]['Прошаблонировано'] = True
                else:
                    well_data.dict_perforation[plast]['Прошаблонировано'] = False
                if all([oktl is True for oktl in plast_raid]):
                    well_data.dict_perforation[plast]['отрайбировано'] = True
                else:
                    well_data.dict_perforation[plast]['отрайбировано'] = False

            if len(plast_del) > 0:
                for plast in plast_del:
                    well_data.dict_perforation.pop(plast)



        well_data.plast_work_short = well_data.plast_work

        definition_plast_work(self)

        if len(well_data.plast_work) == 0:
            perf_true_quest = QMessageBox.question(self, 'Программа',
                                                   'Программа определили,что в скважине интервалов '
                                                   'перфорации нет, верно ли?')
            if perf_true_quest == QMessageBox.StandardButton.Yes:

                well_data.pause = False
                self.close()
                return
            else:

                return
        well_data.pause = False
        self.close()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet()
    window = PerforationCorrect()
    QTimer.singleShot(2000, PerforationCorrect.updateLabel)
    # window.show()
    app.exec_()
