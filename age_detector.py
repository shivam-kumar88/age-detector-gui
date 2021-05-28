from tkinter import *
#import
from datetime import date

root = Tk()
root.geometry("700x1000")
root.title("age calculator")

photo = PhotoImage(file="picture_shivam.png")
myimage = Label(image=photo)
myimage.grid(row=0, column=1)

def agecalculate():
    today = date.today()
    birthDate = date(int(yearEntry.get()), int(monthEntry.get()), int(dayEntry.get()))

    age = today.year - birthDate.year - ((today.month, today.day)<(birthDate.month, birthDate.day))
    Label(text = f"{nameValue.get()} your age is {age}").grid(row=6,column=1)



Label(text="name").grid(row=1, column=0, padx=90)
Label(text="year").grid(row=2, column=0)
Label(text="month").grid(row=3, column=0)
Label(text="day").grid(row=4, column=0)

nameValue = StringVar()
yearValue = StringVar()
monthValue = StringVar()
dayValue = StringVar()

nameEntry = Entry(root, textvariable=nameValue)
yearEntry = Entry(root, textvariable=yearValue)
monthEntry = Entry(root, textvariable=monthValue)
dayEntry = Entry(root, textvariable=dayValue)

nameEntry.grid(row=1, column=1, padx=10)
yearEntry.grid(row=2, column=1, padx=10)
monthEntry.grid(row=3, column=1, padx=10)
dayEntry.grid(row=4, column=1, padx=10)

Button(text="find age", command=agecalculate).grid(row=5, column=1, padx=10)

root.mainloop()