import socket
import threading
import tkinter as tk

class ClientUI:
    def __init__(self, host, port):
        self.host = host
        self.port = port

        self.root = tk.Tk()
        self.root.title("Instant Messaging Client")

        self.message_frame = tk.Frame(self.root)
        self.scrollbar = tk.Scrollbar(self.message_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.message_list = tk.Listbox(self.message_frame, height=15, width=50, yscrollcommand=self.scrollbar.set)
        self.message_list.pack(side=tk.LEFT, fill=tk.BOTH)
        self.message_frame.pack()

        self.message_entry = tk.Entry(self.root, width=50)
        self.message_entry.pack()

        self.send_button = tk.Button(self.root, text="Send", command=self.send_message)
        self.send_button.pack()

        # Connect to server
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.host, self.port))

        # Start receiving messages in a separate thread
        receive_thread = threading.Thread(target=self.receive_messages)
        receive_thread.daemon = True
        receive_thread.start()

    def send_message(self):
        message = self.message_entry.get()
        if message:
            self.client_socket.send(message.encode('utf-8'))
            self.message_entry.delete(0, tk.END)

    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(4096).decode('utf-8')
                if message:
                    self.message_list.insert(tk.END, message)
                    self.message_list.yview(tk.END)
            except Exception as e:
                print(f"Error receiving message: {e}")
                break

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    HOST = '127.0.0.1'  # Server IP address
    PORT = 8080  # Server port

    client_ui = ClientUI(HOST, PORT)
    client_ui.run()

