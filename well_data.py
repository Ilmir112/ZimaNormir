import keyring
import socket
from datetime import datetime
from openpyxl.styles import Border, Side, PatternFill


class ProtectedIsDigit:
    def __init__(self, default_value=None, name=None):
        self._value = default_value
        self._name = name

    def __get__(self, instance, owner):
        if not instance:
            # print(f'значение {self._name} ра3вно {self._value}')
            return self
        return instance.__dict__[self._name]

    def __set__(self, instance, value):
        if 'уст' in str(value).lower():
            self._value = 0
        elif isinstance(value, str):
            try:
                float_value = float(value.replace(",", "").replace(".", ""))  # Пробуем преобразовать строку в число
                self._value = float_value
            except ValueError:
                self._value = None  # Если не удалось преобразовать в число, сохраняем None
        elif isinstance(value, (int, float)):
            self._value = float(value)  # Преобразуем целое число в число с плавающей точкой
        else:
            print(f'Ошибка: Недопустимое значение {value}')


class ProtectedIsNonNone:
    def __init__(self, default_value=None, name=None):
        self._value = default_value
        self._name = name

    def __get__(self, instance, owner):
        if not instance:
            return self
        return instance.__dict__[self._name]

    def __set__(self, instance, value):
        if value is not None and not str(value).replace(",", "").replace(".", "").isdigit():
            instance.__dict__[self._name] = value

        else:
            print(f'Ошибка: {value} - не корректное строковое значение')
            raise ValueError("Значение должно быть строкой")

#
# def save_password(service_name, username, password):
#     keyring.set_password(service_name, username, password)

def get_password(service_name, username):
    return keyring.get_password(service_name, username)


# password = get_password("zima_app", "postgres")
password = '195375AsD+'
type_working = 'КРС'
lifting_unit_combo = 'АПРС-40 (Оснастка 3×4)'
connect_in_base = True
type_kr = ''
column_head_m = ''
work_list_in_ois = ''
date_work = '20.07.2024'
date_drilling_cancel = ''
сommissioning_date = ''
date_drilling_run = ''
appointment = ''
number_bush = ProtectedIsDigit(0)
wellhead_fittings = ''
inv_number = ProtectedIsNonNone('не корректно')
cdng = ProtectedIsNonNone('не корректно')
gnkt_number = 0
gnkt_length = 0
diametr_length = 0
emergency_bottom = ''
iznos = 0
bottomType_list = ['ЦМ', 'РПК', 'РПП', 'ВП', 'Гипсовых отложений', 'проходимости']
type_absorbent = ''
pipe_mileage = 0
pipe_fatigue = 0
pvo = 0
previous_well = 0
bottomhole_drill = ProtectedIsNonNone('не корректно')
bottomhole_artificial = ProtectedIsNonNone('не корректно')
max_angle = ProtectedIsNonNone('не корректно')
max_angle_H = ProtectedIsNonNone('не корректно')
stol_rotora = ProtectedIsNonNone('не корректно')
column_conductor_diametr = ProtectedIsNonNone('не корректно')
column_conductor_wall_thickness = ProtectedIsNonNone('не корректно')
column_conductor_lenght = ProtectedIsNonNone('не корректно')
level_cement_direction = ProtectedIsNonNone('не корректно')
level_cement_conductor = ProtectedIsNonNone('не корректно')
column_diametr = ProtectedIsNonNone('не корректно')
column_wall_thickness = ProtectedIsNonNone('не корректно')
shoe_column = ProtectedIsNonNone('не корректно')
level_cement_column = ProtectedIsNonNone('не корректно')
index_row_pvr_list = []
gis_list = []
pvr_row = []
current_date = datetime.now().date()
pressuar_mkp = ProtectedIsNonNone('не корректно')
column_additional_diametr = ProtectedIsNonNone('не корректно')
column_additional_wall_thickness = ProtectedIsNonNone('не корректно')
head_column_additional = ProtectedIsNonNone('не корректно')
shoe_column_additional = ProtectedIsNonNone('не корректно')
column_direction_lenght = ProtectedIsDigit('не корректно')

