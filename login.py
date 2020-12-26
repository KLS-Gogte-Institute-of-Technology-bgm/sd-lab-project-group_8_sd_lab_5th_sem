# Login System with Python GUI and MySQL


import mysql.connector as sql

from tkinter import *



win = Tk()

win.geometry("500x500")

win.title("Login Page")


def login() :

    db = sql.connect(host = "localhost", user = "root", passwd = "ksk@mysql")

    cur = db.cursor()


    try :

        cur.execute("use db")

        db = sql.connect(host = "localhost", user = "root", passwd = "ksk@mysql", database = "db")

        cur = db.cursor()


    except sql.errors.DatabaseError:

        db = sql.connect(host = "localhost", user = "root", passwd = "ksk@mysql", database = "db")

        cur = db.cursor()


        try :

            cur.execute("create table user(username varchar(50), NOT NULL, password int NOT NULL)")


        except sql.errors.ProgrammingError:

            pass


    finally :

        try :

            cur.execute("create table user(username varchar(50) NOT NULL, "

                        "password int NOT NULL)")


        except sql.errors.ProgrammingError:

            pass


    while True :


        user = user1.get()

        passwd = passwd1.get()


        cur.execute("select * from user where username = '%s' and password = %s" % (user, passwd))

        rud = cur.fetchall()


        if rud:

            print("Welcome")

            break


        else:

            cur.execute("insert into user values('{}', {})".format(str(user), passwd))

            db.commit()

            print("Account Created")

            break


    cur.close()

    db.close()
  

userlvl = Label(win, text = "Username :")

passwdlvl = Label(win, text = "Password  :")


user1 = Entry(win, textvariable = StringVar())

passwd1 = Entry(win, textvariable = IntVar().set(""))


enter = Button(win, text = "Enter", command = lambda : login(), bd = 0)
#lamda: login()
enter.configure(bg = "pink")


user1.place(x = 200, y = 220)

passwd1.place(x = 200, y = 270)


userlvl.place(x = 130, y = 220)

passwdlvl.place(x = 130, y = 270)


enter.place(x = 238, y = 325)


win.mainloop()




