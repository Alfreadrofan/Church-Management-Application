#import libraries
import email
from logging import root
from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
import sqlite3
from turtle import position
from subprocess import call
import datetime


display_screen = Tk()
#function to define database
def Database():
    global conn, cursor
    #creating contact database
    conn = sqlite3.connect("userdata.db")
    cursor = conn.cursor()
    #creating died table
    cursor.execute('''CREATE TABLE IF NOT EXISTS died(
                    RID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                    name text,
                    house text,
                    location text, 
                    email text, 
                    contact number, 
                    gender text, 
                    country text,
                    dob date,
                    occupation text,
                    joined date,
                    possition text,
                    fname text
                )
            ''')
    #create deleted table
    cursor.execute('''CREATE TABLE IF NOT EXISTS deleted(
                    RID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                    name text,
                    house text,
                    location text, 
                    email text, 
                    contact number, 
                    gender text, 
                    country text,
                    dob date,
                    occupation text,
                    joined date,
                    possition text,
                    fname text
                )
            ''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS status(
                    RID INTEGER PRIMARY KEY NOT NULL,
                    Date timestamp,
                    status text
                )
            ''')
    #cursor.execute(
    #    "CREATE TABLE IF NOT EXISTS REGISTRATION (RID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, FNAME TEXT, LNAME TEXT, GENDER TEXT, ADDRESS TEXT, CONTACT TEXT)")
def home():
    display_screen.destroy()
    call(["python", "hom.py"])
#defining function for creating GUI Layout
def DisplayForm():
    #creating window
    #display_screen = Tk()
    #setting width and height for window
    display_screen.geometry("900x400")
    #setting title for window
    display_screen.title("st_thomas_church")
    global tree
    global SEARCH
    global mail,location,possition,occupation,contact
    SEARCH = StringVar()
    mail = StringVar()
    location = StringVar()
    possition = StringVar()
    occupation = StringVar()
    contact = StringVar()
    #creating frames for layout
    #topview frame for heading
    TopViewForm = Frame(display_screen, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    #first left frame for registration from
    LFrom = Frame(display_screen, width="350",bg="#15244C")
    LFrom.pack(side=LEFT, fill=Y)
    #seconf left frame for search form
    LeftViewForm = Frame(display_screen, width=500,bg="#0B4670")
    LeftViewForm.pack(side=LEFT, fill=Y)
    #mid frame for displaying lnames record
    MidViewForm = Frame(display_screen, width=600)
    MidViewForm.pack(side=RIGHT)
    #label for heading
    lbl_text = Label(TopViewForm, text="St Thomas Church", font=('verdana', 18), width=600,bg="cyan")
    lbl_text.pack(fill=X)
    #creating registration form in first left frame
    Label(LFrom, text="Email  ", font=("Arial", 12),bg="#15244C",fg="white").pack(side=TOP)
    Entry(LFrom,font=("Arial",10,"bold"),textvariable=mail).pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="Location ", font=("Arial", 12),bg="#15244C",fg="white").pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, "bold"),textvariable=location).pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="Possition ", font=("Arial", 12),bg="#15244C",fg="white").pack(side=TOP)
    #Entry(LFrom, font=("Arial", 10, "bold"),textvariable=gender).pack(side=TOP, padx=10, fill=X)
    possition.set("Possition")
    content={'Priest','Sister',"Secretary","Casher","Member"}
    OptionMenu(LFrom,possition,*content).pack(side=TOP, padx=10, fill=X)


    Label(LFrom, text="Occupation ", font=("Arial", 12),bg="#15244C",fg="white").pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, "bold"),textvariable=occupation).pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="Contact ", font=("Arial", 12),bg="#15244C",fg="white").pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, "bold"),textvariable=contact).pack(side=TOP, padx=10, fill=X)
    Button(LFrom,text="Home",font=("Arial", 10, "bold"),command=home,bg="cyan",fg="red").pack(side=TOP, padx=10,pady=30, fill=X)

    #creating search label and entry in second frame
    lbl_txtsearch = Label(LeftViewForm, text="Enter the house name", font=('verdana', 10),bg="#0B4670",fg="white")
    lbl_txtsearch.pack()
    #creating search entry
    search = Entry(LeftViewForm, textvariable=SEARCH, font=('verdana', 9), width=10)
    search.pack(side=TOP, padx=10, fill=X)
    #creating search button
    btn_search = Button(LeftViewForm, text="Search", command=SearchRecord,bg="cyan")
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    #creating view button
    btn_view = Button(LeftViewForm, text="View All", command=DisplayData,bg="cyan")
    btn_view.pack(side=TOP, padx=10, pady=10, fill=X)
    #creating reset button
    btn_reset = Button(LeftViewForm, text="Reset", command=Reset,bg="cyan")
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)
    #creating delete button
    btn_delete = Button(LeftViewForm, text="Delete", command=Delete,bg="cyan")
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
    #create died button
    btn_died = Button(LeftViewForm, text="Died", command=Dead,bg="cyan")
    btn_died.pack(side=TOP, padx=10, pady=10, fill=X)
    #create update button
    btn_delete = Button(LeftViewForm, text="Update", command=Update,bg="cyan")
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
    #setting scrollbar
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree = ttk.Treeview(MidViewForm,columns=("RID","Student Id", "Name", "Contact", "Email","Rollno","Branch","Country","DOB","Occupation","Joined","Possition","fname"),
                        selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    #setting headings for the columns
    tree.heading('RID', text="RID", anchor=W)
    tree.heading('Student Id', text="Name", anchor=W)
    tree.heading('Name', text="House Name", anchor=W)
    tree.heading('Contact', text="Location", anchor=W)
    tree.heading('Email', text="Email", anchor=W)
    tree.heading('Rollno', text="Gender", anchor=W)
    tree.heading('Branch', text="Contact", anchor=W)
    tree.heading('Country', text="Country", anchor=W)
    tree.heading('DOB', text="Date of Birth", anchor=W)
    tree.heading('Occupation', text="Occupation", anchor=W)
    tree.heading('Joined', text="Joined", anchor=W)
    tree.heading('Possition', text="Possition", anchor=W)
    tree.heading('fname', text="Father Name", anchor=W)
    #setting width of the columns
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=100)
    tree.column('#2', stretch=NO, minwidth=0, width=150)
    tree.column('#3', stretch=NO, minwidth=0, width=80)
    tree.column('#4', stretch=NO, minwidth=0, width=120)
    tree.pack()
    DisplayData()
