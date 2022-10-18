import view, model

def start():
    while True:
        command = view.show_menu()
        match command:
            case '1':
                view.show_contacts(model.get_contacts())
            case '2':
                model.read_file()
            case '3':
                model.save_file()
            case '4':
                model.add_contact()
            case '5':
                pass # Изменить контакт
            case '6':
                view.show_delete_result(model.delete_contact())
            case '7':
                view.show_contact(model.find_by_name(view.find_contact()))
            case '0':
                break
            
    