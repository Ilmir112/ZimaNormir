from PyQt5 import QtCore, QtWidgets
from PyQt5.Qt import *


from collections import namedtuple

import well_data

class CheckableComboBox(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.combo_box = CheckableComboBoxChild(self)
        layout = QVBoxLayout(self)
        layout.addWidget(self.combo_box)


class CheckableComboBoxChild(QComboBox):
    # Subclass Delegate to increase item height

    class Delegate(QStyledItemDelegate):
        def sizeHint(self, option, index):
            size = super().sizeHint(option, index)
            size.setHeight(20)
            return size

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Make the combo editable to set a custom text
        self.setEditable(True)
        self.setInsertPolicy(QComboBox.NoInsert)
        self.lineEdit().setPlaceholderText("--выбрать пласты--")
        edit = self.lineEdit()
        self.setLineEdit(edit)
        self.completer = QCompleter()
        self.completer.setFilterMode(Qt.MatchContains)
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)
        edit.setCompleter(self.completer)
        self.completer.setModel(self.model())
        edit.returnPressed.connect(self.insertCustomItem)

        # Make the lineedit the same color as QPushButton
        palette = qApp.palette()
        palette.setBrush(QPalette.Base, palette.button())
        self.lineEdit().setPalette(palette)

        # Use custom delegate
        self.setItemDelegate(CheckableComboBoxChild.Delegate())

        # Update the text when an item is toggled
        self.model().dataChanged.connect(self.updateText)

        # Hide and show popup when clicking the line edit
        self.lineEdit().installEventFilter(self)

        # Prevent popup from closing when clicking on an item
        self.view().viewport().installEventFilter(self)

    def resizeEvent(self, event):
        # Recompute text to elide as needed
        self.updateText()
        super().resizeEvent(event)

    def eventFilter(self, object, event):
        try:
            if object == self.view().viewport():
                if event.type() == QEvent.MouseButtonRelease:
                    if self.lineEdit().hasFocus():
                        return True
                    index = self.view().indexAt(event.pos())
                    item = self.model().item(index.row())
                    if item.checkState() == Qt.Checked:
                        item.setCheckState(Qt.Unchecked)
                    else:
                        item.setCheckState(Qt.Checked)
                    return False
            return False
        except:
            pass

    def timerEvent(self, event):

        self.killTimer(event.timerId())

    def updateText(self):
        well_data.texts = []

        for i in range(self.model().rowCount()):

            if self.model().item(i).checkState() == Qt.Checked:
                # print(self.model().item(i).text())

                well_data.texts.append(self.model().item(i).text())

        text = ", ".join(well_data.texts)

        self.lineEdit().setText(text)

    def addItem(self, text, data=None, checked=False):
        from category_correct import TabPage_SO

        item = QStandardItem()
        item.setText(text)
        if data is None:
            item.setData(text)
        else:
            item.setData(data)
        item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsUserCheckable)
        a = text
        b = TabPage_SO.count_plast
        if text in well_data.plast_work and not text in TabPage_SO.count_plast:
            if text not in TabPage_SO.count_plast:
                item.setData(Qt.Unchecked if not text in well_data.plast_work else Qt.Checked, Qt.CheckStateRole)
                TabPage_SO.count_plast.append(text)
        else:
            if well_data.plast_project:
                if text not in TabPage_SO.count_plast:
                    item.setData(Qt.Unchecked if not text in well_data.plast_project else Qt.Checked, Qt.CheckStateRole)

        self.model().appendRow(item)

    def addItems(self, texts, datalist=None):
        for i, text in enumerate(texts):
            try:
                data = datalist[i]
            except (TypeError, IndexError):
                data = None
            self.addItem(text, data)

    def insertCustomItem(self):
        text = self.lineEdit().text().strip()
        # Split the text by comma, and lowercase and strip() each piece
        typedItemsOriginal = [item.strip() for item in text.split(",") if item.strip()]
        typedItemsLower = [item.lower() for item in typedItemsOriginal]
        # Uncheck all items
        for i in range(self.model().rowCount()):
            self.model().item(i).setData(Qt.Unchecked, Qt.CheckStateRole)
        # Loop through each item in the text and check it, if it exists in
        # lowercase
        for i in range(len(typedItemsOriginal)):
            for j in range(self.model().rowCount()):
                if self.model().item(j).text().lower() == typedItemsLower[i]:
                    self.model().item(j).setData(Qt.Checked, Qt.CheckStateRole)
                    break
            else:
                # If the item doesn't exist, add it to the list
                self.addItem(typedItemsOriginal[i], checked=True)
        self.updateText()
        self.showPopup()

    def currentData(self):
        # Return the list of selected items data
        res = []
        for i in range(self.model().rowCount()):
            if self.model().item(i).checkState() == Qt.Checked:
                res.append(self.model().item(i).data())
        return res

