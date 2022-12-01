# VideoChatting Server - class Video-Chatting Server with OpenCV and socket
from Class_VideoChat import VideoChat

if __name__ == "__main__":
    videoChatt_server = VideoChat("Server")
    videoChatt_server.run()