column_direction_diametr = ProtectedIsNonNone('не корректно')
column_direction_wall_thickness = ProtectedIsNonNone('не корректно')
data_list = []
problemWithEk_diametr = 220
data_fond_min = ProtectedIsDigit(0)
cat_well_min = ProtectedIsDigit(0)
cat_well_max = ProtectedIsDigit(0)
data_well_max = ProtectedIsDigit(0)
first_pressure = ProtectedIsDigit(0)
data_pvr_max = ProtectedIsDigit(0)
q_water = ProtectedIsDigit(0)
proc_water = ProtectedIsDigit(100)
data_well_min = ProtectedIsDigit(0)
data_pvr_min = ProtectedIsDigit(0)
pipes_ind = ProtectedIsDigit(0)
condition_of_wells = ProtectedIsDigit(0)
static_level = ProtectedIsNonNone('не корректно')
dinamic_level = ProtectedIsNonNone('не корректно')
sucker_rod_ind = ProtectedIsDigit(0)
data_x_max = ProtectedIsDigit(0)
data_x_min = ProtectedIsDigit(0)

problemWithEk = False
plast_all = []
konte_true = False
gipsInWell = False
grp_plan = False
nkt_opressTrue = False
open_trunk_well = False
lift_ecn_can = False
sucker_rod_none = True
pause = True
curator = '0'
lift_ecn_can_addition = False
column_passability = False
column_additional_passability = False
column_direction_True = False
work_perforations_approved = False
leakiness = False
emergency_well = False
column_additional = False
without_damping = False
well_number = ProtectedIsNonNone('0')
angle_data = []
well_area = ProtectedIsNonNone(' ')
bvo = False
old_version = True
skm_depth = 0

pakerTwoSKO = False
normOfTime = 0
Qoil = 0
template_depth = 0
nkt_diam = 73
b_plan = 0
# host_krs = '31.129.99.186'
host_krs = '176.109.106.199'
expected_Q = 0
expected_P = 0
plast_select = ''
dict_perforation = {}
dict_perforation_project = {}
itog_ind_min = 0
work_plan = None
kat_pvo = 2
gaz_f_pr = []
paker_diametr = 0
cat_gaz_f_pr = []
paker_layout = 0

max_expected_pressure = 0
leakiness_Count = 0

expected_pick_up = {}
fluid_work = 0

ins_ind = 0
number_dp = 0
len_razdel_1 = 0
current_bottom = 0
count_template = 0
forPaker_list = False
current_bottom2 = 5000
dict_leakiness = {}
dict_perforation_short = {}

emergency_count = 0
skm_interval = []
template_lenght = 0
category_pressuar = 3
category_h2s = 3
category_gf = 3
work_perforations = []
work_perforations_dict = {}
paker_do = {"do": 0, "posle": 0}
values = []
depth_fond_paker_do = {"do": 0, "posle": 0}
paker2_do = {"do": 0, "posle": 0}
depth_fond_paker2_do = {"do": 0, "posle": 0}
perforation_roof = 50000
perforation_sole = 0
dict_pump_SHGN = {"do": '0', "posle": '0'}
dict_pump_ECN = {"do": '0', "posle": '0'}
dict_pump_SHGN_h = {"do": '0', "posle": '0'}
dict_pump_ECN_h = {"do": '0', "posle": '0'}
dict_pump = {"do": '0', "posle": '0'}
leakiness_interval = []
dict_pump_h = {"do": 0, "posle": 0}

cat_P_1 = []
costumer = 'ОАО "Башнефть"'
contractor = ''
dict_contractor = {
    'ООО "Ойл-сервис"':
    {
        'Дата ПВО': 'от 15.10.2021'
    },
    'ООО "Ойл-cервис"':
    {
        'Дата ПВО': 'от 15.10.2021'
    },
    'ООО "РН-Сервис"':
    {
        'Дата ПВО': '29.10.2021'
    }
}
countAcid = 0
swabTypeComboIndex = 1
swab_true_edit_type = 1
groove_diameter = ''
bur_rastvor = ''
drilling_interval = []
max_angle = 0
dop_work_list = None
paker_izv_paker = ''
privyazkaSKO = 0
nkt_mistake = False
h2s_pr = []
plan_correct_index = 0
cat_h2s_list = []
user = ['', '']
itog_ind_max = ''
texts = ''
h2s_mg = []
h2s_mg_m3 = []
lift_key = 0
check_data_in_pz = []
dict_category = {}
max_admissible_pressure = 0
region = ''
data_in_base = False
dict_nkt = {}
dict_nkt_po = {}
# path_image = '_internal/'
path_image = ''
count_SBT = 0
data_well_dict = {}
ins_ind2 = 0
data = ''
rowHeights = ''
colWidth = ''
boundaries_dict = ''
Qwater = 100
dict_sucker_rod = {}
dict_sucker_rod_po = {}
row_expected = []
category_pressuar2 = ''
rowHeights = []
plast_project = []
plast_work = []
image_data = []
leakage_window = None
cat_P_P = []
data_well_is_True = False
well_oilfield = 0
template_depth_addition = 0
template_lenght_addition = 0
nkt_template = 59
yellow_fill = PatternFill(start_color="FFFF00", end_color="FFFF00", fill_type="solid")
well_volume_in_PZ = []
image_list = []
problemWithEk_depth = 10000
thin_border = Border(left=Side(style='thin'),
                     right=Side(style='thin'),
                     top=Side(style='thin'),
                     bottom=Side(style='thin'))
