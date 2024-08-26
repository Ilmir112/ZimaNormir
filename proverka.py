from PyQt5 import QtWidgets
from openpyxl.reader.excel import load_workbook
from openpyxl.workbook import Workbook

# fname = 'property_excel/template_normir_new.xlsm'
# wb2 = load_workbook(fname, keep_vba=True)
# name_list = wb2.sheetnames
# # print(name_list)
# ws2 = wb2['АВР']
# if fname:
#     normir_list = []
#     for row_ind, row in enumerate(ws2.iter_rows(max_col=31, min_row=133, max_row=210)):
#         list = []
#         for col, value in enumerate(row):
#             list.append(value.value)
#         normir_list.append(list)
#
#     print(normir_list)
#
# fname = '1234.xlsx'
# wb2 = load_workbook(fname, keep_vba=True)
# name_list = wb2.sheetnames
# # print(name_list)
# ws2 = wb2.active
# lifting_norm_nkt = {}
# if fname:
#     normir_list = []
#     for row_ind, row in enumerate(ws2.iter_rows(max_col=18, min_row=3, max_row=148)):
#         lst = []
#
#         if row[0].value:
#             if 'спуск' not in row[0].value and 'ПА' not in row[0].value \
#                     and 'ЭЦН' not in row[0].value and 'Штанги' not in row[0].value and 'СБТ' not in row[0].value:
#
#                 lifting_norm_nkt.setdefault(row[0].value, {}).\
#                     setdefault(row[1].value, {}).setdefault(row[2].value, {}).setdefault('6.5-7.5', (row[3].value, row[9].value))
#                 lifting_norm_nkt.setdefault(row[0].value, {}). \
#                     setdefault(row[1].value, {}).setdefault(row[2].value, {}).setdefault('7.6-8.5', (row[4].value, row[10].value))
#                 lifting_norm_nkt.setdefault(row[0].value, {}). \
#                     setdefault(row[1].value, {}).setdefault(row[2].value, {}).setdefault('8.6-9.5', (row[5].value, row[11].value))
#                 lifting_norm_nkt.setdefault(row[0].value, {}). \
#                     setdefault(row[1].value, {}).setdefault(row[2].value, {}).setdefault('9.6-10.5', (row[6].value, row[12].value))
#                 lifting_norm_nkt.setdefault(row[0].value, {}). \
#                     setdefault(row[1].value, {}).setdefault(row[2].value, {}).setdefault('10.6-11.5', (row[7].value, row[13].value))
#                 lifting_norm_nkt.setdefault(row[0].value, {}). \
#                     setdefault(row[1].value, {}).setdefault(row[2].value, {}).setdefault('11.6-12.5', (row[8].value, row[14].value))
#                 lifting_norm_nkt.setdefault(row[0].value, {}). \
#                     setdefault(row[1].value, {}).setdefault(row[2].value, {}).setdefault('раздел', row[15].value)fname = '1234.xlsx'
fname = '1234.xlsx'
wb2 = load_workbook(fname, keep_vba=True)
name_list = wb2.sheetnames
# print(name_list)
ws2 = wb2.active
lifting_norm_nkt = {}
if fname:
    normir_list = []
    for row_ind, row in enumerate(ws2.iter_rows(max_col=18, min_row=209, max_row=228)):
        lst = []
        if row[0].value:
            if 'спуск' not in row[0].value and 'ПА' not in row[0].value \
                    and 'ЭЦН' not in row[0].value and 'Штанги' not in row[0].value and 'СБТ' not in row[0].value:

                lifting_norm_nkt.setdefault(row[0].value, {}).\
                    setdefault(row[1].value, {}).setdefault(row[2].value, (row[3].value, row[4].value))

                lifting_norm_nkt.setdefault(row[0].value, {}). \
                    setdefault(row[1].value, {}).setdefault('раздел', row[5].value)

                lifting_norm_nkt.setdefault(row[8].value, {}).\
                    setdefault(row[9].value, {}).setdefault(row[10].value, (row[11].value, row[12].value))

                lifting_norm_nkt.setdefault(row[8].value, {}). \
                    setdefault(row[9].value, {}).setdefault('раздел', row[13].value)



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
    print(lifting_norm_nkt)





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
