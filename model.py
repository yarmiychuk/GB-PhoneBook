from asyncio import constants

path = 'phonebook.txt'
contacts = []

def read_file():
    global contacts
    with open(path) as f:
        contacts = [i.strip().split(';') for i in f.readlines()]
    return contacts

def get_contacts():
    global contacts
    return contacts

def add_contact():
    global contacts
    contacts.append([\
        input('Введите id: '),\
        input('Введите Имя: '),\
        input('Введите Телефон: '),\
        input('Введите Комментарий: ')])
    # id = input('Введите id: ')
    # name = input('Введите Имя: ')
    # phone = input('Введите Телефон: ')
    # comment = input('Введите Комментарий: ')
    # contacts.append(';'.join([id, name, phone, comment]))

def save_file():
    global contacts
    with open(path, 'w', encoding='utf_8') as f:
        for contact in contacts:
            f.write(';'.join(contact) + "\n")