class TabPage_SO(QWidget):
    count_plast = []
    def __init__(self, parent=None):
        super().__init__(parent)

        self.labels_category = {}
        self.type_absorbent_label = QLabel('Тип поглотителя')
        self.type_absorbent = QComboBox()
        self.type_absorbent.addItems(['ХИМТЕХНО 101 Марка А', 'СНПХ-1200', ' EVASORB марки 121'])

        self.plast_all = []
        for plast in well_data.plast_all[::-1]:
            self.plast_all.append(plast)

        for plast in well_data.plast_project:
            self.plast_all.append(plast)

        self.cat_P_1 = well_data.cat_P_1
        self.cat_h2s_list = well_data.cat_h2s_list
        self.cat_gaz_f_pr = well_data.cat_gaz_f_pr
        self.gaz_f_pr = well_data.gaz_f_pr
        self.h2s_mg = well_data.h2s_mg

        self.h2s_pr = well_data.h2s_pr

        self.cat_P_P = well_data.cat_P_P

        self.category_pressuar_Label = QLabel('По Рпл')
        self.category_h2s_Label = QLabel('По H2S')
        self.category_h2s2_Label = QLabel('По H2S')
        self.category_gf_Label = QLabel('По газовому фактору')
        self.calc_h2s_Label = QLabel('расчет поглотителя H2S')

        self.grid = QGridLayout(self)
        self.grid.addWidget(self.type_absorbent_label , 2, 1)
        self.grid.addWidget(self.type_absorbent, 3, 1)
        self.grid.addWidget(self.category_pressuar_Label, 5, 1)
        self.grid.addWidget(self.category_h2s_Label, 6, 1)
        self.grid.addWidget(self.category_h2s2_Label, 7, 1)
        self.grid.addWidget(self.category_gf_Label, 8, 1)


        n = 1
        work_plast_iter = None
        well_data.number_indez = []
        work_plast = ''
        work_plast_index = 1

        for num in range(len(list(set(well_data.cat_P_P)))):

            plast_index = CheckableComboBox(self)
            try:
                work_plast = well_data.plast_work[num]
                work_plast_index = 0
            except:
                if well_data.plast_project:
                    work_plast = well_data.plast_project[0]
                    work_plast_index = 1
            av= work_plast, work_plast_iter, well_data.dict_perforation_project

            if num != 0:
                if len(well_data.dict_perforation_project) != 0 and \
                        any([plast not in well_data.plast_work for plast in well_data.plast_project]):

                    if abs(self.cat_P_P[num] - list([well_data.dict_perforation_project[
                                                         plast]['давление'] for plast in well_data.plast_project][0])[
                        0]) < 1:
                        work_plast = well_data.plast_project[0]
                        work_plast_index = 1
                else:
                    plast_index_str = QMessageBox.question(self, 'рабочие пласты',
                                                           f'Есть ли индекс пласта категорийности {num + 1}'
                                                           f'в интервалах перфорации')
                    if plast_index_str == QMessageBox.StandardButton.No:
                        work_plast, ok = QInputDialog.getText(None, 'индекс пласта',
                                                              'Введите индекc пласта вскрываемого')
                        well_data.plast_project.append(work_plast)
                        work_plast_index = 1

                    self.plast_all.append(work_plast)


            plast_index.combo_box.addItems(self.plast_all)

            plast_index.combo_box.setCurrentIndex(self.plast_all.index(work_plast))

            category_pressuar_line_edit = QLineEdit(self)
            try:
                category_pressuar_line_edit.setText(str(self.ifNone(self.cat_P_1[num])))
            except:
                mes = QMessageBox.warning(self, 'ОШИБКА', 'не вставилось данные по категории')
            pressuar_data_edit = QLineEdit(self)
            try:
                pressuar_data_edit.setText(str(self.ifNone(self.cat_P_P[num])))
            except:
                pass
            # print(num)
            category_h2s_edit = QLineEdit(self)
            try:
                category_h2s_edit.setText(str(self.ifNone(self.cat_h2s_list[num])))
            except:
                pass
            h2s_pr_edit = QLineEdit(self)
            try:
                if str(round(float(str(self.h2s_pr[num]).replace(',', '.')), 3))[-1] == "0":
                    h2s_pr = int(float(self.h2s_pr[num]))
                else:
                    h2s_pr = round(float(str(self.h2s_pr[num]).replace(',', '.')), 4)
                h2s_pr_edit.setText(str(h2s_pr))
            except (IndexError, TypeError):
                pass

            category_h2s2_edit = QLineEdit(self)
            try:
                category_h2s2_edit.setText(str(self.ifNone(self.cat_h2s_list[num])))
                h2s_mg_edit = QLineEdit(self)
            except (IndexError, TypeError):
                pass
            try:
                h2s_mg_edit.setText(str(self.h2s_mg[num]))
            except (IndexError, TypeError):

                pass

            category_gf_edit = QLineEdit(self)
            try:
                category_gf_edit.setText(str(self.ifNone(self.cat_gaz_f_pr[num])))
            except (IndexError, TypeError):
                pass
            gaz_f_pr_edit = QLineEdit(self)
            try:
                gaz_f_pr_edit.setText(str(self.ifNone(self.gaz_f_pr[num])))
            except (IndexError, TypeError):
                pass

            units_pressuar = QLabel('атм')
            units_h2s_pr = QLabel('%')
            units_h2s_pr.setFixedWidth(150)
            units_h2s_mg = QLabel('мг/дм3')
            units_gaz = QLabel('м3/т')
            isolated_plast = QComboBox(self)
            isolated_plast.addItems(['рабочий', 'планируемый', 'изолирован'])
            isolated_plast.setCurrentIndex(work_plast_index)
            if work_plast_iter is None:
                work_plast_iter = work_plast



            # print(Category_h2s_edit.text(), h2s_mg_edit.text(), h2s_pr_edit.text())

            self.grid.addWidget(plast_index, 4, 1 + n, 1, 2)
            self.grid.addWidget(category_pressuar_line_edit, 5, 1 + n)
            self.grid.addWidget(category_h2s_edit, 6, 1 + n)
            self.grid.addWidget(category_h2s2_edit, 7, 1 + n)
            self.grid.addWidget(category_gf_edit, 8, 1 + n)
            self.grid.addWidget(isolated_plast, 9, n + 1, 9, n + 1)

            self.grid.addWidget(pressuar_data_edit, 5, 1 + n + 1)
            self.grid.addWidget(h2s_pr_edit, 6, 1 + n + 1)
            self.grid.addWidget(h2s_mg_edit, 7, 1 + n + 1)
            self.grid.addWidget(gaz_f_pr_edit, 8, 1 + n + 1)
            self.grid.addWidget(units_pressuar, 5, 1 + n + 2)

            self.grid.addWidget(units_h2s_pr, 6, 1 + n + 2)
            self.grid.addWidget(units_h2s_mg, 7, 1 + n + 2)
            self.grid.addWidget(units_gaz, 8, 1 + n + 2)

            # Переименование атрибута
            setattr(self, f"{plast_index}_{n}_line", plast_index)
            setattr(self, f"{category_pressuar_line_edit}_{n}_line", category_pressuar_line_edit)
            setattr(self, f"{pressuar_data_edit}_{n}_line", pressuar_data_edit)
            setattr(self, f"{category_h2s_edit}_{n}_line", category_h2s_edit)
            setattr(self, f"{category_gf_edit}_{n}_line", category_gf_edit)
            setattr(self, f"{h2s_pr_edit}_{n}_line", h2s_pr_edit)
            setattr(self, f"{h2s_mg_edit}_{n}_line", h2s_mg_edit)
            setattr(self, f"{gaz_f_pr_edit}_{n}_line", gaz_f_pr_edit)
            setattr(self, f"{units_pressuar}_{n}_line", units_pressuar)
            setattr(self, f"{units_h2s_pr}_{n}_line", units_h2s_pr)
            setattr(self, f"{units_h2s_mg}_{n}_line", units_h2s_mg)
            setattr(self, f"{units_gaz}_{n}_line", units_gaz)
            setattr(self, f"{isolated_plast}_{n}_line", isolated_plast)



            self.labels_category[n] = (plast_index, category_pressuar_line_edit, category_h2s_edit,
                                       category_gf_edit, h2s_pr_edit, h2s_mg_edit, gaz_f_pr_edit,
                                       pressuar_data_edit, isolated_plast)

            well_data.number_indez.append(n)
            n += 3

    def ifNone(self, string):

        if str(string) in ['0', str(None), '-']:
            return 0
        elif str(string).replace('.', '').replace(',', '').isdigit():
            if str(round(float(str(string).replace(',', '.')), 1))[-1] == "0":
                return int(float(string))
            else:
                return round(float(str(string).replace(',', '.')), 4)
        else:
            return str(string)


