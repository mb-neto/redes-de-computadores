from socket import *

serverName = 'localhost'
serverPort = 61000
clientSocket = socket(AF_INET, SOCK_DGRAM)

message = input('Digite data: ')
clientSocket.sendto(message.encode('utf-8'),(serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print ('O servidor (\'%s\', %d) respondeu com: %s' % (serverName, serverPort, modifiedMessage.decode('utf-8')))
clientSocket.close()