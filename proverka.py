from PyQt5 import QtWidgets
from openpyxl.reader.excel import load_workbook
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter
from openpyxl.workbook import Workbook

# fname = 'property_excel/template_normir_new.xlsm'
# wb2 = load_workbook(fname, keep_vba=True)
# name_list = wb2.sheetnames
# # print(name_list)
# ws2 = wb2['АВР']
# if fname:
#     normir_list = []
#     for row_ind, row in enumerate(ws2.iter_rows(max_col=31, min_row=1252, max_row=1252)):
#         list = []
#         for col, value in enumerate(row):
#             list.append(value.value)
#         normir_list.append(list)
#
#     print(normir_list)

import openpyxl

# Загружаем файл Excel
from openpyxl.worksheet.datavalidation import DataValidation

wb = openpyxl.load_workbook('Книга1.xlsx')
ws2 = wb['Лист1']

# Список работ
work_list = [
    ['Работа 1', 'Описание 1', 10, 20, 30],
    ['Работа 2', 'Описание 2', 40, 50, 60],
    ['Работа 3', 'Описание 3', 70, 80, 90]
]

# Список операций
operation_list = ['Операция 1', 'Операция 2', 'Операция 3']

stop_str = len(work_list)
ind_ins = 2 # Начало вставки данных с 2-й строки

# Заполняем таблицу данными
for i in range(1, stop_str + 1):
    for j in range(1, len(work_list[0]) + 1): # Изменено на len(work_list[0]) + 1
        cell = ws2.cell(row=i, column=j)
        if cell and str(cell) != str(work_list[i - 1][j - 1]):
            if work_list[i - 1][j - 1]:
                if 70 == work_list[i - 1][j - 1]:
                    oper_list = '"' + ','.join(operation_list) + '"'
                    rule = DataValidation(type="list", formula1=oper_list, allow_blank=True)

                    ws2.add_data_validation(rule)
                    ind = f'{get_column_letter(j)}{i}'
                    rule.ranges = ind

                    cell.value = work_list[i - 1][j - 1]
                if i >= ind_ins:
                    # Форматирование ячеек
                    cell.font = Font(name='Times New Roman', size=16, bold=False)
                    # Выравнивание текста в ячейках
                    ws2.cell(row=i, column=2).alignment = Alignment(wrap_text=True, horizontal='center', vertical='center')
                    ws2.cell(row=i, column=3).alignment = Alignment(wrap_text=True, horizontal='left', vertical='center')
                    # Валидация данных



# Сохраняем файл
wb.save('your_excel_file.xlsx')


# fname = '1234.xlsx'
# wb2 = load_workbook(fname, keep_vba=True)
# name_list = wb2.sheetnames
# # print(name_list)
# ws2 = wb2.active
# lifting_norm_nkt = {}
# if fname:
#     normir_list = []
#     for row_ind, row in enumerate(ws2.iter_rows(max_col=18, min_row=310, max_row=338)):
#         lst = []
#         for col_index, col in enumerate(row):
#             if col_index == 8:
#                 normir_list.append(col.value)
# print(normir_list)
#         if row_ind == 0:
#             lifting = row[0]
#             lifting_1 = row[8]
#         if row_ind == 17:
#             lifting_norm_nkt.setdefault(lifting.value, {}).setdefault('19', row[3].value)
#             lifting_norm_nkt.setdefault(lifting.value, {}).setdefault('раздел', row[5].value)
#             lifting_norm_nkt.setdefault(lifting_1.value, {}).setdefault('19', row[11].value)
#             lifting_norm_nkt.setdefault(lifting_1.value, {}).setdefault('раздел', row[13].value)
#
#         elif row_ind == 18:
#             lifting_norm_nkt.setdefault(lifting.value, {}).setdefault('22', row[3].value)
#             lifting_norm_nkt.setdefault(lifting.value, {}).setdefault('раздел', row[5].value)
#             lifting_norm_nkt.setdefault(lifting_1.value, {}).setdefault('25', row[11].value)
#             lifting_norm_nkt.setdefault(lifting_1.value, {}).setdefault('раздел', row[13].value)
# print(lifting_norm_nkt)

