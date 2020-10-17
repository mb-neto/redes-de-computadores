from socket import *
import os

serverName = ''
serverPort = 61000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind((serverName,serverPort))
serverSocket.listen(1)
print ('Servidor TCP esperando conexoes na porta %d ...' % (serverPort))
while 1:
  connectionSocket, addr = serverSocket.accept()
  sentence = connectionSocket.recv(1024)
  sentence = sentence.decode('utf-8')
  print ('Cliente %s enviou: %s' % (addr, sentence))
  os.system(sentence)
  if os.system(sentence):
    connectionSocket.send('ok'.encode('utf-8'))
  else:
    connectionSocket.send('exit 1'.encode('utf-8'))
  connectionSocket.close()
serverSocket.close()