postgres_params_classif = {
            f'database': 'databaseclassification',
            f'user': 'postgres',
            f'password': f'{password}',
            f'host': f'{host_krs}',
            f'port': '5432'
        }
postgres_params_data_well = {
            f'database': 'well_data',
            f'user': 'postgres',
            f'password': f'{password}',
            f'host': f'{host_krs}',
            f'port': '5432'
        }

postgres_conn_gnkt = {
    'database': 'gnkt_database',
    'user': 'postgres',
    'password': f'{password}',
    f'host': f'{host_krs}',
    'port': '5432'
        }
postgres_conn_work_well = {
    'database': 'databasewellwork',
    'user': 'postgres',
    'password': f'{password}',
    f'host': f'{host_krs}',
    'port': '5432'
}
postgres_conn_user = {
    'database': 'krs2',
    'user': 'postgres',
    'password': f'{password}',
    f'host': f'{host_krs}',
    'port': '5432'
}

dict_telephon = {'Бригада № 1': 9228432791,
                 'Бригада № 2': 9174006602,
                 'Бригада № 3': 9174009883,
                 'Бригада № 4': 9228035896,
                 'Бригада № 5': 9228432597,
                 'Бригада № 7 ': 9228451907,
                 'Бригада № 8': 9228452018,
                 'Бригада № 9': 9228449698,
                 'Бригада № 10': 9228432980,
                 'Бригада № 12': 9228180254,
                 'Бригада № 14': 9228034462,
                 'Бригада № 15': 9228382609,
                 'Бригада № 16': 9325425972,
                 'Бригада № 17': 9228035385,
                 'Бригада № 18': 9228449048,
                 'Бригада № 19': 9328486359,
                 'Бригада № 20': 9228556638,
                 'Бригада № 21': 9374978836,
                 'Бригада № 22': 9270869338,
                 'Бригада № 23': 9373146981,
                 'Бригада № 24': 9373146135,
                 'Бригада № 25': 9373521496,
                 'Бригада № 28': 9373519867,
                 'Бригада № 29': 9373519358,
                 'Бригада № 30': 9373518753,
                 'Бригада № 31': 9374861861,
                 'Бригада № 33': 9273029571,
                 'Бригада № 34': 9378367419,
                 'Бригада № 36 ': 9374993472,
                 'Бригада № 37': 9273211829,
                 'Бригада № 38': 9273211926,
                 'Бригада № 43': 9273254843,
                 'Бригада № 44': 9273254834,
                 'Бригада № 45': 9273254830,
                 'Бригада № 46': 9373362319,
                 'Бригада № 47': 9373519738,
                 'Бригада № 48': 9378367421,
                 'Бригада № 49': 9378309337,
                 'Бригада № 54': 9270869358,
                 'Бригада № 55': 9279368415,
                 'Бригада № 56': 9279368421,
                 'Бригада № 58': 9270864957,
                 'Бригада № 59': 9174002382,
                 'Бригада № 60 ': 9273460812,
                 'Бригада № 61': 9273029274,
                 'Бригада № 64': 9378452378,
                 'Бригада № 65': 9273029526,
                 'Бригада № 66': 9279368446,
                 'Бригада № 68': 9279368423,
                 'Бригада № 70': 9373084741,
                 'Бригада № 71': 9373085348,
                 'Бригада № 72': 9373085351,
                 'Бригада № 73': 9373310474,
                 'Бригада № 74': 9373639774,
                 'Бригада № 75': 9174009934,
                 'Бригада № 77': 9373639370,
                 'Бригада № 78': 9174001660,
                 'Бригада № 79': 9174003079,
                 'Бригада № 80': 9174002580,
                 'Бригада № 81': 9174003114,
                 'Бригада № 82': 9174002682,
                 'Бригада № 83': 9174001783,
                 'Бригада № 84': 9174002844,
                 'Бригада № 85': 9174001915,
                 'Бригада № 86': 9174002824,
                 'Бригада № 87': 9174002873,
                 'Бригада № 88': 9174002564,
                 'Бригада № 90': 9174002494,
                 'Бригада № 91': 9174002791,
                 'Бригада № 92': 9174008192,
                 'Бригада № 93': 9174002893,
                 'Бригада № 94': 9174002382,
                 'Бригада № 95': 9174009557,
                 'Бригада № 97': 9174008597,
                 'Бригада № 98': 9226245380,
                 'Бригада № 99': 9228739012,
                 'Бригада № 100': 9228390349,
                 'Бригада № 101': 9226245342,
                 'Бригада № 102': 9228180653,
                 'Бригада № 103': 9325425834,
                 'Бригада № 104': 9325559708,
                 'Бригада № 105': 9325300276,
                 'Бригада № 106': 9228378241,
                 'Бригада № 107': 9228377310,
                 'Бригада № 108': 9328425178,
                 'Бригада № 109': 9228378610,
                 'Бригада № 110': 9328489427,
                 'Бригада № 111': 9174002633,
                 'Бригада № 112': 9174006899,
                 'Бригада № 114': 9174002769,
                 'Бригада № 116': 9174009979,
                 'Бригада № 117': 9174001627,
                 'Бригада № 118': 9198625311,
                 'Бригада № 119': 9174002340,
                 'Бригада № 120': 9325426037,
                 'Бригада № 121': 9198625269,
                 'Бригада № 122': 9198625364,
                 'Бригада № 123': 9867803956,
                 'Бригада № 124': 9867804254,
                 'Бригада № 125': 9867806579,
                 'Бригада № 126': 9867807081,
                 'Бригада № 127': 9174007527,
                 'Бригада № 128': 9174002881,
                 'Бригада № 129': 9174002707,
                 'Бригада № 130': 9174001962,
                 'Бригада № 131': 9174001882,
                 'Бригада № 132': 9174009853,
                 'Бригада № 133': 9174002035,
                 'Бригада № 134': 9174009821,
                 'Бригада № 136': 9273211908,
                 'Бригада № 137': 9273460185,
                 'Бригада № 138': 9174008389,
                 'Бригада № 139': 9174003046,
                 'Бригада № 140': 9174003936,
                 'Бригада № 141': 9228378408,
                 'Бригада ТРС № 1': 9228928015,
                 'Бригада ТРС № 2': 9228927913,
                 'Бригада ТРС № 3': 9228928016,
                 'Бригада ГНКТ №1': 9174003142,
                 'Бригада ГНКТ №2': 9174001690}


