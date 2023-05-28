def creating ():
    file = 'Phonebook.txt'
    with open (file, 'w', encoding = 'utf-8') as data:
        data.write(f'Фамилия;Имя;Телефон;Описание\n')

