from socket import *

HOST_IP = "127.0.0.1"
PORT = 9999

# 클라이언트 측 소켓 생성
client_socket = socket(AF_INET, SOCK_STREAM)

# 지정 주소, 포트로 소켓 연결
client_socket.connect((HOST_IP, PORT))

# 서버로 메시지 전송
client_socket.sendall("안녕".encode())

# 메시지 수신
data = client_socket.recv(1024)
print(f"Received: {repr(data.decode())}")

# 소켓 닫기
client_socket.close()