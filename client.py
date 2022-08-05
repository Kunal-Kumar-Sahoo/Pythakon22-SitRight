from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Login")
root.geometry("925x500+300+200")
root.configure(bg="#fff")
root.resizable(False, False)

img = PhotoImage(file="login.png")
Label(root, image=img, bg='white').place(x=50, y=50)

frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=70)

heading = Label(frame, text="Sign in", fg="#57a178", bg="white", font=('Arial', 23, 'bold'))
heading.place(x=100, y=5)

user = Entry(frame, width=25, fg="black", borderwidth=0, highlightthickness=0, bg="white", font=('Arial', 11))
user.place(x=30, y=80)
user.insert(0, 'Username')

Frame(frame, width=295, height=2, bg="black").place(x=25, y=100)

code = Entry(frame, width=25, fg="black", borderwidth=0, highlightthickness=0, bg="white", font=('Arial', 11))
code.place(x=30, y=150)
code.insert(0, 'Password')

Frame(frame, width=295, height=2, bg="black").place(x=25, y=177)


def submitForm():
    print('Submitted')


Button(frame,width=30, pady=7, text="Sign in", bg="#57a1f8", fg="white", border=0, command=submitForm()).place(x=35, y=204)

root.mainloop()