def if_None(value):
    if isinstance(value, datetime):
        return value
    elif value is None or 'отс' in str(value).lower() or str(value).replace(' ', '') == '-' \
            or value == 0 or str(value).replace(' ', '') == '':
        return 'отсут'
    else:
        return value

region_list = ['', 'АГМ', 'ИГМ', 'ТГМ', 'ЧГМ', 'КГМ']

type_kr_list = [
    ' ',
    'КР1  Ремонтно - изоляционные работы',
    'КР1-1  Отключение отдельных интервалов и пропластков объекта эксплуатации',
    'КР1-2  Отключение отдельных пластов',
    'КР1-2.1  Отключение верхних и нижних промежуточных пластов ( пачек)',
    'КР1-2.2  Отключение нижних пластов',
    'КР1-3  Восстановление герметичности цементного кольца',
    'КР1-4  Наращивание цементного кольца за эксплуатационной, промежуточной колонной, кондуктором, направлением',
    'КР1-4.1  Наращивание цементного кольца за эксплуатационной колонной',
    'КР1-4.2  Наращивание цементного кольца за кондуктором, технической колонной, направлением',
    'КР1-5  Крепление слабосцементированных пород призабойной зоны пласта',
    'КР2  Устранение негерметичности эксплуатационной колонны',
    'КР2-1  Устранение негерметичности тампонированием',
    'КР2-2  Устранение негерметичности установкой пластыря',
    'КР2-3  Устранение негерметичности спуском дополнительной обсадной колонны меньшего диаметра',
    'КР2-4  Устранение негерметичности частичной сменой эксплуатац-й колонны',
    'КР2-5  Устранение негерметичности эксплуатационной колонны доворотом',
    'КР3  Устранение аварий, допущенных в процессе эксплуатации или ремонта',
    'КР3-1  Извлечение оборудования из скважины после аварии или инцидента, допущенного в процессе эксплуатации',
    'КР3-1.1  Извлечение оборудования УЭЦН из скважины после аварии или инцидента, допущенного в процессе эксплуатации',
    'КР3-1.2  Извлечение оборудования УЭДН из скважины после аварии или инцидента, допущенного в процессе эксплуатации',
    'КР3-1.3  Извлечение оборудования УЭВН из скважины после аварии или инцидента, допущенного в процессе эксплуатации',
    'КР3-1.4  Извлечение оборудования ШГН из скважины после аварии или инцидента, допущенного в процессе эксплуатации',
    'КР3-1.5  Извлечение оборудования УШВН из скважины после аварии или инцидента, допущенного в процессе эксплуатации',
    'КР3-1.6  Извлечение НКТ из скважины после аварии или инцидента, допущенного в процессе эксплуатации',
    'КР3-1.7  Извлечение пакера из скважины после аварии или инцидента, допущенного в процессе эксплуатации',
    'КР3-1.8  Ликвидация аварии или инцидента из-за коррозионного износа НКТ',
    'КР3-1.9  Очистка забоя и ствола скважины от посторонних предметов',
    'КР3-1.10  Ревизия и замена глубинного оборудования',
    'КР3-1.11  Замена устьевого оборудования',
    'КР3-1.12  Восстановление циркуляции при спущенной в скважину УЭЦН, УЭВН, УЭДН (размыв парафино-гидратных пробок '
    'в эксплуатационной колонне и НКТ)',
    'КР3-1.13  Восстановление циркуляции при спущенной в скважину ШГН (УШВН)',
    'КР3-1.14  Восстановление циркуляции при спущенных в скважину НКТ',
    'КР3-1.15  Промывка забоя скважины',
    'КР3-1.16  Прочие работы по устранению аварий или инцидента, допущенных при эксплуатации  скважин',
    'КР3-2  Ликвидация аварии или инцидента с эксплуатационной колонной',
    'КР3-3  Очистка забоя и ствола скважины от посторонних предметов',
    'КР3-4  Очистка ствола и забоя  скважины от парафино-гидратных отложений, солей, гипса, песчаных и гидратных '
    'пробок',
    'КР3-5  Ликвидация аварии или инцидента, допущенных в процессе ремонта скважин',
    'КР3-6  Восстановление циркуляции (размыв парафино-гидратных пробок) в эксплуатационной колонне и НКТ'
    'КР3-7  Прочие работы по ликвидации аварий или инцидента, допущенных в процессе ремонта  скважин',
    'КР3-7.1  Извлечение оборудования УЭЦН из скважины после аварии или инцидента, допущенного в процессе ремонта '
    'скважины',
    'КР3-7.2  Извлечение оборудования УЭДН из скважины после аварии или инцидента, допущенного в процессе ремонта '
    'скважины',
    'КР3-7.3  Извлечение оборудования УЭВН из скважины после аварии или инцидента, допущенного в процессе ремонта '
    'скважины',
    'КР3-7.4  Извлечение оборудования ШГН из скважины после аварии или инцидента, допущенного в процессе ремонта '
    'скважины',
    'КР3-7.5  Извлечение оборудования УШВН из скважины после аварии или инцидента, допущенного в процессе ремонта '
    'скважины',
    'КР3-7.6  Извлечение НКТ из скважины после аварии или инцидента, допущенного в процессе ремонта скважины',
    'КР3-7.7  Извлечение пакера из скважины после аварии или инцидента, допущенного в процессе ремонта скважины',
    'КР4  Изоляция одних и приобщение других горизонтов',
    'КР4-1  Изоляция одних и приобщение вышележащих или нижележащих горизонтов',
    'КР4-2  Приобщение пластов для совместной эксплуатации дострелом, с изменением диаметра или глубины скважины',
    'КР4-3  Приобщение дополнительного количества пластов дострелом для совместной эксплуатации',
    'КР5  Спуск и подъем оборудования для раздельной эксплуатации и закачки различных реагентов в пласт',
    'КР6   Комплекс подземных работ по восстановлению работоспособности скважин с использованием '
    'технических элементов бурения, включая проводку горизонтальных участков ствола скважин',
    'КР6-1  Зарезка и бурение бокового ствола в преждевременно обводненных или низко-продуктивных скважинах',
    'КР6-2  Зарезка и бурение бокового ствола в аварийной скважине',
    'КР6-3  Зарезка бокового или продолжение ствола скважины с переходом на горизон-тальный участок в '
    'преждевременно обводненной или н/продуктивной скв-не'
    'КР6-4  Проводка горизонт-го участка скважины с целью повышения н/отдачи пласта',
    'КР6-5  Бурение цементного стакана',
    'КР6-6  Фрезерование башмака колонны с углублением ствола в горной породе',
    'КР6-7  Бурение и оборудование шурфов, артезианских и стендовых скважин',
    'КР6-8  Зарезка и бурение бокового ствола в скважине с многоствольным заканчива-нием и с проводкой горизонтального '
    'участка в продуктивном пласте',
    'КР6-9  Зарезка и бурение бокового горизонтального ствола в аварийной скважине',
    'КР7  Обработка призабойной зоны пласта и вызов притока',
    'КР7-1  Проведение кислотной обработки:',
    'КР7-1.1  соляной кислотой',
    'КР7-1.2  грязевой кислотой',
    'КР7-1.3  пенокислотная обработка',
    'КР7-1.4  другими кислотами',
    'КР7-2  Проведение ГРП',
    'КР7-3  Проведение ГГРП',
    'КР7-4  Проведение ГПП',
    'КР7-5  Виброобработка призабойной зоны пласта',
    'КР7-6  Термообработка призабойной зоны пласта',
    'КР7-6.1  Электропрогрев',
    'КР7-6.2  Закачка пара',
    'КР7-6.3  Закачка горячей воды',
    'КР7-6.4  Термокислотная обработка ',
    'КР7-6.5  Термохимическая обработка',
    'КР7-7  Промывка призабойной зоны',
    'КР7-7.1  Промывка скважины горячей нефтью',
    'КР7-7.2  Промывка скважины водой',
    'КР7-8  Промывка и пропитка призабойной зоны пласта растворами ПАВ',
    'КР7-9  Обработка скважин термогазохимическими методами (ТГХВ и т.д.)',
    'КР7-10  Проведение УОС и его модификаций',
    'КР7-11  Проведение КИИ-95 (ИПТ и др.)',
    'КР7-12  Вызов притока свабированием, желонкой, заменой жидкости, компрессир-нием',
    'КР7-13  Выравнивание профиля иливосстановление приемистости нагнетат-й скважины',
    'КР7-14  Проведение прострелочных и взрывных работ (перфорация, торпедир-е и т.д.)',
    'КР7-15  Опытные работы по испытанию новых видов скважинного оборудования',
    'КР7-16  Прочие виды обработки призабойной зоны пласта',
    'КР7-16.1  Проведение ОПЗ с применением технологий гибких непрерывных НКТ',
    'КР7-16.2  Проведение реагентной разглинизации ПЗП',
    'КР7-16.3  Проведение повторной перфорации на кислых растворах',
    'КР7-16.4  Проведение депрессионной перфорации пласта',
    'КР7-16.5  Проведение МГД',
    'КР7-16.6  Обработка щелочными растворами',
    'КР7-16.7  Обработка растворителями',
    'КР8  Исследование скважин',
    'КР8-1 Иследование характера насыщенности и выработки продуктивных пластов, уточнение геологического разреза в '
    'скважине',
    'КР8-2  Оценка технического состояния скважины (обследование скважины)',
    'КР9  Перевод скважин на использование по другому назначению',
    'КР9-1  Освоение скважины под нагнетание',
    'КР9-2  Перевод скважины под отбор технической воды',
    'КР9-3  Перевод скважины в наблюдательную, пьезометрическую, контрольную',
    'КР9-4  Перевод скважин под нагнетание теплоносителя, воздуха или газа',
    'КР9-5  Перевод скважин в добывающие',
    'КР9-6  Перевод скважин в газодобывающие из других категорий',
    'КР10  Ввод в эксплуатацию и ремонт нагнетательных скважин',
    'КР10-1  Восстановление приемистости нагнетательной скважины',
    'КР10-1.1  Проведением кислотной обработки',
    'КР10-1.2  Освоением высоким давлением',
    'КР10-1.3  Термохимической обработкой',
    'КР10-1.4  Пенокислотной обработкой',
    'КР10-1.5  Виброобработкой',
    'КР10-1.6  ГРП',
    'КР10-1.7  Обработкой растворами ПАВ',
    'КР10-2  Смена пакера в нагнетательной скважине',
    'КР10-3  Оснащение паро-и воздухонагнетательных скважин противопесочным оборуд-м',
    'КР10-4  Промывка в паро-и воздухонагнетательных скважинах песчаных пробок',
    'КР10-5  Прочие виды работ по восстановлению приемистости нагнетательной скважины',
    'КР11  Консервация и расконсервация скважин',
    'КР11-1  Консервация  скважины',
    'КР11-2  Расконсервация скважины',
    'КР12  Ликвидация скважин',
    'КР12-1  Ликвидация скважины без наращивания цементного кольца за эксплуатац кол-й',
    'КР12-2  Ликвидация скважины с наращиванием цементного кольца за эксплуатац кол-й',
    'КР12-3  Ликвидация скважины при смещении  эксплуатационной колонны',
    'КР13  Прочие виды работ',
    'КР13-1  Подготовительные работы к ГРП (ПР)',
    'КР13-2  Освоение скважины после ГРП (ЗР)',
    'КР13-1  Подготовительные работы к ГРП (ПР) КР13-2  Освоение скважины после ГРП (ЗР)',
    'КР13-3  Подготовка скважины к забуриванию дополнительного ствола',
    'КР13-4  Освоение скважины после забуривания дополнительного ствола',
    'КР13-5  Подготовка скважины к проведению работ по повышению н/отдачи пластов',
    'КР13-6  Подготовительные работы к ГГРП (ПР)',
    'КР13-7  Заключительные работы (ЗР) после ГГРП (освоение скважины и т.д.)',
    'КР13-8  Промывка забоя водозаборных и артезианских скважин с компрессором',
    'КР13-9  Ремонт водозаборных скважин со спуском дополнительн колонны и промывкой',
    'КР13-10  Ремонт поглощающей скважины',
    'КР14-4 Освоение эксплуатационной скважины с горизонтальным окончанием'
]
dict_calc_CaCl = {
    1.01: (14.9, 997),
    1.02: (29.5, 995),
    1.03: (44.2, 993),
    1.04: (58, 991),
    1.05: (67.3, 988),
    1.06: (84.4, 984),
    1.07: (97.6, 980),
    1.08: (104.5, 976),
    1.09: (117.4, 973),
    1.10: (126.8, 970),
    1.11: (144.5, 965),
    1.12: (160.5, 957),
    1.13: (175, 952),
    1.14: (195.3, 948),
    1.15: (204.1, 943),
    1.16: (218.8, 940),
    1.17: (233.4, 935),
    1.18: (248, 928),
    1.19: (264.1, 925.9),
    1.2: (277.2, 922.8),
    1.21: (291.8, 918.2),
    1.22: (306.4, 913.6),
    1.23: (321.1, 908.9),
    1.24: (332.9, 907.1),
    1.25: (351, 899),
    1.26: (366.4, 893.6),
    1.27: (382, 888),
    1.28: (398, 882),
    1.29: (407.8, 872),
    1.30: (430.7, 869.3),
    1.31: (466, 844),
    1.32: (482, 838)
    }

dict_calc_CaZHG = {
    1.33: (498, 832),
    1.34: (513, 827),
    1.35: (529, 821),
    1.36: (545, 815),
    1.37: (560, 810),
    1.38: (576, 804),
    1.39: (592, 798),
    1.40: (607, 793),
    1.41: (623, 787),
    1.42: (639, 781),
    1.43: (654, 776),
    1.44: (670, 770),
    1.45: (686, 764),
    1.46: (702, 759),
    1.47: (717, 753),
    1.48: (733, 747),
    1.49: (749, 741),
    1.50: (764, 736),
    1.51: (780, 730),
    1.52: (796, 724),
    1.53: (811, 719),
    1.54: (827, 713),
    1.55: (845, 705),
    1.56: (858, 698),
    1.57: (880, 690),
    1.58: (900, 680),
    1.59: (915, 675),
    1.60: (928, 667)
    }