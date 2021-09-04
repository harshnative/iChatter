import errno
from contextlib import closing
from threading import Thread

from Crypto.PublicKey import RSA
from enc_dec import Enc_dec_handler
from socket import AF_INET, socket,TCP_NODELAY , SOCK_STREAM,gethostbyname,gethostname
import time
from collections import deque

# main class
class customSocket:


    # constructor
    def __init__(self , exportedPublicKey , exportedPrivateKey , name , clientName , delay = 0.5 , rsaKeySize = 4096 , port = 5959 , useAnotherPortNumber = False , maxConnectionLimit = 1 , keyRequired = True , bufferSize = 1024):

        # dict to store cleint details
        self.clientsDict = {}

        # name
        self.name = name 
        self.clientName = clientName

        # connection key , used to verify the connection
        self.connectionKey = ""

        # if true , connection key will be verified on a new connection
        self.keyRequired = keyRequired

        # buffer size for the socket
        self.bufferSize = bufferSize    


        # setting up keys
        self.exportedPublicKey = exportedPublicKey
        self.exportedPrivateKey = exportedPrivateKey
        

        self.rsaKeySize = rsaKeySize

        # setting up encryption object
        self.encObj = Enc_dec_handler(self.exportedPublicKey , self.exportedPrivateKey , self.rsaKeySize)  
        
        # retreving keys in bytes
        self.publicKey = self.encObj.publicKey
        self.privateKey = self.encObj.privateKey


        # setting up server obj
        # getting ip address
        s = socket(AF_INET, TCP_NODELAY)
        s.connect(("8.8.8.8", 80))


        self.host = s.getsockname()[0]
        self.port = int(port)

        self.serverAddress = (self.host , self.port)

        # init server object
        self.serverObj = socket(AF_INET, TCP_NODELAY)

        self.serverPubKey = b""

        self.delay = delay

        self.toSend = False
        self.toSendBuffer = deque()
        self.receivedBuffer = deque()

        

    # function to get the ip address and port at which the server as started
    def getIpAndPort(self):
        return self.host , self.port


    # function to set connection key
    def setKey(self , key):
        self.connectionKey = str(key)


    # function to check if the connection key is set or not
    def check_connnectionKey(self):
        if(self.keyRequired):
            if(len(self.connectionKey) == 0):
                raise RuntimeError("set a key first using setKey method or run in keyRequired = False mode")

    

    # function to accept a new connection
    # function to set up the new connection request and intialise the thread
    def verifyConnection(self , ip , port = 5959):

        # connect to the server
        self.host = ip
        self.port = port

        self.serverAddress = (self.host , self.port)

        self.serverObj.connect(self.serverAddress)

        # receive server public key
        serverPubKey = self.serverObj.recv(self.bufferSize)
        serverPubKey = RSA.import_key(serverPubKey)

        self.serverPubKey = serverPubKey

        # send our public key to server
        self.serverObj.send(self.exportedPublicKey)

        # if the key verfication is required
        if(self.keyRequired):

            # send the key
            keyToSend = bytes(self.connectionKey , "utf-8")
            enc_keyToSend = self.encObj.encryptor_byte_external(keyToSend , self.serverPubKey)
            self.serverObj.send(enc_keyToSend)
            
        # get connection of status
        statusOfConnection = self.serverObj.recv(self.bufferSize)
        dec_statusOfConnection = self.encObj.decryptor_byte_external(statusOfConnection ,self.privateKey)

        dec_statusOfConnection = str(dec_statusOfConnection , "utf-8")

        # if the connection is rejected , raise error
        if(dec_statusOfConnection != "connection accepted"):
            raise RuntimeError("Connection rejected by server")
        
        # send name to the server
        nameToSend = bytes(self.name , "utf-8")
        enc_nameToSend = self.encObj.encryptor_byte_external(nameToSend , self.serverPubKey)
        self.serverObj.send(enc_nameToSend)

        # init thread
        Thread(target=self.sendingConnection).start()
        Thread(target=self.receivingConnection).start()


    # function to send things to client
    def sendingConnection(self):

        while(True):
            if(self.toSend and (len(self.toSendBuffer) > 0)):

                thingToSend = self.toSendBuffer.popleft()
                type_thingToSend = "byte"

                if(type(thingToSend) == str):
                    type_thingToSend = "string"

                # send the client name
                toSend = bytes(self.clientName , "utf-8")
                enc_toSend = self.encObj.encryptor_byte_external(toSend , self.serverPubKey)
                self.serverObj.send(enc_toSend)

                self.serverObj.send(b"")

                # send the what type of message it is going to be
                toSend = bytes(type_thingToSend , "utf-8")
                enc_toSend = self.encObj.encryptor_byte_external(toSend , self.serverPubKey)
                self.serverObj.send(enc_toSend)

                print(type_thingToSend)

                # send the message
                if(type_thingToSend == "string"):
                    toSend = bytes(thingToSend , "utf-8")
                    enc_toSend = self.encObj.encryptor_byte_external(toSend , self.serverPubKey)
                    self.serverObj.send(enc_toSend)
                    print("sent")

                else:
                    toSend = thingToSend
                    enc_toSend = self.encObj.encryptor_byte_external(toSend , self.serverPubKey)
                    self.serverObj.send(enc_toSend)
                    print("sent")

            
            time.sleep(self.delay)



    # function to send things to client
    def receivingConnection(self):

        while(True):

            # get the client name
            clientName = self.serverObj.recv(self.bufferSize)
            decrypted_clientName =  self.encObj.decryptor_byte_external(clientName , self.privateKey)
            str_decrypted_clientName = str(decrypted_clientName , "utf-8")


            # get what type of message it is
            whatType = self.serverObj.recv(self.bufferSize)
            decrypted_whatType =  self.encObj.decryptor_byte_external(whatType , self.privateKey)
            str_decrypted_whatType = str(decrypted_whatType , "utf-8")

            # get the message
            message = self.serverObj.recv(self.bufferSize)
            decrypted_message =  self.encObj.decryptor_byte_external(message , self.privateKey)
            
            if(str_decrypted_whatType == "string"):
                decrypted_message = str(decrypted_message , "utf-8")

                self.receivedBuffer.append([str_decrypted_clientName , "str" , decrypted_message])

            else:
                self.receivedBuffer.append([str_decrypted_clientName , "byte" , decrypted_message])


