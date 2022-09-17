from socket import *
import pickle
import struct
import cv2 as cv
import numpy as np

HOST = "127.0.0.1"
PORT = 9999

# 클라이언트 소켓 생성
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((HOST, PORT))

cap = cv.VideoCapture(0)

while cap.isOpened:
    try:
        success, frame = cap.read()

        if not success:
            print("ignoring this frame..")
            continue

        # 데이터 직렬화
        data = pickle.dumps(frame)

        # 데이터 길이
        data_size = struct.pack("L", len(data))

        # 데이터 전송
        client_socket.sendall(data_size + data)

        message = client_socket.recv(1024)

        if repr(message.decode()) == "finished":
            cap.release()
            break
    
    except Exception as e:
        print("server closed...")
        break

client_socket.close()