# VideoChat_Client.py
from Class_VideoChat import VideoChat
# Application of VideoChat as TCP Client
if __name__ == "__main__":
    videoChatt_client = VideoChat("Client")
    videoChatt_client.run()