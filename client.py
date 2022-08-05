from tkinter import *
from tkinter import messagebox
import socket
import threading
import argparse

parser = argparse.ArgumentParser(description='Enter IP Address:')
parser.add_argument('host', help='Interface the sever listens at')
parser.add_argument('-p', metavar='PORT', type=int, default=1060, help='TCP PORT(default 1060)')

args = parser.parse_args()

HOST = args.host
PORT = args.p

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

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


def on_enter(e):
    user.delete(0, 'end')


def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0, 'Username')
    print(name)


user = Entry(frame, width=25, fg="black", borderwidth=0, highlightthickness=0, bg="white", font=('Arial', 11))
user.place(x=30, y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg="black").place(x=25, y=100)


def on_enter(e):
    code.delete(0, 'end')


def on_leave(e):
    passw = code.get()
    if passw == '':
        code.insert(0, 'Password')
    print(passw)


code = Entry(frame, width=25, fg="black", borderwidth=0, highlightthickness=0, bg="white", font=('Arial', 11))
code.place(x=30, y=150)
code.insert(0, 'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg="black").place(x=25, y=177)


def submitform():
    print('Submitted')


Button(frame, width=30, pady=7, text="Sign in", bg="#57a1f8", fg="white", border=0, command=submitform()).place(x=35,
                                                                                                                y=204)

root.mainloop()
