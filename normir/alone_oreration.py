import json
import logging
from collections import namedtuple
from datetime import datetime

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QInputDialog, QMessageBox
from openpyxl.styles import Font, Alignment
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

import well_data
from normir.files_with_list import operation_list

def definition_plast_work(self):
    # Определение работающих пластов
    plast_work = set()
    perforation_roof = well_data.current_bottom
    perforation_sole = 0

    for plast, value in well_data.dict_perforation.items():
        for interval in value['интервал']:

            if well_data.dict_perforation[plast]["отключение"] is False:
                plast_work.add(plast)
            roof = min(list(map(lambda x: x[0], list(well_data.dict_perforation[plast]['интервал']))))
            sole = max(list(map(lambda x: x[1], list(well_data.dict_perforation[plast]['интервал']))))
            well_data.dict_perforation[plast]["кровля"] = roof
            well_data.dict_perforation[plast]["подошва"] = sole
            if well_data.dict_perforation[plast]["отключение"] is False:

                if perforation_roof >= roof and well_data.current_bottom > roof:
                    perforation_roof = roof
                if perforation_sole < sole and well_data.current_bottom > sole:
                    perforation_sole = sole

    well_data.perforation_roof = perforation_roof
    well_data.perforation_sole = perforation_sole
    well_data.dict_perforation = dict(
        sorted(well_data.dict_perforation.items(), key=lambda item: (not item[1]['отключение'],
                                                                     item[0])))
    well_data.plast_all = list(well_data.dict_perforation.keys())
    well_data.plast_work = list(plast_work)


def count_row_height(ws2, work_list,  merged_cells_dict):


    ind_ins = 46

    stop_str = len(work_list)
    for i in range(1, stop_str + 1):  # Добавлением работ
        for j in range(1, 31):
            cell = ws2.cell(row=i, column=j)
            if cell and str(cell) != str(work_list[i - 1][j - 1]):
                if work_list[i - 1][j - 1]:
                    # if work_list[i - 1][j - 1] in operation_list:
                    #     oper_list = '"' + ','.join(operation_list) + '"'
                    #     rule = DataValidation(type="list", formula1=oper_list, allow_blank=True)
                    #
                    #     ws2.add_data_validation(rule)
                    #     ind = f'{get_column_letter(j)}{i}'
                    #     rule.ranges = ind

                    cell.value = is_num(work_list[i - 1][j - 1])
                    if i >= ind_ins:

                        if j == 11:
                            cell.font = Font(name='Times New Roman', size=11, bold=False)
                        else:
                            cell.font = Font(name='Times New Roman', size=16, bold=False)
                        ws2.cell(row=i, column=2).alignment = Alignment(wrap_text=True, horizontal='center',
                                                                        vertical='center')
                        ws2.cell(row=i, column=11).alignment = Alignment(wrap_text=True, horizontal='center',
                                                                         vertical='center')
                        ws2.cell(row=i, column=12).alignment = Alignment(wrap_text=True, horizontal='center',
                                                                         vertical='center')
                        ws2.cell(row=i, column=3).alignment = Alignment(wrap_text=True, horizontal='left',
                                                                        vertical='center')






    ws2.merge_cells(start_row=77, start_column=2, end_row=77, end_column=3)
    ws2.merge_cells(start_row=77, start_column=6, end_row=77, end_column=14)
    for key, row in merged_cells_dict.items():
        ws2.merge_cells(start_row=row[1], start_column=row[0], end_row=row[3], end_column=row[2])

    return 'Высота изменена'

def is_num(num):
    try:
        if isinstance(num, datetime):
            return num.strftime('%d.%m.%Y')
        elif str(round(float(num), 6))[-1] != 0:
            return round(float(num), 6)
        elif str(round(float(num), 5))[-1] != 0:
            return round(float(num), 5)
        elif str(round(float(num), 4))[-1] != 0:
            return round(float(num), 4)
        elif str(round(float(num), 3))[-1] != 0:
            return round(float(num), 3)
        elif str(round(float(num), 2))[-1] != 0:
            return round(float(num), 2)
        elif str(round(float(num), 1))[-1] != 0:
            return round(float(num), 1)
        elif str(round(float(num), 0))[-1] != 0:
            return int(float(num))
    except:
        return num
def is_number(num):
    if num is None:
        return 0
    try:
        float(str(num).replace(",", "."))
        return True
    except ValueError or TypeError:
        return False


# Определение трех режимов давлений при определении приемистости
def pressure_mode(mode, plast):
    mode = float(mode) / 10 * 10
    if mode > well_data.max_admissible_pressure._value and (plast != 'D2ps' or plast.lower() != 'дпаш'):
        mode_str = f'{float(mode)}, {float(mode) - 10}, {float(mode) - 20}'
    elif (plast == 'D2ps' or plast.lower() == 'дпаш') and well_data.region == 'ИГМ':
        mode_str = f'{120}, {140}, {160}'
    else:
        mode_str = f'{float(mode) - 10}, {float(mode)}, {float(mode) + 10}'
    return mode_str


