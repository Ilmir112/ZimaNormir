from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QInputDialog, QWidget, QLabel, QLineEdit, QComboBox, QGridLayout, QTabWidget, QPushButton, \
    QMessageBox

import well_data
from main import MyWindow


class TabPage_SO_curator(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.curator_label = QLabel("Куратор", self)
        self.curator_combo = QComboBox(self)
        curator_list = ['ГРР', 'ОР', 'ГТМ', 'ГО', 'ВНС']
        self.curator_combo.addItems(curator_list)

        self.grid = QGridLayout(self)
        self.grid.addWidget(self.curator_label, 2, 0)
        self.grid.addWidget(self.curator_combo, 3, 0)


class TabWidget(QTabWidget):
    def __init__(self):
        super().__init__()
        self.addTab(TabPage_SO_curator(), 'Куратор')


class SelectCurator(MyWindow):

    def __init__(self, parent=None):
        super(MyWindow, self).__init__()
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

        self.tabWidget = TabWidget()

        self.buttonadd_work = QPushButton('Изменить')
        self.buttonadd_work.clicked.connect(self.add_work, Qt.QueuedConnection)

        vbox = QGridLayout(self.centralWidget)

        vbox.addWidget(self.tabWidget, 0, 0, 1, 2)
        vbox.addWidget(self.buttonadd_work, 3, 0)

    def add_work(self):
        curator_combo = self.tabWidget.currentWidget().curator_combo.currentText()
        well_data.curator = curator_combo

        well_data.pause = False
        self.close()



