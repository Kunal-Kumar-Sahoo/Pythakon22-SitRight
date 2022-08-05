from tkinter import *
from tkinter import messagebox
import tkinter as tk

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


def write(message_arr):
    message = f"{message_arr[0]}:{message_arr[1]}"
    sock.send(message.encode('utf-8'))
    print("Data transmitted successfully")

def submitact():
    user = Username.get()
    passw = password.get()

    print(f"The name entered by you is {user} {passw}")
    write([user, passw])


root = tk.Tk()
root.geometry("300x300")
root.title("Login Page")


lblfrstrow = tk.Label(root, text="Username -", )
lblfrstrow.place(x=50, y=20)

Username = tk.Entry(root, width=35)
Username.place(x=150, y=20, width=100)

lblsecrow = tk.Label(root, text="Password -")
lblsecrow.place(x=50, y=50)

password = tk.Entry(root, width=35)
password.place(x=150, y=50, width=100)

submitbtn = tk.Button(root, text="Login",
                      bg='blue', command=submitact)
submitbtn.place(x=150, y=135, width=55)

root.mainloop()
