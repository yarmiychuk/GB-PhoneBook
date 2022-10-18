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
    if len(contacts) == 0:
        print('Список контактов пуст')
    else:
        [print(contact) for contact in contacts]
    print()

def show_contact(contact: list):
    if (contact == None):
        print('Нет контакта для отображения\n')
    else:
        print(f'{contact}\n')

def find_contact():
    name = input('Введите имя контакта для поиска: ')
    return name

def show_read_result(contacts: list):
    if len(contacts) == 0:
        print('Файл прочитан, записей контактов не содержит\n')
    else:
        print('Файл прочитан, содержит записи:')
        show_contacts(contacts)

def show_write_result(result: bool):
    if result:
        print('Контакты успешно сохранены в файл\n')
    else:
        print('Ошибка сохрания\n')

def show_add_result(contact: list):
    print(f'Новая запись добавлена:\n{contact}\n')

def show_edit_result(contact: list):
    if contact == None:
        print('Для редактирования контакта воспользуйтесь поиском\n')
    else:
        print(f'Запись отредактирована:\n{contact}\n')

def show_delete_result(result: bool):
    if result:
        print('Контакт удален\n')
    else:
        print('Выберите контакт для удаления, воспользовавшись поиском\n')