#function to update data into database
def Update():
    Database()
    #getting form data
    fname1=mail.get()
    lname1=location.get()
    gender1=possition.get()
    address1=occupation.get()
    contact1=contact.get()
    #applying empty validation
    
    #getting selected data
    curItem = tree.focus()
    contents = (tree.item(curItem))
    selecteditem = contents['values']
    #update query
    if fname1=='':
        fname1=selecteditem[4] 
    if lname1=='':
        lname1=selecteditem[3] 
    if gender1=='' :
        gender1=selecteditem[11] 
    if address1=='':
        address1=selecteditem[9]
    if contact1=='':
        contact1=selecteditem[5]
    #conn.execute('UPDATE member SET email=?,location=?,possition=?,occupation=?,contact=? WHERE email =  %d' % selecteditem[0],(fname1,lname1,gender1,address1,contact1))
    #conn.commit()
    sql_update_query = """Update member set email=?,location=?,possition=?,occupation=?,contact=? where RID = ?"""
    data = (fname1,lname1,gender1,address1,contact1,selecteditem[0])
    cursor.execute(sql_update_query, data)
    conn.commit()
    tkMessageBox.showinfo("Message","Updated successfully")
    #reset form
    Reset()
    #refresh table data
    DisplayData()
    conn.close()


def Reset():
    #clear current data from table
    tree.delete(*tree.get_children())
    #refresh table data
    DisplayData()
    #clear search text
    SEARCH.set("")
    mail.set("")
    location.set("")
    possition.set("")
    occupation.set("")
    contact.set("")
