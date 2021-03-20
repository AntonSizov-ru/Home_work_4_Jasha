anya = {'Секретные материалы': 'фантастика', 'Карточный домик': 'драма', 'Рик и Морти': 'фантастика'}
olya = {'Клан Сопрано': 'криминал', '24': 'драма', 'Во все тяжкие': 'криминал', 'Карточный домик': 'драма'}
nastya = {'Ведьмак': 'фэнтази', 'Игра престолов': 'фэнтази'}
sveta = {'Черное зеркало': 'фантастика', 'Карточный домик': 'драма', 'Рик и Морти': 'фантастика'}
# создаём списки по ключам
anya_likes = set(anya.keys())
olya_likes = set(olya.keys())
nastya_likes = set(nastya.keys())
sveta_likes = set(sveta.keys())
'''print(anya_likes, '\n',
      olya_likes, '\n',
      nastya_likes, '\n',
      sveta_likes)'''
# сравниваем списки
anya_olya_likes = anya_likes & olya_likes
anya_nastya_likes = anya_likes & nastya_likes
anya_sveta_likes = anya_likes & sveta_likes
# находим длину каждого списка
aol = len(anya_olya_likes)
anl = len(anya_nastya_likes)
asl = len(anya_sveta_likes)
# узнаём какой список больше остальных
if int(aol) > int(anl) and int(aol) > int(asl):
    result = ''.join(anya_olya_likes)
    print('Оля разделяет предпочтения Ани в сериалах больше остальных, они обе смотрят: ' + result + '.')
elif int(anl) > int(aol) and int(anl) > int(asl):
    result = ''.join(anya_nastya_likes)
    print('Настя разделяет предпочтения Ани в сериалах больше остальных, они обе смотрят: ' + result + '.')
elif int(asl) > int(aol) and int(asl) > int(anl):
    result = ', '.join(anya_sveta_likes)
    print('Света разделяет предпочтения Ани в сериалах больше остальных, они обе смотрят: ' + result + '.')
else:
    print('Нет такой коллеги, которая бы разделяла предпочтение Ани в сериалах больше других.')
