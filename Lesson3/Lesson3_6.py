def int_func (s):
    return s.title()

print(int_func('text'))

t=''
for i in int_func('text1 text2 text3').split():
    t += i + ' '
print(t)