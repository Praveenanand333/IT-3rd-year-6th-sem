import socket
def client():
    host = "10.11.147.7"
    port = 8081
    client_socket = socket.socket()
    client_socket.connect((host, port))
    num1 = input("Enter number 1:")
    num2 = input("Enter number 2:")
    op=input("Enter the operation:")
    client_socket.send(num1.encode())
    client_socket.send(num2.encode())
    client_socket.send(op.encode())
    res= client_socket.recv(1024)
    print("Result is:",float(res))
    client_socket.close()
client()