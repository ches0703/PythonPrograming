# Userdefined module - Class_VideoChat.py
import socket
import cv2
import time
import numpy as np
import threading
from queue import Queue
# Set Port number
PORT = 9999


class VideoChat():
    def __init__(self, mode):
        self.my_mode = mode                 # Set user's mode
        print("VideoChat initiated as {} ...".format(mode))
        hostname = socket.gethostname()     # Get user's IP Address
        self.my_address = socket.gethostbyname(hostname)
        print("My IP addressess = {}".format(self.my_address))
        self.myWebCam = 0                   # Set Webcam
        self.op_state = "RUN"               # Set op_state
        self.queue = Queue()                # Save send data temporary
        # Make Socket, for use TCP
        self.mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def run(self):  # Run by mode
        if self.my_mode == "Server":    # Mode : Server
            self.mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            # Bind socket to (Host's IP Adress, port_number)
            self.mySocket.bind((self.my_address, PORT))
            self.mySocket.listen()  # Waiating for Connection
            print('Server::Video chatting server started')
            print('Server::Waiting for client .... ')
            # if detect connection request : accept
            self.peerSocket, self.peer_address = self.mySocket.accept()
            print('Server::connected to client ({} : {})'.format(self.peerSocket, self.peer_address))
        elif self.my_mode == "Client":  # Mode : Client
            self.peer_address = input("Input server IP addressess = ")
            print('Client::Connecting to Server')
            # Send connect request to TCP server         
            self.mySocket.connect((self.peer_address, PORT))
            print('Client::Connected to Server({}:{})'.format(self.peer_address, PORT))
            self.peerSocket = self.mySocket

        # Make Thread & Start
        thread_CaptureVideo = threading.Thread(target=self.captureVideo, args=(self.queue,))
        thread_sendVideo = threading.Thread(target=self.sendVideo, args=(self.peerSocket, self.queue))
        thread_recieveVideo = threading.Thread(target=self.recieveVideo, args=(self.peerSocket,))
        thread_CaptureVideo.start()
        thread_sendVideo.start()
        thread_recieveVideo.start()

        # Waiting for thread has done
        thread_sendVideo.join()
        thread_recieveVideo.join()
        thread_CaptureVideo.join()
        
        # all thiread has done : end program
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

    def sendVideo(self, peerSocket, queue):
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
        print("{}:: terminating thread_sendVideo() ...".format(self.my_mode))

    def captureVideo(self, queue):
        # Add Webcam
        user_webcam = cv2.VideoCapture(self.myWebCam)
        # Get webcam's info & Print
        fr_width, fr_height, fps = user_webcam.get(
            3), user_webcam.get(4), user_webcam.get(cv2.CAP_PROP_FPS)
        print("{}_webcam frame width ({}), height({}), fps({})".format(
            self.my_mode, fr_width, fr_height, fps))
        while True:
            if self.op_state == "QUIT":
                break
            # Get data from user's webcam
            ret, frame = user_webcam.read()
            if ret is False:    # Error : can't get frame
                continue
            # Resizing Frame : Got from user's webcam
            resized_svrfr = cv2.resize(frame, (int(frame.shape[1] / 2), int(frame.shape[0] / 2)))
            # Set Frame's quality & Encoding to integer
            encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
            # Img encoding
            result, imgencode = cv2.imencode('.jpg', resized_svrfr, encode_param)
            img_data = np.array(imgencode)      # Make Img data with numpy
            stringData = img_data.tobytes()     # Convert Img data to String
            queue.put(stringData)               # Put data in Queue : ready for send Img data
            # Show user's cam
            cv2.imshow('{} :: My cam'.format(self.my_mode), resized_svrfr)
            # if ESC key is input, then exit
            key = cv2.waitKey(1)
            if key == 27:
                print("{} :: ESC key pressed => exit".format(self.my_mode))
                self.op_state = "QUIT"
                break
            time.sleep(0.05)
        print("{}:: terminating thread_captureVideo() ...".format(self.my_mode))

    def recieveVideo(self, peerSocket):
        while True:
            if self.op_state == "QUIT":
                break
            # Get length data of Img data
            length = self.recvall(peerSocket, 16)
            if length == 0 or length is None or length == b'':
                self.op_state = "QUIT"
                break
            # Get Img data & Save as string
            stringData = self.recvall(peerSocket, int(length))
            # Save to data as Set string data type uint8
            data = np.frombuffer(stringData, dtype='uint8')
            # Decoding data & Save to decimg
            decimg = cv2.imdecode(data, 1)
            # Print Get Img data
            cv2.imshow('{} :: Received video'.format(self.my_mode), decimg)
            # if ESC key is input, then exit
            key = cv2.waitKey(1)
            if key == 27:
                print("{} :: ESC key pressed => exit".format(self.my_mode))
                self.op_state = "QUIT"
                break
            time.sleep(0.05)
        print("{}:: terminating thread_recieveVideo() ...".format(self.my_mode))
