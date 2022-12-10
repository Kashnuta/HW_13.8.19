kol_bil = int(input('Количество билетов:'))
zakaz= 0
vozrast = 0
for i in range(1, kol_bil+1):
    vozrast = int(input('Возраст:'))
    if 0 <= vozrast < 18:
        zakaz += 0
    elif 18 <= vozrast <= 25:
        zakaz += 990
    elif vozrast > 25:
        zakaz += 1390
if kol_bil > 3:
    zakaz *= 0.9
print('Сумма к оплате', zakaz, 'рублей')