#==================================Вишлист============================================
# Разработал: Миргхани Монтасир 15.01.2020
#==================================Вишлист============================================

# %s - Mysql
# ? -> Sqlite

from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
import pymysql

root = Tk()
root.title("Вишлист")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 1280
height = 500
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root.resizable(0, 0)

#==================================METHODS============================================
def Database():
    global conn, cursor
    conn = pymysql.connect(host = '', user = '', password = '', db = '')
    cursor = conn.cursor()

def Create():
    if  TITLE.get() == "" or price.get() == "" or STATUS.get() == "" or LINK.get() == "" or NOTE.get() == "" or CONTACT.get() == "":
        txt_result.config(text="Пожалуйста, заполните обязательные поля!", fg="red")
    else:
        Database()
        #cursor.execute("INSERT INTO `wishlist` (title, price, status, link, note, contact) VALUES(?, ?, ?, ?, ?, ?)",
        cursor.execute("INSERT INTO `wishlist` (title, price, status, link, note, contact) VALUES(%s, %s, %s, %s, %s, %s)",
                       (str(TITLE.get()), str(PRICE.get()), str(STATUS.get()), str(LINK.get()), str(NOTE.get()), str(CONTACT.get())))
        tree.delete(*tree.get_children())
        cursor.execute("SELECT * FROM `wishlist` ORDER BY `price` ASC")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data[0], data[1], data[2], data[3], data[4], data[5], data[6]))
        conn.commit()
        TITLE.set("")
        PRICE.set("")
        STATUS.set("")
        LINK.set("")
        NOTE.set("")
        CONTACT.set("")
        cursor.close()
        conn.close()
        txt_result.config(text="Записи успешно созданы!", fg="green")

def Read():
    tree.delete(*tree.get_children())
    Database()
    cursor.execute("SELECT * FROM `wishlist` ORDER BY `price` ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data[0], data[1], data[2], data[3], data[4], data[5], data[6]))
    cursor.close()
    conn.close()
    txt_result.config(text="Успешно прочитанные данные из базы данных", fg="black")

def Update():
    Database()
    if STATUS.get() == "":
        txt_result.config(text="Пожалуйста, введите пол", fg="red")
    else:
        tree.delete(*tree.get_children())
        cursor.execute("UPDATE `wishlist` SET `title` = %s, `price` = %s, `status` = %s,  `link` = %s,  `note` = %s, `contact` = %s WHERE `prod_id` = %s",
                       (str(TITLE.get()), str(PRICE.get()), str(STATUS.get()), str(LINK.get()), str(NOTE.get()), str(CONTACT.get()), int(prod_id)))
        conn.commit()
        cursor.execute("SELECT * FROM `wishlist` ORDER BY `price` ASC")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data[0], data[1], data[2], data[3], data[4], data[5], data[6]))
        cursor.close()
        conn.close()
        TITLE.set("")
        PRICE.set("")
        STATUS.set("")
        LINK.set("")
        NOTE.set("")
        CONTACT.set("")
        btn_create.config(state=NORMAL)
        btn_read.config(state=NORMAL)
        btn_update.config(state=DISABLED)
        btn_delete.config(state=NORMAL)
        txt_result.config(text="Вишлист успешно обновлен!", fg="black")


def OnSelected(event):
    global prod_id;
    curItem = tree.focus()
    contents =(tree.item(curItem))
    selecteditem = contents['values']
    prod_id = selecteditem[0]
    TITLE.set("")
    PRICE.set("")
    STATUS.set("")
    LINK.set("")
    NOTE.set("")
    CONTACT.set("")
    TITLE.set(selecteditem[1])
    PRICE.set(selecteditem[2])
    STATUS.set(selecteditem[3])
    LINK.set(selecteditem[4])
    NOTE.set(selecteditem[5])
    CONTACT.set(selecteditem[6])
    btn_create.config(state=DISABLED)
    btn_read.config(state=DISABLED)
    btn_update.config(state=NORMAL)
    btn_delete.config(state=DISABLED)

