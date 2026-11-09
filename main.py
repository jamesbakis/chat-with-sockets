import socket
import threading

def main():
    HOST = '0.0.0.0'
    PORT = 5000

    #Create socket object, AF_NET for ipv4, SOCK_STREAM for TCP
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Bind host and port to server
    server.bind((HOST, PORT))
    server.listen()
    
    clients = []
    usernames = {}

    def broadcast(message, _client):
        for client in clients:
            if client != _client:
                try:
                    client.send(message)
                except:
                    client.close()
                    clients.remove(client)

    def handle_client(client):
        while True:
            try:
                message = client.recv(1024)
                broadcast(message, client)
            except:
                print("Client disconnected.")
                clients.remove(client)
                client.close()
                break

    def receive_connections():
        print(f"Server is running on port {PORT}...")
        while True:
            client, address = server.accept()
            print(f"New connection: {address}")
            clients.append(client)

            thread = threading.Thread(target=handle_client, args=(client,))
            thread.start()

    receive_connections()

if __name__ == "__main__":
    main()