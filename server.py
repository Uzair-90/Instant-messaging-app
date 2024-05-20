import socket
import threading

# Global variables
clients = {}  # Dictionary to store client connections

def handle_client(client_socket, client_address):
    try:
        while True:
            message = client_socket.recv(4096).decode('utf-8')
            if message:
                print(f"Received message from {client_address}: {message}")
                send_to_other_clients(client_socket, message)
            else:
                print(f"Client {client_address} disconnected.")
                del clients[client_socket]
                break
    except Exception as e:
        print(f"Error handling client {client_address}: {e}")
        del clients[client_socket]
        client_socket.close()

def send_to_other_clients(sender_socket, message):
    for client_socket in clients:
        if client_socket != sender_socket:
            try:
                client_socket.send(message.encode('utf-8'))
            except Exception as e:
                print(f"Error sending message to client: {e}")

def start_server(host, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print("Server listening on", host, "port", port)

    while True:
        client_socket, client_address = server.accept()
        print("Accepted connection from", client_address)
        clients[client_socket] = client_address

        # Start a new thread to handle the client
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

if __name__ == "__main__":
    HOST = '127.0.0.1'  # Server IP address
    PORT = 8080  # Server port
    start_server(HOST, PORT)

