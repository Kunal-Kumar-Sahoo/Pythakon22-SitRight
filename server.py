import socket
import argparse
import threading

def handle(client):
    while True:
        try:
            global message
            message = client.recv(1024).decode('utf-8')
            # print(message)
            username = message[0:message.index(':')]
            password = message[message.index(':') + 1:]
            f = open("credential.txt", 'w')
            print(username, password)
            f.write(f'{username}\n{password}')
            print('success')
            f.close()
        except Exception as e:
            print(e)
            pass

def receive():
    while True:
        client, address = server.accept()
        print(f'Connected with {address}')
        clients.append(client)
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Login server')
    parser.add_argument('host')
    parser.add_argument('-p', metavar='PORT', type=int, default=1060)
    args = parser.parse_args()

    HOST = args.host
    PORT = args.p

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))

    server.listen()

    global message
    global clients
    clients = []


    print('Server running')
    receive()
