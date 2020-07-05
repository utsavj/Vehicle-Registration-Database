from tkinter import *
import sqlite3
    
def Print():
    conn = sqlite3.connect('Form.db')
    with conn:
        cursor=conn.cursor()
    cursor = conn.execute("SELECT Fullname, Regnum, carnum, state, city, carmodel FROM car")
    print("Registered Car Details:")
    for value in cursor:
        print()
        print("Name: "+str(value[0]))
        print("Registration no.: "+value[1])
        print("Car no.: "+value[2])
        print("State: "+value[3])
        print("City: "+value[4])
        print("Car Model: "+value[5])
        print()


def database():
    name1=Fullname.get()
    regnum=Regnum.get()
    carnum=var.get()
    state=c.get()
    city=var1.get()
    carmodel=Carmodel.get()
    conn = sqlite3.connect('Form.db')
    with conn:
        cursor=conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS car (Fullname TEXT,Regnum TEXT,carnum TEXT,state TEXT,city TEXT, carmodel TEXT)')
    cursor.execute('INSERT INTO car (FullName,Regnum,carnum,state,city,carmodel) VALUES(?,?,?,?,?,?)',(name1,regnum,carnum,state,city,carmodel))
    conn.commit()

def databasedel():
    regn=registrationnum.get()
    conn = sqlite3.connect('Form.db')
    with conn:
        cursor=conn.cursor()
    cursor.execute('DELETE FROM car WHERE Regnum =?',(regn,))
    conn.commit()

def databasesearch():
    regn=regnums.get()
    conn = sqlite3.connect('Form.db')
    with conn:
        cursor=conn.cursor()
    cursor.execute('SELECT Fullname, Regnum, carnum, state, city, carmodel FROM car WHERE Regnum =?',(regn,))
    for value in cursor:
        print("Details for the searched entry:")
        print()
        print("Name:"+str(value[0]))
        print("Registration no.: "+value[1])
        print("Car no.: "+value[2])
        print("State: "+value[3])
        print("City: "+value[4])
        print("Car Model: "+value[5])
        print()

def databaseupdate():
    regn=regnums.get()
    fname=fullnamen.get()
    st=staten.get()
    ct=cityn.get()
    conn = sqlite3.connect('Form.db')
    with conn:
        cursor=conn.cursor()
    cursor.execute('UPDATE car SET Fullname=?, state=?, city=? WHERE Regnum =?',(fname,st,ct,regn))
    conn.commit()
    
    
def About():
    root=Toplevel()
    root.geometry("550x360")
    root.configure(bg="red")

    head = Label(root, text='      Vehicle Registration Form      ', font=("Arial", 15), bg="#90d2d8")
    head.grid(row=2,column=0,padx=10, pady=10)

    name1 = Label(root, text="This code helps the user to enter the details required for registering", font=("Arial", 12,),fg="white" ,bg="blue")
    name1.grid(row=3,column=0,padx=10, pady=10,columnspan="3")

    name2 = Label(root, text="     the vehicle. It has other options which enables the user to", font=("Arial", 12),fg="white", bg="blue")
    name2.grid(row=4,column=0,padx=10, pady=10)

    name3 = Label(root, text="  Delete, Update, Search and Print the entries stored in the database.", font=("Arial", 12),fg="white", bg="blue")
    name3.grid(row=5,column=0,padx=10, pady=10)

    name4 = Label(root, text="     User can use the Options menu and select the required option.", font=("Arial", 12),fg="white", bg="blue")
    name4.grid(row=6,column=0,padx=10, pady=10)
        
    root.mainloop()
def Insert():
    root=Toplevel()
    root.geometry("550x360")
    root.configure(bg="red")
    
    label_0 = Label(root, text="Registration form",width=20,font=("bold", 20))
    label_0.grid(row=2,column=0,padx=10, pady=10)


    label_1 = Label(root, text="FullName",width=20,font=("bold", 10))
    label_1.grid(row=5,column=0,padx=10, pady=10)

    entry_1 = Entry(root,textvar=Fullname)
    entry_1.grid(row=5,column=1,padx=10, pady=10)

    label_2 = Label(root, text="Registration Number",width=20,font=("bold", 10))
    label_2.grid(row=6,column=0,padx=10, pady=10)

    entry_2 = Entry(root,textvar=Regnum)
    entry_2.grid(row=6,column=1,padx=10, pady=10)

    label_3 = Label(root, text="Car Number",width=20,font=("bold", 10))
    label_3.grid(row=7,column=0,padx=10, pady=10)

    entry_3= Entry(root,textvar=var)
    entry_3.grid(row=7,column=1,padx=10, pady=10)

    label_4 = Label(root, text="state",width=20,font=("bold", 10))
    label_4.grid(row=8,column=0,padx=10, pady=10)

    list1 = ['Maharashtra','Punjab','Haryana','Karnataka','West Bengal','Tamil Nadu'];

    droplist=OptionMenu(root,c, *list1)
    droplist.config(width=15)
    c.set('select your state') 
    droplist.grid(row=8,column=1,padx=10, pady=10)

    label_6 = Label(root, text="City",width=20,font=("bold", 10))
    label_6.grid(row=9,column=0,padx=10, pady=10)

    entry_6= Entry(root,text=var1)
    entry_6.grid(row=9,column=1,padx=10, pady=10)

    label_5 = Label(root, text="Car Model",width=20,font=("bold", 10))
    label_5.grid(row=10,column=0,padx=10, pady=10)

    entry_5= Entry(root,text=Carmodel)
    entry_5.grid(row=10,column=1,padx=10, pady=10)

    Button(root, text='Submit',width=20,bg='brown',fg='white',command=database).grid(row=11,column=1,padx=10, pady=10)
    root.mainloop()

