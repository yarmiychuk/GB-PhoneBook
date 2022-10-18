from asyncio import constants

path = 'phonebook.txt'
contacts = []
last_id: str = '0'

def read_file():
    global contacts, last_id
    with open(path) as f:
        contacts = [i.strip().split(';') for i in f.readlines()]
    last_id = '0' if len(contacts) == 0 else contacts[len(contacts) - 1][0]
    return contacts

def get_contacts():
    global contacts
    return contacts

def add_contact():
    global contacts, last_id
    contacts.append([\
        str(int(last_id) + 1),\
        input('Введите Имя: '),\
        input('Введите Телефон: '),\
        input('Введите Комментарий: ')])

def save_file():
    global contacts
    with open(path, 'w', encoding='utf_8') as f:
        for contact in contacts:
            f.write(';'.join(contact) + "\n")

