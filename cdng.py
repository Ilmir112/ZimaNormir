import well_data


region_dict = {
    'ИГМ': ['АкЦДНГ 01', 'АкЦДНГ 02', 'АкЦДНГ 03', 'ИЦДНГ 01', 'ИЦДНГ 02', 'ИЦДНГ 03', 'ИЦДНГ 04', 'ИЦДНГ 05'],
    'ТГМ': ['ОЦДНГ 01', 'ОЦДНГ 02', 'ОЦДНГ 03', 'ТЦДНГ 01', 'ТЦДНГ 02', 'ТЦДНГ 03'],
    'КГМ': ['КЦДНГ 01', 'КЦДНГ 02', 'КЦДНГ 03', 'КЦДНГ 04', 'КЦДНГ 05', 'КЦДНГ 06', 'КЦДНГ 07', 'КЦДНГ 08'],
    'ЧГМ': ['УЦДНГ 01', 'УЦДНГ 02', 'УЦДНГ 03', 'УЦДНГ 04', 'ЧЦДНГ 01', 'ЧЦДНГ 02', 'ЧЦДНГ 03', 'ЧЦППД'],
    'АГМ': ['АЦДНГ 01', 'АЦДНГ 02', 'АЦДНГ 03', 'АЦДНГ 04', 'ЮЦДНГ 01', 'ЮЦДНГ 02', 'ЮЦДНГ 03']
}

region_p = {
    "ТГМ": [
        {'Заместитель начальника региона ДНГ (ТГМ) УДНГ ООО "Башнефть-Добыча"': 'М.М. Гарифуллин'},
        {'Главный геолог региона ДНГ (ТГМ) УРМ ООО "Башнефть-Добыча"': 'Р.З. Имамов'},
        {'Руководитель Сектора  разработки ТГМ ОРМ УРМ ': 'С.В. Петров'},
        {'Руководитель Сектора  ТГМ ПТО УДНГ': 'Д.В. Аглетдинов'},
        {'Руководитель сектора АиП ГТМ ТГМ': 'Р.Р. Хаертдинов'},
        {
            'Ведущий региональный супервайзер Отдел супервайзинга ТиКРС,'
            ' Управление супервайзинга ремонта скважин и скважинных '
            'технологий ООО “Башнефть - Добыча”.': 'К.В. Семенов'},
        {'Ведущий геолог ОПиМ ЭБиЗБС ООО "Башнефть-Добыча"': 'Ф.Р. Сафин'},
        {'Ведущий инженер УППР и ГТМ КГМ / Отдел интенсификации добычи': 'И.И.Самигуллин'},
        {'Ведущий инженер СРМ КГМ ООО "Башнефть-Добыча': 'Л.Н. Усова'}],
    'ЧГМ': [
        {'Заместитель начальника Чекмагушевского РДНГ ООО " Башнефть-Добыча"': 'Р.Н. Ибрагимов'},
        {'Главный геолог региона ДНГ (ЧГМ) УРМ ООО "Башнефть-Добыча"': 'Н.С. Асташкин'},
        {'Руководитель Сектора  разработки ЧГМ ОРМ УРМ ': 'Р.А. Нугуманов'},
        {'Руководитель сектора АиП ГТМ ЧГМ': 'А.А. Набиев'},
        {'Руководитель сектора ПТО ЧГМ': 'А.В. Кулеш'},
        {
            'Ведущий региональный супервайзер Отдел супервайзинга ТиКРС, Управление супервайзинга ремонта скважин и '
            'скважинных технологий ООО “Башнефть - Добыча”.': 'Р.С. Шайхатдаров'},
        {'Менеджер ОПиМ ЭБиЗБС   ООО "Башнефть-Добыча"': 'М.Р. Гилимханов'},
        {'Ведущий инженер УППР и ГТМ КГМ / Отдел интенсификации добычи': 'И.Ф. Ахунов'},
        {
            'Главный специалист сектора анализа и управления разработкой месторождений  ООО "Башнефть-Добыча"':
                'А.Р. Гареев'},
        {'Ведущий инженер СРМ КГМ ООО "Башнефть-Добыча': 'И.Н. Хаков'}
    ],
    'ИГМ': [
        {'Заместитель начальника Ишимбайского РДНГ ООО " Башнефть-Добыча"': 'А.Ю. Жадаев'},
        {'Главный геолог региона ДНГ (ИГМ) УРМ ООО "Башнефть-Добыча"': 'А.Н. Турдыматов'},
        {'Руководитель Сектора  разработки ИГМ ОРМ УРМ ': 'И.М. Рахматуллин'},
        {'Руководитель сектора АиП ГТМ ЧГМ': 'Ф.Ш. Адршин'},
        {'Ведущий инженер ПТО УДНГ ИР': 'Р.В. Абросимов'},
        {'Менеджер ОС ТКРС УСРСиСТ ООО «Башнефть-Добыча»': 'Р.Р. Кинзябаев'},
        {
            'Главный специалист сектора анализа и управления разработкой месторождений '
            'ООО "Башнефть-Добыча"': 'А.Р. Гареев'},
        {'Ведущий инженер СРМ КГМ ООО "Башнефть-Добыча': 'И.Н. Хаков'}],
    'КГМ': [
        {'Заместитель начальника Краснохолмского РДНГ ООО " Башнефть-Добыча"': 'Ю.А. Дорошин'},
        {'Главный геолог региона ДНГ (КГМ) УРМ ООО "Башнефть-Добыча"': 'Ф.Ф. Ахметшин'},
        {'Руководитель Сектора  разработки КГМ ОРМ УРМ ': 'Е.Г. Густов'},
        {'Руководитель сектора АиП ГТМ КГМ': 'А.Ф. Магадиев'},
        {'Менеджер ПТО УДНиГ': 'Е.Ю. Зартдинов'},
        {
            'Ведущий региональный супервайзер Отдел супервайзинга ТиКРС, Управление супервайзинга ремонта '
            'скважин и скважинных технологий ООО “Башнефть - Добыча”.': 'Р.Н. Гареев'},
        {'Ведущий геолог ОПиМ ЭБиЗБС ООО "Башнефть-Добыча"': 'И.Р. Гусманов'},
        {'Ведущий инженер УППР и ГТМ КГМ / Отдел интенсификации добычи': 'Р.З. Шагалиев'},
        {'Ведущий инженер СРМ КГМ ООО "Башнефть-Добыча': 'И.Н. Хаков'}],
    'АГМ': [
        {'Заместитель начальника Арланского РДНГ ООО " Башнефть-Добыча"': 'Р.Н. Ян'},
        {'Главный геолог региона ДНГ (АГМ) УРМ ООО "Башнефть-Добыча"': 'И.Ф. Самигуллин'},
        {'Руководитель Сектора  разработки АГМ ОРМ УРМ ': 'М.В. Ценева'},
        {'Руководитель сектора АиП ГТМ АГМ': 'А.К. Зарипов'},
        {'Ведущий инженер сектора по АГМ ПТО УДНиГ ООО "Башнефть-Добыча"': 'И.В. Хузин'},
        {'Менеджер ОС ТКРС УСРСиСТ ООО «Башнефть-Добыча»': 'И.К. Муллаяров '},
        {None: None},
        {None: None}
    ]
}

