import random

shows = {'Секретные материалы': 'фантастика', 'Ведьмак': 'фэнтази', 'Клан Сопрано': 'криминал', '24': 'драма',
         'Черное зеркало': 'фантастика', 'Во все тяжкие': 'криминал', 'Игра престолов': 'фэнтази',
         'Карточный домик': 'драма', 'Рик и Морти': 'фантастика'}
ratings = {'Секретные материалы': 0.9, 'Ведьмак': 0.95, 'Клан Сопрано': 0.8, '24': 0.75, 'Черное зеркало': 0.98,
           'Во все тяжкие': 0.85, 'Игра престолов': 0.87, 'Карточный домик': 0.82, 'Рик и Морти': 1}

# узнаём жанр у пользователя и минимальный рейтинг
chose = str(input('Уажите жанр для исключения из поиска\n:')).strip().lower()
top = float(input('Уажите минимальный приемливый для вас рейтинг от 0.00 до 1\n:'))
# создаём список для рейтингов
outputs = []
ratings_outputs = {}
series = []
result = []

for show, genre in shows.items():
    if genre != chose:
        outputs.append(show)
        random.shuffle(outputs)
    if ratings[show] >= top:
        ratings_outputs = dict((key, value) for key, value in ratings.items() if key in outputs)
for output in outputs:
    for serial in ratings_outputs.keys():
        if ratings_outputs[serial] >= top:
            series.append(serial)
            for rating in series:
                if rating not in result:
                    result.append(rating)
print(result)
while len(result) > 0:
    print(result)
    print(f'\nИсходя из Ваших предпочтений, мы рекомендуем вам к просмотру сериал "{result[0]}" в '
          f'жанре {shows[result[0]]}.\nНа Metacritic рейтинг сериала составляет: '
          f'{ratings[result[0]] * 10}/ 10.')
    answer = str(input('Если хотите останавливаться на этом сериале введите "Стоп", если хотите '
                       'продолжить поиск, то введите "Далее".\n'
                       'Ввод иных команд приведёт к выходу из поиска.\n:')).strip().lower()
    del result[0]
    if answer == 'стоп':
        print(f'\nВы остановилиси свой выбор на сериале {result[0]} в жанре {shows[result[0]]}, рейтинг '
              f'на Metacritic {ratings[result[0]] * 10} / 10.')
        break
    elif answer == 'далее':
        continue
else:
    print('Сожалем, что не смогли Вам помочь. Но подходящих для Вас сериалов у нас не осталось.\n До новых встреч!')
