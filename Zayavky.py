'''
Завдання 1
Потрібно розробити програму, яка імітує приймання й обробку заявок: програма має автоматично 
генерувати нові заявки (ідентифіковані унікальним номером або іншими даними), додавати їх до 
черги, а потім послідовно видаляти з черги для "обробки", імітуючи таким чином роботу сервісного центру.
'''



from queue import Queue
import random
import time


#Робимо функцію для створення нових заявок і їх додавання в чергу
def generate_request(user_input):
    #Створюємо чергу заявок
    q = Queue()
    for i in range (1, user_input+1):
        difficulties = random.randint(1,10)
        q.put(f'Заявка номер {i} зі складністю {difficulties}')
    print(f'Додані до черги заявки з їхньою складністю: {q.queue}')
    print(f'Кількість доданих до черги заявок: {q.qsize()}')
    return(q)

#Робимо функцію для перевірки черги і її обробки
def process_request(cherga):
    if cherga:
        while not cherga.empty():
            current_request = cherga.get()
            print (f'Обробляється {current_request}')
            timeout = int(current_request.split()[5])
            time.sleep(timeout/5)
    else:
        print('Черга пуста')

#Робимо головний цикл програми, який створює і виконує заявки, поки користувач не вийде з програми
def main():
    while True:
        user_input = input('Введіть ціле число від 1 до 20 або введіть <Exit> для виходу з програми> ')
        if user_input == 'Exit' or user_input == 'exit' or user_input == '<exit>' :
            print('На все добре!')
            break
        user_input = int(user_input)
        if user_input > 0 and user_input < 21:
            cherga = Queue()
            cherga = generate_request(user_input)
            process_request(cherga)
        else:
            print('Invalid command.')


if __name__ == "__main__":
    main()