def Delete():
    if not tree.selection():
       txt_result.config(text="Please select an item first", fg="red")
    else:
        result = tkMessageBox.askquestion('Вишлист', 'Вы уверены, что хотите удалить запись?', icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents =(tree.item(curItem))
            selecteditem = contents['values']
            tree.delete(curItem)
            Database()
            cursor.execute("DELETE FROM `wishlist` WHERE `prod_id` = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()
            txt_result.config(text="Запись успешно удалена.", fg="black")


def Exit():
    result = tkMessageBox.askquestion('Вишлист', 'Вы уверены, что хотите выйти?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()

#==================================VARIABLES==========================================
TITLE = StringVar()
PRICE = StringVar()
STATUS = StringVar()
LINK = StringVar()
NOTE = StringVar()
CONTACT = StringVar()

#==================================FRAME==============================================
Top = Frame(root, width=900, height=50, bd=2, relief="raise")
Top.pack(side=TOP)
Left = Frame(root, width=300, height=500, bd=2, relief="raise")
Left.pack(side=LEFT)
Right = Frame(root, width=600, height=500, bd=2, relief="raise")
Right.pack(side=RIGHT)
Forms = Frame(Left, width=300, height=450)
Forms.pack(side=TOP)
Buttons = Frame(Left, width=300, height=100, bd=2, relief="raise")
Buttons.pack(side=BOTTOM)
RadioGroup = Frame(Forms)
Male = Radiobutton(RadioGroup, text="в наличии", variable=STATUS, value="в наличии", font=('arial', 16)).pack(side=LEFT)
Female = Radiobutton(RadioGroup, text="скоро появится", variable=STATUS, value="скоро появится", font=('arial', 16)).pack(side=LEFT)

#==================================LABEL WIDGET=======================================
txt_title = Label(Top, width=900, font=('arial', 24), text = "Вишлист")
txt_title.pack()
txt_title = Label(Forms, text="Название:", font=('arial', 16), bd=15)
txt_title.grid(row=0, sticky="e")
txt_price = Label(Forms, text="Цена:", font=('arial', 16), bd=15)
txt_price.grid(row=1, sticky="e")
txt_status = Label(Forms, text="Статус:", font=('arial', 16), bd=15)
txt_status.grid(row=2, sticky="e")
txt_link = Label(Forms, text="Ссылка на страницу:", font=('arial', 16), bd=15)
txt_link.grid(row=3, sticky="e")
txt_note = Label(Forms, text="Примечание:", font=('arial', 16), bd=15)
txt_note.grid(row=4, sticky="e")
txt_contact = Label(Forms, text="Контакт:", font=('arial', 16), bd=15)
txt_contact.grid(row=5, sticky="e")
txt_result = Label(Buttons)
txt_result.pack(side=TOP)

#==================================ENTRY WIDGET=======================================
title = Entry(Forms, textvariable=TITLE, width=30)
title.grid(row=0, column=1)
price = Entry(Forms, textvariable=PRICE, width=30)
price.grid(row=1, column=1)
RadioGroup.grid(row=2, column=1)
link = Entry(Forms, textvariable=LINK, width=30)
link.grid(row=3, column=1)
note = Entry(Forms, textvariable=NOTE, width=30)
note.grid(row=4, column=1)
contact = Entry(Forms, textvariable=CONTACT, width=30)
contact.grid(row=5, column=1)

#==================================BUTTONS WIDGET=====================================
btn_create = Button(Buttons, width=10, text="Создать", command=Create)
btn_create.pack(side=LEFT)
btn_read = Button(Buttons, width=10, text="Читать", command=Read )
btn_read.pack(side=LEFT)
btn_update = Button(Buttons, width=10, text="Обновить", command=Update, state=DISABLED)
btn_update.pack(side=LEFT)
btn_delete = Button(Buttons, width=10, text="Удалить", command=Delete)
btn_delete.pack(side=LEFT)
btn_exit = Button(Buttons, width=10, text="Выйти", command=Exit)
btn_exit.pack(side=LEFT)

#==================================LIST WIDGET========================================
scrollbary = Scrollbar(Right, orient=VERTICAL)
scrollbarx = Scrollbar(Right, orient=HORIZONTAL)
tree = ttk.Treeview(Right, columns=("ProductID", "Title", "Price", "Status", "Link", "Note", "Contact"), selectmode="extended", height=500, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading('ProductID', text="ProductID", anchor=W)
tree.heading('Title', text="Название", anchor=W)
tree.heading('Price', text="Цена", anchor=W)
tree.heading('Status', text="Статус", anchor=W)
tree.heading('Link', text="Ссылка на страницу", anchor=W)
tree.heading('Note', text="Примечание", anchor=W)
tree.heading('Contact', text="Контакт", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=0)
tree.column('#2', stretch=NO, minwidth=0, width=140)
tree.column('#3', stretch=NO, minwidth=0, width=80)
tree.column('#4', stretch=NO, minwidth=0, width=100)
tree.column('#5', stretch=NO, minwidth=0, width=200)
tree.column('#6', stretch=NO, minwidth=0, width=110)
tree.column('#7', stretch=NO, minwidth=0, width=200)
tree.pack()
tree.bind('<Double-Button-1>', OnSelected)

#==================================INITIALIZATION=====================================
if __name__ == '__main__':
    Read()
    root.mainloop()
