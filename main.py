import txt

with open('1.txt', 'w', encoding='utf-8') as f:
    f.write('Строка номер 1 файла номер 1\nСтрока номер 2 файла номер 1')

with open('2.txt', 'w', encoding='utf-8') as f:
    f.write('Строка номер 1 файла номер 2')

with open('Final file', 'a', encoding='utf-8') as f:
    f.write('2.txt\n1\nСтрока номер 1 файла номер 2\n1.txt\n2\nСтрока номер 1 файла номер 1\nСтрока номер 2 файла номер 1')