cause_presence_of_downtime_list = ['',
    'по причине РУДНГ', 'ПГО Тюменьпромгеофизика', 'ООО Башнефть-Петротест', 'АО Башнефтегеофизика', 'ООО РН-ГРП',
    'ООО Крезол-НС', 'ООО Петрол-Сервис', 'ООО ТаграС-РемСервис (ГРП)', 'ООО РН-Транспорт', 'ООО ТранCпецCервис ',
    'ООО УК Система-Сервис', 'ОП Новомет-Юг', 'ООО ПК Борец', 'ООО РН-Сервис ГНКТ Уфа', 'ООО Ветеран',
    'по причине ООО Югсон-Сервис', 'по причине ООО РостСтройПроект ', 'по причине ООО РИР  2С',
    'по причине ООО Крезол Нефтесервис ОПЗ', 'по причине ООО Инфрек', 'по причине ООО  НТС Лидер',
    'по причине ООО Римера-Сервис', 'сервис по УЭЦН', 'сервис по ШГН', 'сервис по НКТ, штангам', 'сервис по НПО',
    'по причине ____________________', 'ПО ТКРС']

cause_presence_of_jamming = ['', 'операции', 'Тех. ожидание', 'Метео', 'Простои Заказчика', 'Простои Подрядчика',
                             'Глушение по согл.заказчиком',
                             'Глушение без согл.', 'Глушение опереж.']

cause_presence_of_downtime_classifocations_list = ['',
    '01.Отсутствие НКТ', '02.Отсутствие ГНО и НО', '03.Отсутствие спец.материалов и оборудования',
    '04.Бездорожье (паводок), неподготовлены куст.площадки', '04.1 Отсутствие подъездных дорог',
    '04.2 Не готовность территории (скв., куст.площадки)', '05.Неисправность цехового оборудования',
    '06.Отсутствие спец.техники', '07.Отсутствие ППУ', '08.Отсутствие трубовозов', '09.По вине ЭПУ-сервис',
    '10.Неритмичность работы сервисных бригад', '11.По вине геофизиков', '12.Отключение э/энергии',
    '16.Ожидание принятия/исполнения решения', '22. Ожидание освобождения устья (ЗБС, ВНС)', '20. ОТМ ЦДНГ',
    '17.Ожидание ГРП', '15.Остановка по ТБ', '18.Прочие', '21. Неподготовленность скважины к ремонту',
    '19. Отсутствие водной переправы', '23. Перерасчёт ГНО', '1.Отсутствие НКТ', '2.Отсутствие жидкости глушения',
    '3.Отсутствие спец.материалов', '4.Неисправность цехового оборудования', '5.Отсутствие спец.техники',
    '6.Отсутствие ППУ', '8.Отсутствие грузоподъемной техники', '9.Отсутствие техники для переезда',
    '10.Ремонт подъемников и спец.техники', '11.Неполный состав вахт', '12.По вине ЭПУ-сервис',
    '13.Неритмичность работы сервисных бригад', '16.Ожидание принятия/исполнения решения',
    '17.Остановка по ТБ, запрет супервайзера', '18.Неисправность оборудования бригады', '21.Прочие',
    '22. Простои по заявкам', '22.8 Несвоевременная заявка на оборудование ГРП',
    '22.3 Несвоевременная заявка на ГДИ (СИАМ, ЛСГ)', '22.6 Несвоевременная заявка на ЖГ/кислоты',
    '22.5 Несвоевременная заявка на ГНО (ЭЦН/ШГН)', '14.Ожидание движения', '22.1. Несвоевременная заявка на ГФР',
    '22.4 Несвоевременная заявка на обеспечение оборудованием  (фонд. НКТ/штанги и др.)',
    '22.2. Несвоевременная заявка на ПГИ (СВАБ)', '22.7 Несвоевременная заявка на спец. тех-ку ЦДНГ']

operations_of_downtimes_list = ['Тех. ожидание', 'Метео', 'Простои Заказчика', 'Простои Подрядчика',
                                'Глушение по согл.заказчиком', 'Глушение без согл.', 'Глушение опереж.']

cause_discharge_list = ['', 'Остаточное ( не более 2 ч)', 'После глушения (не кор.Рпл)',
                        'после СКО, ПВР', 'после свабирования', 'после РГД', 'по причине неисправности задвижек',
                        'по причине наличия пробок в скважине', 'иное']

