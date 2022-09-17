from socket import *
import pickle
import struct
from _thread import *
import cv2 as cv

import MediapipeHands as mphand

HOST = "127.0.0.1"
PORT = 9999

# 서버 측 소켓 생성
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

client_socket, client_addr = server_socket.accept()

data = b""
payload_size = struct.calcsize("L")

while True:
    while len(data) < payload_size:
        data += client_socket.recv(4096)
    
    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack("L", packed_msg_size)[0]

    # 메시지 사이즈 기준으로 데이터 구성
    while len(data) < msg_size:
        data += client_socket.recv(4096)

    frame_data = data[:msg_size]
    data = data[msg_size:]

    # 프레임 로드
    frame = pickle.loads(frame_data)

    # MediaPipe Hands 적용
    frame = mphand.get_landmark(frame)

    # 창으로 나타내기
    cv.imshow('server', frame)

    client_socket.sendall("continue".encode())
    
    if cv.waitKey(1) == 27:
        cv.destroyAllWindows()

        # 클라이언트로 데이터 에코
        client_socket.sendall("finished".encode())
        break

client_socket.close()