import time

class TrafficLight:
    __color = ('green', 'yellow', 'red')

    def running (self):
        n='Y'
        while n == 'Y':
            for i in self.__color:
                if i=='green':
                    print('\033[32m'+ i.upper())
                    time.sleep(7)
                elif i=='yellow':
                    print('\033[33m'+ i.upper())
                    time.sleep(2)
                elif i == 'red':
                    print('\033[31m' + i.upper())
                    time.sleep(5)
            print('\33[37m','\n'*50)
            n = input('Продолжить? Y/N ').upper()

t = TrafficLight()
t.running()

