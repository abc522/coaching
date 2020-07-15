import tkinter
from tkinter import *
from tkinter.ttk import *
import os
import sqlite3

conn=sqlite3.connect('My.project12.db')
window=Tk()
window.title("ACCOUNT LOGIN")
window.geometry('550x300')

#window.configure(background="orange")
#window.configure(highlightbackground="#d9d9d9")
#window.configure(highlightcolor="black")

global txt5
global txt6
global txt7
global txt8
global txt9
global txt10
global txt11
global txt12
global txt13
global txt14
global txt15
global txt16
global txt17
global txt18
global txt19
global txt20
global txt21
global txt22
global txt23
global txt24
global txt25
global txt26
global txt27
global txt28
global txt29

global combo1
global combo2
global combo3
global combo4
global combo5
global combo6

def clicked():
    window = Tk()
    window.geometry('550x300')
    window.title("HOME PAGE")

    root_menu = tkinter.Menu(window)
    window.config(menu=root_menu)

    def funcreg():
        conn = sqlite3.connect('My.project5.db')
        window = Tk()
        window.title("REGISTRATION FORM")
        window.geometry('550x300')

        print("opened database connectivity")

        # conn.execute('''CREATE TABLE EMPDATA1
        # (ID INT PRIMARY KEY,
        # NAME TEXT NOT NULL,
        # EMAIL CHAR[50] NOT NULL,
        # ADDRESS CHAR[50] NOT NULL,
        # GENDER CHAR[50] NOT NULL,
        # QUALIFICATION CHAR[50] NOT NULL,
        # CITY TEXT NOT NULL,
        # STATE TEXT NOT NULL);''')

        print("TABLE CREATED SUCCESSFULLY")

        name = StringVar()
        email = StringVar()
        address = StringVar()
        gender = StringVar()
        qualification = StringVar()
        city = StringVar()
        state = StringVar()

        global txt1
        global txt2
        global txt3
        global txt4

        lb1 = Label(window, text="ID")
        lb1.grid(column=0, row=0)
        lb2 = Label(window, text="NAME")
        lb2.grid(column=0, row=1)
        lb3 = Label(window, text="EMAIL")
        lb3.grid(column=0, row=2)
        lb4 = Label(window, text="ADDRESS")
        lb4.grid(column=0, row=3)
        lb5 = Label(window, text="GENDER")
        lb5.grid(column=0, row=4)
        lb6 = Label(window, text="QUALIFICATION")
        lb6.grid(column=0, row=5)
        lb7 = Label(window, text="CITY")
        lb7.grid(column=0, row=6)
        lb8 = Label(window, text="STATE")
        lb8.grid(column=0, row=7)

        txt1=StringVar()

        txt1 = Entry(window, width=30)
        txt1.grid(column=1, row=0)
        txt2 = Entry(window, width=30, textvariable=name)
        txt2.grid(column=1, row=1)
        txt3 = Entry(window, width=30, textvariable=email)
        txt3.grid(column=1, row=2)
        txt4 = Entry(window, width=30, textvariable=address)
        txt4.grid(column=1, row=3)

        combo1 = Combobox(window, textvariable=city)
        combo1['values'] = (
            "Amaravati ", "Itanagar", "Dispur", "Patna", "Raipur", "Panaji", "Gandhinagar", "Chandigarh", "Shimla",
            "Srinagar",
            "Ranchi", "Bengaluru", "Thiruvananthapuram", "Bhopal", "Mumbai", "Imphal", "Shillong", "Aizawl", "Kohima",
            "Bhubaneswar", "Chandigarh", "Jaipur", "Gangtok", "Chennai", "Telangana", "Hyderabad", "Lucknow",
            "Dehradun",
            "Kolkata")
        combo1.current(0)
        combo1.grid(column=1, row=6)
        combo2 = Combobox(window, textvariable=state)
        combo2['values'] = (
            "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana",
            "Himachal Pradesh", "Jharkhand", "JAMMU & KASHMIR", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra",
            "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu",
            "Telangana",
            "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal")
        combo2.current(0)
        combo2.grid(column=1, row=7)
        combo3 = Combobox(window, textvariable=qualification)
        combo3['values'] = ("SSC", "HSC", "GRADUATE", "POST GRADUATE")
        combo3.current(0)
        combo3.grid(column=1, row=5)
        combo4 = Combobox(window, textvariable=gender)
        combo4['values'] = ("MALE", "FEMALE")
        combo4.current(0)
        combo4.grid(column=1, row=4)

        global res1
        global res2
        global res3

        res1 = txt1.get()
        res2 = txt2.get()
        res3 = txt3.get()

        def clicked1():
            print(txt1.get())
            print(txt2.get())
            print(txt3.get())
            print(txt4.get())
            print(combo4.get())
            print(combo3.get())
            print(combo1.get())
            print(combo2.get())
            conn.execute("INSERT INTO EMPDATA1 VALUES (" + txt1.get() + ",'" + txt2.get() + "','" + txt3.get() + "','" + txt4.get() + "' ,'" + combo4.get() + "','" + combo3.get() + "', '" + combo1.get() + "','" + combo2.get() + "');")

        btn = Button(window, text="SUBMIT", command=clicked1)
        btn.grid(column=1, row=8)

        window.mainloop()
        conn.commit()
        conn.close()

    def funcsel():
        conn = sqlite3.connect('My.project13.db')
        window = Tk()
        window.title("COURSES SELECTION")
        window.geometry('550x300')

        print("opened database connectivity")

        #conn.execute('''CREATE TABLE TBLCRS1
        #(ID INT PRIMARY KEY,
        #COURSENAME CHAR[50] NOT NULL,
        #COURSESUBJECT CHAR[50] NOT NULL);''')

        print("TABLE CREATED SUCCESSFULLY")

        coursename = StringVar()
        coursesubject = StringVar()

        global res4
        global res5

        lb1 = Label(window, text="ID")
        lb1.grid(column=0, row=0)
        lb2 = Label(window, text="COURSENAME")
        lb2.grid(column=0, row=1)
        lb3 = Label(window, text="COURSESUBJECT")
        lb3.grid(column=0, row=2)

        txt5 = Entry(window, width=30, textvariable=id)
        txt5.grid(column=1, row=0)
        combo5 = Combobox(window, textvariable=coursename)
        combo5['values'] = ("JAVA", "HTML", "PYTHON", "DATABASE", "CLOUD COMPUTING", ".NET")
        combo5.current(0)
        combo5.grid(column=1, row=1)
        combo6 = Combobox(window, textvariable=coursesubject)
        combo6['values'] = ("CORE JAVA", "ADVANCED JAVA", "HTML5", "PYTHON3", "AWS", "AZURE", "ASP.NET")
        combo6.current(0)
        combo6.grid(column=1, row=2)

        res4 = combo5.get()
        res5 = combo6.get()

        def clicked2():
            print(combo5.get())
            print(combo6.get())
            conn.execute("INSERT INTO TBLCRS1 VALUES (" + txt5.get() +" , '" + combo5.get() + "','" + combo6.get() + "');")

        btn = Button(window, text="SUBMIT", command=clicked2)
        btn.grid(column=1, row=3)

        window.mainloop()
        conn.commit()
        conn.close()

    def changepass():
        conn = sqlite3.connect('My.project12.db')
        window = Tk()
        window.title("CHANGE PASSWORD FORM")
        window.geometry('550x300')

        # conn.execute('''CREATE TABLE TBLREG
        # (USERNAME CHAR[50] PRIMARY KEY,
        # PASSWORD CHAR[50] NOT NULL,
        # NEW PASSWORD CHAR[50] NOT NULL);''')

        username = StringVar()
        password = StringVar()

        lb1 = Label(window, text="USERNAME")
        lb1.grid(column=0, row=0)
        lb2 = Label(window, text="OLD PASSWORD")
        lb2.grid(column=0, row=1)
        lb2 = Label(window, text="NEW PASSWORD")
        lb2.grid(column=0, row=2)

        txt6 = Entry(window, width=30)
        txt6.grid(column=1, row=0)
        txt7 = Entry(window, width=30)
        txt7.grid(column=1, row=1)
        txt8 = Entry(window, width=30)
        txt8.grid(column=1, row=2)

        def clicked3():
            conn.execute(
                "INSERT INTO TBLCHGPASS VALUES ('" + txt6.get() + "' , '" + txt7.get() + "', '" + txt8.get() + "');")

        btn = Button(window, text="SUBMIT", command=clicked3)
        btn.grid(column=1, row=3)

        window.mainloop()
        conn.commit()
        conn.close()

    def funcrate():
        conn = sqlite3.connect('My.project5.db')
        window = Tk()
        window.title("TRANSACTION FORM")
        window.geometry('550x300')

        #conn.execute('''CREATE TABLE TBLTRAN2
        #(FEES INT NOT NULL,
        #DISCOUNT INT NOT NULL,
        #NET FEES INT NOT NULL);''')

        global res6
        global res7
        global res8

        lb1 = Label(window, text="FEES")
        lb1.grid(column=0, row=0)
        lb2 = Label(window, text="DISCOUNT")
        lb2.grid(column=0, row=1)
        lb3 = Label(window, text="NET FEES")
        lb3.grid(column=0, row=3)

        txt9 = Entry(window, width=30)
        txt9.grid(column=1, row=0)
        txt10 = Entry(window, width=30)
        txt10.grid(column=1, row=1)
        txt11 = Entry(window, width=30)
        txt11.grid(column=1, row=3)

        res6=txt9.get()
        res7=txt10.get()
        res8=txt11.get()

        def calc():
            print(txt9.get())
            print(txt10.get())
            print(txt11.get())
            res = int(txt9.get()) - int(txt10.get())
            txt11.insert(INSERT, res)

        def clicked4():
            conn.execute("INSERT INTO TBLTRAN2 VALUES (" + txt9.get() + " , " + txt10.get() + ", " + txt11.get() + ");")

        btn = Button(window, text="CALCULATE", command=calc)
        btn.grid(column=1, row=2)

        btn = Button(window, text="SUBMIT", command=clicked4)
        btn.grid(column=1, row=4)

        window.mainloop()
        conn.commit()
        conn.close()

    utility_menu = tkinter.Menu(root_menu)
    root_menu.add_cascade(label="UTILITY", menu=utility_menu)
    utility_menu.add_cascade(label="CHANGE PASSWORRD", command=changepass)
    utility_menu.add_cascade(label="CALCULATION", command=funcrate)
    utility_menu.add_separator()
    utility_menu.add_cascade(label="EXIT", command=window.quit)

    master_menu = tkinter.Menu(root_menu)
    root_menu.add_cascade(label="MASTER", menu=master_menu)
    master_menu.add_cascade(label="REGISTRATION", command=funcreg)
    master_menu.add_cascade(label="COURSES", command=funcsel)

    def functran():
        conn = sqlite3.connect('My.project5.db')
        window = Tk()
        window.title("TRANSACTION FORM")
        window.geometry('550x300')

        # conn.execute('''CREATE TABLE EMPDATA1
        # (FEES INT NOT NULL,
        # DISCOUNT INT NOT NULL,
        # NET FEES INT NOT NULL);''')

        lb0 = Label(window, text="GET")
        lb0.grid(column=0, row=0)
        lb1 = Label(window, text="ID")
        lb1.grid(column=0, row=1)
        lb2 = Label(window, text="NAME")
        lb2.grid(column=0, row=2)
        lb3 = Label(window, text="EMAIL")
        lb3.grid(column=0, row=3)
        lb4 = Label(window, text="COURSENAME")
        lb4.grid(column=0, row=4)
        lb5 = Label(window, text="COURSESUBJECT")
        lb5.grid(column=0, row=5)
        lb6 = Label(window, text="FEES")
        lb6.grid(column=0, row=6)
        lb7 = Label(window, text="DISCOUNT")
        lb7.grid(column=0, row=7)
        lb8 = Label(window, text="NET FEES")
        lb8.grid(column=0, row=8)

        txt12 = Entry(window, width=30)
        txt12.grid(column=1, row=1)
        txt13 = Entry(window, width=30)
        txt13.grid(column=1, row=2)
        txt14 = Entry(window, width=30)
        txt14.grid(column=1, row=3)
        txt15 = Entry(window, width=30)
        txt15.grid(column=1, row=4)
        txt16 = Entry(window, width=30)
        txt16.grid(column=1, row=5)
        txt17 = Entry(window, width=30)
        txt17.grid(column=1, row=6)
        txt18 = Entry(window, width=30)
        txt18.grid(column=1, row=7)
        txt19 = Entry(window, width=30)
        txt19.grid(column=1, row=8)


        def pay():
            window = Tk()
            window.title("PAYMENT GATEWAY")
            window.geometry('550x300')

            def funcmon():
                global login_success_screen
                login_success_screen = Toplevel(window)
                login_success_screen.title("PAYMENT SUCCESSFUL")
                login_success_screen.geometry("150x100")
                Label(login_success_screen, text="VISIT AGAIN").pack()
                Button(login_success_screen, text="THANK YOU", command=delete_funcmon).pack()

            def delete_funcmon():
                login_success_screen.destroy()

            def funcnet():
                window = Tk()
                window.title("NET BANKING")
                window.geometry('350x350')

                lb = Label(window)
                lb.grid(column=0, row=0)
                lb1 = Label(window, text="NAME")
                lb1.grid(column=0, row=1)
                lb = Label(window)
                lb.grid(column=0, row=2)
                lb2 = Label(window, text="BANK NAME")
                lb2.grid(column=0, row=3)
                lb = Label(window)
                lb.grid(column=0, row=4)
                lb3 = Label(window, text="ACCOUNT NO.")
                lb3.grid(column=0, row=5)
                lb = Label(window)
                lb.grid(column=0, row=6)
                lb4 = Label(window, text="IFSC NO.")
                lb4.grid(column=0, row=7)
                lb = Label(window)
                lb.grid(column=0, row=8)
                lb5 = Label(window, text="AMOUNT PAID")
                lb5.grid(column=0, row=9)

                lb = Label(window)
                lb.grid(column=1, row=0)
                txt20 = Entry(window, width=30)
                txt20.grid(column=1, row=1)
                lb = Label(window)
                lb.grid(column=1, row=2)
                txt21 = Entry(window, width=30)
                txt21.grid(column=1, row=3)
                lb = Label(window)
                lb.grid(column=1, row=4)
                txt22 = Entry(window, width=30)
                txt22.grid(column=1, row=5)
                lb = Label(window)
                lb.grid(column=1, row=6)
                txt23 = Entry(window, width=30)
                txt23.grid(column=1, row=7)
                lb = Label(window)
                lb.grid(column=1, row=8)
                txt24 = Entry(window, width=30)
                txt24.grid(column=1, row=9)

                lb = Label(window)
                lb.grid(column=1, row=10)
                btn2 = Button(window, text="TRANSFER", command=funcmon)
                btn2.grid(column=1, row=11)

                window.mainloop()

            def funcdeb():
                window = Tk()
                window.title("DEBIT CARD")
                window.geometry('550x300')

                lb = Label(window)
                lb.grid(column=0, row=0)
                lb1 = Label(window, text="NAME")
                lb1.grid(column=0, row=1)
                lb = Label(window)
                lb.grid(column=0, row=2)
                lb2 = Label(window, text="BANK NAME")
                lb2.grid(column=0, row=3)
                lb = Label(window)
                lb.grid(column=0, row=4)
                lb3 = Label(window, text="CARD NO.")
                lb3.grid(column=0, row=5)
                lb = Label(window)
                lb.grid(column=0, row=6)
                lb4 = Label(window, text="CVV NO.")
                lb4.grid(column=0, row=7)
                lb = Label(window)
                lb.grid(column=0, row=8)
                lb5 = Label(window, text="AMOUNT PAID")
                lb5.grid(column=0, row=9)

                lb = Label(window)
                lb.grid(column=1, row=0)
                txt25 = Entry(window, width=30)
                txt25.grid(column=1, row=1)
                lb = Label(window)
                lb.grid(column=1, row=2)
                txt26 = Entry(window, width=30)
                txt26.grid(column=1, row=3)
                lb = Label(window)
                lb.grid(column=1, row=4)
                txt27 = Entry(window, width=30)
                txt27.grid(column=1, row=5)
                lb = Label(window)
                lb.grid(column=1, row=6)
                txt28 = Entry(window, width=30)
                txt28.grid(column=1, row=7)
                lb = Label(window)
                lb.grid(column=1, row=8)
                txt29 = Entry(window, width=30)
                txt29.grid(column=1, row=9)

                lb = Label(window)
                lb.grid(column=1, row=10)
                btn2 = Button(window, text="TRANSFER", command=funcmon)
                btn2.grid(column=1, row=11)

                window.mainloop()

            lb = Label(window)
            lb.pack()
            btn1 = Button(window, text="NET BANKING", command=funcnet)
            btn1.pack()
            lb = Label(window)
            lb.pack()
            btn2 = Button(window, text="DEBIT CARD", command=funcdeb)
            btn2.pack()

            window.mainloop()

        def detail():
            txt12.insert(INSERT, res1)
            txt13.insert(INSERT, res2)
            txt14.insert(INSERT, res3)
            txt15.insert(INSERT, res4)
            txt16.insert(INSERT, res5)
            txt17.insert(INSERT, res6)
            txt18.insert(INSERT, res7)
            txt19.insert(INSERT, res8)

        btn = Button(window, text="DETAILS", command=detail)
        btn.grid(column=1, row=0)
        btn = Button(window, text="PAY", command=pay)
        btn.grid(column=1, row=9)

        window.mainloop()
        conn.commit()
        conn.close()
    transaction_menu = tkinter.Menu(root_menu)
    root_menu.add_cascade(label="TRANSACTION", menu=transaction_menu)
    transaction_menu.add_cascade(label="TRANSACTION", command=functran)

    window.mainloop()

def signup():
    global register_screen
    register_screen = Toplevel(window)
    register_screen.title("Register")
    window.geometry('550x300')

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Please enter details below").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register",command = register_user).pack()

def login():
    global login_screen
    login_screen = Toplevel(window)
    login_screen.title("Login")
    window.geometry('550x300')
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", command = login_verify).pack()

# Implementing event on register button

def register_user():

    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(register_screen, text="Registration Success").pack()

# Implementing event on login button

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()

        else:
            password_not_recognised()

    else:
        user_not_found()


def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=clicked).pack()


# Designing popup for login invalid password

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()


# Designing popup for user not found

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()


# Deleting popups

def delete_login_success():
    login_success_screen.destroy()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()





lb = Label(window)
lb.pack()
btn1=Button(window,text="LOGIN",command=login)
btn1.pack()
lb = Label(window)
lb.pack()
btn2=Button(window,text="SIGN UP",command=signup)
btn2.pack()


window.mainloop()
conn.commit()
conn.close()
