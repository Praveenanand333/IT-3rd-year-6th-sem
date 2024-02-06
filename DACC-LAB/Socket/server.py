import socket
import threading

def receive_messages(client_socket):
    while True:
        data = client_socket.recv(1024).decode()
        if not data:
            break
        print(f"Received from client: {data}")

def send_messages(client_socket):
    while True:
        response = input("Enter response to send to client (Type 'bye' to exit): ")
        if response.lower().strip() == "bye":
            break
        client_socket.send(response.encode())

def server():
    host = socket.gethostname()
    port = 21042
    s = socket.socket()
    s.bind((host, port))
    s.listen(2)
    c, address = s.accept()
    print(f"Connected to: {address}")

    # Create threads for receiving and sending
    receive_thread = threading.Thread(target=receive_messages, args=(c,))
    send_thread = threading.Thread(target=send_messages, args=(c,))

    # Start the threads
    receive_thread.start()
    send_thread.start()

    # Wait for both threads to finish
    receive_thread.join()
    send_thread.join()

    c.close()

server()
