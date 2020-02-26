def person_info(name, secondName, year, city, email, tel ):
    text = 'Ввведненые данные: '+ name+' '+secondName +' родился в '+year+' и проживает в городе '+city+'. Email: '+email+', телефон '+tel
    return text

print(person_info(name=input('Введите имя: '),secondName=input('Введите Фамилию: '), year=input('Год Рождения: '),
                  city=input('Город проживания: '), email=input('e-mail: '), tel=input('Телефон: ')))
