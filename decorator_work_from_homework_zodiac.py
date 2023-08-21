from decorator_corrected import logger
from os import path

path = 'test_log.txt'

@logger(path)
def get_zodiac(birthday,date):
  if date >=21 and birthday =='март' or birthday =='апрель' and date <=19:# даты овена
    print("Поздравляем!вы-Овен!")
  elif birthday =='апрель' and date >=20 or birthday=='май' and date<=20:#даты тельца
    print("поздравляем!вы-Телец!")
  elif birthday =='май' and date >=21 or birthday=='июнь' and date<=20:#даты близнецов
    print("поздравляем!вы-Близнецы")
  elif birthday =='июнь' and date>=21 or birthday=='июль' and date<=22:#даты раков
    print("поздравляем!вы-РАК!!!")
  elif birthday =='июль' and date>=23 or birthday=='август' and date<=22:#даты львов
    print("поздравляем!вы-Лев!!!")
  elif birthday =='август' and date>=23 or birthday=='сентябрь' and date<=22:#даты дев
    print("поздравляем!вы-Дева!!!")
  elif birthday =='сентябрь' and date>=23 or birthday=='октябрь' and date<=22:#даты весов
    print("поздравляем!вы-Весы!!!")
  elif birthday =='октябрь' and date>=23 or birthday=='ноябрь' and date<=21:#даты скорпионов
    print("поздравляем!вы-Скорпион!!!")
  elif birthday =='ноябрь' and date>=22 or birthday=='декабрь' and date<=21:#даты Стрельцов
    print("поздравляем!вы-Стрелец!!!")
  elif birthday =='декабрь' and date>=21 or birthday=='январь' and date<=19:#даты козерогов
    print("поздравляем!вы-Козерог!!!")
  elif birthday =='январь' and date>=20 or birthday=='февраль' and date<=18:#даты водолеев
    print("поздравляем!вы-Водолей!!!")
  elif birthday =='февраль' and date>=19 or birthday=='март' and date<=20:#даты рыб
    print("поздравляем!вы-Рыбы!!!")
  else:
    print("вы неправильно ввели дату и месяц рождения")


result = get_zodiac('март',28)
print(result)