import socket
import threading

def accept_clients(server_socket):
    while True:
        client, address = server_socket.accept()
        print(f"Accepted connection from {address}")
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

def handle_client(client_socket):
    # Handle individual client tasks (if needed)
    pass

def multicast_messages(server_socket, client_ips):
    multicast_group = "224.0.0.1"
    port = 8081

    multicast_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    multicast_socket.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)

    while True:
        message = input("Enter message to multicast: ")
        for client_ip in client_ips:
            multicast_socket.sendto(message.encode(), (client_ip, port))


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 8080))
server_socket.listen(5)

client_ips = ["10.11.147.7", "10.11.157.229"]

accept_thread = threading.Thread(target=accept_clients, args=(server_socket,))
multicast_thread = threading.Thread(target=multicast_messages, args=(server_socket, client_ips))

accept_thread.start()
multicast_thread.start()

accept_thread.join()
multicast_thread.join()
