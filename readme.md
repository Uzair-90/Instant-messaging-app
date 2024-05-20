# Instant Messaging System

## Project Overview
This project involves the design and implementation of an instant messaging system, which 
includes both server and client components. The system enables real-time, text-based 
communication between multiple users, supporting message exchange through a client-server 
architecture.

## Group Members
- Uzair Rehman (2020509)
- Atif Khan (2020092)
- Zaeem Shakir (2020487)

## Supervisor
- Lecturer Salman Saeed

## Introduction
The instant messaging system is a tool for real-time communication over the internet. This 
project presents the design and implementation of an instant messaging system that facilitates 
text-based communication between multiple users. It supports real-time message exchange using a 
client-server architecture.

## System Architecture
The system follows a client-server architecture:
- **Server Component (`Server.py`)**: Manages client connections, message routing, and 
communication with clients.
- **Client Component (`Client.py`)**: Provides a graphical user interface (GUI) for users to 
send and receive messages.

## Workflow
1. The server starts listening for incoming connections on a specified host and port.
2. Clients connect to the server and send messages to each other through the server.
3. The server receives messages from clients, determines the recipients, and forwards the 
messages.
4. Clients receive messages from the server and display them in the user interface.

## Components
### Server
- **`Server.py`**: Handles client connections, message routing, and communication with clients 
using sockets and threading for concurrent message handling.

### Client
- **`Client.py`**: Provides a Tkinter-based GUI for users to send and receive messages.

## Deployment Instructions
1. Ensure Python is installed on your system.
2. Run `Server.py` to start the server.
   ```sh
   python Server.py

