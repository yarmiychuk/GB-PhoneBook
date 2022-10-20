from tkinter import END
import view, model, interface

def start():
    interface.start()
    while True:
        command = view.show_menu()
        match command:
            case '1':
                menu1()
            case '2':
                menu2()
            case '3':
                menu3()
            case '4':
                menu4()
            case '5':
                menu5()
            case '6':
                menu6()
            case '7':
                menu7()
            case '0':
                break

def menu1():
    result = model.read_file()
    view.show_read_result(result)
    interface.show_read_result(result)

def menu2():
    view.show_contacts(model.get_contacts())

def menu3():
    view.show_write_result(model.save_file())

def menu4():
    view.show_add_result(model.add_contact())

def menu5():
    view.show_contact(model.find_by_name(view.find_contact()))

def menu6():
    view.show_contact(model.get_current())
    view.show_edit_result(model.edit_contact())

def menu7():
    view.show_delete_result(model.delete_contact())
            
    