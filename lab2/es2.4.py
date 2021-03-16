from socket import *

serverPort = 12000
serverSocket = socket(AF_INET,SOCK_DGRAM)
binding = ('', serverPort)
serverSocket.bind(binding)

print ("Ready...")

while 1:
    message, clientAddress = serverSocket.recvfrom(2048)
    print("client address: ",clientAddress)
    message = message.decode('utf-8')
    num = int(message)
    flag = "primo"
    for i in range(2,num)
        if (num%i == 0)
            flag = "non primo"
            break
    serverSocket.sendto(flag.encode('utf-8'),clientAddress)