def Delete():
    #open database
    Database()
    if not tree.selection():
        tkMessageBox.showwarning("Warning","Select data to delete")
    else:
        result = tkMessageBox.askquestion('Confirm', 'Are you sure you want to delete this record?',
                                          icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents = (tree.item(curItem))
            selecteditem = contents['values']
            
            
            #add to another table
            cursor=conn.execute("SELECT * FROM member WHERE RID = %d" % selecteditem[0])
            #fetch all matching records
            fetch = cursor.fetchall()
            #loop for displaying all records into GUI
            
             #insert to died table
            thislist=[]
            j=0
            for i in fetch:
                thislist.insert(j,i)
            sql="""INSERT INTO deleted 
                          VALUES (?, ?, ?, ?,?,?,?,?,?,?,?,?,?);"""
            cursor.executemany(sql, thislist)
            conn.commit()
            my_data=(selecteditem[0],datetime.datetime.now(),"Deleted")
            my_query="INSERT INTO status values(?,?,?)"
            conn.execute(my_query,my_data)
            conn.commit()
            #cursor.executemany(sql,selecteditem)
            conn.commit()
            tree.delete(curItem)
            cursor=conn.execute("DELETE FROM member WHERE RID = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()

def Dead():
    #open database
    Database()
    if not tree.selection():
        tkMessageBox.showwarning("Warning","Select the data of died member")
    else:
        result = tkMessageBox.askquestion('Confirm', 'Are you sure the member is died?',
                                          icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents = (tree.item(curItem))
            selecteditem = contents['values']
            
            #add to another table
            cursor=conn.execute("SELECT * FROM member WHERE RID = %d" % selecteditem[0])
            #fetch all matching records
            fetch = cursor.fetchall()
            #loop for displaying all records into GUI

            #insert to died table
            thislist=[]
            j=0
            for i in fetch:
                thislist.insert(j,i)
            #cursor=conn.execute('INSERT INTO deleted VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)',(thislist[0],thislist[1],thislist[2],thislist[3],thislist[4],thislist[5],thislist[6],thislist[7],thislist[8],thislist[9],thislist[10],thislist[11],thislist[12],thislist[13]));
            sql="""INSERT INTO died 
                          VALUES (?, ?, ?, ?,?,?,?,?,?,?,?,?,?);"""
            cursor.executemany(sql, thislist)
            conn.commit()
            my_data=(selecteditem[0],datetime.datetime.now(),"Died")
            my_query="INSERT INTO status values(?,?,?)"
            conn.execute(my_query,my_data)
            conn.commit()

            tree.delete(curItem)
            cursor=conn.execute("DELETE FROM member WHERE RID = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()

#function to search data
def SearchRecord():
    #open database
    Database()
    #checking search text is empty or not
    if SEARCH.get() != "":
        #clearing current display data
        tree.delete(*tree.get_children())
        #select query with where clause
        cursor=conn.execute("SELECT * FROM member WHERE house LIKE ?", ('%' + str(SEARCH.get()) + '%',))
        #fetch all matching records
        fetch = cursor.fetchall()
        #loop for displaying all records into GUI
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
#defining function to access data from SQLite database
def DisplayData():
    #open database
    Database()
    #clear current data
    tree.delete(*tree.get_children())
    #select query
    cursor=conn.execute("SELECT * FROM member")
    #fetch all data from database
    fetch = cursor.fetchall()
    #loop for displaying all data in GUI
    for data in fetch:
        tree.insert('', 'end', values=(data))
        tree.bind("<Double-1>",OnDoubleClick)
    cursor.close()
    conn.close()
def OnDoubleClick(self):
    #getting focused item from treeview
    curItem = tree.focus()
    contents = (tree.item(curItem))
    selecteditem = contents['values']
    #set values in the fields
    mail.set(selecteditem[1])
    location.set(selecteditem[2])
    possition.set(selecteditem[3])
    occupation.set(selecteditem[4])
    contact.set(selecteditem[5])

#calling function
DisplayForm()
if __name__=='__main__':
    #Running Application
    mainloop()