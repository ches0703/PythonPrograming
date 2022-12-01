# User0defined module - Class_VideoChat (1)
import socket
import cv2
import time
import numpy as np
import threading
from queue import Queue
PORT = 9999


class VideoChat():
    def __init__(self, mode):
        self.my_mode = mode
        print("VideoChat initiated as {} ...".format(mode))
        hostname = socket.gethostname()
        self.my_address = socket.gethostbyname(hostname)
        print("My IP addressess = {}".format(self.my_address))
        self.myWebCam = 0  # SERVER_WEBCAM = 0

    def run(self):
        if self.my_mode == "Server":
            self.mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.mySocket.bind((self.my_address, PORT))
            self.mySocket.listen()
            print('Server::Video chatting server started')
            print('Server::Waiting for client .... ')
            self.peerSocket, self.peer_address = self.mySocket.accept()
            print('Server::connected to client ({} : {})'.format(
                self.peerSocket, self.peer_address))
        elif self.my_mode == "Client":
            self.peer_address = input("Input server IP addressess = ")
            print('Client::Connecting to Server')
            self.mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.mySocket.connect((self.peer_address, PORT))
            print('Client::Connected to Server({}:{})'.format(self.peer_address, PORT))
            self.peerSocket = self.mySocket

        self.queue = Queue()
        thrd_CaptureVideo = threading.Thread(
            target=self.captureVideo, args=(self.queue,))
        thrd_CaptureVideo.start()
        thrd_TxVideo = threading.Thread(target=self.txVideo, args=(
            self.peerSocket, self.queue))
        thrd_TxVideo.start()
        thrd_RxVideo = threading.Thread(
            target=self.rxVideo, args=(self.peerSocket,))
        thrd_RxVideo.start()

        thrd_TxVideo.join()
        thrd_RxVideo.join()
        thrd_CaptureVideo.join()
        print("VideoChatt( {}) is closing socket and quit video chatt".format(self.my_mode))
        self.mySocket.close()

    def recvall(self, sock, count):
        if count == 0 or count is None:
            return None
        buf = b''
        # Get data & Save in buffer
        while count:
            try:
                newbuf = sock.recv(count)
            except Exception:
                self.op_state = "QUIT"
                break
            if not newbuf:
                return None
            buf += newbuf
            count -= len(newbuf)
        return buf

    def txVideo(self, peerSocket, queue):
        while True:
            if self.op_state == "QUIT":
                break
            if not queue.empty():   # if queue is not empty
                try:                # Get String data
                    stringData = queue.get()
                    # Send data : String's length. String
                    peerSocket.send(str(len(stringData)).ljust(16).encode())    # Send String's length data
                    peerSocket.send(stringData)                                 # Send String data
                except Exception:   # ConnectionResetError, ConnectionAbortedError
                    self.op_state = "QUIT"
                    break
            time.sleep(0.1)
        print("{}:: closing peerSocket() ...".format(self.my_mode))
        peerSocket.close()
        print("{}:: terminating thread_txVideo() ...".format(self.my_mode))

    def captureVideo(self, queue):
        server_webcam = cv2.VideoCapture(self.myWebCam)
        fr_width, fr_height, fps = server_webcam.get(
            3), server_webcam.get(4), server_webcam.get(cv2.CAP_PROP_FPS)
        print("{}_webcam frame width ({}), height({}), fps({})".format(
            self.my_mode, fr_width, fr_height, fps))
        while True:
            if self.op_state == "QUIT":
                break
            ret, serv_frame = server_webcam.read()
            if ret is False:
                continue
            resized_svrfr = cv2.resize(
                serv_frame, (int(serv_frame.shape[1] / 2), int(serv_frame.shape[0] / 2)))
            encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
            result, imgencode = cv2.imencode(
                '.jpg', resized_svrfr, encode_param)
            img_data = np.array(imgencode)
            stringData = img_data.tobytes()
            queue.put(stringData)
            cv2.imshow('Server:: Resized_Server_Video', resized_svrfr)
            key = cv2.waitKey(1)
            if key == 27:  # if ESC key is input, then exit
                print("{} :: ESC key pressed => exit".format(self.my_mode))
                self.op_state = "QUIT"
                break
            time.sleep(0.05)
        print("{}:: terminating thread_captureVideo() ...".format(self.my_mode))

    def rxVideo(self, peerSocket):
        while True:
            if self.op_state == "QUIT":
                break
            length = self.recvall(peerSocket, 16)
            if length == 0 or length is None or length == b'':
                self.op_state = "QUIT"
                break
            stringData = self.recvall(peerSocket, int(length))
            data = np.frombuffer(stringData, dtype='uint8')
            decimg = cv2.imdecode(data, 1)
            cv2.imshow('{} :: received video from peer'.format(
                self.my_mode), decimg)
            key = cv2.waitKey(1)
            if key == 27:  # if ESC key is input, then exit
                print("{} :: ESC key pressed => exit".format(self.my_mode))
                self.op_state = "QUIT"
                break
            time.sleep(0.05)
        print("{}:: terminating thread_rxVideo() ...".format(self.my_mode))