# if fname:
#     normir_list = []
#     for row_ind, row in enumerate(ws2.iter_rows(max_col=18, min_row=235, max_row=235)):
#         lst = []
#
#         if row[0].value:
#             if 'спуск' in row[0].value:
#                 for i in ['АЗИНМАШ-37А (Оснастка 2×3)', 'АПРС-32 (Оснастка 2×3)', 'АПРС-40 (Оснастка 2×3)', 'АПРС-40 (Оснастка 3×4)', 'АПРС-50 (Оснастка 3×4)', 'АПР60/80 (Оснастка 3×4)', 'БАРС60/80 (Оснастка 3×4)', 'УПТ-32 (Оснастка 3×4)']:
#
#                     lifting_norm_nkt.setdefault(i, {}).\
#                         setdefault(row[1].value, {}).setdefault('6.5-7.5', row[3].value)
#                     lifting_norm_nkt.setdefault(i, {}). \
#                         setdefault(row[1].value, {}).setdefault('7.6-8.5', row[4].value)
#                     lifting_norm_nkt.setdefault(i, {}). \
#                         setdefault(row[1].value, {}).setdefault('8.6-9.5', row[5].value)
#                     lifting_norm_nkt.setdefault(i, {}). \
#                         setdefault(row[1].value, {}).setdefault('9.6-10.5', row[6].value)
#                     lifting_norm_nkt.setdefault(i, {}). \
#                         setdefault(row[1].value, {}).setdefault('10.6-11.5', row[7].value)
#                     # lifting_norm_nkt.setdefault(i, {}). \
#                     #     setdefault(row[1].value, {}).setdefault(row[2].value, {}).setdefault('11.6-12.5', (row[8].value, row[14].value))
#                     lifting_norm_nkt.setdefault(i, {}). \
#                         setdefault(row[1].value, {}).setdefault('раздел', row[15].value)
# print(lifting_norm_nkt)
# if fname:
#     normir_list = []
#     for row_ind, row in enumerate(ws2.iter_rows(max_col=18, min_row=3, max_row=148)):
#         lst = []
#
#         if row[0].value:
#             if 'спуск' in str(row[0].value) and 10 < row_ind < 51:
#                 lifting_norm_nkt.setdefault('АЗИНМАШ-37А (Оснастка 2×3)', {}). \
#                     setdefault(row[1].value, {}).setdefault('6.5-7.5', row[3].value)
#                 lifting_norm_nkt.setdefault('АЗИНМАШ-37А (Оснастка 2×3)', {}). \
#                     setdefault(row[1].value, {}).setdefault('7.6-8.5', row[3].value)
#                 lifting_norm_nkt.setdefault('АЗИНМАШ-37А (Оснастка 2×3)', {}). \
#                     setdefault(row[1].value, {}).setdefault('8.6-9.5', row[3].value)
#                 lifting_norm_nkt.setdefault('АЗИНМАШ-37А (Оснастка 2×3)', {}). \
#                     setdefault(row[1].value, {}).setdefault('9.6-10.5', row[3].value)
#                 lifting_norm_nkt.setdefault('АЗИНМАШ-37А (Оснастка 2×3)', {}). \
#                     setdefault(row[1].value, {}).setdefault('10.6-11.5', row[3].value)
#                 lifting_norm_nkt.setdefault('АЗИНМАШ-37А (Оснастка 2×3)', {}). \
#                     setdefault(row[1].value, {}).setdefault('11.6-12.5', row[3].value)
#                 lifting_norm_nkt.setdefault('АЗИНМАШ-37А (Оснастка 2×3)', {}). \
#                     setdefault(row[1].value, {}).setdefault('раздел', row[15].value)
#
#                 lifting_norm_nkt.setdefault('АПРС-32 (Оснастка 2×3)', {}). \
#                     setdefault(row[1].value, {}).setdefault('6.5-7.5', row[3].value)
#                 lifting_norm_nkt.setdefault('АПРС-32 (Оснастка 2×3)', {}). \
#                     setdefault(row[1].value, {}).setdefault('7.6-8.5', row[3].value)
#                 lifting_norm_nkt.setdefault('АПРС-32 (Оснастка 2×3)', {}). \
#                     setdefault(row[1].value, {}).setdefault('8.6-9.5', row[3].value)
#                 lifting_norm_nkt.setdefault('АПРС-32 (Оснастка 2×3)', {}). \
#                     setdefault(row[1].value, {}).setdefault('9.6-10.5', row[3].value)
#                 lifting_norm_nkt.setdefault('АПРС-32 (Оснастка 2×3)', {}). \
#                     setdefault(row[1].value, {}).setdefault('10.6-11.5', row[3].value)
#                 lifting_norm_nkt.setdefault('АПРС-32 (Оснастка 2×3)', {}). \
#                     setdefault(row[1].value, {}).setdefault('11.6-12.5', row[3].value)
#                 lifting_norm_nkt.setdefault('АПРС-32 (Оснастка 2×3)', {}). \
#                     setdefault(row[1].value, {}).setdefault('раздел', row[15].value)
#                 lifting_norm_nkt.setdefault('АПРС-40 (Оснастка 2×3)', {}). \
#                     setdefault(row[1].value, {}).setdefault('6.5-7.5', row[3].value)
#                 lifting_norm_nkt.setdefault('АПРС-40 (Оснастка 2×3)', {}). \
#                     setdefault(row[1].value, {}).setdefault('7.6-8.5', row[3].value)
#                 lifting_norm_nkt.setdefault('АПРС-40 (Оснастка 2×3)', {}). \
#                     setdefault(row[1].value, {}).setdefault('8.6-9.5', row[3].value)
#                 lifting_norm_nkt.setdefault('АПРС-40 (Оснастка 2×3)', {}). \
#                     setdefault(row[1].value, {}).setdefault('9.6-10.5', row[3].value)
#                 lifting_norm_nkt.setdefault('АПРС-40 (Оснастка 2×3)', {}). \
#                     setdefault(row[1].value, {}).setdefault('10.6-11.5', row[3].value)
#                 lifting_norm_nkt.setdefault('АПРС-40 (Оснастка 2×3)', {}). \
#                     setdefault(row[1].value, {}).setdefault('11.6-12.5', row[3].value)
#                 lifting_norm_nkt.setdefault('АПРС-40 (Оснастка 2×3)', {}). \
#                     setdefault(row[1].value, {}).setdefault('раздел', row[15].value)
#             elif 'спуск' in str(row[0].value) and 51 < row_ind < 69:
#                 lifting_norm_nkt.setdefault('АПРС-40 (Оснастка 3×4)', {}). \
#                     setdefault(row[1].value, {}).setdefault('6.5-7.5', row[3].value)
#                 lifting_norm_nkt.setdefault('АПРС-40 (Оснастка 3×4)', {}). \
#                     setdefault(row[1].value, {}).setdefault('7.6-8.5', row[3].value)
#                 lifting_norm_nkt.setdefault('АПРС-40 (Оснастка 3×4)', {}). \
#                     setdefault(row[1].value, {}).setdefault('8.6-9.5', row[3].value)
#                 lifting_norm_nkt.setdefault('АПРС-40 (Оснастка 3×4)', {}). \
#                     setdefault(row[1].value, {}).setdefault('9.6-10.5', row[3].value)
#                 lifting_norm_nkt.setdefault('АПРС-40 (Оснастка 3×4)', {}). \
#                     setdefault(row[1].value, {}).setdefault('10.6-11.5', row[3].value)
#                 lifting_norm_nkt.setdefault('АПРС-40 (Оснастка 3×4)', {}). \
#                     setdefault(row[1].value, {}).setdefault('11.6-12.5', row[3].value)
#                 lifting_norm_nkt.setdefault('АПРС-40 (Оснастка 3×4)', {}). \
#                     setdefault(row[1].value, {}).setdefault('раздел', row[15].value)
#             elif 'спуск' in str(row[0].value) and 69 < row_ind < 87:
#
#                 lifting_norm_nkt.setdefault('АПРС-50 (Оснастка 3×4)', {}). \
#                     setdefault(row[1].value, {}).setdefault('6.5-7.5', row[3].value)
#                 lifting_norm_nkt.setdefault('АПРС-50 (Оснастка 3×4)', {}). \
#                     setdefault(row[1].value, {}).setdefault('7.6-8.5', row[3].value)
#                 lifting_norm_nkt.setdefault('АПРС-50 (Оснастка 3×4)', {}). \
#                     setdefault(row[1].value, {}).setdefault('8.6-9.5', row[3].value)
#                 lifting_norm_nkt.setdefault('АПРС-50 (Оснастка 3×4)', {}). \
#                     setdefault(row[1].value, {}).setdefault('9.6-10.5', row[3].value)
#                 lifting_norm_nkt.setdefault('АПРС-50 (Оснастка 3×4)', {}). \
#                     setdefault(row[1].value, {}).setdefault('10.6-11.5', row[3].value)
#                 lifting_norm_nkt.setdefault('АПРС-50 (Оснастка 3×4)', {}). \
#                     setdefault(row[1].value, {}).setdefault('11.6-12.5', row[3].value)
#                 lifting_norm_nkt.setdefault('АПРС-50 (Оснастка 3×4)', {}). \
#                     setdefault(row[1].value, {}).setdefault('раздел', row[15].value)
#             elif 'спуск' in str(row[0].value) and 87 < row_ind < 105:
#
#                 lifting_norm_nkt.setdefault('АПР60/80 (Оснастка 3×4)', {}). \
#                     setdefault(row[1].value, {}).setdefault('6.5-7.5', row[3].value)
#                 lifting_norm_nkt.setdefault('АПР60/80 (Оснастка 3×4)', {}). \
#                     setdefault(row[1].value, {}).setdefault('7.6-8.5', row[3].value)
#                 lifting_norm_nkt.setdefault('АПР60/80 (Оснастка 3×4)', {}). \
#                     setdefault(row[1].value, {}).setdefault('8.6-9.5', row[3].value)
#                 lifting_norm_nkt.setdefault('АПР60/80 (Оснастка 3×4)', {}). \
#                     setdefault(row[1].value, {}).setdefault('9.6-10.5', row[3].value)
#                 lifting_norm_nkt.setdefault('АПР60/80 (Оснастка 3×4)', {}). \
#                     setdefault(row[1].value, {}).setdefault('10.6-11.5', row[3].value)
#                 lifting_norm_nkt.setdefault('АПР60/80 (Оснастка 3×4)', {}). \
#                     setdefault(row[1].value, {}).setdefault('11.6-12.5', row[3].value)
#                 lifting_norm_nkt.setdefault('АПР60/80 (Оснастка 3×4)', {}). \
#                     setdefault(row[1].value, {}).setdefault('раздел', row[15].value)
#
#                 lifting_norm_nkt.setdefault('БАРС60/80 (Оснастка 3×4)', {}). \
#                     setdefault(row[1].value, {}).setdefault('6.5-7.5', row[3].value)
#                 lifting_norm_nkt.setdefault('БАРС60/80 (Оснастка 3×4)', {}). \
#                     setdefault(row[1].value, {}).setdefault('7.6-8.5', row[3].value)
#                 lifting_norm_nkt.setdefault('БАРС60/80 (Оснастка 3×4)', {}). \
#                     setdefault(row[1].value, {}).setdefault('8.6-9.5', row[3].value)
#                 lifting_norm_nkt.setdefault('БАРС60/80 (Оснастка 3×4)', {}). \
#                     setdefault(row[1].value, {}).setdefault('9.6-10.5', row[3].value)
#                 lifting_norm_nkt.setdefault('БАРС60/80 (Оснастка 3×4)', {}). \
#                     setdefault(row[1].value, {}).setdefault('10.6-11.5', row[3].value)
#                 lifting_norm_nkt.setdefault('БАРС60/80 (Оснастка 3×4)', {}). \
#                     setdefault(row[1].value, {}).setdefault('11.6-12.5', row[3].value)
#                 lifting_norm_nkt.setdefault('БАРС60/80 (Оснастка 3×4)', {}). \
#                     setdefault(row[1].value, {}).setdefault('раздел', row[15].value)
#
#             elif 'спуск' in str(row[0].value) and 105 < row_ind < 126:
#
#                 lifting_norm_nkt.setdefault('УПА-60/80 (Оснастка 3×4)', {}). \
#                     setdefault(row[1].value, {}).setdefault('6.5-7.5', row[3].value)
#                 lifting_norm_nkt.setdefault('УПА-60/80 (Оснастка 3×4)', {}). \
#                     setdefault(row[1].value, {}).setdefault('7.6-8.5', row[3].value)
#                 lifting_norm_nkt.setdefault('УПА-60/80 (Оснастка 3×4)', {}). \
#                     setdefault(row[1].value, {}).setdefault('8.6-9.5', row[3].value)
#                 lifting_norm_nkt.setdefault('УПА-60/80 (Оснастка 3×4)', {}). \
#                     setdefault(row[1].value, {}).setdefault('9.6-10.5', row[3].value)
#                 lifting_norm_nkt.setdefault('УПА-60/80 (Оснастка 3×4)', {}). \
#                     setdefault(row[1].value, {}).setdefault('10.6-11.5', row[3].value)
#                 lifting_norm_nkt.setdefault('УПА-60/80 (Оснастка 3×4)', {}). \
#                     setdefault(row[1].value, {}).setdefault('11.6-12.5', row[3].value)
#                 lifting_norm_nkt.setdefault('УПА-60/80 (Оснастка 3×4)', {}). \
#                     setdefault(row[1].value, {}).setdefault('раздел', row[15].value)
#             elif 'спуск' in str(row[0].value) and 126 < row_ind < 147:
#
#                 lifting_norm_nkt.setdefault('УПТ-32 (Оснастка 3×4)', {}). \
#                     setdefault(row[1].value, {}).setdefault('6.5-7.5', row[3].value)
#                 lifting_norm_nkt.setdefault('УПТ-32 (Оснастка 3×4)', {}). \
#                     setdefault(row[1].value, {}).setdefault('7.6-8.5', row[3].value)
#                 lifting_norm_nkt.setdefault('УПТ-32 (Оснастка 3×4)', {}). \
#                     setdefault(row[1].value, {}).setdefault('8.6-9.5', row[3].value)
#                 lifting_norm_nkt.setdefault('УПТ-32 (Оснастка 3×4)', {}). \
#                     setdefault(row[1].value, {}).setdefault('9.6-10.5', row[3].value)
#                 lifting_norm_nkt.setdefault('УПТ-32 (Оснастка 3×4)', {}). \
#                     setdefault(row[1].value, {}).setdefault('10.6-11.5', row[3].value)
#                 lifting_norm_nkt.setdefault('УПТ-32 (Оснастка 3×4)', {}). \
#                     setdefault(row[1].value, {}).setdefault('11.6-12.5', row[3].value)
#                 lifting_norm_nkt.setdefault('УПТ-32 (Оснастка 3×4)', {}). \
#                     setdefault(row[1].value, {}).setdefault('раздел', row[15].value)
#
# print(lifting_norm_nkt)





