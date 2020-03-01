from sys import argv

script_name, hour, money_time, prize = argv
hour=int(hour)
money_time=int(money_time)
prize=int(prize)
print('зарплата равна ',hour*money_time+prize)
