'''
Завдання 2
Необхідно розробити функцію, яка приймає рядок як вхідний параметр, додає всі його 
символи до двосторонньої черги (deque з модуля collections в Python), а потім порівнює 
символи з обох кінців черги, щоб визначити, чи є рядок паліндромом. Програма повинна 
правильно враховувати як рядки з парною, так і з непарною кількістю символів, а також 
бути нечутливою до регістру та пробілів.
'''



from collections import deque


#Зробимо функцію для визначення, чи є вхідний рядок поліндромом
def palindrom(vhidna_stroka):
    if not vhidna_stroka:
        return (-1)

#Приберемо всі символи і пробіли, окрім букв і приведемо всі букви до єдиного регістру
    letter_string = ''.join(a for a in vhidna_stroka if a.isalpha())
    lowercase_string = letter_string.lower()

#Зробимо перевірку отриманої строки на паліндромність і повернемо результат
    string_len = len(lowercase_string)
    q1 = deque(lowercase_string)
    q2 = deque(lowercase_string)
    q2.reverse()
    for i in range (string_len):
        if q1[i] != q2[i]:
            return(0)
    return(1)


#Головний модуль. Введемо декілька строчок для перевірки правильності відпрацьовки нашої функції
def main():
    spysok_strok = ['Кому дикі ріки думок?',
    'Язик до Києва доведе',
    'Усе доведе в Одесу',
    'Madam, Im Adam',
    'Три психи пили Пилипихи спирт.',
    '']
    spysok_len = len(spysok_strok)
    for i in range (0, spysok_len):
        stroka = spysok_strok[i]
        result = palindrom(stroka)
        if  result == 1:
            print (f'Строка {stroka} є паліндромом')
        elif result == 0:
            print (f'Строка {stroka} не є паліндромом')
        else:
            print (f'Строка порожня')
if __name__ == "__main__":
    main()