from socket import * # sockets
import time

serverName = ''
serverPort = 61000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind((serverName, serverPort))
print ('Servidor UDP esperando conexoes na porta %d ...' % (serverPort))
while 1:
    message, clientAddress = serverSocket.recvfrom(2048)
    message = message.decode('utf-8')
    if message == "data":
      modifiedMessage = time.ctime()
      print ('Cliente %s enviou: %s, transformando em: %s' % (clientAddress, message, str(modifiedMessage)))
      serverSocket.sendto(modifiedMessage.encode('utf-8'), clientAddress) 
    else: 
      modifiedMessage = "Comando inválido"
      serverSocket.sendto(modifiedMessage.encode('utf-8'), clientAddress)
serverSocket.close()
