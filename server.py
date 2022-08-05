import socket
import argparse
import threading

parser = argparse.ArgumentParser(description='Login server')
parser.add_argument('host')
parser.add_argument('-p', metavar='PORT', type=int, default=1060)
args = parser.parse_args()

HOST = args.host
PORT = args.p

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen()

message = ''
clients = []


def handle(client):
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            print(message)
            print(message[0:message.index(':')])
            print(message[message.index(':') + 1:])
        except Exception as e:
            clients.remove(client)
            client.close()
            print(e)
            break

def receive():
    while True:
        client, address = server.accept()
        print(f'Connected with {address}')
        clients.append(client)
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print('Server running')
receive()
