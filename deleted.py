#import library
#import library for creating GUI
from tkinter import *
import tkinter.ttk as ttk
#import library for handling SQLite database
import sqlite3
from subprocess import call
display_screen = Tk()


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
    LeftViewForm = Frame(display_screen, width=600,bg="#00cc66")
    LeftViewForm.pack(side=LEFT, fill=Y)
    MidViewForm = Frame(display_screen, width=600)
    MidViewForm.pack(side=RIGHT)
    lbl_text = Label(TopViewForm, text="ST THOMAS CHURCH", font=('verdana', 18), width=600,bg="#1C2833",fg="white")
    lbl_text.pack(fill=X)
    lbl_text = Label(TopViewForm, text="STATUS", font=('verdana', 18), width=400,bg="#1C2833",fg="cyan")
    lbl_text.pack(fill=X)
    lbl_txtsearch = Label(LeftViewForm, text="Enter House Name", font=('verdana', 10),bg="#00cc66")
    lbl_txtsearch.pack(side=TOP, padx=30, anchor=W)

    search = Entry(LeftViewForm, textvariable=SEARCH, font=('verdana', 9), width=10)
    search.pack(side=TOP, padx=10, fill=X)
    btn_search = Button(LeftViewForm, text="Search", command=SearchRecord)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_search = Button(LeftViewForm, text="View All", command=DisplayData)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_search = Button(LeftViewForm, text="Removed", command=Deleted)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_search = Button(LeftViewForm, text="Died", command=Died)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_search = Button(LeftViewForm, text="Home", command=home)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)

    #setting scrollbar
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree = ttk.Treeview(MidViewForm,columns=("UID", "Name", "House", "Location","Email","Contact","Gender","Country","DOB","Occupation","Joined","Possition","Fname","Modified","Status"),
                        selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview,)
    scrollbarx.pack(side=BOTTOM, fill=X)
    #setting headings for the columns
    tree.heading('UID', text="RID", anchor=W)
    tree.heading('Name', text="Name", anchor=W)
    tree.heading('House', text="House", anchor=W)
    tree.heading('Location', text="Location", anchor=W)
    tree.heading('Email', text="Email", anchor=W)
    tree.heading('Contact', text="Contact", anchor=W)
    tree.heading('Gender', text="Gender", anchor=W)
    tree.heading('Country', text="Country", anchor=W)
    tree.heading('DOB', text="DOB", anchor=W)
    tree.heading('Occupation', text="Occupation", anchor=W)
    tree.heading('Joined', text="Joined", anchor=W)
    tree.heading('Possition', text="Possition", anchor=W)
    tree.heading('Fname', text="Father Name", anchor=W)
    tree.heading('Modified', text="Modified", anchor=W)
    tree.heading('Status', text="Status", anchor=W)
    #setting width of the columns
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=50)
    tree.column('#2', stretch=NO, minwidth=0, width=150)
    tree.column('#3', stretch=NO, minwidth=0, width=80)
    tree.column('#4', stretch=NO, minwidth=0, width=80)
    tree.column('#5', stretch=NO, minwidth=0, width=120)
    tree.column('#6', stretch=NO, minwidth=0, width=100)
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
        cursor=conn.execute("SELECT * FROM deleted WHERE house LIKE ?", ('%' + str(SEARCH.get()) + '%',))
        #fetch all matching records
        fetch = cursor.fetchall()
        #loop for displaying all records into GUI
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        cursor=conn.execute("SELECT * FROM died WHERE house LIKE ?", ('%' + str(SEARCH.get()) + '%',))
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
    cursor=conn.execute("SELECT deleted.RID, name, house, location, email, contact, gender, country, dob, occupation, joined, possition, fname, Date, status FROM deleted join status where deleted.RID=status.RID")
    #fetch all data from database
    fetch = cursor.fetchall()
    #loop for displaying all data in GUI
    for data in fetch:
        tree.insert('', 'end', values=(data))
    #tree.insert("Died")
    cursor=conn.execute("SELECT died.RID, name, house, location, email, contact, gender, country, dob, occupation, joined, possition, fname, Date, status FROM died  join status where died.RID=status.RID")
    #fetch all data from database
    fetch = cursor.fetchall()
    #loop for displaying all data in GUI
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()
def Deleted():
    #clear current data
    tree.delete(*tree.get_children())
    # open databse
    conn = sqlite3.connect('userdata.db')
    #select query
    cursor=conn.execute("SELECT deleted.RID, name, house, location, email, contact, gender, country, dob, occupation, joined, possition, fname, Date, status FROM deleted join status where deleted.RID=status.RID")
    #fetch all data from database
    fetch = cursor.fetchall()
    #loop for displaying all data in GUI
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()
def Died():
    #clear current data
    tree.delete(*tree.get_children())
    # open databse
    conn = sqlite3.connect('userdata.db')
    #select query
    cursor=conn.execute("SELECT died.RID, name, house, location, email, contact, gender, country, dob, occupation, joined, possition, fname, Date, status FROM died  join status where died.RID=status.RID")
    #fetch all data from database
    fetch = cursor.fetchall()
    #loop for displaying all data in GUI
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

#calling function
DisplayForm()
if __name__=='__main__':
#Running Application
 mainloop()