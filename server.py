from socket import *

HOST_IP = "127.0.0.1"
PORT = 9999

# 서버 측 소켓 생성
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) # 포트 사용중으로 인한 연결 불가능 오류 처리
server_socket.bind((HOST_IP, PORT))
server_socket.listen()

# accept 함수로 클라이언트의 접속을 대기, 새로운 클라이언트 소켓 반환
client_socket, client_addr = server_socket.accept()

print(
    "-" * 10,
    f"Connected by {client_addr}",
    "-" * 10 
)

while True:
    data = client_socket.recv(1024)

    # 빈 문자열을 수신하면 통신 종료
    if not data:
        break

    print(f"Received from {client_addr}: {data.decode()}")

    # 클라이언트로 데이터 에코
    client_socket.sendall(data)

# 소켓 닫기
client_socket.close()
server_socket.close()