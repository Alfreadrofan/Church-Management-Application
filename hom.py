from tkinter import *
from tkinter import ttk, font, messagebox
from PIL import ImageTk, Image
import os
from subprocess import call


root = Tk()
root.title("St_thomas_church")
# Adding window icon
#root.iconbitmap('afekaImage.ico')

rootWidth, rootHeight = 600, 600

screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()

topLeftPosition = (screenWidth / 2 - rootWidth / 2, screenHeight / 2 - rootHeight / 2)

# Configure window size
root.geometry('940x500')



# adjusting background image to fit window
def adjustBackgroundImage(event):
    label = event.widget
    # avoid garbage collection option 1
    # global resizedBackgroundImage, newBackgroundImage
    # ----------
    width = event.width
    height = event.height
    resizedBackgroundImage = copyImage.resize((width, height))
    newBackgroundImage = ImageTk.PhotoImage(resizedBackgroundImage)
    label.config(image=newBackgroundImage)
    # avoid garbage collection option 2
    label.image = newBackgroundImage
    # ----------
def add_member():
    root.destroy()
    call(["python", "add_member.py"])
def view():
    root.destroy()
    call(["python", "view.py"])
def deleted():
    root.destroy()
    call(["python", "deleted.py"])
def died():
    root.destroy()
    call(["python", "died.py"])
def logout():
    root.destroy()
    call(["python", "log_reg.py"])



image = Image.open('index.jpg')
copyImage = image.copy()
backgroundImage = ImageTk.PhotoImage(image)
label = ttk.Label(root, image=backgroundImage)
label.bind('<Configure>', adjustBackgroundImage)
label.pack(fill=BOTH, expand=YES)

fontStyle = font.Font(family="Helvetica", size=9, weight=font.BOLD)

# Create buttons
button_add = Button(root, text="MEMBER ADD", command=add_member, font=fontStyle)
button_add.place(relx=0.01, rely=0.2, relwidth=0.2, relheight=0.09)

button_overview = Button(root, text="VIEW", command=view, font=fontStyle)
button_overview.place(relx=0.01, rely=0.3, relwidth=0.2, relheight=0.09)

button_died = Button(root, text="STATUS", font=fontStyle, command=deleted)
button_died.place(relx=0.01, rely=0.4, relwidth=0.2, relheight=0.09)

button_deleted = Button(root, text="APPROVE", font=fontStyle, command=died)
button_deleted.place(relx=0.01, rely=0.5, relwidth=0.2, relheight=0.09)

button_logout = Button(root, text="LOGOUT", font=fontStyle, command=logout)
button_logout.place(relx=0.01, rely=0.6, relwidth=0.2, relheight=0.09)

root.mainloop()
