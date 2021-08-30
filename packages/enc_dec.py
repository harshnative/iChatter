from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_PKCS1_v1_5
# pip install pycryptodome

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '.'))

from sqlitewrapper import SqliteCipher
import json

class Enc_dec_handler:

    def __init__(self , strPublicKey , strPrivateKey):
        self.publicKey = RSA.import_key(strPublicKey)
        self.privateKey = RSA.import_key(strPrivateKey)
        self.cipherPublic = Cipher_PKCS1_v1_5.new(self.publicKey)
        self.cipherPrivate = Cipher_PKCS1_v1_5.new(self.privateKey)
        self.chunkSize = int(2048//12)
        self.randomStringSeperator = b"1w0cMwcEjlFdH30UQDsO5xdNiQ0ndJ5gdW3Z0dK78pfsjOvDQ71WQ65S7N2tlmrWb57Ozk14i7DflP296S1VOgnYbHMjN6rh7ab97Y94dDDSu6MUY8KxDk39tVb1al89"
        



    # returns byte type object
    def encryptor_str(self , string):

        string = str(string)

        chunkList = []

        for i in range(0 , len(string) , self.chunkSize):
            chunkList.append(string[i : i + self.chunkSize])

        encodedStringList = []

        for i in chunkList:
            encodedStringChunk = self.cipherPublic.encrypt(i.encode())
            encodedStringList.append(encodedStringChunk)
            encodedStringList.append(self.randomStringSeperator)

        cipher_text = b''.join(encodedStringList)
        return cipher_text


    # returns str
    def decryptor_str(self , encryptedStr):
        chunkList = encryptedStr.split(self.randomStringSeperator)

        # print(len(encryptedStr))

        # for i in range(0 , len(encryptedStr) , self.chunkSize):
        #     chunkList.append(encryptedStr[i : i + self.chunkSize])

        decodedStringList = []

        for i in chunkList:

            if(len(i) == 0):
                continue

            # sentinal is the object to return whenever the error is detacted , here it is None
            decodedStringChunk = self.cipherPrivate.decrypt(i , None)

            decodedStringList.append(decodedStringChunk)

        decipher_text = b''.join(decodedStringList)

        return decipher_text.decode()


    # returns byte type object
    def encryptor_byte(self , byteToEnc):
        chunkList = []

        for i in range(0 , len(byteToEnc) , self.chunkSize):
            chunkList.append(byteToEnc[i : i + self.chunkSize])

        encodedByteList = []

        for i in chunkList:
            i = str(i)
            encodedByteChunk = self.cipherPublic.encrypt(i)
            encodedByteList.append(encodedByteChunk)

        cipher_text = b''.join(encodedByteList)
        return cipher_text


    # returns byte
    def decryptor_byte(self , encryptedByte):

        chunkList = []

        for i in range(0 , len(encryptedByte) , self.chunkSize):
            chunkList.append(encryptedByte[i : i + self.chunkSize])

        decodedByteList = []

        for i in chunkList:

            # sentinal is the object to return whenever the error is detacted , here it is None
            decodedByteChunk = self.cipherPrivate.decrypt(i , None)

            decodedByteList.append(decodedByteChunk)

        decipher_text = b''.join(decodedByteList)

        return decipher_text




if __name__ == "__main__":

    dbObj = SqliteCipher(dataBasePath="iChatterData/iChatterData.db" , checkSameThread=False , password="helloboi")


    colList , resultList = dbObj.getDataFromTable("pubpirKeys" , omitID=True)


    strPublicKey = resultList[0][0]
    strPrivateKey = resultList[0][1]

    obj = Enc_dec_handler(strPublicKey , strPrivateKey)

    enc = obj.encryptor_str("x"*(2048//13))
    print(enc , type(enc))

    dec = obj.decryptor_str(enc)
    print(dec , type(dec))


    chunkList = []

    with open("images/Group7.svg" , "rb") as file:
        data = bytes(file.read())


    


    


    

    
        

