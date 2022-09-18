'''
Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
'''

with open('original_from_Task1.txt', encoding = "utf-8") as file:
    original_text = file.read()

result = " " .join(filter(lambda x: 'абв' not in x, original_text.split()))

new_from_Task1 = open('new_from_Task1.txt','w', encoding='utf-8')
new_from_Task1.write(result)
new_from_Task1.close()