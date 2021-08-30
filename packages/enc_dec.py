from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_PKCS1_v1_5
# pip install pycryptodome

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '.'))

from sqlitewrapper import SqliteCipher

class Enc_dec_handler:

    def __init__(self , strPublicKey , strPrivateKey):
        self.publicKey = RSA.import_key(strPublicKey)
        self.privateKey = RSA.import_key(strPrivateKey)
        self.cipherPublic = Cipher_PKCS1_v1_5.new(self.publicKey)
        self.cipherPrivate = Cipher_PKCS1_v1_5.new(self.privateKey)



    # returns byte type object
    def encryptor_str(self , string):
        string = str(string)
        cipher_text = self.cipherPublic.encrypt(string.encode())
        return cipher_text

    # returns str
    def decryptor_str(self , encryptedStr):

        # sentinal is the object to return whenever the error is detacted , here it is None
        decipher_text = self.cipherPrivate.decrypt(encryptedStr , None).decode()

        return decipher_text


    # returns byte type object
    def encryptor_byte(self , byteToEnc):
        cipher_text = self.cipherPublic.encrypt(byteToEnc)
        return cipher_text

    # returns byte
    def decryptor_byte(self , encryptedByte):

        # sentinal is the object to return whenever the error is detacted , here it is None
        decipher_text = self.cipherPrivate.decrypt(encryptedByte , None)

        return decipher_text





if __name__ == "__main__":

    dbObj = SqliteCipher(dataBasePath="iChatterData/iChatterData.db" , checkSameThread=False , password="helloboi")


    colList , resultList = dbObj.getDataFromTable("pubpirKeys" , omitID=True)


    strPublicKey = resultList[0][0]
    strPrivateKey = resultList[0][1]

    obj = Enc_dec_handler(strPublicKey , strPrivateKey)

    enc = obj.encryptor_str("x"*(2048//10))
    print(enc , type(enc))

    dec = obj.decryptor_str(enc)
    print(dec , type(dec))

    chunkSize = 2048//10

    chunkList = []

    with open("images/Group7.svg" , "rb") as file:
        data = bytes(file.read())


    for i in range(0 , len(data) , chunkSize):
        print(i , i+chunkSize)
        chunkList.append(data[i : i+chunkSize])


    print(len(data) , (2048//10))

    for i in chunkList:
        print(i , type(i))
        print()

    print(len(chunkList))

    encList = []

    for i in chunkList:
        encByte = obj.encryptor_byte(i)
        encList.append(encByte)

    print("\n\n\n")

    for i in encList:
        print(i , type(i))
        print()

    print(len(encList))

    decList = []

    for i in encList:
        decList.append(obj.decryptor_byte(i))

    newData = b''.join(decList)

    with open("images/newTestedGroup7.svg" , "wb") as file:
        file.write(newData)


    


    

    
        

