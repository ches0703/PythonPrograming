# TextChat_Client.py
from Class_TextChat import TextChat
# Application of TextChat as TCP Client
if __name__ == "__main__":
    print("Running TCP Client")
    textChatClient = TextChat('Client')
    textChatClient.win.mainloop()