region_dict = {
    'ИГМ': ['АкЦДНГ 01', 'АкЦДНГ 02', 'АкЦДНГ 03', 'ИЦДНГ 01', 'ИЦДНГ 02', 'ИЦДНГ 03', 'ИЦДНГ 04', 'ИЦДНГ 05'],
    'ТГМ': ['ОЦДНГ 01', 'ОЦДНГ 02', 'ОЦДНГ 03', 'ТЦДНГ 01', 'ТЦДНГ 02', 'ТЦДНГ 03'],
    'КГМ': ['КЦДНГ 01', 'КЦДНГ 02', 'КЦДНГ 03', 'КЦДНГ 04', 'КЦДНГ 05', 'КЦДНГ 06', 'КЦДНГ 07', 'КЦДНГ 08'],
    'ЧГМ': ['УЦДНГ 01', 'УЦДНГ 02', 'УЦДНГ 03', 'УЦДНГ 04', 'ЧЦДНГ 01', 'ЧЦДНГ 02', 'ЧЦДНГ 03', 'ЧЦППД'],
    'АГМ': ['АЦДНГ 01', 'АЦДНГ 02', 'АЦДНГ 03', 'АЦДНГ 04', 'ЮЦДНГ 01', 'ЮЦДНГ 02', 'ЮЦДНГ 03', 'АЦППД']
}


def itog_1():

    itog_1 = [
        [None, 'ИТОГО:', None, None, None, None, None, None, None, None, None,
         f'=ROUND(SUM(L{well_data.itog_ind_min + 2}:L{well_data.itog_ind_max}),1)'],
        [None, 'Герметизация , разгерметизация  устья  скважины', None, None, None, None, None, None, None,
         None, None, f'=ROUND(SUM(L{well_data.itog_ind_min + 2}:L{well_data.itog_ind_max - 1})/11.5*11/60 ,1)'],
        [None, 'Заправка ДВС', None, None, None, None, None, None, None, None, None,
         f'=ROUND(SUM(L{well_data.itog_ind_min}:L{well_data.itog_ind_max - 1})/11.5*0.3    ,1)'],
        [None, 'ПЗР в начале и конце смены с заполнением вахтового журнала', None, None, None, None, None,
         None, None, None, None, f'=ROUND(SUM(L{well_data.itog_ind_min}:L{well_data.itog_ind_max - 1})/11.5*0.3,1)'],
        [None, 'Непредвиденные  работы  : ', None, None, None, None, None, None, None, None, None,
         f'=ROUND(SUM(L{well_data.itog_ind_min}:L{well_data.itog_ind_max + 2})*'
         f'{well_data.bottomhole_artificial._value}/100*0.0004 ,1)'],
        [None, 'ВСЕГО  :', None, None, None, None, None, None, None, None, None,
         f'=ROUND(l{well_data.itog_ind_max + 1} + l{well_data.itog_ind_max + 2} +'
         f' l{well_data.itog_ind_max + 3} + l{well_data.itog_ind_max + 4} +l{well_data.itog_ind_max + 5}, 1)'],
        [None,
         'Примечания: В соответствии с регламентом на производство КРС – заблаговременно подавать заявки на '
         'необходимое оборудование, а так же вызывать представителя Заказчика на геофизические работы, ПВР, '
         'установку пакера, срыв планшайбы, опрессовку колонны и другие технологические операции, прием '
         'скважины в ремонт и сдача из ремонта.',
         None, None, None, None, None, None, None, None, None, None],
        [None, 'ПРИМЕЧАНИЕ:', None, ' ', None, None, None, None, None, None, None, None],
        [None,
         'При незначительных изменениях в плане работ (изменении компоновки подземного оборудования, '
         'объемов закачки и т.д.)  и доп. работах в виде единичных СПО, технол.операций и др. возможна '
         'работа без доп. плана - по письму Заказчика.   ',
         None, None, None, None, None, None, None, None, None, None],
        [None, 'поглощения жидкости не допускать', None, None, None, None, None, None, None, None, None,
         None],
        [None, 'Ответственный за соблюдением и создание безопасных условий работ – мастера КPС ', None, None,
         None, None, None, None, None, None, None, None]]
    return itog_1
