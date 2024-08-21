import well_data
import re

from PyQt5 import QtCore, QtWidgets
from PyQt5.Qt import *
from perforation_correct import FloatLineEdit


class TabPage_SO_correct(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.labels_nkt = {}
        self.labels_nkt_po = {}
        self.labels_sucker = {}
        self.labels_sucker_po = {}

        self.column_direction_diametr_Label = QLabel("диаметр направление", self)
        self.column_direction_diametr_edit = FloatLineEdit(self)
        if well_data.column_direction_True:
            self.column_direction_diametr_edit.setText(f'{str(well_data.column_direction_diametr._value).strip()}')
        else:
            self.column_direction_diametr_edit.setText(f'отсут')

        self.column_direction_wall_thickness_Label = QLabel("Толщина стенки направление", self)
        self.column_direction_wall_thickness_edit = FloatLineEdit(self)
        if well_data.column_direction_True:
            self.column_direction_wall_thickness_edit.setText(
                f'{str(well_data.column_direction_wall_thickness._value).strip()}')
        else:
            self.column_direction_wall_thickness_edit.setText(f'отсут')
        self.column_direction_lenght_Label = QLabel("башмак направления", self)
        self.column_direction_lenght_edit = FloatLineEdit(self)
        if well_data.column_direction_True:
            self.column_direction_lenght_edit.setText(f'{str(well_data.column_direction_lenght._value).strip()}')
        else:
            self.column_direction_lenght_edit.setText(f'отсут')

        self.level_cement_direction_Label = QLabel("Уровень цемента за направление", self)
        self.level_cement_direction_edit = FloatLineEdit(self)
        if well_data.column_direction_True:
            self.level_cement_direction_edit.setText(f'{str(well_data.level_cement_direction._value).strip()}')
        else:
            self.level_cement_direction_edit.setText(f'отсут')

        self.column_conductor_diametr_Label = QLabel("диаметр кондуктора", self)
        self.column_conductor_diametr_edit = FloatLineEdit(self)
        self.column_conductor_diametr_edit.setText(f'{str(well_data.column_conductor_diametr._value).strip()}')

        self.column_conductor_wall_thickness_Label = QLabel("Толщина стенки ", self)
        self.column_conductor_wall_thickness_edit = FloatLineEdit(self)
        self.column_conductor_wall_thickness_edit.setText(
            f'{str(well_data.column_conductor_wall_thickness._value).strip()}')

        self.column_conductor_lenght_Label = QLabel("башмак кондуктора", self)
        self.column_conductor_lenght_edit = FloatLineEdit(self)
        self.column_conductor_lenght_edit.setText(f'{str(well_data.column_conductor_lenght._value).strip()}')

        self.level_cement_conductor_Label = QLabel("Уровень цемента за кондуктором", self)
        self.level_cement_conductor_edit = FloatLineEdit(self)
        self.level_cement_conductor_edit.setText(f'{str(well_data.level_cement_conductor._value).strip()}')

        self.columnLabel = QLabel("диаметр ЭК", self)
        self.columnType = FloatLineEdit(self)
        self.columnType.setText(f"{self.ifNone(well_data.column_diametr._value)}")

        # self.columnType.setClearButtonEnabled(True)

        self.column_wall_thicknessLabel = QLabel("Толщина стенки ЭК", self)
        self.column_wall_thicknessedit_type2 = FloatLineEdit(self)
        self.column_wall_thicknessedit_type2.setText(f"{self.ifNone(well_data.column_wall_thickness._value)}")
        # self.column_wall_thicknessedit_type2.setClearButtonEnabled(True)

        self.shoe_columnLabel = QLabel("башмак ЭК", self)
        self.shoe_columnedit_type2 = FloatLineEdit(self)
        self.shoe_columnedit_type2.setText(f"{self.ifNone(well_data.shoe_column._value)}")
        # self.shoe_columnedit_type2.setClearButtonEnabled(True)

        self.column_add_trueLabel = QLabel("наличие Доп. колонны", self)
        self.column_add_true_comboBox = QComboBox(self)
        self.column_add_true_comboBox.addItems(['в наличии', 'отсутствует'])
        if well_data.column_additional is True:
            column_add = 0
        else:
            column_add = 1
        self.column_add_true_comboBox.setCurrentIndex(column_add)

        self.column_addLabel = QLabel("диаметр доп. колонны", self)
        self.column_addedit_type = FloatLineEdit(self)
        self.column_addedit_type.setText(f"{self.ifNone(well_data.column_additional_diametr._value)}")
        # self.column_addedit_type.setClearButtonEnabled(True)

        self.column_add_wall_thicknessLabel = QLabel("Толщина стенки доп.колонны", self)
        self.column_add_wall_thicknessedit_type2 = FloatLineEdit(self)
        self.column_add_wall_thicknessedit_type2.setText(
            F'{self.ifNone(well_data.column_additional_wall_thickness._value)}')
        # self.column_add_wall_thicknessedit_type2.setClearButtonEnabled(True)

        self.head_column_addLabel = QLabel("Голова доп колонны", self)
        self.head_column_add_edit_type2 = FloatLineEdit(self)
        self.head_column_add_edit_type2.setText(f'{self.ifNone(well_data.head_column_additional._value)}')

        self.shoe_column_addLabel = QLabel("башмак доп колонны", self)
        self.shoe_column_add_edit_type2 = FloatLineEdit(self)
        self.shoe_column_add_edit_type2.setText(f'{self.ifNone(well_data.shoe_column_additional._value)}')
        # self.shoe_column_add_edit_type2.setClearButtonEnabled(True)

        self.bottomhole_drill_Label = QLabel('Пробуренный забой')
        self.bottomhole_drill_edit_type = FloatLineEdit(self)
        self.bottomhole_drill_edit_type.setText(
            f'{self.remove_non_numeric_chars(self.ifNone(well_data.bottomhole_drill._value))}')

        self.bottomhole_artificial_Label = QLabel('Искусственный забой')
        self.bottomhole_artificial_edit_type = FloatLineEdit(self)
        self.bottomhole_artificial_edit_type.setText(
            f'{self.remove_non_numeric_chars(self.ifNone(well_data.bottomhole_artificial._value))}')

        self.current_bottom_Label = QLabel('Текущий забой')
        self.current_bottom_edit_type = FloatLineEdit(self)
        self.current_bottom_edit_type.setText(
            f'{self.remove_non_numeric_chars(self.ifNone(well_data.current_bottom))}')

        self.max_angle_Label = QLabel('Максимальный угол')
        self.max_angle_edit_type = FloatLineEdit(self)
        self.max_angle_edit_type.setText(f'{self.ifNone(well_data.max_angle._value)}')

        self.max_angle_H_Label = QLabel('Глубина максимального угла')
        self.max_angle_H_edit_type = FloatLineEdit(self)
        self.max_angle_H_edit_type.setText(f'{self.ifNone(well_data.max_angle_H._value)}')

        self.max_expected_pressure_Label = QLabel('Максимальный ожидаемое давление')
        self.max_expected_pressure_edit_type = FloatLineEdit(self)
        self.max_expected_pressure_edit_type.setText(
            f'{self.remove_non_numeric_chars(self.ifNone(well_data.max_expected_pressure._value))}')

        self.max_admissible_pressure_Label = QLabel('Максимальный допустимое давление')
        self.max_admissible_pressure_edit_type = FloatLineEdit(self)
        self.max_admissible_pressure_edit_type.setText(
            f'{self.remove_non_numeric_chars(self.ifNone(well_data.max_admissible_pressure._value))}')

        self.pump_SHGN_do_Label = QLabel('Штанговый насос')
        self.pump_SHGN_do_edit_type = QLineEdit(self)
        self.pump_SHGN_do_edit_type.setText(f'{self.ifNone(well_data.dict_pump_SHGN["do"])}')

        self.pump_SHGN_depth_do_Label = QLabel('Глубина штангового насоса')
        self.pump_SHGN_depth_do_edit_type = FloatLineEdit(self)
        if self.pump_SHGN_do_edit_type.text() != 'отсут':
            self.pump_SHGN_depth_do_edit_type.setText(
                f'{self.remove_non_numeric_chars(self.ifNone(well_data.dict_pump_SHGN_h["do"]))}')
        else:
            self.pump_SHGN_depth_do_edit_type.setText('отсут')

        self.pump_SHGN_posle_Label = QLabel('Плановый штанговый насос')
        self.pump_SHGN_posle_edit_type = QLineEdit(self)
        self.pump_SHGN_posle_edit_type.setText(f'{self.ifNone(well_data.dict_pump_SHGN["posle"])}')

        self.pump_SHGN_depth_posle_Label = QLabel('Плановая глубина спуска насоса')
        self.pump_SHGN_depth_posle_edit_type = FloatLineEdit(self)
        if self.pump_SHGN_posle_edit_type.text() != 'отсут':
            self.pump_SHGN_depth_posle_edit_type.setText(
                f'{self.remove_non_numeric_chars(self.ifNone(well_data.dict_pump_SHGN_h["posle"]))}')
        else:
            self.pump_SHGN_depth_posle_edit_type.setText('отсут')

        self.pump_ECN_do_Label = QLabel('Спущенный ЭЦН')
        self.pump_ECN_do_edit_type = QLineEdit(self)
        self.pump_ECN_do_edit_type.setText(f'{self.ifNone(well_data.dict_pump_ECN["do"])}')

        self.pump_ECN_depth_do_Label = QLabel('Глубина спуска ЭЦН')
        self.pump_ECN_depth_do_edit_type = FloatLineEdit(self)
        if self.pump_ECN_do_edit_type.text() != 'отсут':
            self.pump_ECN_depth_do_edit_type.setText(
                f'{self.remove_non_numeric_chars(self.ifNone(well_data.dict_pump_ECN_h["do"]))}')
        else:
            self.pump_ECN_depth_do_edit_type.setText('отсут')

        self.pump_ECN_posle_Label = QLabel('Плановый ЭЦН на спуск')
        self.pump_ECN_posle_edit_type = QLineEdit(self)
        self.pump_ECN_posle_edit_type.setText(f'{self.ifNone(well_data.dict_pump_ECN["posle"])}')

        self.pump_ECN_depth_posle_Label = QLabel('Плановая глубина спуска ЭЦН')
        self.pump_ECN_depth_posle_edit_type = FloatLineEdit(self)
        if self.pump_ECN_posle_edit_type.text() != 'отсут':
            self.pump_ECN_depth_posle_edit_type.setText(
                f'{self.remove_non_numeric_chars(self.ifNone(well_data.dict_pump_ECN_h["posle"]))}')
        else:
            self.pump_ECN_depth_posle_edit_type.setText('отсут')

        self.paker_do_Label = QLabel('Спущенный пакер')
        self.paker_do_edit_type = QLineEdit(self)
        self.paker_do_edit_type.setText(f'{self.ifNone(well_data.paker_do["do"])}')

        self.paker_depth_do_Label = QLabel('Глубина спуска пакера')
        self.paker_depth_do_edit_type = FloatLineEdit(self)
        self.paker_depth_do_edit_type.setText(
            f'{self.remove_non_numeric_chars(self.ifNone(well_data.depth_fond_paker_do["do"]))}')

        self.paker_posle_Label = QLabel('пакер на спуск')
        self.paker_posle_edit_type = QLineEdit(self)
        self.paker_posle_edit_type.setText(f'{self.ifNone(well_data.paker_do["posle"])}')

        self.paker_depth_posle_Label = QLabel('Глубина спуска пакера')
        self.paker_depth_posle_edit_type = FloatLineEdit(self)
        self.paker_depth_posle_edit_type.setText(
            f'{self.remove_non_numeric_chars(self.ifNone(well_data.depth_fond_paker_do["posle"]))}')

        self.paker2_do_Label = QLabel('Спущенный пакер')
        self.paker2_do_edit_type = QLineEdit(self)
        self.paker2_do_edit_type.setText(f'{self.ifNone(well_data.paker2_do["do"])}')

        self.paker2_depth_do_Label = QLabel('Глубина спуска пакера')
        self.paker2_depth_do_edit_type = FloatLineEdit(self)
        self.paker2_depth_do_edit_type.setText(self.remove_non_numeric_chars(
            self.ifNone(str(well_data.depth_fond_paker2_do["do"]))))

        self.paker2_posle_Label = QLabel('пакер на спуск')
        self.paker2_posle_edit_type = QLineEdit(self)
        # print(well_data.paker2_do[self.ifNone("posle")])
        self.paker2_posle_edit_type.setText(str(self.ifNone(well_data.paker2_do["posle"])))

        self.paker2_depth_posle_Label = QLabel('Глубина спуска пакера')
        self.paker2_depth_posle_edit_type = FloatLineEdit(self)
        self.paker2_depth_posle_edit_type.setText(
            self.remove_non_numeric_chars(self.ifNone(str(well_data.depth_fond_paker2_do["posle"]))))
        # print(f' насос спуск {well_data.dict_pump["posle"]}')

        self.static_level_Label = QLabel('Статический уровень в скважине')
        self.static_level_edit_type = FloatLineEdit(self)
        self.static_level_edit_type.setText(self.remove_non_numeric_chars(self.ifNone(well_data.static_level._value)))

        self.dinamic_level_Label = QLabel('Динамический уровень в скважине')
        self.dinamic_level_edit_type = FloatLineEdit(self)
        self.dinamic_level_edit_type.setText(self.remove_non_numeric_chars(self.ifNone(well_data.dinamic_level._value)))

        self.curator_Label = QLabel('Куратор ремонта')
        self.curator_Combo = QComboBox(self)
        self.curator_Combo.setMinimumWidth(50)


        self.region_Label = QLabel('Регион')
        self.region_Combo = QComboBox(self)

        self.type_kr_Label = QLabel('Вид и категория ремонта, его шифр')
        self.type_kr_Combo = QComboBox(self)

        self.nkt_do_label = QLabel('НКТ  до ремонта')
        self.nkt_posle_label = QLabel('НКТ плановое согласно расчета')

        self.sucker_rod_label = QLabel('Штанги  до ремонта')
        self.sucker_rod_po_label = QLabel('Штанги плановое согласно расчета')

        self.dict_nkt = well_data.dict_nkt
        self.dict_nkt_po = well_data.dict_nkt_po
        # print(well_data.dict_nkt,  well_data.dict_nkt_po)
        a = well_data.dict_sucker_rod
        self.dict_sucker_rod = well_data.dict_sucker_rod
        self.dict_sucker_rod_po = well_data.dict_sucker_rod_po

        self.grid = QGridLayout(self)

        self.grid.addWidget(self.column_direction_diametr_Label, 0, 0)
        self.grid.addWidget(self.column_direction_diametr_edit, 1, 0)
        self.grid.addWidget(self.column_direction_wall_thickness_Label, 0, 1)
        self.grid.addWidget(self.column_direction_wall_thickness_edit, 1, 1)
        self.grid.addWidget(self.column_direction_lenght_Label, 0, 2)
        self.grid.addWidget(self.column_direction_lenght_edit, 1, 2)
        self.grid.addWidget(self.level_cement_direction_Label, 0, 4)
        self.grid.addWidget(self.level_cement_direction_edit, 1, 4)

        self.grid.addWidget(self.column_conductor_diametr_Label, 2, 0)
        self.grid.addWidget(self.column_conductor_diametr_edit, 3, 0)
        self.grid.addWidget(self.column_conductor_wall_thickness_Label, 2, 1)
        self.grid.addWidget(self.column_conductor_wall_thickness_edit, 3, 1)
        self.grid.addWidget(self.column_conductor_lenght_Label, 2, 2)
        self.grid.addWidget(self.column_conductor_lenght_edit, 3, 2)
        self.grid.addWidget(self.level_cement_conductor_Label, 2, 4)
        self.grid.addWidget(self.level_cement_conductor_edit, 3, 4)

        self.grid.addWidget(self.columnLabel, 8, 0)
        self.grid.addWidget(self.columnType, 9, 0)
        self.grid.addWidget(self.column_wall_thicknessLabel, 8, 1)
        self.grid.addWidget(self.column_wall_thicknessedit_type2, 9, 1)
        self.grid.addWidget(self.shoe_columnLabel, 8, 2)
        self.grid.addWidget(self.shoe_columnedit_type2, 9, 2)
        self.grid.addWidget(self.column_add_trueLabel, 8, 3)
        self.grid.addWidget(self.column_add_true_comboBox, 9, 3)
        self.grid.addWidget(self.column_addLabel, 8, 4)
        self.grid.addWidget(self.column_addedit_type, 9, 4)
        self.grid.addWidget(self.column_add_wall_thicknessLabel, 8, 5)
        self.grid.addWidget(self.column_add_wall_thicknessedit_type2, 9, 5)
        self.grid.addWidget(self.head_column_addLabel, 8, 6)
        self.grid.addWidget(self.head_column_add_edit_type2, 9, 6)
        self.grid.addWidget(self.shoe_column_addLabel, 8, 7)
        self.grid.addWidget(self.shoe_column_add_edit_type2, 9, 7)

        self.grid.addWidget(self.bottomhole_drill_Label, 10, 0)
        self.grid.addWidget(self.bottomhole_drill_edit_type, 11, 0)
        self.grid.addWidget(self.bottomhole_artificial_Label, 10, 1)
        self.grid.addWidget(self.bottomhole_artificial_edit_type, 11, 1)
        self.grid.addWidget(self.current_bottom_Label, 10, 2)
        self.grid.addWidget(self.current_bottom_edit_type, 11, 2)
        self.grid.addWidget(self.max_angle_Label, 10, 3)
        self.grid.addWidget(self.max_angle_edit_type, 11, 3)
        self.grid.addWidget(self.max_angle_H_Label, 10, 4)
        self.grid.addWidget(self.max_angle_H_edit_type, 11, 4)
        self.grid.addWidget(self.max_expected_pressure_Label, 10, 5)
        self.grid.addWidget(self.max_expected_pressure_edit_type, 11, 5)
        self.grid.addWidget(self.max_admissible_pressure_Label, 10, 6)
        self.grid.addWidget(self.max_admissible_pressure_edit_type, 11, 6)
        self.grid.addWidget(self.pump_ECN_do_Label, 13, 0)
        self.grid.addWidget(self.pump_ECN_do_edit_type, 14, 0)
        self.grid.addWidget(self.pump_ECN_depth_do_Label, 13, 1)
        self.grid.addWidget(self.pump_ECN_depth_do_edit_type, 14, 1)
        self.grid.addWidget(self.pump_ECN_posle_Label, 13, 4)
        self.grid.addWidget(self.pump_ECN_posle_edit_type, 14, 4)
        self.grid.addWidget(self.pump_ECN_depth_posle_Label, 13, 5)
        self.grid.addWidget(self.pump_ECN_depth_posle_edit_type, 14, 5)

        self.grid.addWidget(self.pump_SHGN_do_Label, 15, 0)
        self.grid.addWidget(self.pump_SHGN_do_edit_type, 16, 0)
        self.grid.addWidget(self.pump_SHGN_depth_do_Label, 15, 1)
        self.grid.addWidget(self.pump_SHGN_depth_do_edit_type, 16, 1)
        self.grid.addWidget(self.pump_SHGN_posle_Label, 15, 4)
        self.grid.addWidget(self.pump_SHGN_posle_edit_type, 16, 4)
        self.grid.addWidget(self.pump_SHGN_depth_posle_Label, 15, 5)
        self.grid.addWidget(self.pump_SHGN_depth_posle_edit_type, 16, 5)

        self.grid.addWidget(self.paker_do_Label, 17, 0)
        self.grid.addWidget(self.paker_do_edit_type, 18, 0)
        self.grid.addWidget(self.paker_depth_do_Label, 17, 1)
        self.grid.addWidget(self.paker_depth_do_edit_type, 18, 1)
        self.grid.addWidget(self.paker_posle_Label, 17, 4)
        self.grid.addWidget(self.paker_posle_edit_type, 18, 4)
        self.grid.addWidget(self.paker_depth_posle_Label, 17, 5)
        self.grid.addWidget(self.paker_depth_posle_edit_type, 18, 5)

        self.grid.addWidget(self.paker2_do_Label, 19, 0)
        self.grid.addWidget(self.paker2_do_edit_type, 20, 0)
        self.grid.addWidget(self.paker2_depth_do_Label, 19, 1)
        self.grid.addWidget(self.paker2_depth_do_edit_type, 20, 1)
        self.grid.addWidget(self.paker2_posle_Label, 19, 4)
        self.grid.addWidget(self.paker2_posle_edit_type, 20, 4)
        self.grid.addWidget(self.paker2_depth_posle_Label, 19, 5)
        self.grid.addWidget(self.paker2_depth_posle_edit_type, 20, 5)

        self.grid.addWidget(self.static_level_Label, 21, 2)
        self.grid.addWidget(self.static_level_edit_type, 22, 2)
        self.grid.addWidget(self.dinamic_level_Label, 21, 3)
        self.grid.addWidget(self.dinamic_level_edit_type, 22, 3)

        self.grid.addWidget(self.curator_Label, 23, 1)
        self.grid.addWidget(self.curator_Combo, 24, 1)

        self.grid.addWidget(self.region_Label, 23, 2)
        self.grid.addWidget(self.region_Combo, 24, 2)

        self.grid.addWidget(self.type_kr_Label, 23, 3)
        self.grid.addWidget(self.type_kr_Combo, 24, 3)

        self.grid.addWidget(self.nkt_do_label, 27, 1)
        self.grid.addWidget(self.nkt_posle_label, 27, 5)

        self.grid.addWidget(self.sucker_rod_label, 35, 1)
        self.grid.addWidget(self.sucker_rod_po_label, 35, 5)

        self.grid.setColumnStretch(3, 1)
        self.grid.setColumnMinimumWidth(3, 50)

        # добавление строк с НКТ спущенных
        if len(self.dict_nkt) != 0:
            n = 1
            for nkt, lenght in self.dict_nkt.items():
                # print(f'НКТ {nkt, lenght}')
                nkt_line_edit = QLineEdit(self)
                nkt_line_edit.setText(str(self.ifNone(nkt)))

                lenght_line_edit = QLineEdit(self)
                lenght_line_edit.setText(str(self.ifNone(lenght)))

                self.grid.addWidget(nkt_line_edit, 27 + n, 1)
                self.grid.addWidget(lenght_line_edit, 27 + n, 2)

                # Переименование атрибута
                setattr(self, f"{nkt}_{n}_line", nkt_line_edit)
                setattr(self, f"{lenght}_{n}_line", lenght_line_edit)

                self.labels_nkt[n] = (nkt_line_edit, lenght_line_edit)
                n += 1
        else:
            nkt_line_edit = QLineEdit(self)
            lenght_line_edit = QLineEdit(self)

            setattr(self, f"nkt_line", nkt_line_edit)
            setattr(self, f"lenght_line", lenght_line_edit)

            self.labels_nkt[1] = (nkt_line_edit, lenght_line_edit)

            self.grid.addWidget(nkt_line_edit, 28, 1)
            self.grid.addWidget(lenght_line_edit, 28, 2)

        # добавление строк с штанг спущенных
        if len(self.dict_sucker_rod) != 0:
            n = 1
            for sucker, lenght in self.dict_sucker_rod.items():
                sucker_rod_line_edit = QLineEdit(self)
                sucker_rod_line_edit.setText(str(self.ifNone(sucker)))

                lenght_sucker_line_edit = QLineEdit(self)
                lenght_sucker_line_edit.setText(str(self.ifNone(lenght)))

                self.grid.addWidget(sucker_rod_line_edit, 37 + n, 1)
                self.grid.addWidget(lenght_sucker_line_edit, 37 + n, 2)

                # Переименование атрибута
                setattr(self, f"sucker_{n}_line", sucker_rod_line_edit)
                setattr(self, f"lenght_{n}_line", lenght_sucker_line_edit)

                self.labels_sucker[n] = (sucker_rod_line_edit, lenght_sucker_line_edit)
                n += 1
        else:
            sucker_rod_line_edit = QLineEdit(self)
            lenght_sucker_line_edit = QLineEdit(self)

            # Переименование атрибута
            setattr(self, f"sucker_line", sucker_rod_line_edit)
            setattr(self, f"lenght_line", lenght_sucker_line_edit)

            self.labels_sucker[1] = (sucker_rod_line_edit, lenght_sucker_line_edit)

            self.grid.addWidget(sucker_rod_line_edit, 38, 1)
            self.grid.addWidget(lenght_sucker_line_edit, 38, 2)

        if len(self.dict_nkt_po) != 0:
            # добавление строк с НКТ плановых
            n = 1
            for nkt_po, lenght_po in self.dict_nkt_po.items():
                # print(f'НКТ план {nkt_po, lenght_po}')

                nkt_po_line_edit = QLineEdit(self)
                nkt_po_line_edit.setText(str(self.ifNone(nkt_po)))

                lenght_po_line_edit = QLineEdit(self)
                lenght_po_line_edit.setText(str(self.ifNone(lenght_po)))

                self.grid.addWidget(nkt_po_line_edit, 27 + n, 5)
                self.grid.addWidget(lenght_po_line_edit, 27 + n, 6)

                # Переименование атрибута
                setattr(self, f"nkt_po_{n}_line", nkt_po_line_edit)
                setattr(self, f"lenght_po_{n}_line", lenght_po_line_edit)

                self.labels_nkt_po[n] = (nkt_po_line_edit, lenght_po_line_edit)
                n += 1
        else:
            nkt_po_line_edit = QLineEdit(self)
            lenght_po_line_edit = QLineEdit(self)

            # Переименование атрибута
            setattr(self, f"nkt_po_line", nkt_po_line_edit)
            setattr(self, f"lenght_po_line", lenght_po_line_edit)

            self.labels_nkt_po[1] = (nkt_po_line_edit, lenght_po_line_edit)

            self.grid.addWidget(nkt_po_line_edit, 28, 5)
            self.grid.addWidget(lenght_po_line_edit, 28, 6)
        # добавление строк с штангами плановых

        if len(self.dict_sucker_rod_po) != 0:
            n = 1
            for sucker_po, lenght_po in self.dict_sucker_rod_po.items():
                # print(f'штанги план {sucker_po, lenght_po}')
                sucker_rod_po_line_edit = QLineEdit(self)
                sucker_rod_po_line_edit.setText(str(self.ifNone(sucker_po)))

                lenght_sucker_po_line_edit = QLineEdit(self)
                lenght_sucker_po_line_edit.setText(str(self.ifNone(lenght_po)))

                self.grid.addWidget(sucker_rod_po_line_edit, 37 + n, 5)
                self.grid.addWidget(lenght_sucker_po_line_edit, 37 + n, 6)

                # Переименование атрибута
                setattr(self, f"sucker_{n}_line", sucker_rod_po_line_edit)
                setattr(self, f"lenght_{n}_line", lenght_sucker_po_line_edit)

                self.labels_sucker_po[n] = (sucker_rod_po_line_edit, lenght_sucker_po_line_edit)
                n += 1
        else:
            sucker_rod_po_line_edit = QLineEdit(self)
            lenght_sucker_po_line_edit = QLineEdit(self)

            # Переименование атрибута
            setattr(self, f"sucker_line", sucker_rod_po_line_edit)
            setattr(self, f"lenght_line", lenght_sucker_po_line_edit)

            self.labels_sucker_po[1] = (sucker_rod_po_line_edit, lenght_sucker_po_line_edit)

            self.grid.addWidget(sucker_rod_po_line_edit, 38, 5)
            self.grid.addWidget(lenght_sucker_po_line_edit, 38, 6)

        if self.curator_Combo.currentText() == 'ОР':

            self.expected_Q_label = QLabel('Ожидаемая приемистость')
            self.expected_Q_edit = FloatLineEdit(self)
            try:
                self.expected_Q_edit.setText(f'{well_data.expected_Q}')
                # print(f'ожидаемая приемистисть{well_data.expected_Q}')
            except:
                pass
            self.grid.addWidget(self.expected_Q_label, 25, 2)
            self.grid.addWidget(self.expected_Q_edit, 26, 2)

            self.expected_P_label = QLabel('Ожидаемое давление закачки')
            self.expected_P_edit = FloatLineEdit(self)
            try:
                self.expected_P_edit.setText(f'{well_data.expected_P}')
            except:
                pass
            self.grid.addWidget(self.expected_P_label, 25, 3)
            self.grid.addWidget(self.expected_P_edit, 26, 3)
        else:
            self.Qwater_Label = QLabel('Дебит по жидкости')
            self.Qwater_edit = FloatLineEdit(self)
            try:
                self.Qwater_edit.setText(f'{well_data.Qwater}')
            except:
                pass
            self.grid.addWidget(self.Qwater_Label, 25, 1)
            self.grid.addWidget(self.Qwater_edit, 26, 1)
            self.Qoil_Label = QLabel('Дебит по нефти')
            self.Qoil_edit = FloatLineEdit(self)
            try:
                self.Qoil_edit.setText(f'{well_data.Qoil}')
            except:
                pass
            self.grid.addWidget(self.Qoil_Label, 25, 2)
            self.grid.addWidget(self.Qoil_edit, 26, 2)
            self.proc_water_Label = QLabel('Обводненность')

            self.proc_water_edit = FloatLineEdit(self)
            try:
                self.proc_water_edit.setText(f'{well_data.proc_water}')
            except:
                pass
            self.grid.addWidget(self.proc_water_Label, 25, 3)
            self.grid.addWidget(self.proc_water_edit, 26, 3)

        curator_list = ['ГРР', 'ОР', 'ГТМ', 'ГО', 'ВНС']
        self.curator_Combo.addItems(curator_list)
        # print(self.pump_SHGN_posle_edit_type.text() != 'отсут', self.pump_ECN_posle_edit_type.text() != 'отсут')

        curator = 'ОР' if (self.pump_SHGN_posle_edit_type.text() == 'отсут' \
                           and self.pump_ECN_posle_edit_type.text() == 'отсут') else 'ГТМ'
        if well_data.work_plan in ['gnkt_frez', 'gnkt_bopz']:
            curator = 'ВНС'

        self.curator_Combo.currentTextChanged.connect(self.update_curator)
        # print(f'куратор индекс {curator, curator_list.index(curator)}')
        self.curator_Combo.setCurrentIndex(curator_list.index(curator))
        self.region_Combo.addItems(well_data.region_list)
        self.region_Combo.setCurrentIndex(well_data.region_list.index(well_data.region))

        self.type_kr_Combo.view().setWordWrap(True)
        self.type_kr_Combo.setSizeAdjustPolicy(QComboBox.AdjustToMinimumContentsLength)

        self.type_kr_Combo.addItems(well_data.type_kr_list)

        try:
            self.type_kr_Combo.setCurrentIndex(well_data.type_kr_list.index(well_data.type_kr))
        except:
            pass

    def update_curator(self):

        # Очистка и удаление существующих виджетов, если они уже были добавлены ранее

        try:
            self.expected_P_label.setParent(None)
        except:
            pass
        try:
            self.expected_P_edit.setParent(None)
        except:
            pass
        try:
            self.expected_Q_label.setParent(None)
        except:
            pass
        try:
            self.expected_Q_edit.setParent(None)
        except:
            pass
        try:
            self.Qwater_Label.setParent(None)
        except:
            pass
        try:
            self.Qwater_edit.setParent(None)
        except:
            pass
        try:
            self.Qoil_Label.setParent(None)
        except:
            pass
        try:
            self.Qoil_edit.setParent(None)
        except:
            pass
        try:
            self.proc_water_Label.setParent(None)
        except:
            pass
        try:
            self.proc_water_edit.setParent(None)
        except:
            pass

        if self.curator_Combo.currentText() == 'ОР':
            self.expected_Q_label = QLabel('Ожидаемая приемистость')
            self.expected_Q_edit = FloatLineEdit(self)
            try:
                self.expected_Q_edit.setText(f'{well_data.expected_Q}')
            except:
                pass
            self.grid.addWidget(self.expected_Q_label, 25, 4)
            self.grid.addWidget(self.expected_Q_edit, 26, 4)

            self.expected_P_label = QLabel('Ожидаемое давление закачки')
            self.expected_P_edit = FloatLineEdit(self)
            self.expected_P_edit.setText(f'{well_data.expected_P}')
            self.grid.addWidget(self.expected_P_label, 25, 5)
            self.grid.addWidget(self.expected_P_edit, 26, 5)
        else:
            self.Qwater_Label = QLabel('Дебит по жидкости')
            self.Qwater_edit = FloatLineEdit(self)
            try:
                self.Qwater_edit.setText(f'{well_data.Qwater}')
            except:
                pass
            self.grid.addWidget(self.Qwater_Label, 25, 1)
            self.grid.addWidget(self.Qwater_edit, 26, 1)
            self.Qoil_Label = QLabel('Дебит по нефти')
            self.Qoil_edit = FloatLineEdit(self)
            try:
                self.Qoil_edit.setText(f'{well_data.Qoil}')
            except:
                pass
            self.grid.addWidget(self.Qoil_Label, 25, 2)
            self.grid.addWidget(self.Qoil_edit, 26, 2)
            self.proc_water_Label = QLabel('Обводненность')

            self.proc_water_edit = FloatLineEdit(self)
            try:
                self.proc_water_edit.setText(f'{well_data.proc_water}')
            except:
                pass
            self.grid.addWidget(self.proc_water_Label, 25, 3)
            self.grid.addWidget(self.proc_water_edit, 26, 3)

    def ifNone(self, string):

        if str(string) in ['0', str(None), '-', '--']:
            return 'отсут'
        if '/' in str(string):
            return string.split('/')[0]
        elif str(string).replace('.', '').replace(',', '').isdigit():

            # print(str(round(float(string), 1))[-1] == '0', int(string), float(string))
            return int(float(str(string).replace(',', '.'))) if str(round(float(str(string).replace(',', '.')), 1))[-1] == "0" else \
                round(float(str(string).replace(',', '.')), 1)
        else:
            return str(string)

    def remove_non_numeric_chars(self, string):

        pattern = r"[^\d\.,]"
        if re.sub(pattern, "", str(string)) == '':
            return string
        else:
            return re.sub(pattern, "", str(string))

    def updateLabel(self):
        # self.dinamic_level_Label
        self.columnType.setText()
        self.column_addedit_type.setText()
        self.update()


class TabWidget(QTabWidget):
    def __init__(self):
        super().__init__()
        self.addTab(TabPage_SO_correct(self), 'Проверка корректности данных')


class DataWindow(QMainWindow):

    def __init__(self, parent=None):
        super(DataWindow, self).__init__()

        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.setWindowModality(QtCore.Qt.ApplicationModal)  # Устанавливаем модальность окна

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
        from find import ProtectedIsNonNone, ProtectedIsDigit


        region_Combo = self.tabWidget.currentWidget().region_Combo.currentText()
        type_kr_Combo = self.tabWidget.currentWidget().type_kr_Combo.currentText()


        if region_Combo == '':
            QMessageBox.warning(self, 'ОШИБКА', 'Не выбран регион')
            return
        if type_kr_Combo == '':
            QMessageBox.warning(self, 'ОШИБКА', 'Не выбран Вид и категория ремонта')
            return


        columnType = self.tabWidget.currentWidget().columnType.text()
        column_wall_thickness = self.tabWidget.currentWidget().column_wall_thicknessedit_type2.text()
        shoe_column = self.tabWidget.currentWidget().shoe_columnedit_type2.text()
        column_add_True = str(self.tabWidget.currentWidget().column_add_true_comboBox.currentText())
        if column_add_True == 'в наличии':
            well_data.column_additional = True
        else:
            well_data.column_additional = False
        column_additional_diametr = self.tabWidget.currentWidget().column_addedit_type.text()
        column_additional_wall_thickness = self.tabWidget.currentWidget().column_add_wall_thicknessedit_type2.text()
        shoe_column_additional = self.tabWidget.currentWidget().shoe_column_add_edit_type2.text()
        head_column_additional = self.tabWidget.currentWidget().head_column_add_edit_type2.text()
        bottomhole_drill = self.tabWidget.currentWidget().bottomhole_drill_edit_type.text()
        bottomhole_artificial = self.tabWidget.currentWidget().bottomhole_artificial_edit_type.text()
        current_bottom = self.tabWidget.currentWidget().current_bottom_edit_type.text().replace(',', '.')
        max_angle_H = self.tabWidget.currentWidget().max_angle_H_edit_type.text()
        max_angle = self.tabWidget.currentWidget().max_angle_edit_type.text()
        max_expected_pressure = self.tabWidget.currentWidget().max_expected_pressure_edit_type.text()
        max_admissible_pressure = self.tabWidget.currentWidget().max_admissible_pressure_edit_type.text()

        column_direction_diametr = self.tabWidget.currentWidget().column_direction_diametr_edit.text()
        column_direction_wall_thickness = self.tabWidget.currentWidget().column_direction_wall_thickness_edit.text()
        column_direction_lenght = self.tabWidget.currentWidget().column_direction_lenght_edit.text()
        level_cement_direction = self.tabWidget.currentWidget().level_cement_direction_edit.text()
        column_conductor_diametr = self.tabWidget.currentWidget().column_conductor_diametr_edit.text()
        column_conductor_wall_thickness = self.tabWidget.currentWidget().column_conductor_wall_thickness_edit.text()
        column_conductor_lenght = self.tabWidget.currentWidget().column_conductor_lenght_edit.text()
        level_cement_conductor = self.tabWidget.currentWidget().level_cement_conductor_edit.text()

        dict_pump_SHGN_do = str(self.tabWidget.currentWidget().pump_SHGN_do_edit_type.text())
        dict_pump_SHGN_h_do = self.tabWidget.currentWidget().pump_SHGN_depth_do_edit_type.text()

        dict_pump_SHGN_posle = str(self.tabWidget.currentWidget().pump_SHGN_posle_edit_type.text())
        dict_pump_SHGN_h_posle = str(self.tabWidget.currentWidget().pump_SHGN_depth_posle_edit_type.text())

        dict_pump_ECN_do = str(self.tabWidget.currentWidget().pump_ECN_do_edit_type.text())
        dict_pump_ECN_h_do = self.tabWidget.currentWidget().pump_ECN_depth_do_edit_type.text()

        dict_pump_ECN_posle = str(self.tabWidget.currentWidget().pump_ECN_posle_edit_type.text())
        dict_pump_ECN_h_posle = str(self.tabWidget.currentWidget().pump_ECN_depth_posle_edit_type.text())

        # print(f'прио {type(dict_pump_h_posle)}')
        paker_do = str(self.tabWidget.currentWidget().paker_do_edit_type.text())
        depth_fond_paker_do = str(self.tabWidget.currentWidget().paker_depth_do_edit_type.text())
        paker_posle = self.tabWidget.currentWidget().paker_posle_edit_type.text()
        depth_fond_paker_posle = self.tabWidget.currentWidget().paker_depth_posle_edit_type.text()

        paker2_do = str(self.tabWidget.currentWidget().paker2_do_edit_type.text())
        depth_fond_paker2_do = self.tabWidget.currentWidget().paker2_depth_do_edit_type.text()
        paker2_posle = self.tabWidget.currentWidget().paker2_posle_edit_type.text()
        depth_fond_paker2_posle = self.tabWidget.currentWidget().paker2_depth_posle_edit_type.text()

        static_level = self.tabWidget.currentWidget().static_level_edit_type.text()
        dinamic_level = self.tabWidget.currentWidget().dinamic_level_edit_type.text()
        curator = str(self.tabWidget.currentWidget().curator_Combo.currentText())

        if curator == 'ОР':
            expected_Q_edit = self.tabWidget.currentWidget().expected_Q_edit.text()
            expected_P_edit = self.tabWidget.currentWidget().expected_P_edit.text()
        else:
            Qwater_edit = self.tabWidget.currentWidget().Qwater_edit.text()
            Qoil_edit = self.tabWidget.currentWidget().Qoil_edit.text()
            proc_water_edit = self.tabWidget.currentWidget().proc_water_edit.text()

        # Пересохранение данных по НКТ и штангам
        self.dict_sucker_rod = well_data.dict_sucker_rod
        self.dict_sucker_rod = well_data.dict_sucker_rod_po
        self.dict_nkt = well_data.dict_nkt
        self.dict_nkt_po = well_data.dict_nkt_po
        # print(self.dict_nkt, self.dict_nkt_po)
        if self.dict_nkt:
            for key in range(1, len(self.dict_nkt)):
                well_data.dict_nkt[self.tabWidget.currentWidget().labels_nkt[key][0].text()] = self.if_None(
                    int(float(self.tabWidget.currentWidget().labels_nkt[key][1].text())))
        else:
            if self.tabWidget.currentWidget().labels_nkt[1][1].text():
                well_data.dict_nkt[self.tabWidget.currentWidget().labels_nkt[1][0].text()] = self.if_None(
                    int(float(self.tabWidget.currentWidget().labels_nkt[1][1].text())))
        if self.dict_nkt_po:
            for key in range(1, len(self.dict_nkt_po)):
                dict_nkt_correct = self.tabWidget.currentWidget().labels_nkt_po[key][1].text()

                well_data.dict_nkt_po[self.tabWidget.currentWidget().labels_nkt_po[key][0].text()] = self.if_None(
                    int(float(dict_nkt_correct)))
        else:
            if self.tabWidget.currentWidget().labels_nkt_po[1][1].text():
                well_data.dict_nkt[self.tabWidget.currentWidget().labels_nkt_po[1][0].text()] = self.if_None(
                    int(float(self.tabWidget.currentWidget().labels_nkt_po[1][1].text())))

        if self.dict_sucker_rod.items():
            for key in range(1, len(self.dict_sucker_rod.items())):
                well_data.dict_sucker_rod_po[
                    self.tabWidget.currentWidget().labels_sucker_po[key][0].text()] = self.if_None(
                    self.tabWidget.currentWidget().labels_sucker_po[key][1].text())
        else:
            if self.tabWidget.currentWidget().labels_sucker_po[1][1].text():
                well_data.dict_sucker_rod_po[
                    self.tabWidget.currentWidget().labels_sucker_po[1][0].text()] = self.if_None(
                    self.tabWidget.currentWidget().labels_sucker_po[1][1].text())

        close_file = True

        if any([self.ifNum(data_well) is False or data_well in ['не корректно', 0, 'отсут'] for data_well in
                [columnType, column_wall_thickness, shoe_column]]):
            msg = QMessageBox.information(self, 'Внимание', 'Не все поля в данных колонне соответствуют значениям')
            close_file = False

        elif float(bottomhole_artificial) > 10000 or float(bottomhole_drill) > 10000:
            QMessageBox.information(self, 'Внимание', 'Забой не корректный')
            close_file = False

        elif any([self.ifNum(data_well) is False for data_well in
                  [column_additional_diametr, column_additional_wall_thickness,
                   shoe_column_additional, head_column_additional]]) and well_data.column_additional is True:
            msg = QMessageBox.information(self, 'Внимание', 'Не все поля в доп колонне соответствуют значениям')
            close_file = False
        elif self.ifNum(bottomhole_artificial) is False \
                or self.ifNum(bottomhole_drill) is False \
                or self.ifNum(current_bottom) is False \
                or self.ifNum(max_angle_H) is False \
                or self.ifNum(max_angle) is False \
                or self.ifNum(max_admissible_pressure) is False \
                or self.ifNum(max_expected_pressure) is False:
            msg = QMessageBox.information(self, 'Внимание', 'Не все поля в забое соответствуют значениям')
            close_file = False
        elif self.ifNum(static_level) is False \
                or self.ifNum(dinamic_level) is False:
            msg = QMessageBox.information(self, 'Внимание', 'Не все поля в уровнях соответствуют значениям')
            close_file = False
        elif self.ifNum(dict_pump_ECN_h_do) is False \
                or self.ifNum(dict_pump_ECN_h_posle) is False \
                or self.ifNum(dict_pump_SHGN_h_do) is False \
                or self.ifNum(dict_pump_SHGN_h_posle) is False \
                or self.ifNum(depth_fond_paker_do) is False \
                or self.ifNum(depth_fond_paker_posle) is False \
                or self.ifNum(depth_fond_paker2_do) is False \
                or self.ifNum(depth_fond_paker2_posle) is False:
            msg = QMessageBox.information(self, 'Внимание', 'Не все поля в спущенном оборудовании'
                                                            ' соответствуют значениям')
            close_file = False
        elif well_data.column_additional:
            if int(float(str(head_column_additional).replace(',', '.'))) < 10:
                msg = QMessageBox.information(self, 'Внимание', 'доп колонна не может быть близко 0')
                close_file = False
        elif self.ifNum(column_direction_diametr) is False \
                or self.ifNum(column_direction_wall_thickness) is False \
                or self.ifNum(column_direction_lenght) is False \
                or self.ifNum(level_cement_direction) is False:

            msg = QMessageBox.information(self, 'Внимание', 'Не все поля в Направлении соответствуют значениям')
            close_file = False
        elif self.ifNum(column_conductor_diametr) is False \
                or self.ifNum(column_conductor_wall_thickness) is False \
                or self.ifNum(column_conductor_lenght) is False \
                or self.ifNum(column_direction_lenght) is False \
                or self.ifNum(level_cement_conductor) is False:

            msg = QMessageBox.information(self, 'Внимание', 'Не все поля в кондукторе соответствуют значениям')
            close_file = False

        elif any(['НВ' in dict_pump_SHGN_do.upper(), 'ШГН' in dict_pump_SHGN_do.upper(),
                  'НН' in dict_pump_SHGN_do.upper(), dict_pump_SHGN_do == 'отсут',
                  'RH' in dict_pump_SHGN_do.upper()]) is False \
                or any(['НВ' in dict_pump_SHGN_posle.upper(), 'ШГН' in dict_pump_SHGN_posle.upper(),
                        'НН' in dict_pump_SHGN_posle.upper(), dict_pump_SHGN_posle == 'отсут',
                        'RHAM' in dict_pump_SHGN_do]) is False \
                or any(['ЭЦН' in dict_pump_ECN_posle.upper(), 'ВНН' in dict_pump_ECN_posle.upper(),
                        dict_pump_ECN_posle == 'отсут']) is False \
                or (dict_pump_ECN_do != 'отсут' and dict_pump_ECN_h_do == 'отсут') \
                or (dict_pump_ECN_posle != 'отсут' and dict_pump_ECN_h_posle == 'отсут') \
                or (dict_pump_SHGN_do != 'отсут' and dict_pump_SHGN_h_do == 'отсут') \
                or (dict_pump_SHGN_posle != 'отсут' and dict_pump_SHGN_h_posle == 'отсут') \
                or (paker_do != 'отсут' and depth_fond_paker_do == 'отсут') \
                or (paker_posle != 'отсут' and depth_fond_paker_posle == 'отсут') \
                or (paker2_do != 'отсут' and depth_fond_paker2_do == 'отсут') \
                or (paker2_posle != 'отсут' and depth_fond_paker2_posle == 'отсут') \
                or any(['ЭЦН' in dict_pump_ECN_do.upper(), 'ВНН' in dict_pump_ECN_do.upper(),
                        dict_pump_ECN_do == 'отсут']) is False:

            msg = QMessageBox.information(self, 'Внимание', 'Не все поля соответствуют значениям')
            close_file = False
        elif isinstance(self.ifNum(head_column_additional), str):
            # print(self.if_None(head_column_additional), isinstance(self.ifNum(head_column_additional), str))
            if self.if_None(20 if self.ifNum(head_column_additional) else head_column_additional) < 5:
                # print(self.if_None(head_column_additional))
                msg = QMessageBox.information(self, 'Внимание', 'В скважине отсутствует доп колонна')
                close_file = False
            else:
                msg = QMessageBox.information(self, 'Внимание', 'В скважине отсутствует доп колонна')
                close_file = False

        elif all([pump for pump in [self.ifNum(dict_pump_ECN_do), self.ifNum(paker2_do),
                                    self.ifNum(dict_pump_SHGN_do), self.ifNum(paker_do)]]):
            voronka_question = QMessageBox.question(self, 'Внимание',
                                                    'Программа определила что в скважине до ремонта воронка, верно ли')
            if voronka_question == QMessageBox.StandardButton.No:
                close_file = False
            else:
                close_file = True

        elif all([pump for pump in [self.ifNum(dict_pump_ECN_posle), self.ifNum(paker2_posle),
                                    self.ifNum(dict_pump_SHGN_posle), self.ifNum(paker_posle)]]):

            voronka_question = QMessageBox.question(self, 'Внимание',
                                                    'Программа определила что в скважине После ремонта воронка, верно ли')
            if voronka_question == QMessageBox.StandardButton.No:
                close_file = False
            else:
                close_file = True
        elif (well_data.nkt_mistake is True and len(well_data.dict_nkt) == 0):
            msg = QMessageBox.information(self, 'Внимание',
                                          'При вызванной ошибке НКТ до ремонта не может быть пустым')
            close_file = False
        elif well_data.nkt_mistake is True and len(well_data.dict_nkt_po) == 0:
            msg = QMessageBox.information(self, 'Внимание',
                                          'При вызванной ошибке НКТ после ремонта не может быть пустым')
            close_file = False

        elif well_data.column_additional:
            if int(column_additional_diametr) >= int(columnType):
                msg = QMessageBox.information(self, 'Внимание', 'Ошибка в диаметре доп колонны')
                close_file = False

        if type_kr_Combo in ['КР13-1  Подготовительные работы к ГРП (ПР)',
                             'КР13-2  Освоение скважины после ГРП (ЗР)',
                             'КР13-1  Подготовительные работы к ГРП (ПР) КР13-2  Освоение скважины после ГРП (ЗР)',
                             'КР13-5  Подготовка скважины к проведению работ по повышению н/отдачи пластов',
                             'КР13-6  Подготовительные работы к ГГРП (ПР)',
                             'КР13-7  Заключительные работы (ЗР) после ГГРП (освоение скважины и т.д.)',
                             'КР7-2  Проведение ГРП',
                             'КР7-3  Проведение ГГРП',
                             'КР7-4  Проведение ГПП']:
            well_data.grp_plan = True
        else:
            well_data.grp_plan = False

        if curator == 'ОР':
            if self.ifNum(expected_Q_edit) is False or self.ifNum(expected_P_edit) is False:
                msg = QMessageBox.information(self, 'Внимание',
                                              'Не все поля в Ожидаемых показателях соответствуют значениям')
                close_file = False
        else:
            if self.ifNum(Qwater_edit) is False or self.ifNum(Qoil_edit) is False or \
                    self.ifNum(proc_water_edit) is False:
                QMessageBox.information(self, 'Внимание',
                                              'Не все поля в Ожидаемых показателях соответствуют значениям')
                close_file = False
        try:
            if float(shoe_column) < 30:
                QMessageBox.warning(self, 'Ошибка', 'Башмак ЭК слишком короткий')
                return
        except Exception as e:
             QMessageBox.warning(self, 'Ошибка', f'Башмак ЭК не корректен {type(e).__name__}\n\n{str(e)}')



        if close_file is False:
            return
        elif close_file is True:
            well_data.column_diametr = ProtectedIsDigit(self.if_None(columnType))
            well_data.column_wall_thickness = ProtectedIsDigit(self.if_None(column_wall_thickness))
            well_data.shoe_column = ProtectedIsDigit(int(float(self.if_None(shoe_column))))
            if well_data.column_additional:
                well_data.column_additional_diametr = ProtectedIsDigit(self.if_None(column_additional_diametr))
                well_data.column_additional_wall_thickness = ProtectedIsDigit(
                    self.if_None(column_additional_wall_thickness))
                well_data.shoe_column_additional = ProtectedIsDigit(int(float(self.if_None(shoe_column_additional))))
                well_data.head_column_additional = ProtectedIsDigit(int(float(self.if_None(head_column_additional))))
            else:
                well_data.column_additional_diametr = ProtectedIsDigit(0)
                well_data.column_additional_wall_thickness = ProtectedIsDigit(0)
                well_data.shoe_column_additional = ProtectedIsDigit(0)
                well_data.head_column_additional = ProtectedIsDigit(0)

            well_data.bottomhole_drill = ProtectedIsDigit(self.if_None(bottomhole_drill))
            well_data.bottomhole_artificial = ProtectedIsDigit(self.if_None(bottomhole_artificial))
            well_data.current_bottom = self.if_None(current_bottom)
            well_data.bottom = self.if_None(current_bottom)
            well_data.max_angle = ProtectedIsDigit(self.if_None(max_angle))
            well_data.max_expected_pressure = ProtectedIsDigit(self.if_None(max_expected_pressure))
            well_data.max_admissible_pressure = ProtectedIsDigit(self.if_None(max_admissible_pressure))

            # print(f'макс {well_data.max_expected_pressure._value}')
            well_data.dict_pump_SHGN["do"] = self.if_None(dict_pump_SHGN_do)
            well_data.dict_pump_SHGN_h["do"] = self.if_None(dict_pump_SHGN_h_do)
            well_data.dict_pump_SHGN_h["posle"] = self.if_None(dict_pump_SHGN_h_posle)
            well_data.dict_pump_SHGN["posle"] = self.if_None(dict_pump_SHGN_posle)

            well_data.dict_pump_ECN["do"] = self.if_None(dict_pump_ECN_do)
            well_data.dict_pump_ECN_h["do"] = self.if_None(dict_pump_ECN_h_do)
            well_data.dict_pump_ECN["posle"] = self.if_None(dict_pump_ECN_posle)
            well_data.dict_pump_ECN_h["posle"] = self.if_None(dict_pump_ECN_h_posle)

            well_data.paker_do["do"] = self.if_None(paker_do)
            well_data.depth_fond_paker_do["do"] = self.if_None(depth_fond_paker_do)
            well_data.paker_do["posle"] = self.if_None(paker_posle)
            well_data.depth_fond_paker_do["posle"] = self.if_None(depth_fond_paker_posle)

            well_data.paker2_do["do"] = self.if_None(paker2_do)
            well_data.depth_fond_paker2_do["do"] = self.if_None(depth_fond_paker2_do)
            well_data.paker2_do["posle"] = self.if_None(paker2_posle)
            well_data.depth_fond_paker2_do["posle"] = self.if_None(depth_fond_paker2_posle)
            well_data.static_level = ProtectedIsDigit(self.if_None(static_level))
            well_data.dinamic_level = ProtectedIsDigit(self.if_None(dinamic_level))

            well_data.column_direction_diametr = ProtectedIsDigit(self.if_None(column_direction_diametr))
            well_data.column_direction_wall_thickness = ProtectedIsDigit(self.if_None(column_direction_wall_thickness))
            well_data.column_direction_lenght = ProtectedIsDigit(self.if_None(column_direction_lenght))
            well_data.level_cement_direction = ProtectedIsDigit(self.if_None(level_cement_direction))
            well_data.column_conductor_diametr = ProtectedIsDigit(self.if_None(column_conductor_diametr))
            well_data.column_conductor_wall_thickness = ProtectedIsDigit(self.if_None(column_conductor_wall_thickness))
            well_data.column_conductor_lenght = ProtectedIsDigit(self.if_None(column_conductor_lenght))
            well_data.level_cement_conductor = ProtectedIsDigit(self.if_None(level_cement_conductor))
            if curator == 'ОР':
                well_data.expected_P = self.if_None(expected_P_edit)
                well_data.expected_Q = self.if_None(expected_Q_edit)
                well_data.expected_pick_up[well_data.expected_Q] = well_data.expected_P
                well_data.proc_water = 100
            else:
                well_data.Qoil = self.if_None(Qoil_edit)
                well_data.Qwater = self.if_None(Qwater_edit)
                well_data.proc_water = int(self.if_None(proc_water_edit))

            well_data.curator = curator
            if curator in ['ВНС']:
                well_data.bvo = True
            elif curator in ['ГРР'] and well_data.work_plan in ['gnkt_after_grp']:
                well_data.bvo = True
            elif well_data.work_plan in ['gnkt_frez']:
                well_data.bvo = True
            well_data.data_well_dict = {
                'направление': {
                    'диаметр': well_data.column_direction_diametr._value,
                    'толщина стенки': well_data.column_direction_wall_thickness._value,
                    'башмак': well_data.column_direction_lenght._value,
                    'цемент': well_data.level_cement_direction._value},
                'кондуктор': {
                    'диаметр': well_data.column_conductor_diametr._value,
                    'толщина стенки': well_data.column_conductor_wall_thickness._value,
                    'башмак': well_data.column_conductor_lenght._value,
                    'цемент': well_data.level_cement_conductor._value},
                'ЭК': {
                    'диаметр': well_data.column_diametr._value,
                    'толщина стенки': well_data.column_wall_thickness._value,
                    'башмак': well_data.shoe_column._value,
                    'цемент': well_data.level_cement_column._value},
                'допколонна': {
                    'наличие': well_data.column_additional,
                    'диаметр': well_data.column_additional_diametr._value,
                    'толщина стенки': well_data.column_additional_wall_thickness._value,
                    'голова': well_data.head_column_additional._value,
                    'башмак': well_data.shoe_column_additional._value},
                'куратор': curator,
                'регион': well_data.region,
                'ЦДНГ': well_data.cdng._value,
                'оборудование': {
                    'ЭЦН':
                        {
                            'тип': well_data.dict_pump_ECN,
                            'глубина ': well_data.dict_pump_ECN_h
                        },
                    'ШГН':
                        {
                            'тип': well_data.dict_pump_SHGN,
                            'глубина ': well_data.dict_pump_SHGN_h
                        },
                    'пакер':
                        {
                            'тип': well_data.paker_do,
                            'глубина ': well_data.depth_fond_paker_do
                        },
                    'пакер2':
                        {
                            'тип': well_data.paker2_do,
                            'глубина ': well_data.depth_fond_paker2_do
                        },

                },
                'статика': well_data.static_level._value,
                'динамика': well_data.dinamic_level._value,
                'НКТ': well_data.dict_nkt_po,
                'штанги': well_data.dict_sucker_rod_po,
                'ожидаемые': {
                    'нефть': well_data.Qoil,
                    'вода': well_data.Qwater,
                    'обводненность': well_data.proc_water,
                    'давление': well_data.expected_P,
                    'приемистость': well_data.expected_Q
                },
                'данные': {
                    'пробуренный забой': well_data.bottomhole_drill._value,
                    'искусственный забой': well_data.bottomhole_artificial._value,
                    'максимальный угол': well_data.max_angle._value,
                    'глубина': well_data.max_angle_H._value,
                    'максимальное ожидаемое давление': well_data.max_expected_pressure._value,
                    'максимальное допустимое давление': well_data.max_admissible_pressure._value
                }
            }

            if str(well_data.paker_do['posle']).lower() not in ['0', 0, '-', 'отсут', '', None]:
                a = well_data.depth_fond_paker_do['posle']



            well_data.pause = False
            self.close()

    def if_None(self, value):
        if value is None or 'отс' in str(value).lower() or value == '-' or str(value) == '0':
            return 0
        elif isinstance(value, int):
            return int(value)
        elif str(value).replace('.', '').replace(',', '').isdigit():

            if str(round(float(value.replace(',', '.')), 1))[-1] == "0":

                return int(float(value.replace(',', '.')))
            else:

                return round(float(value.replace(',', '.')), 1)
        else:
            return value

    def if_string_list(self, string):
        try:
            if len(string.split('-')) == 2:
                return True
            else:
                if str(string) == 'отсут' or string == 0:
                    return True
                else:
                    return False
        except:
            if str(string) == 'отсут' or string == 0:
                return True
            else:
                return False

    def ifNum(self, string):
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
    window = DataWindow()
    QTimer.singleShot(2000, DataWindow.updateLabel)
    # window.show()
    app.exec_()
