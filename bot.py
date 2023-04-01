print('Приветствую вас! Я - Сабби, помощник для покупки подписок на различные сервисы')

entry = input('Чем я могу вам помочь? ').lower()
entry_lst = entry.split()

# Приветствие
entries = []
entries.extend('\nНаша команда занимается оформлением подписок для различных сервисов.')
entries.extend('Работаем мы уже долгое время и всё полностью безопасно.')
entries.extend('Итак, как здесь работает покупка?\nВы задаёте вопрос по подпискам.')
entries.extend('На выбор имеются разные категории подписок.')
entries.extend('Выберите категорию, затем нужный сервис.')
entries.extend('В выборе категории написаны цены.')

# Ответ - описание
desc_lst = ['расскажи','себе','кто','описание','как','работает']
for i in [b in desc_lst for b in entry_lst]:
	if i == True:
		for i in entries:
			print(i)
		break

# Ответ - приоберетение
buy_lst = ['приобрести','купить','оформить','хочу','подписку']
for i in [b in buy_lst for b in entry_lst]:
	if i == True:
		buy = True
		break

# Покупка

# База данных
category = ['музыка', 'кино', 'такси', 'образование', 'книги', 'игры', 'мультиподписки', '1', '2', '3', '4', '5', '6', '7']
music_subs = ['spotify','спотифай','яндекс.плюс','яндекс','яндекс плюс','apple music','эпл','эпл мьюзик']
music_subs.extend(['эплмьюзик','эппл','эппл мьюзик','yandex','yandex plus','я.плюс'])
music_desc = 'Spotify, Яндекс.Плюс, Apple Music'
# Спотифай 99 Я.Плюс 119 Эпл 129
cinema_subs = ['амедиатека','amediateka','netflix','нетфликс','иви','ivi','okko','окко','ютуб','ютуб премиум']
cinema_subs.extend(['youtube','youtube premium'])
cinema_desc = 'Amediateka, Netflix, IVI, Okko, Youtube Premium'
# Амедиа 449 Нетфликс 499 Иви 359 Окко 179 Ют.Прем 149
taxi_subs = ['yandex','yandex.taxi','яндекс','яндекс.такси','ситимобил','gett','гетт','убер','uber']
taxi_desc = 'Яндекс.Такси, Ситимобил, Gett, Uber'
# Я.Такси 59/п Ситимобил 49/п Гетт - 75/п Умер - 59/п
edu_subs = ['skyeng','скайэнг','скайенг','лингуалео','lingualeo']
edu_desc = 'Skyeng, Lingualeo'
# Скайэнг - 599 Лингуалео - 1999
book_subs = ['storytel','сторител','сторитэл','patefon','патефон','bookmate','букмейт']
book_desc = 'Storytel, Патефон, Букмейт'
# Сторител - 399 Патефон - 529 Букмейт - 269/449
game_subs = ['xbox','xbox game pass','game pass','ea play','иксбокс','eaplay','ubisoft+']
game_subs.extend(['ubisoft plus','юбисофт плюс','humble','humble bundle','psplus','ps plus'])
game_subs.extend(['пс плюс','псн','плейстейшн','playstation','psn'])
game_desc = 'Xbox Game Pass, EA Play, Ubisoft+, Humble Bundle, PSPlus'
# Xbox Game Pass - 499 EA Play - 279 Ubisoft+ - 899 Humble Bundle - 799 PSPlus - 479
multi_subs = ['яндекс.плюс','яндекс','яндекс плюс','x5paket','х5пакет','x5','х5','пакет','ogon','огонь']
multi_subs.extend(['megafon plus','megafon','мегафон плюс','мегафон','sberprime','sber','сбер','сберпрайм'])
multi_subs.extend(['vk combo','vkcombo','vk','вк','вк комбо','вк'])
multi_desc = 'Яндекс.Плюс, X5Пакет, Огонь, Мегафон Плюс, СберПрайм, VK Combo'
# Я.Плюс - 299 X5Paket - 99 Огонь - 179 Мегафон Плюс - 349 СберПрайм - 179 Vk Combo - 129

if buy:
	print('В нашей коллекции имеются подписки следующих категорий:')
	print('(1) Музыка, (2) кино, (3) такси, (4) образование, (5) книги, (6) игры и (7) мультиподписки.')
	ask_category = input('Какая категория вас интересует?\n').lower()
	while ask_category not in category:
		ask_category = input('Ошибка, попробуйте ещё раз').lower()
	subs = []
	desc = ''
	if (ask_category == 'музыка') or (ask_category == '1'):
		subs.append(music_subs)
		desc += music_desc
	if (ask_category == 'кино') or (ask_category == '2'):
		subs.append(cinema_subs)
		desc += cinema_desc
	if (ask_category == 'такси') or (ask_category == '3'):
		subs.append(taxi_subs)
		desc += taxi_desc
	if (ask_category == 'образование') or (ask_category == '4'):
		subs.append(edu_subs)
		desc += edu_desc
	if (ask_category == 'книги') or (ask_category == '5'):
		subs.append(book_subs)
		desc += book_desc
	if (ask_category == 'игры') or (ask_category == '6'):
		subs.append(game_subs)
		desc += game_desc
	if (ask_category == 'мультиподписки') or (ask_category == '7'):
		subs.append(multi_subs)
		desc += multi_desc

	confirm = ''
	while confirm != 'да':
		print('Какая подписка вас интересует?\n',desc,sep='')
		ask_sub = input()
		if ask_sub.lower() in subs:
			for i in subs:
				if i == ask_sub:
					buy_sub = i
		print('Вы собираетесь купить подписку',ask_sub)
		confirm = input('Вы уверены в выборе? ').lower()
	mail = input('Введите почту/телефон от аккаунта: ')
	password = input('Введите пароль от аккаунта: ')
	print('Перейдите по ссылке и оплатите заказ, а затем пришлите чек:')
	print('Оплата проведена успешно. Подписка будет активирована в течение часа.')

question = input('Какие ещё вопросы у вас имеются? ')
question.split()

for i in [b in ['подписка','не','оформлена','оформилась'] for b in question]:
	if i == True:
		q_help = True
		break
	
print('Спасибо, что воспользовались нашими услугами! До скорой встречи!')