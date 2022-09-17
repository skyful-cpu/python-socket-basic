from socket import *
from _thread import *

# 스레드에서 실행되는 코드
# 접속한 클라이언트마다 새로운 스레드를 만들어 통신
def threaded(client_socket, addr):
    print(f"connected by: {addr[0]} : {addr[1]}")

    # 클라이언트가 접속을 끊을 때 까지
    while True:
        try:
            data = client_socket.recv(1024)

            if not data:
                print(f"disconnected by: {addr[0]} : {addr[1]}")
                break

            print(f"received from {addr[0]} : {addr[1]} : {data.decode()}")
            client_socket.send(data)
        
        except ConnectionResetError as e:
            print(f"disconnected by: {addr[0]} : {addr[1]}")
            break

    client_socket.close()

HOST = "127.0.0.1"
PORT = 9999

# 서버 측 소켓 생성
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"{'-'*10}server start{'-'*10}")

# 새로운 클라이언트 접속이 들어오면 스레드 생성 후 통신 시작
while True:
    client_socket, addr = server_socket.accept()
    start_new_thread(threaded, (client_socket, addr))