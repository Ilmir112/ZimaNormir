import logging
import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QObject, pyqtSignal

import logging

import sys
from PyQt5.QtCore import Qt, QObject, pyqtSignal, QThread, pyqtSlot
from PyQt5.QtWidgets import QPlainTextEdit, QApplication


def except_hook(exctype, value, traceback):
    # Записываем информацию об ошибке в логгер
    logger.critical(f"Критическая ошибка: {exctype}, {value}, {traceback}")
    sys.__excepthook__(exctype, value, traceback)


sys.excepthook = except_hook

# Создание логгера
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)  # Уровень логирования (DEBUG, INFO, WARNING, ERROR, CRITICAL)

# Создание обработчика (куда будут записываться логи)
file_handler = logging.FileHandler('my_app.log')  # Запись в файл
console_handler = logging.StreamHandler()  # Вывод в консоль

# Формат логов
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Добавляем обработчики к логгеру
logger.addHandler(file_handler)
logger.addHandler(console_handler)

from PyQt5.QtCore import Qt, QObject, pyqtSignal
from PyQt5.QtWidgets import QPlainTextEdit



class QPlainTextEditLogger(logging.Handler, QObject):
    appendPlainText = pyqtSignal(str)

    def __init__(self, parent):
        super().__init__()
        QObject.__init__(self)
        self.widget = QPlainTextEdit(parent)
        self.widget.setReadOnly(True)
        self.appendPlainText.connect(self.widget.appendPlainText)

    def emit(self, record):
        msg = self.format(record)
        self.appendPlainText.emit(msg)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # ... другая инициализация главного окна ...

        self.log_widget = QPlainTextEditLogger(self)
        logger.addHandler(self.log_widget)
        self.setCentralWidget(self.log_widget.widget)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt Логирование")

        # Добавляем кнопку для тестирования
        button = QtWidgets.QPushButton("Нажми меня!")
        button.clicked.connect(self.on_button_click)

        # Логирование в виджет
        self.log_widget = QPlainTextEditLogger(self)
        logger.addHandler(self.log_widget)

        # Добавляем виджеты на главное окно
        central_widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(button)
        layout.addWidget(self.log_widget.widget)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def on_button_click(self):
       pass

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
