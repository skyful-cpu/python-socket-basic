from socket import *

HOST = "127.0.0.1"
PORT = 9999

# 클라이언트 측 소켓 생성
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((HOST, PORT))

# "quit" 입력 전까지 서버와 텍스트를 주고받는 통신
while True:
    message = input("Enter Message: ")

    if message == "quit":
        break

    client_socket.send(message.encode())
    data = client_socket.recv(1024)

    print(f"received from server: {repr(data.decode())}")

client_socket.close()