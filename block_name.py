from datetime import datetime

import well_data
from cdng import region_dict
import json


def region(cdng):
    region_work = ''.join([key for key, value in region_dict.items() if cdng in value])
    return region_work


# выбор подписантов в зависимости от вида ГТМ
def curator_sel(curator, region):
    with open(f'{well_data.path_image}podpisant.json', 'r', encoding='utf-8') as file:
        podpis_dict = json.load(file)
    if curator == 'ОР':
        return (podpis_dict["регион"][region]['ruk_orm']['post'], podpis_dict["регион"][region]["ruk_orm"]['surname'])
    elif curator == 'ГТМ':
        return (podpis_dict["регион"][region]["ruk_gtm"]['post'], podpis_dict["регион"][region]["ruk_gtm"]['surname'])
    elif curator == 'ГО':
        return (podpis_dict["регион"][region]['go']['post'], podpis_dict["регион"][region]["go"]['surname'])
    elif curator == 'ВНС':
        return (podpis_dict["регион"][region]['go']['post'], podpis_dict["регион"][region]["go"]['surname'])
    elif curator == 'ГРР':
        return (podpis_dict["регион"][region]['grr']['post'], podpis_dict["регион"][region]["grr"]['surname'])


current_datetime = datetime.today()


# Выбор подписантов в зависимости от региона
def pop_down(self, region, curator_sel):

    with open(f'{well_data.path_image}podpisant.json', 'r', encoding='utf-8') as file:
        podpis_dict = json.load(file)
    nach_list = ''
    if 'Ойл' in well_data.contractor:
        nach_tkrs = ''
        nach_tkrs_post = ''
        if region == 'ЧГМ' or region == 'ТГМ' or 'gnkt' in well_data.work_plan:
            nach_tkrs = podpis_dict["ООО Ойл-сервис"]["head_of_workshop_1"]["surname"]
            nach_tkrs_post = podpis_dict["ООО Ойл-сервис"]["head_of_workshop_1"]["post"]
        elif region == 'КГМ' or region == 'АГМ':
            nach_tkrs = podpis_dict["ООО Ойл-сервис"]["head_of_workshop_2"]["surname"]
            nach_tkrs_post = podpis_dict["ООО Ойл-сервис"]["head_of_workshop_2"]["post"]
        elif region == 'ИГМ':
            nach_tkrs = podpis_dict["ООО Ойл-сервис"]["head_of_workshop_4"]["surname"]
            nach_tkrs_post = podpis_dict["ООО Ойл-сервис"]["head_of_workshop_4"]["post"]

        nach_list = [
            [None, f'План работ составил {well_data.user[0]}', None, None, None, None, '___________________', None,
             None,
             f'{well_data.user[1]}', None, None],
            [None, None, None, None, None, None, None, None, 'дата составления', None,
             datetime.now().strftime('%d.%m.%Y'),
             None],
            [None, None, f'{nach_tkrs_post}', None, None, None, None, None, None,
             nach_tkrs, None, None],
            [None, None, None, None, None, None, None, None, None, '     дата подписания', None, None]]
    elif "РН" in well_data.contractor:
        nach_list = [
            [None, f'План работ составил {well_data.user[0]}', None, None, None, None, '___________________', None,
             None,
             f'{well_data.user[1]}', None, None],
            [None, None, None, None, None, None, None, None, 'дата составления', None,
             datetime.now().strftime('%d.%m.%Y'),
             None]]

    with open(f'{well_data.path_image}podpisant.json', 'r', encoding='utf-8') as file:
        podpis_dict = json.load(file)

    podp_down = [
        [None, ' ', 'Согласовано:', None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, '', None, None, '', None, None],
        [None, curator_sel[0], None, None, None, None, '___________________', None, None,
         curator_sel[1], None, None],
        [None, None, None, None, None, None, '"___"___________', None, None, '     дата подписания', None,
         None],
        [None, podpis_dict["регион"][region]['ruk_pto']['post'], None, None, None, None, '___________________', None,
         None,
         podpis_dict["регион"][region]["ruk_pto"]['surname'], None, ' '],
        [None, None, None, None, None, None, '"___"___________', None, None, '     дата подписания', None,
         None],
        [None, podpis_dict["регион"][region]['usrs']['post'], None, None, None, None,
         '___________________', None, None, podpis_dict["регион"][region]['usrs']['surname'], None, None],
        [None, None, None, None, None, None, '"___"___________', None, None, '     дата подписания', None,
         None],
        [None, None, None, None, None, None, None, None, None, None, None, None],

        [None, 'Замечания:', None, None, None, None, None, None, None, None, None, None],
        [None, '1.', '________________________________________________________________________________________________',
         None, None, None, None,
         None,
         None,
         None, None, None],
        [None, '2.', '________________________________________________________________________________________________',
         None, None, None, None,
         None,
         None,
         None, None, None],
        [None, '3.', '________________________________________________________________________________________________',
         None, None, None, None,
         None,
         None,
         None, None, None],
        [None, '4.', '________________________________________________________________________________________________',
         None, None, None, None,
         None,
         None,
         None, None, None],
        [None, '5.', '________________________________________________________________________________________________',
         None, None, None, None,
         None,
         None,
         None, None, None],
        [None, None, None, 'Проинструктированы, с планом работ ознакомлены:                         ', None,
         None, None, None, None, None, None, None],
        [None, None, 'Мастер бригады', None, None, None, f'Инструктаж провел мастер бригады {well_data.contractor}',
         None, None, None, None, None],
        [None, None, 'Мастер бригады', None, None, None, None, None, None, None, 'подпись', None],
        [None, f'Бурильщик {well_data.contractor}', None, None,
         f'_____________________Бурильщик {well_data.contractor}________________________', None, None, None, None,
         None, None, None],
        [None, f'Пом.бур-ка {well_data.contractor}', None, None,
         f'_____________________Пом.бур-ка {well_data.contractor}_______________________', None, None, None, None,
         None, None, None],
        [None, f'Пом.бур-ка {well_data.contractor}', None, None,
         f'_____________________Пом.бур-ка {well_data.contractor}_______________________', None, None, None, None,
         None, None, None],
        [None, None, 'Машинист', None,
         '_____________________ Машинист ________________________', None, None, None,
         None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None, None, None]]

    for row in nach_list[::-1]:
        podp_down.insert(0, row)

    ved_gtm_list = [None, podpis_dict["регион"][region]['ved_gtm']['post'], None, None, None, None, '_______________',
                    None, None,
                    podpis_dict["регион"][region]['ved_gtm']['surname'], None, None]

    ved_orm_list = [None, podpis_dict["регион"][region]['ved_orm']['post'], None, None, None, None, '_______________',
                    None, None,
                    podpis_dict["регион"][region]['ved_orm']['surname'], None, None]
    if (region == 'ЧГМ') and well_data.curator == 'ОР':
        podp_down.insert(13, ved_orm_list)
        podp_down.insert(14,
                         [None, None, None, None, None, None, '"___"___________', None, None, '     дата подписания',
                          None,
                          None])
    elif (region == 'КГМ') and well_data.curator == 'ОР' and well_data.work_plan == 'gnkt_opz':

        podp_down.insert(12, ved_orm_list)
        podp_down.insert(13,
                         [None, None, None, None, None, None, '"___"___________', None, None, '     дата подписания',
                          None,
                          None])
    elif (region == 'КГМ') and well_data.curator == 'ОР':

        podp_down.insert(12, ved_gtm_list)
        podp_down.insert(13,
                         [None, None, None, None, None, None, '"___"___________', None, None, '     дата подписания',
                          None,
                          None])
    elif region == 'КГМ' or region == 'ЧГМ' and well_data.curator == 'ГТМ':
        podp_down.insert(12, ved_gtm_list)
        podp_down.insert(13,
                         [None, None, None, None, None, None, '"___"___________', None, None, '     дата подписания',
                          None,
                          None])
    elif region == 'КГМ' or region == 'ЧГМ' and well_data.curator == 'ГТМ':
        podp_down.insert(12, ved_gtm_list)
        podp_down.insert(13,
                         [None, None, None, None, None, None, '"___"___________', None, None, '     дата подписания',
                          None,
                          None])
    if well_data.curator == "ВНС":
        podp_down.insert(6, [None, 'Менеджер ТКРС БНД', None, None, None, None, '___________________', None, None,
                             'А.М. Кузьмин', None, ' '])
        podp_down.insert(7,
                         [None, None, None, None, None, None, '"___"___________', None, None, '     дата подписания',
                          None,
                          None])

    return podp_down


