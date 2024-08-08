
import socket
import threading
import tkinter as tk
from tkinter import simpledialog, scrolledtext, messagebox
import sys

# Server-side function to handle clients
def handle_client(client_socket, clients, nicknames):
    while True:
        try:
            message = client_socket.recv(1024)
            broadcast(message, clients)
        except:
            index = clients.index(client_socket)
            clients.remove(client_socket)
            client_socket.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} left the chat!'.encode('utf-8'), clients)
            nicknames.remove(nickname)
            break

# Broadcast messages to all clients
def broadcast(message, clients):
    for client in clients:
        client.send(message)

# Server-side main function
def start_server(host='127.0.0.1', port=12345):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()

    clients = []
    nicknames = []

    print(f"Server is listening on {host}:{port}...")

    while True:
        client_socket, address = server.accept()
        print(f"Connection from {str(address)} established!")

        client_socket.send("NICKNAME : ".encode('utf-8'))
        nickname = client_socket.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client_socket)

        print(f"Nickname of the client is {nickname}")
        broadcast(f"{nickname} joined the chat!".encode('utf-8'), clients)
        client_socket.send("Connected to the server!".encode('utf-8'))

        thread = threading.Thread(target=handle_client, args=(client_socket, clients, nicknames))
        thread.start()

# Client-side GUI class
class ChatGUI:
    def __init__(self, client_socket):
        self.client_socket = client_socket

        self.window = tk.Tk()
        self.window.title("Chat Application")

        # Chat area
        self.chat_area = scrolledtext.ScrolledText(self.window, wrap=tk.WORD)
        self.chat_area.pack(padx=20, pady=5)
        self.chat_area.config(state=tk.DISABLED)

        # Message input
        self.msg_entry = tk.Entry(self.window)
        self.msg_entry.pack(padx=20, pady=5)
        self.msg_entry.bind("<Return>", self.write)

        # Thread for receiving messages
        receive_thread = threading.Thread(target=self.receive)
        receive_thread.start()

        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.window.mainloop()

    def write(self, event=None):
        message = f"{nickname}: {self.msg_entry.get()}"
        self.client_socket.send(message.encode('utf-8'))
        self.msg_entry.delete(0, tk.END)

    def receive(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode('utf-8')
                self.chat_area.config(state=tk.NORMAL)
                self.chat_area.insert(tk.END, message + '\n')
                self.chat_area.yview(tk.END)
                self.chat_area.config(state=tk.DISABLED)
            except:
                print("An error occurred!")
                self.client_socket.close()
                break

    def on_closing(self, event=None):
        self.client_socket.close()
        self.window.quit()

# Client-side main function
def start_client(host='127.0.0.1', port=12345):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    # Get nickname through a simple dialog
    global nickname
    nickname = simpledialog.askstring("Nickname", "Please choose a nickname", parent=tk.Tk())

    if nickname:
        client_socket.send(nickname.encode('utf-8'))
        chat_gui = ChatGUI(client_socket)
    else:
        messagebox.showerror("Error", "Nickname cannot be empty!")
        sys.exit()

# Entry point
if __name__ == "__main__":
    choice = simpledialog.askstring("Server or Client", "Type 'server' to start as server, or 'client' to start as client:", parent=tk.Tk())

    if choice == 'server':
        start_server()
    elif choice == 'client':
        start_client()
    else:
        messagebox.showerror("Error", "Invalid choice! Exiting...")
        sys.exit()


