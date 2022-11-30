# co routine

def echoMsg():
    print("Start echoMsg() co-routine")
    while True:
        msg = (yield)
        print("Received Msg = ", msg)


genMsg = echoMsg()
print("genMsg : ", genMsg)
next(genMsg)

genMsg.send("First")
genMsg.send("Second")
genMsg.send("Third")
genMsg.close()