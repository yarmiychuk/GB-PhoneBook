def show_menu():
    question = 'Введите необходимую команду:\
        \n1 - Показать все контакты\
        \n2 - Открыть файл с контактами\
        \n3 - Записать файл с контактами\
        \n4 - Добавить контакт\
        \n5 - Изменить контакт\
        \n6 - Удалить контакт\
        \n7 - Поиск по контактам\
        \n0 - Выход\
        \n'
    command = input(question)
    return command

def show_contacts(contacts: list):
    [print(contact) for contact in contacts]

def show_contact(contact: list):
    print(contact)

def find_contact():
    name = input('Введите имя контакта для поиска: ')
    return name

def show_delete_result(result: bool):
    if result:
        print('Контакт удален')
    else:
        print('Выберите контакт для удаления, воспользовавшись поиском')