count_jamming_list = ['', '1ый подход глушения', '2ой подход глушения', '3ий подход глушения', 'Приготовление УТЖ',
                      'Приготовление БП']

contractor_zhgs_list = ['', 'ПО ТКРС', 'Крезол', 'РостСтройпроект', 'ОПИ', 'БашНИПИ']

technological_expectation_list = ['', 'Тех. ожидание', 'Метео', 'Простои Заказчика', 'Простои Подрядчика',
                                  'Глушение по согл.заказчиком', 'Глушение без согл.', 'Глушение опереж.']

cause_jamming_first_list = ['',
    'при техн. невозможности опер.глушения (наличие пакеров, не исправность АУ и т.д.)',
    'при необходимости предварительной разрядки (ЗР ГРП, ППД и т.д.)',
    'высокодебитный фонд, где опережающее глушение экономически не целесообразно',
    'при бездорожье (звено глушения заезжает с буксировкой при переезде бригады)',
    'при необходимости приготовления ЖГ на основе солей силами бригады',
    'при изменении графика движения бригад по приоритету',
    'по причине не проведения опер.глушения (без оплаты)'
]

drilling_ek_list = ['', 'ЦМ', 'ВП', 'проппатовая корка', 'ЭК', 'Ав.головы']

cause_jamming_second_list = ['',
    'Некорректное пластовое давление	',
    'Аномально низкое пластовое давление при высоких фильтрационных свойствах пласта(сложность подбора плотности '
    'и вязкости блок-пачки и ЖГ)	',
    'Многопластовые скважины, с различными пластовыми давлениями (более 20%) и фильтрационными свойствами	',
    'Высокая приемистость интервала перфорации (поглощение ЖГ)	',
    'Высокое значение газосодержания (газового фактора) – необходимость корректировки плотности ЖГ	',
    'Прорыв газа из газовой шапки – необходимость корректировки плотности ЖГ	',
    'Наличие разломов	',
    'Неоднородность пластов и их свойств	',
    'Несоблюдение технологии глушения скважин	',
    'Образование ЗКЦ (изменение пластового давления, характера приемистости)	',
    'Выявление негерметичности эксплуатационной колонны НЭК при проведении ремонта на скважине	',
    'Негерметичность забоя (поглощение ЖГ)	',
    'Несовместимость пластовой и закачиваемой воды (риски выпадения солей)	',
    'Риски несовместимости ЖГ с породой (набухание глин)	',
    'Кавернозность открытой части продуктивного интервала ствола скважины ',
    '(расширение из-за разрушения приствольной части продуктивных интервалов в результате эксплуатации и '
    'воздействия на ПЗП составами для ОПЗ)	',
    'Негерметичность лифта НКТ	',
    'Высокое влияние скважин ППД	',
    'После проведения ПВР, ОПЗ, свабирования.	'
]
cause_jamming_three_list = [
    'Некорректное пластовое давление',
    'Аномально низкое пластовое давление при высоких фильтрационных свойствах пласта(сложность подбора плотности и '
    'вязкости блок-пачки и ЖГ)',
    'Многопластовые скважины, с различными пластовыми давлениями (более 20%) и фильтрационными свойствами',
    'Высокая приемистость интервала перфорации (поглощение ЖГ)',
    'Высокое значение газосодержания (газового фактора) – необходимость корректировки плотности ЖГ',
    'Прорыв газа из газовой шапки – необходимость корректировки плотности ЖГ',
    'Наличие разломов',
    'Неоднородность пластов и их свойств',
    'Несоблюдение технологии глушения скважин',
    'Образование ЗКЦ (изменение пластового давления, характера приемистости)',
    'Выявление негерметичности эксплуатационной колонны НЭК при проведении ремонта на скважине',
    'Негерметичность забоя (поглощение ЖГ)',
    'Несовместимость пластовой и закачиваемой воды (риски выпадения солей)',
    'Риски несовместимости ЖГ с породой (набухание глин)',
    'Кавернозность открытой части продуктивного интервала ствола скважины ',
    '(расширение из-за разрушения приствольной части продуктивных интервалов в результате эксплуатации и '
    'воздействия на ПЗП составами для ОПЗ)',
    'Негерметичность лифта НКТ',
    'Высокое влияние скважин ППД',
    'После проведения ПВР, ОПЗ, свабирования.',
    'Предоставление не корректных данных в план-заказе, в связи с чем не корректный расчёт глушения (объем, плотность)'

]
