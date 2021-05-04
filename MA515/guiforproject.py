from tkinter import *
from tkinter.ttk import *
import mysql.connector
from mysql.connector import errorcode

passwords = [('gnas','uw4life')]
seller_ids = {('gnas','uw4life'):4}

root = Tk()
root.geometry("300x100")

def open_seller_menu(current_seller_id):
    smenu = Toplevel(root)
    smenu.title("My CardTraders")
    smenu.geometry("500x500")   

    def get_my_buyers(current_seller_id):
        cnx = mysql.connector.connect(host= 'localhost',
                              user='kgal',
                              password='1e4&tFq*',
                              database='cardtraders',
                              auth_plugin='mysql_native_password')
        cursor = cnx.cursor()

        query1 = "SELECT fname, lname, item_name, quantity, a.price FROM buyers as b join orders as o join all_stock as a on o.item_id = a. item_id on b.id_no = o.buyer_id WHERE seller_id = %s;"
        query2 = (current_seller_id, )

        cursor.execute(query1, query2)
    
        i = 1
        for x in cursor:
            for j in range(len(x)):
                e = Label(smenu, width=50, text=x[j])
                e.grid(row = i, column = j)
            i += 1

        cursor.close()
        cnx.close()

    display_buyers = Button(smenu, text = 'Show my buyers.', command = lambda : get_my_buyers(current_seller_id))
    display_stock = Button(smenu, text = 'Show my stock.', command = None)#get_my_buyers(current_seller_id))
    display_info = Button(smenu, text = 'Show my info.', command = None)#get_my_buyers(current_seller_id))
    
    display_buyers.grid(row=0,column=0)
    display_stock.grid(row=0,column=1)
    display_info.grid(row=0,column=2)

name_var = StringVar()
pass_var = StringVar()

def submit():
    name = name_var.get()
    password = pass_var.get()

    print("The name is :" + name)
    print("The password is : " + password)

    name_var.set("")
    pass_var.set("")

    if (name,password) in passwords:
        open_seller_menu(seller_ids[(name,password)])
    else:
        wrong_pass = Toplevel(root)
        wrong_pass.title("Incorrect Username/Password")
        wrong_pass.geometry("300x300")
        label = Label(wrong_pass, text = "The username and/or password you entered is incorrect.")
        label.pack()
        back_to_main = Button(wrong_pass, text = 'Close this window.', command = wrong_pass.destroy)
        back_to_main.pack()

name_label = Label(root, text = 'Username', font = ("Calibri", 10, "bold"))
name_entry = Entry(root, textvariable = name_var, font = ("Calibri", 10, "normal"))

pass_label = Label(root, text = "Password", font = ("Calibri", 10, "bold"))
pass_entry = Entry(root, textvariable = pass_var, font = ("Calibri", 10, "normal"), show = "*")

submit_button = Button(root, text = "Submit", command = submit)

name_label.grid(row = 0, column = 0)
name_entry.grid(row = 0, column = 1)
pass_label.grid(row = 1, column = 0)
pass_entry.grid(row = 1, column = 1)
submit_button.grid(row = 2, column = 1)

mainloop()