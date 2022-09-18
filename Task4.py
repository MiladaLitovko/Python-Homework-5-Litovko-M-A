'''
Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
'''
with open('original_from_Task4.txt') as file:
    original = file.read()

count = 1
arr = ''
for i in range(len(original) - 1):
    if original[i] == original[i + 1]:
        count += 1
    else:
        arr += original[i] + f'{count}' + ' '
        count = 1


new_from_Task4 = open('new_from_Task4.txt','w', encoding='utf-8')
new_from_Task4.write(arr + '' + original[-1] + f'{count}')
new_from_Task4.close()