# fname = '1234.xlsx'
# wb2 = load_workbook(fname, keep_vba=True)
# name_list = wb2.sheetnames
# # print(name_list)
# ws2 = wb2.active
# lifting_norm_nkt = {}
# if fname:
#     normir_list = []
#     for row_ind, row in enumerate(ws2.iter_rows(max_col=18, min_row=209, max_row=228)):
#         lst = []
#         if row[0].value:
#             if 'спуск' not in row[0].value and 'ПА' not in row[0].value \
#                     and 'ЭЦН' not in row[0].value and 'Штанги' not in row[0].value and 'СБТ' not in row[0].value:
#
#                 lifting_norm_nkt.setdefault(row[0].value, {}).\
#                     setdefault(row[1].value, {}).setdefault(row[2].value, (row[3].value, row[4].value))
#
#                 lifting_norm_nkt.setdefault(row[0].value, {}). \
#                     setdefault(row[1].value, {}).setdefault('раздел', row[5].value)
#
#                 lifting_norm_nkt.setdefault(row[8].value, {}).\
#                     setdefault(row[9].value, {}).setdefault(row[10].value, (row[11].value, row[12].value))
#
#                 lifting_norm_nkt.setdefault(row[8].value, {}). \
#                     setdefault(row[9].value, {}).setdefault('раздел', row[13].value)
#


    #
    # {'АЗИНМАШ-37А (Оснастка 2×3)': {19: {'III': (0.0116, 423), 'раздел': 'п.1.1 раздел 2'},
    #                                 22: {'III': (0.0133, 317), 'раздел': 'п.1.1 раздел 2'},
    #                                 25: {'III': (0.0133, 242), 'раздел': 'п.1.1 раздел 2'}},
    #  'АПРС-40 (Оснастка 3×4)': {19: {'III': (0.015, 429), 'раздел': 'п.1.1 раздел 2'},
    #                             22: {'III': (0.0166, 347), 'раздел': 'п.1.1 раздел 2'},
    #                             25: {'III': (0.0166, 307), 'раздел': 'п.1.1 раздел 2'}},
    #  'АПРС-50 (Оснастка 3×4)': {19: {'III': (0.0116, 438), 'раздел': 'п.1.1 раздел 2'},
    #                             22: {'III': (0.0133, 426), 'раздел': 'п.1.1 раздел 2'},
    #                             25: {'III': (0.0133, 326), 'раздел': 'п.1.1 раздел 2'}}}

    #
#
    # print(lifting_norm_nkt)





#
#
# fname = '23 Гордеевское КР4-3 (Ойл-С, бр.139) 01.06.2023.xlsm'
# wb2 = Workbook()
# ws2 = wb2.get_sheet_by_name('Sheet')
# if fname:
#     wb_summary = load_workbook(fname, keep_vba=True)
#
#     name_list = wb_summary.sheetnames
#     for name in name_list:
#         ws_summar = wb_summary[name]
#         title_list = ws_summar.title
#
#         normir_list = []
#         for row_ind, row in enumerate(ws_summar.iter_rows(max_col=55)):
#             list = []
#
#             for col, value in enumerate(row):
#                 list.append(value.value)
#             normir_list.append(list)
#
#         wb2.create_sheet(title_list)
#
#         print(title_list)
#
#         for i in range(len(normir_list)):
#             print(i)
#             for j in range(len(normir_list[i])):
#                 cell = ws2.cell(row=i+1, column=j+1)
#                 cell.value = normir_list[i][j]
#
# wb2.save('1234.xlsx')