def Delete():
    root=Toplevel()
    root.geometry("550x360")
    root.configure(bg="red")
    
    label_0 = Label(root, text="Delete an entry",width=20,font=("bold", 20))
    label_0.grid(row=2,column=0,padx=10, pady=10)


    label_1 = Label(root, text="Registration number",width=20,font=("bold", 10))
    label_1.grid(row=3,column=0,padx=10, pady=10)

    entry_1 = Entry(root,textvar=registrationnum)
    entry_1.grid(row=3,column=1,padx=10, pady=10)

    Button(root, text='Delete',width=20,bg='brown',fg='white',command=databasedel).grid(row=4,column=1,padx=10, pady=10)

    root.mainloop()

def Search():
    root=Toplevel()
    root.geometry("550x360")
    root.configure(bg="red")
    label_0 = Label(root, text="Search an entry",width=20,font=("bold", 20))
    label_0.grid(row=2,column=0,padx=10, pady=10)


    label_1 = Label(root, text="Registration number",width=20,font=("bold", 10))
    label_1.grid(row=3,column=0,padx=10, pady=10)

    entry_1 = Entry(root,textvar=regnums)
    entry_1.grid(row=3,column=1,padx=10, pady=10)

    Button(root, text='Search',width=20,bg='brown',fg='white',command=databasesearch).grid(row=4,column=1,padx=10, pady=10)

    root.mainloop()

def Update():
    root=Toplevel()
    root.geometry("550x360")
    root.configure(bg="red")
    
    label_0 = Label(root, text="Update/Change an entry",width=20,font=("bold", 20))
    label_0.grid(row=2,column=0,padx=10, pady=10)

    label_7 = Label(root, text="Enter registration number for which you want to update the database",font=("bold", 8))
    label_7.grid(row=3,column=0,padx=10, pady=10)

    label_1 = Label(root, text="Registration number:",width=20,font=("bold", 10))
    label_1.grid(row=4,column=0,padx=10, pady=10)

    entry_1 = Entry(root,textvar=regnums)
    entry_1.grid(row=4,column=1,padx=10, pady=10)

    label_2 = Label(root, text="FullName",width=20,font=("bold", 10))
    label_2.grid(row=5,column=0,padx=10, pady=10)

    entry_2 = Entry(root,textvar=fullnamen)
    entry_2.grid(row=5,column=1,padx=10, pady=10)

    label_4 = Label(root, text="state",width=20,font=("bold", 10))
    label_4.grid(row=6,column=0,padx=10, pady=10)

    list1 = ['Maharashtra','Punjab','Haryana','Karnataka','West Bengal','Tamil Nadu'];

    droplist=OptionMenu(root,staten, *list1)
    droplist.config(width=15)
    c.set('select your state') 
    droplist.grid(row=6,column=1,padx=10, pady=10)

    label_5 = Label(root, text="City",width=20,font=("bold", 10))
    label_5.grid(row=7,column=0,padx=10, pady=10)

    entry_5= Entry(root,text=cityn)
    entry_5.grid(row=7,column=1,padx=10, pady=10)

    Button(root, text='Update',width=20,bg='brown',fg='white',command=databaseupdate).grid(row=8,column=1,padx=10, pady=10)

    root.mainloop()
    
root = Tk()

menu = Menu(root)
root.geometry('550x360')

Fullname=StringVar()
Regnum=StringVar()
var = StringVar()
c=StringVar()
var1=StringVar()
Carmodel=StringVar()
registrationnum=StringVar()
regnums=StringVar()
fullnamen=StringVar()
cityn=StringVar()
staten=StringVar()


root.config(menu=menu)
filemenu = Menu(menu,tearoff=0)
menu.add_cascade(label="Home", menu=filemenu)
filemenu.add_command(label="About", command=About)

optionsmenu=Menu(menu,tearoff=0)
menu.add_cascade(label="Options", menu=optionsmenu)
optionsmenu.add_command(label="Insert", command=Insert)
optionsmenu.add_command(label="Delete", command=Delete)
optionsmenu.add_command(label="Update", command=Update)
optionsmenu.add_command(label="Search", command=Search)
optionsmenu.add_command(label="Print All", command=Print)






fm = Canvas(root, width = 550, height = 360, bg="red")


head = Label(root, text='      Vehicle Registration Form      ', font=("Arial", 15), bg="#90d2d8")
head.place(x=0,y=10)

name1 = Label(root, text="Utsav Jariwala B258", font=("Arial", 12,),fg="white" ,bg="blue")
name1.place(x=10,y=50)



fm.pack()


mainloop() 