class TabWidget(QTabWidget):
    def __init__(self):
        super().__init__()
        self.addTab(TabPage_SO(self), 'Проверка корректности данных')


class CategoryWindow(QMainWindow):
    dict_category = {}

    def __init__(self, parent=None):
        super(CategoryWindow, self).__init__()

        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.setWindowModality(QtCore.Qt.ApplicationModal)  # Устанавливаем модальность окна
        self.tabWidget = TabWidget()
        self.dict_category = {}

        self.buttonAdd = QPushButton('сохранить данные')
        self.buttonAdd.clicked.connect(self.add_row_table)

        vbox = QGridLayout(self.centralWidget)
        vbox.addWidget(self.tabWidget, 0, 0, 1, 2)
        # vbox.addWidget(self.tableWidget, 0, 0, 1, 2)
        vbox.addWidget(self.buttonAdd, 3, 0)

    def add_row_table(self):

        # Пересохранение по сереводорода

        cat_P_1 = well_data.cat_P_1
        well_data.type_absorbent = self.tabWidget.currentWidget().type_absorbent.currentText()
        plast_index = []
        Pressuar = namedtuple("Pressuar", "category data_pressuar")
        Data_h2s = namedtuple("Data_h2s", "category data_procent data_mg_l poglot")
        Data_gaz = namedtuple("Data_gaz", "category data")
        if cat_P_1:
            for index in well_data.number_indez:
                for ind in range(1, 6):
                    if self.ifNum(self.tabWidget.currentWidget().labels_category[index][ind].text()) is False:
                        mes = QMessageBox.warning(self, 'Ошибка', 'ошибка в сохранении данных, не корректные данные ')
                        return

                plast_sel = self.tabWidget.currentWidget().labels_category[index][0].combo_box.currentText()
                if plast_sel == '':
                    mes = QMessageBox.warning(self, 'Выбрать пласты', 'Необходимо выбрать пласты выбрать пласты')
                    return
                for plast in plast_sel.split(', '):
                    plast_index.append(plast)

                    if self.tabWidget.currentWidget().labels_category[index][8].currentText() == 'планируемый':
                        well_data.plast_project.append(plast)
                    try:
                        CategoryWindow.dict_category.setdefault(plast, {}).setdefault(
                            'по давлению',
                            Pressuar(int(self.tabWidget.currentWidget().labels_category[index][1].text()),
                                     float(self.tabWidget.currentWidget().labels_category[index][7].text())))

                        CategoryWindow.dict_category.setdefault(plast, {}).setdefault(
                            'по сероводороду', Data_h2s(
                                int(self.tabWidget.currentWidget().labels_category[index][2].text()),
                                float(self.tabWidget.currentWidget().labels_category[index][4].text()),
                                float(self.tabWidget.currentWidget().labels_category[index][5].text()),
                                25))

                        CategoryWindow.dict_category.setdefault(plast, {}).setdefault(
                            'по газовому фактору', Data_gaz(
                                int(self.tabWidget.currentWidget().labels_category[index][3].text()),
                                float(self.tabWidget.currentWidget().labels_category[index][6].text())))

                        CategoryWindow.dict_category.setdefault(plast, {}).setdefault(
                            'отключение', self.tabWidget.currentWidget().labels_category[index][8].currentText())

                    except Exception as e:
                        mes = QMessageBox.warning(self, 'Ошибка', f"Ошибка сохранения данных по категории {e}")
                        return

        well_data.pause = False
        self.close()

    def ifNum(self, string):
        # метод для проверки и преобразования введенных значений
        if str(string) == "['0']":
            return False
        elif str(string) == 'отсут':
            return True
        elif str(string).replace('.', '').replace(',', '').isdigit():
            if float(string.replace(',', '.')) < 5000:
                return True
            else:
                return False
        else:
            return False


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet()
    window = CategoryWindow()
    QTimer.singleShot(2000, CategoryWindow)
    # window.show()
    app.exec_()
