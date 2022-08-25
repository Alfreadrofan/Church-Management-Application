#import library
#import library for creating GUI
from tkinter import *
import tkinter.ttk as ttk
#import library for handling SQLite database
import sqlite3
from subprocess import call
import tkinter.messagebox as tkMessageBox
display_screen = Tk()

def Database():
    global conn, cursor
    #creating contact database
    conn = sqlite3.connect("userdata.db")
    cursor = conn.cursor()
    #creating died table
def home():
    display_screen.destroy()
    call(["python", "hom.py"])
#defining function for creating GUI Layout
def DisplayForm():
    #creating window
    #display_screen = Tk()
    #setting width and height for window
    display_screen.geometry("940x500")
    #setting title for window
    display_screen.title("st_thomas_church")
    global tree
    global SEARCH
    SEARCH = StringVar()
    #creating frame
    TopViewForm = Frame(display_screen, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    LeftViewForm = Frame(display_screen, width=600,bg="#1C2833")
    LeftViewForm.pack(side=LEFT, fill=Y)
    MidViewForm = Frame(display_screen, width=600)
    MidViewForm.pack(side=LEFT)
    lbl_text = Label(TopViewForm, text="ST THOMAS CHURCH", font=('verdana', 18), width=600,bg="#1C2833",fg="white")
    lbl_text.pack(fill=X)
    lbl_text = Label(TopViewForm, text="APPROVE USER", font=('verdana', 18), width=400,bg="#1C2833",fg="cyan")
    lbl_text.pack(fill=X)
    lbl_txtsearch = Label(LeftViewForm, text="Enter Email", font=('verdana', 10),bg="#1C2833",fg="white")
    lbl_txtsearch.pack(side=TOP,padx=30, anchor=W)

    search = Entry(LeftViewForm, textvariable=SEARCH, font=('verdana', 15), width=10)
    search.pack(side=TOP, padx=10, fill=X)
    btn_search = Button(LeftViewForm, text="SEARCH", command=SearchRecord)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_search = Button(LeftViewForm, text="View All", command=DisplayData)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_search = Button(LeftViewForm, text="APPROVE", command=approve)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_search = Button(LeftViewForm, text="USERS", command=users)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_search = Button(LeftViewForm, text="HOME", command=home)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)

    #setting scrollbar
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree = ttk.Treeview(MidViewForm,columns=("Id","Name", "Email", "Contact", "Gender","Country"),
                        selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    #setting headings for the columns
    tree.heading('Id', text="Id", anchor=W)
    tree.heading('Name', text="Name", anchor=W)
    tree.heading('Email', text="Email", anchor=W)
    tree.heading('Contact', text="Contact", anchor=W)
    tree.heading('Gender', text="Gender", anchor=W)
    tree.heading('Country', text="Country", anchor=W)
   
    #setting width of the columns
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=100)
    tree.column('#2', stretch=NO, minwidth=0, width=100)
    tree.column('#3', stretch=NO, minwidth=0, width=100)
    tree.column('#4', stretch=NO, minwidth=0, width=100)
    tree.pack()
    DisplayData()
#function to search data
def SearchRecord():
    #checking search text is empty or not
    if SEARCH.get() != "":
        #clearing current display data
        tree.delete(*tree.get_children())
        #open database
        conn = sqlite3.connect('userdata.db')
        #select query with where clause
        cursor=conn.execute("SELECT * FROM record WHERE email LIKE ?", ('%' + str(SEARCH.get()) + '%',))
        #fetch all matching records
        fetch = cursor.fetchall()
        #loop for displaying all records into GUI
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
#defining function to access data from SQLite database
def DisplayData():
    #clear current data
    tree.delete(*tree.get_children())
    # open databse
    conn = sqlite3.connect('userdata.db')
    #select query
    cursor=conn.execute("SELECT * FROM record")
    #fetch all data from database
    fetch = cursor.fetchall()
    #loop for displaying all data in GUI
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()
def users():
    #clear current data
    tree.delete(*tree.get_children())
    # open databse
    conn = sqlite3.connect('userdata.db')
    #select query
    cursor=conn.execute("SELECT * FROM approved")
    #fetch all data from database
    fetch = cursor.fetchall()
    #loop for displaying all data in GUI
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()
def approve():
    #open database
    Database()
    if not tree.selection():
        tkMessageBox.showwarning("Warning","Select data to approve")
    else:
        result = tkMessageBox.askquestion('Confirm', 'Are you sure you want to Approve the user?',
                                          icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents = (tree.item(curItem))
            selecteditem = contents['values']
            
            
            #add to another table
            cursor=conn.execute("SELECT * FROM record WHERE id = %d" % selecteditem[0])
            #fetch all matching records
            fetch = cursor.fetchall()
            #loop for displaying all records into GUI
            
             #insert to died table
            thislist=[]
            j=0
            for i in fetch:
                thislist.insert(j,i)
            
            sql="""INSERT INTO approved 
                          VALUES (?, ?, ?, ?,?,?,?);"""
            cursor.executemany(sql, thislist)
            conn.commit()
            #cursor.executemany(sql,selecteditem)
            tree.delete(curItem)
            cursor=conn.execute("DELETE FROM record WHERE id = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()


#calling function
DisplayForm()
if __name__=='__main__':
#Running Application
 mainloop()