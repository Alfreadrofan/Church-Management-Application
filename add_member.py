from tkinter import *
from tkinter import messagebox
import sqlite3
from subprocess import call

f = ('Times', 14)

con = sqlite3.connect('userdata.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS member(
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
con.commit()
ws = Tk()
ws.title('st_thomas_church')
ws.geometry('940x500')
ws.config(bg='#0B5A81')
def home():
    ws.destroy()
    call(["python", "hom.py"])


def insert_record():
    check_counter=0
    warn = ""
    if register_name.get() == "":
       warn = "Name can't be empty"
    else:
        check_counter += 1
        
    if register_email.get() == "":
        warn = "Email is empty"
        check_counter += 1
    else:
        check_counter += 1

    if register_mobile.get() == "":
       warn = "Contact can't be empty"
    else:
        check_counter += 1
    
    if  var.get() == "":
        warn = "Select Gender"
    else:
        check_counter += 1

    if variable.get() == "":
       warn = "Select Country"
    else:
        check_counter += 1

    if dob.get() == "":
        warn = "Date of Birth can't be empty"
    else:
        check_counter += 1

    if doj.get() == "":
        warn = "Date of Join can't be empty"
    else:
        check_counter += 1

    if house_tf.get() == "":
        warn = "House name can't be empty"

    else:
        check_counter += 1

    if location_tf.get() == "":
        warn = "Location can't be empty"

    else:
        check_counter += 1

    if fname_tf.get() == "":
        warn = "Father name can't be empty"

    else:
        check_counter += 1

    if occupation_tf.get() == "":
        warn = "Occupation can't be empty"

    else:
        check_counter += 1

    if possition.get() == "":
        warn = "Position can't be empty"

    else:
        check_counter += 1

    if check_counter == 12:        
        try:
            con = sqlite3.connect('userdata.db')
            cur = con.cursor()
            cur.execute("INSERT INTO member (name,house,location,email,contact,gender,country,dob,occupation,joined,possition,fname) VALUES (:name,:house,:location ,:email, :contact, :gender, :country, :dob,:occupation,:joined,:possition,:fname)", {
                            'name': register_name.get(),
                            'house':house_tf.get(),
                            'location':location_tf.get(),
                            'email': register_email.get(),
                            'contact': register_mobile.get(),
                            'gender': var.get(),
                            'country': variable.get(),
                            'dob': dob.get(),
                            'occupation':occupation_tf.get(),
                            'joined': doj.get(),
                            'possition': possition.get(),
                            'fname': fname_tf.get()


            })
            con.commit()
            messagebox.showinfo('confirmation', 'Record Saved')

        except Exception as ep:
            messagebox.showerror('', ep) 
    else:
        messagebox.showerror('Error', warn)
var = StringVar()
var.set('male')

countries = []
variable = StringVar()
world = open('countries.txt', 'r')
for country in world:
    country = country.rstrip('\n')
    countries.append(country)
variable.set(countries[22])
#possition in list
poss = []
possition = StringVar()
lis = open('possition.txt', 'r')
for pos in lis:
    pos = pos.rstrip('\n')
    poss.append(pos)
possition.set(poss[4])
# widgets
left_frame = Frame(
    ws, 
    bd=2, 
    bg='#CCCCCC',   
    relief=SOLID, 
    padx=10, 
    pady=10
    )

Label(
    left_frame, 
    text="House Name", 
    bg='#CCCCCC',
    font=f).grid(row=0, column=0, sticky=W, pady=10)

Label(
    left_frame, 
    text="Location", 
    bg='#CCCCCC',
    font=f
    ).grid(row=1, column=0, pady=10)
Label(
    left_frame, 
    text="Father Name", 
    bg='#CCCCCC',
    font=f
    ).grid(row=2, column=0, pady=10)
Label(
    left_frame, 
    text="Occupation", 
    bg='#CCCCCC',
    font=f
    ).grid(row=3, column=0, pady=10)
Label(
    left_frame, 
    text="Possition", 
    bg='#CCCCCC',
    font=f
    ).grid(row=4, column=0, sticky=W, pady=10)

house_tf = Entry(
    left_frame, 
    font=f
    )
location_tf = Entry(
    left_frame, 
    font=f,
    #show='*'
    )
fname_tf = Entry(
    left_frame, 
    font=f,
    #show='*'
    )
occupation_tf = Entry(
    left_frame, 
    font=f,
    #show='*'
    )
possition_in_church = OptionMenu(
    left_frame, 
    possition, 
    *poss)

possition_in_church.config(
    width=15, 
    font=('Times', 12)
)
home_btn = Button(
    left_frame, 
    width=15, 
    text='Home', 
    font=f, 
    relief=SOLID,
    cursor='hand2',
    command=home
    )
right_frame = Frame(
    ws, 
    bd=2, 
    bg='#CCCCCC',
    relief=SOLID, 
    padx=10, 
    pady=10
    )

Label(
    right_frame, 
    text="Enter Name", 
    bg='#CCCCCC',
    font=f
    ).grid(row=0, column=0, sticky=W, pady=10)

Label(
    right_frame, 
    text="Enter Email", 
    bg='#CCCCCC',
    font=f
    ).grid(row=1, column=0, sticky=W, pady=10)

Label(
    right_frame, 
    text="Contact Number", 
    bg='#CCCCCC',
    font=f
    ).grid(row=2, column=0, sticky=W, pady=10)

Label(
    right_frame, 
    text="Select Gender", 
    bg='#CCCCCC',
    font=f
    ).grid(row=3, column=0, sticky=W, pady=10)

Label(
    right_frame, 
    text="Select Country", 
    bg='#CCCCCC',
    font=f
    ).grid(row=4, column=0, sticky=W, pady=10)

Label(
    right_frame, 
    text="Date of Birth", 
    bg='#CCCCCC',
    font=f
    ).grid(row=5, column=0, sticky=W, pady=10)

Label(
    right_frame, 
    text="Date of Join", 
    bg='#CCCCCC',
    font=f
    ).grid(row=6, column=0, sticky=W, pady=10)

gender_frame = LabelFrame(
    right_frame,
    bg='#CCCCCC',
    padx=10, 
    pady=10,
    )


register_name = Entry(
    right_frame, 
    font=f
    )

register_email = Entry(
    right_frame, 
    font=f
    )

register_mobile = Entry(
    right_frame, 
    font=f
    )


male_rb = Radiobutton(
    gender_frame, 
    text='Male',
    bg='#CCCCCC',
    variable=var,
    value='male',
    font=('Times', 10),
    
)

female_rb = Radiobutton(
    gender_frame,
    text='Female',
    bg='#CCCCCC',
    variable=var,
    value='female',
    font=('Times', 10),
  
)

others_rb = Radiobutton(
    gender_frame,
    text='Others',
    bg='#CCCCCC',
    variable=var,
    value='others',
    font=('Times', 10)
   
)

register_country = OptionMenu(
    right_frame, 
    variable, 
    *countries)

register_country.config(
    width=15, 
    font=('Times', 12)
)
dob = Entry(
    right_frame, 
    font=f,
    #show='*'
)
doj = Entry(
    right_frame, 
    font=f,
    #show='*'
)

add_btn = Button(
    right_frame, 
    width=15, 
    text='ADD MEMbER', 
    font=f, 
    relief=SOLID,
    cursor='hand2',
    command=insert_record
)
#right
# widgets placement
house_tf.grid(row=0, column=1, pady=10, padx=20)
location_tf.grid(row=1, column=1, pady=10, padx=20)
fname_tf.grid(row=2, column=1, pady=10, padx=20)
occupation_tf.grid(row=3, column=1, pady=10, padx=20)
possition_in_church.grid(row=4, column=1, pady=10, padx=20)
home_btn.grid(row=5, column=1, pady=10, padx=20)
left_frame.place(x=500, y=50)

#left

register_name.grid(row=0, column=1, pady=10, padx=20)
register_email.grid(row=1, column=1, pady=10, padx=20) 
register_mobile.grid(row=2, column=1, pady=10, padx=20)
register_country.grid(row=4, column=1, pady=10, padx=20)
dob.grid(row=5, column=1, pady=10, padx=20)
doj.grid(row=6, column=1, pady=10, padx=20)
add_btn.grid(row=7, column=1, pady=10, padx=20)
right_frame.place(x=50, y=50)

gender_frame.grid(row=3, column=1, pady=10, padx=20)
male_rb.pack(expand=True, side=LEFT)
female_rb.pack(expand=True, side=LEFT)
others_rb.pack(expand=True, side=LEFT)

# infinite loop
ws.mainloop()