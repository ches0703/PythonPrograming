# VideoChat_Server.py
from Class_VideoChat import VideoChat
# Application of VideoChat as TCP Seerver
if __name__ == "__main__":
    videoChatt_server = VideoChat("Server")
    videoChatt_server.run()