import socket 
import errno
from contextlib import closing
from threading import Thread

from Crypto.PublicKey import RSA
from enc_dec import Enc_dec_handler
from socket import AF_INET, socket, SOCK_STREAM,gethostbyname,gethostname

# main class
class customSocket:


    # constructor
    def __init__(self , exportedPublicKey , exportedPrivateKey , rsaKeySize = 4096 , port = 5959 , useAnotherPortNumber = False , maxConnectionLimit = 1 , keyRequired = True , bufferSize = 1024):

        # dict to store cleint details
        self.clientsDict = {}

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
        s = socket(AF_INET, SOCK_STREAM)
        s.connect(("8.8.8.8", 80))


        self.host = s.getsockname()[0]
        self.port = int(port)

        self.serverAddress = (self.host , self.port)

        # init server object
        self.serverObj = socket(AF_INET, SOCK_STREAM)

        self.serverPubKey = b""

        

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

        self.host = ip
        self.port = port

        self.serverAddress = (self.host , self.port)

        self.serverObj.connect(self.serverAddress)

        serverPubKey = self.serverObj.recv(self.bufferSize)
        serverPubKey = RSA.import_key(serverPubKey)

        self.serverPubKey = serverPubKey

        self.serverObj.send(self.exportedPublicKey)

        if(self.keyRequired):
            keyToSend = bytes(self.connectionKey , "utf-8")
            enc_keyToSend = self.encObj.encryptor_byte_external(keyToSend , self.serverPubKey)
            self.serverObj.send(enc_keyToSend)
            
            statusOfConnection = self.serverObj.recv(self.bufferSize)
            dec_statusOfConnection = self.encObj.decryptor_byte_external(statusOfConnection ,self.privateKey)

            dec_statusOfConnection = str(dec_statusOfConnection , "utf-8")





