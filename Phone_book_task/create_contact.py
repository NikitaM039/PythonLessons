from create_txt import creating
from write_txt import writing_txt

def greeting():
    print("Телефонный справочник!")
def get_info ():
    info = []
    Last_Name = input('Введите фамилию: ')
    info.append(Last_Name)
    Name = input('Введите имя: ')
    info.append(Name)
    phone_number = input('Укажите телефон: ')
    info.append(phone_number)
    Comment = input('Укажите комментарий: ')
    info.append(Comment)
    return [Last_Name, Name, phone_number, Comment]
