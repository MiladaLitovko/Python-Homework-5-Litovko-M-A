'''
Создайте программу для игры в ""Крестики-нолики"".

Пример интерфейса:

   |   | 0
-----------    
   |   |
-----------
   | X |
Ввод можно реализовать через введение двух чисел (номеров строки и столбца).
'''

array = [['1' ,'|', '2' ,'|', '3'], ['-','-','-','-','-'],['4' ,'|', '5' ,'|', '6'], ['-','-','-','-','-'],['7' ,'|', '8' ,'|', '9'] ]
player1 = 'O'
player2 = 'X'

def print_desk():
    for i in array: 
        print(' '.join(list(map(str, i))))

def motion(player):
    number = str(input(f'Введите число, на которое нужно поставить {player}: '))
    flag = False
    for i in range(len(array)):
        for k in range(len(array)):
            if array[i][k] == number:
                array[i][k] = player
                flag = True
    print_desk()
    return flag

def itogi():
    is_num_in_desk = False
    for i in range(len(array)):
        for k in range(len(array)):
            if array[i][k] in str(range(1,10)):
                is_num_in_desk = True
    return is_num_in_desk

print_desk() 


current_player = player1
while itogi():
    if motion(current_player):
        if current_player == player1:
            current_player = player2
        else:
            current_player = player1
    else:
        print(f'Неверное число, игрок {current_player} вводит число заново')



