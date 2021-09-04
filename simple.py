# a = 2
# b = 0.5
# print(a+b)

# name = 'denis1 '
# print('Privet', name.replace('1','').strip().capitalize())

# v = int(input('Введите число от 1 до 10: '))
# if v<1:
#     print('Ti chto, durak?')
# elif v>10:
#     print('Ti real`no durak')
# else:
#     print(f'{v+10}')

# name = input('Введите ваше имя: ')
# print(f'Privet, {name}! Kak dela?')

# print(float('1'))
# print(int(float('2.5')))
# print(bool(1))
# print(bool(''))
# print(bool(0))

# list = ['3','5','7','9', '10.5']
# print(list)
# list.append('Python')
# print(list)
# print(len(list))

# print(list[0])
# print(list[-1])
# print(list[1:4])
# list.remove('Python')
# print(list)

dict1 =  {'city': 'Moskva', 'temperature': '20'}
print(dict1['city'])
dict1['temperature'] = int(dict1['temperature']) - 5
print(dict1)

print(dict1.get('country'))
print(dict1.get('country', 'Russia'))
dict1['date'] = '27.05.2019'
print(len(dict1))