'''
Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

file_from_Task4 = open('file_from_Task4.txt','w')
file_from_Task4.write(result[3:])
file_from_Task4.close()
'''

with open('original_from_Task1.txt', encoding = "utf-8") as file:
    original_text = file.read()

result = " " .join(filter(lambda x: 'абв' not in x, original_text.split()))

new_from_Task1 = open('new_from_Task1.txt','w', encoding='utf-8')
new_from_Task1.write(result)
new_from_Task1.close()