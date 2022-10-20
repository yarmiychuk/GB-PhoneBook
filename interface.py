from tkinter import *
import controller, model, view

text: Text

def start():
    global text

    root = Tk()

    root['bg'] = '#ffffff'
    root.title('Phone Book')
    root.wm_attributes('-alpha', 1.0)
    root.geometry('400x820')

    root.resizable(width=False, height=False)

    loadimage = PhotoImage(file="./images/button.png")
    loadimage2 = PhotoImage(file="./images/button2.png")
    loadimage3 = PhotoImage(file="./images/button3.png")

    loadimage4 = PhotoImage(file="./images/button4.png")
    loadimage5 = PhotoImage(file="./images/button5.png")
    loadimage6 = PhotoImage(file="./images/button6.png")

    loadimage7 = PhotoImage(file="./images/button7.png")
    loadimage8 = PhotoImage(file="./images/button8.png")
    loadimage9 = PhotoImage(file="./images/button9.png")

    loadimageX = PhotoImage(file="./images/buttonX.png")
    loadimage0 = PhotoImage(file="./images/button0.png")
    loadimageM = PhotoImage(file="./images/buttonM.png")

    label = Label(root)
    label.place(x=30, y=20, width='335', height='340')

    text = Text(root, width=40, bd='3')
    text.place(x=35, y=20)

    btn1 = Button(root, text='1', width = '80', height='80',border='0', bg='#ffffff',  image=loadimage, command=lambda: controller.menu1())
    btn1.place(x=30,y=420)
    btn2 = Button(root, text='2', width = '80', height='80',border='0', bg='#ffffff',  image=loadimage2, command=lambda: controller.menu2())
    btn2.place(x=160,y=420)
    btn3 = Button(root, text='3', width = '80', height='80',border='0', bg='#ffffff',  image=loadimage3, command=lambda: controller.menu3())
    btn3.place(x=290,y=420)

    btn4 = Button(root, text='4', width = '80', height='80',border='0', bg='#ffffff',  image=loadimage4, command=lambda: controller.menu4())
    btn4.place(x=30,y=520)
    btn5 = Button(root, text='5', width = '80', height='80',border='0', bg='#ffffff',  image=loadimage5, command= lambda: controller.menu5())
    btn5.place(x=160,y=520)
    btn6 = Button(root, text='6', width = '80', height='80',border='0', bg='#ffffff',  image=loadimage6, command=lambda: controller.menu6())
    btn6.place(x=290,y=520)

    btn7 = Button(root, text='7', width = '80', height='80',border='0', bg='#ffffff',  image=loadimage7, command=lambda: controller.menu7())
    btn7.place(x=30,y=620)
    btn8 = Button(root, text='8', width = '80', height='80',border='0', bg='#ffffff',  image=loadimage8)
    btn8.place(x=160,y=620)
    btn9 = Button(root, text='9', width = '80', height='80',border='0', bg='#ffffff',  image=loadimage9, command=lambda: text.insert(1.0, 'Some Text'))
    btn9.place(x=290,y=620)

    btnX = Button(root, text='9', width = '80', height='80',border='0', bg='#ffffff',  image=loadimageX, command=lambda: exit())
    btnX.place(x=30,y=720)
    btn0 = Button(root, text='8', width = '80', height='80',border='0', bg='#ffffff',  image=loadimage0)
    btn0.place(x=160,y=720)
    btnM = Button(root, text='9', width = '80', height='80',border='0', bg='#ffffff',  image=loadimageM, command=lambda: view.show_menu())
    btnM.place(x=290,y=720)

    root.mainloop()

def show_read_result(contacts: list):
    global text
    if len(contacts) == 0:
        text.insert(1.0, 'Файл прочитан, записей контактов не содержит')
    else:
        result = 'Файл прочитан, содержит записи:'
        for item in contacts:
            result += '\n' + item[1] + '\n  ' + \
                item[2] + ' (' + item[3] + ')'
        text.delete(1.0, END)
        text.insert(1.0, result)