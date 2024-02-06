import socket
import threading

def receive_messages(client_socket):
    while True:
        data = client_socket.recv(1024).decode()
        if not data:
            break
        print("Received from server: " + data)

def send_messages(client_socket):
    while True:
        message = input("Enter your message (Type 'bye' to exit): ")
        if message.lower().strip() == "bye":
            break
        client_socket.send(message.encode())

def client():
    host = socket.gethostname()
    port = 21042
    client_socket = socket.socket()
    client_socket.connect((host, port))
    print("Connected to server.")

    # Create threads for receiving and sending
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    send_thread = threading.Thread(target=send_messages, args=(client_socket,))

    # Start the threads
    receive_thread.start()
    send_thread.start()

    # Wait for both threads to finish
    receive_thread.join()
    send_thread.join()

    client_socket.close()

client()
