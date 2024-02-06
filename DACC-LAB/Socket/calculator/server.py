import socket
def server():
    host = "10.11.147.7"
    port = 8081
    s = socket.socket()
    s.bind((host, port))
    s.listen(2)
    c, address = s.accept()
    print(f"Connected to: {address}")
    num1= c.recv(1024).decode()
    num2= c.recv(1024).decode()
    op=c.recv(1024).decode()
    if(op=='+'):
        res=int(num1)+int(num2)
    elif(op=='-'):
        res=int(num1)-int(num2)
    elif(op=='*'):
        res=int(num1)*int(num2)
    elif(op=='/'):
        res=int(num1)/int(num2)
    else:
        res=0
    c.send(str(res).encode())
    c.close()


server()