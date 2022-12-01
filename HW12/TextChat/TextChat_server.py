# TextChat_Server.py
from Class_TextChat import TextChat
# Application of TextChat as TCP Server
if __name__ == "__main__":
    print("Running TCP server")
    textChatServer = TextChat("Server")
    textChatServer.win.mainloop()