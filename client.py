import socket
import threading
from datetime import datetime
import time
import os
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv("IP")
PORT = 5000

_user = input("Enter a username: ")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            print("\n" + message)
        except:
            print("Disconnected from server")
            client.close()
            break

def send_messages(user):
    while True:
        message = (f"{user}: {input()}\n{datetime.now().strftime("%H:%M:%S")}")
        client.send(message.encode('utf-8'))

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

send_thread = threading.Thread(target=send_messages(_user))
send_thread.start()