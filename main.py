immutable_var = (['Каждый','охотник'], 3, 4, True)
print("Незменяемый объект 'Кортеж':", immutable_var)
print(type(immutable_var))
#  попытка изменить элемент кортежа, например:
#       immutable_var[2] = 8
#  выдаст ошибку, т.к кортеж не поддерживает обращение по элементам.
print('Кортеж (tuple) не поддерживает обращение по элементам\n')
mutable_list = ['желает', 'знать', 7, 8, False]
print("Изменяемый объект 'Список':", mutable_list)
print(type(mutable_list))
mutable_list[0]='умеет'
mutable_list[1]='стрелять'
mutable_list[4]='NULL'
print("Измененный Список:", mutable_list)