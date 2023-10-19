# Задание 1

s = input()
a = s.split()

def de_none():
    if 'None' in a:
        a.remove('None')
        print(a)

de_none()

# Задание 2

# a = input('Исходный список: ')
# ref_list = a.split()

# start = input('Числовой номер позиции Start: ')

# num = input('Число: ')

# rep = input('Число повторений: ')

# def list_insert():
#     a = [ref_list]
#     ref_list[int(start):int(start) + int(rep)] = [int(num)]


# list_insert()
# print(ref_list)