def razdel_1(self, region, contractor):
    with open(f'{well_data.path_image}podpisant.json', 'r', encoding='utf-8') as file:
        podpis_dict = json.load(file)
    razdel_1 = ''
    if 'Ойл' in contractor:

        razdel_1 = [
            [None, 'СОГЛАСОВАНО:', None, None, None, None, None, 'УТВЕРЖДАЕМ:', None, None, None, None],
            [None, podpis_dict["регион"][region]['gi']['post'], None, None, None, None, None,
             f'{podpis_dict["ООО Ойл-сервис"]["сhief_engineer"]["post"]}', None, None, None, None],
            [None, f'____________{podpis_dict["регион"][region]["gi"]["surname"]}', None, None, None, None, None,
             f'_____________{podpis_dict["ООО Ойл-сервис"]["сhief_engineer"]["surname"]}', None, None, None, None],
            [None, f'"____"_____________________{current_datetime.year}г.', None, None, None, None, None,
             f'"____"_____________________{current_datetime.year}г.', None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None],
            [None, podpis_dict["регион"][region]['gg']['post'], None, None, None,
             None,
             None, f'{podpis_dict["ООО Ойл-сервис"]["chief_geologist"]["post"]}', None, None, None, None],
            [None, f'_____________{podpis_dict["регион"][region]["gg"]["surname"]}', None, None, None, None, None,
             f'_____________{podpis_dict["ООО Ойл-сервис"]["chief_geologist"]["surname"]}', None, None, '',
             None],
            [None, f'"____"_____________________{current_datetime.year}г.', None, None, '', None, None,
             f'"____"_____________________{current_datetime.year}г.', None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None]]
    elif 'РН' in contractor:
        razdel_1 = [
            [None, 'СОГЛАСОВАНО:', None, None, None, None, None, 'УТВЕРЖДАЕМ:', None, None, None, None],
            [None, podpis_dict["регион"][region]['gi']['post'], None, None, None, None, None,
             f'Главный Инженер {well_data.contractor} филиал г. Уфа ', None, None, None, None],
            [None, f'____________{podpis_dict["регион"][region]["gi"]["surname"]}', None, None, None, None, None,
             '_____________К.Н. Фазлиахметов ', None, None, None, None],
            [None, f'"____"_____________________{current_datetime.year}г.', None, None, None, None, None,
             f'"____"_____________________{current_datetime.year}г.', None, None, None, None],
            [None, None, None, None, None, None,
             None, None, None,
             None, None, None],
            [None, podpis_dict["регион"][region]['gg']['post'], None, None, None,
             None,
             None, 'Доверенность №27 от 01.09.2023г.', 'Доверенность №27 от 01.09.2023г.', None, None, None],

            [None, f'_____________{podpis_dict["регион"][region]["gg"]["surname"]}', None, None, None, None, None,
             '', None, None, '',
             None],
            [None, f'"____"_____________________{current_datetime.year}г.', None, None, '', None, None,
             f'', None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None]]

    podp_grp = [[None, 'Представитель подрядчика по ГРП', None, None, None, None, None, None, None, None, None,
                 None],
                [None, '_____________', None, None, None, None, None, None, None, None, None, None],
                [None, f'"____"_____________________{current_datetime.year}г.', None, None, None, None, None, None,
                 None, None, None,
                 None]]
    podp_bvo = [
        [None, 'Районный инженер Башкирского ', None, None, None, None, None, None, None, None, None, None],
        [None, 'военизированного отряда ', None, None, None, None, None, None, None, None, None, None],
        [None, '_____________', None, None, None, None, None, None, None, None, None, None],
        [None, f'"____"_____________________{current_datetime.year}г.', None, None, None, None, None, None,
         None, None, None,
         None]]
    if well_data.data_in_base is False:

        if len(well_data.plast_work) != 0:
            # print(well_data.plast_work, well_data.dict_category)
            try:
                cat_P_1 = well_data.dict_category[well_data.plast_work[0]]['по давлению'].category
                cat_h2s_list = well_data.dict_category[well_data.plast_work[0]]['по сероводороду'].category
                cat_gaz = well_data.dict_category[well_data.plast_work[0]]['по газовому фактору'].category
            except:
                cat_P_1 = well_data.cat_P_1[0]
                cat_h2s_list = well_data.cat_h2s_list[0]
                cat_gaz = well_data.cat_gaz_f_pr[0]
        else:

            cat_P_1 = well_data.cat_P_1[0]
            cat_h2s_list = well_data.cat_h2s_list[0]
            cat_gaz = well_data.cat_gaz_f_pr[0]
        try:
            cat_P_1_plan = well_data.dict_category[well_data.plast_project[0]]['по давлению'].category
            cat_h2s_list_plan = well_data.dict_category[well_data.plast_project[0]]['по сероводороду'].category
            cat_gaz_plan = well_data.dict_category[well_data.plast_project[0]]['по газовому фактору'].category
        except:
            cat_P_1_plan = 3
            cat_h2s_list_plan = 3
            cat_gaz_plan = 3

        if 1 in [cat_P_1, cat_P_1_plan, cat_h2s_list, cat_gaz, cat_h2s_list_plan, cat_gaz_plan,
                 well_data.category_pressuar] or '1' in [cat_P_1, cat_P_1_plan, cat_h2s_list, cat_gaz,
                                                         cat_h2s_list_plan, cat_gaz_plan,
                                                         well_data.category_pressuar] or \
                well_data.curator == 'ВНС':
            for row in range(len(podp_bvo)):
                for col in range(len(podp_bvo[row])):
                    razdel_1[row + 9][col] = podp_bvo[row][col]
        if 1 in [cat_P_1, cat_h2s_list, cat_gaz] or \
                well_data.curator == 'ВНС':
            well_data.kat_pvo = 1
            well_data.bvo = True

        if well_data.grp_plan is True:
            for row in range(len(podp_grp)):
                for col in range(len(podp_grp[row])):
                    razdel_1[row + 12][col] = podp_grp[row][col]

    return razdel_1
