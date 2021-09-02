import socket 
import errno
from contextlib import closing
from threading import Thread
from enc_dec import Enc_dec_handler
from socket import AF_INET, socket, SOCK_STREAM,gethostbyname,gethostname
from Crypto.PublicKey import RSA


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

        try:

            # bind the server
            self.serverObj.bind(self.serverAddress)

        except socket.error as e:

                # if the port number is unavailable
                if(e.errno == errno.EADDRINUSE):

                    # if using another port is not allowed
                    if(useAnotherPortNumber):
                        raise RuntimeError("{} port is currenlty in use".format(self.port))

                    else:

                        # getting the port number
                        with closing(s) as s:
                            s.close()
                            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

                            s.bind(('', 0))
                            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                                
                            # assign the port to object
                            self.port = s.getsockname()[1]

                            # initialising serve object
                            s.close()

                        self.serverAddress = (self.host , self.port)
                        self.serverObj.bind(self.serverAddress)

        self.serverObj.listen(maxConnectionLimit)

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


    # function to start accepting connection thread
    def startAcceptingConnection(self):
        startThreading = Thread(target=self._acceptIncomingConnection)
        startThreading.start()
    

    # function to accept a new connection
    # function to set up the new connection request and intialise the thread
    def _acceptIncomingConnection(self):

        # virtually can handle unlimited connections
        while(True):

            client , clientAddress = self.serverObj.accept()

            client.send(self.exportedPublicKey)

            clientPubKey = client.recv(self.bufferSize)
            clientPubKey = RSA.import_key(clientPubKey)

            if(self.keyRequired):
                verificationKey = client.recv(self.bufferSize)

                decrypted_verificationKey = self.encObj.decryptor_byte_external(verificationKey , self.privateKey)

                strDecrypted_verificationKey = str(decrypted_verificationKey , "utf-8")

                if(strDecrypted_verificationKey != self.connectionKey):
                    toSend = bytes("connection rejected" , "utf-8")
                    toSendEnc = self.encObj.encryptor_byte_external(toSend , clientPubKey)
                    client.send(toSendEnc)
                    continue
                else:
                    toSend = bytes("connection accepted" , "utf-8")
                    toSendEnc = self.encObj.encryptor_byte_external(toSend , clientPubKey)
                    client.send(toSendEnc)

            # storing the new connection details in dictionary
            self.clientsDict[client] = [clientAddress , clientPubKey]

            # init thread
            # Thread(target=cls.handleClient , args=(client , )).start()