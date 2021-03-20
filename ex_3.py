shows = {'Секретные материалы': 'фантастика', 'Ведьмак': 'фэнтази', 'Клан Сопрано': 'криминал', '24': 'драма',
         'Черное зеркало': 'фантастика', 'Во все тяжкие': 'криминал', 'Игра престолов': 'фэнтази',
         'Карточный домик': 'драма', 'Рик и Морти': 'фантастика'}
ratings = {'Секретные материалы': 0.9, 'Ведьмак': 0.95, 'Клан Сопрано': 0.8, '24': 0.75, 'Черное зеркало': 0.98,
           'Во все тяжкие': 0.85, 'Игра престолов': 0.87, 'Карточный домик': 0.82, 'Рик и Морти': 1}
# узнаём жанр у пользователя
chose = str(input('Укажите жанр сериала\n:')).strip().lower()
# создаём список для сериалов подходящих по жанру
search = shows.items()
# создаём список для рейтингов
outputs = []
# узнаём какие сериалы подходят под жанр полученный от пользователя
for show, genre in search:
    if genre == chose:
        # наполняем список для рейтинга сериалов
        outputs.append(show)
# узнаём рейтинг сериалов из списка и выводим результаты для каждого из них в отдельности.
for result in outputs:
    if result in ratings.keys():
        print('У сериала "' + result + '" в жанре ' + chose + ' на Metacritic рейтинг составляет:', ratings[result]*10,
              '/ 10.')