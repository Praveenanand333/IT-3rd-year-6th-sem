import socket

def client():
    multicast_group = "224.0.0.1"
    port = 8081

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    client_socket.bind(("", port))
    mreq = socket.inet_aton(multicast_group) + socket.inet_aton("0.0.0.0")
    client_socket.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    while True:
        message, address = client_socket.recvfrom(1024)
        print(f"Multicast message received from {address}: {message.decode()}")

client()
