from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_PKCS1_v1_5
# pip install pycryptodome

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '.'))

from sqlitewrapper import SqliteCipher


# main class
class Enc_dec_handler:

    # constructor
    def __init__(self , exportedPublicKey , exportedPrivateKey , bits = 4096):
        
        # init keys
        self.publicKey = RSA.import_key(exportedPublicKey)
        self.privateKey = RSA.import_key(exportedPrivateKey)

        # init encrypting objects
        self.cipherPublic = Cipher_PKCS1_v1_5.new(self.publicKey)
        self.cipherPrivate = Cipher_PKCS1_v1_5.new(self.privateKey)

        # define chunks size
        self.bits = bits
        self.chunkSize = int(self.bits//12)


    # function to encrypt a string
    # returns byte type object
    def encryptor_str(self , string):

        string = str(string)

        # convert the string into chunks
        chunkList = []

        for i in range(0 , len(string) , self.chunkSize):
            chunkList.append(string[i : i + self.chunkSize])

        encodedStringList = []

        # encrypt the chunks
        for i in chunkList:
            encodedStringChunk = self.cipherPublic.encrypt(i.encode())
            encodedStringList.append(encodedStringChunk)

        # join the encrypted chunks and return
        cipher_text = b''.join(encodedStringList)
        return cipher_text


    # function to decrypt a encrypted string using above function
    # returns str
    def decryptor_str(self , encryptedStr):

        chunkList = []
 
        # as the encrypted chunk size is bits // 8 not matter the string input size 
        bitesby8 = self.bits//8

        # make chunks
        for i in range(0 , len(encryptedStr) , bitesby8):
            chunkList.append(encryptedStr[i : i + bitesby8])

        decodedStringList = []

        # decrypt chunks
        for i in chunkList:

            # skip if the chunk lenght is zero
            if(len(i) == 0):
                continue

            # sentinal is the object to return whenever the error is detacted , here it is None
            decodedStringChunk = self.cipherPrivate.decrypt(i , None)

            decodedStringList.append(decodedStringChunk)


        # combine decrypted chunks and return
        decipher_text = b''.join(decodedStringList)

        return decipher_text.decode()


    # returns byte type object
    def encryptor_byte(self , byteToEnc):

        # convert the string into chunks
        chunkList = []

        for i in range(0 , len(byteToEnc) , self.chunkSize):
            chunkList.append(byteToEnc[i : i + self.chunkSize])

        encodedBytesList = []

        # encrypt the chunks
        for i in chunkList:
            encodedBytesChunk = self.cipherPublic.encrypt(i)
            encodedBytesList.append(encodedBytesChunk)

        # join the encrypted chunks and return
        cipher_text = b''.join(encodedBytesList)
        return cipher_text


    # returns byte
    def decryptor_byte(self , encryptedByte):

        chunkList = []
 
        # as the encrypted chunk size is bits // 8 not matter the string input size 
        bitesby8 = self.bits//8

        # make chunks
        for i in range(0 , len(encryptedByte) , bitesby8):
            chunkList.append(encryptedByte[i : i + bitesby8])

        decodedBytesList = []

        # decrypt chunks
        for i in chunkList:

            # skip if the chunk lenght is zero
            if(len(i) == 0):
                continue

            # sentinal is the object to return whenever the error is detacted , here it is None
            decodedBytesChunk = self.cipherPrivate.decrypt(i , None)

            decodedBytesList.append(decodedBytesChunk)


        # combine decrypted chunks and return
        decipher_text = b''.join(decodedBytesList)

        return decipher_text


    # function to encrypt a string
    # returns byte type object
    def encryptor_str_external(self , string , publicKey):

        # init encrypting objects
        cipherPublic = Cipher_PKCS1_v1_5.new(publicKey)

        string = str(string)

        # convert the string into chunks
        chunkList = []

        for i in range(0 , len(string) , self.chunkSize):
            chunkList.append(string[i : i + self.chunkSize])

        encodedStringList = []

        # encrypt the chunks
        for i in chunkList:
            encodedStringChunk = cipherPublic.encrypt(i.encode())
            encodedStringList.append(encodedStringChunk)

        # join the encrypted chunks and return
        cipher_text = b''.join(encodedStringList)
        return cipher_text


    # function to decrypt a encrypted string using above function
    # returns str
    def decryptor_str_external(self , encryptedStr , privateKey):

        # init encrypting objects
        cipherPrivate = Cipher_PKCS1_v1_5.new(privateKey)

        chunkList = []
 
        # as the encrypted chunk size is bits // 8 not matter the string input size 
        bitesby8 = self.bits//8

        # make chunks
        for i in range(0 , len(encryptedStr) , bitesby8):
            chunkList.append(encryptedStr[i : i + bitesby8])

        decodedStringList = []

        # decrypt chunks
        for i in chunkList:

            # skip if the chunk lenght is zero
            if(len(i) == 0):
                continue

            # sentinal is the object to return whenever the error is detacted , here it is None
            decodedStringChunk = cipherPrivate.decrypt(i , None)

            decodedStringList.append(decodedStringChunk)


        # combine decrypted chunks and return
        decipher_text = b''.join(decodedStringList)

        return decipher_text.decode()


    # returns byte type object
    def encryptor_byte_external(self , byteToEnc , publicKey):

        # init encrypting objects
        cipherPublic = Cipher_PKCS1_v1_5.new(publicKey)

        # convert the string into chunks
        chunkList = []

        for i in range(0 , len(byteToEnc) , self.chunkSize):
            chunkList.append(byteToEnc[i : i + self.chunkSize])

        encodedBytesList = []

        # encrypt the chunks
        for i in chunkList:
            encodedBytesChunk = cipherPublic.encrypt(i)
            encodedBytesList.append(encodedBytesChunk)

        # join the encrypted chunks and return
        cipher_text = b''.join(encodedBytesList)
        return cipher_text


    # returns byte
    def decryptor_byte_external(self , encryptedByte , privateKey):

        # init encrypting objects
        cipherPrivate = Cipher_PKCS1_v1_5.new(privateKey)

        chunkList = []
 
        # as the encrypted chunk size is bits // 8 not matter the string input size 
        bitesby8 = self.bits//8

        # make chunks
        for i in range(0 , len(encryptedByte) , bitesby8):
            chunkList.append(encryptedByte[i : i + bitesby8])

        decodedBytesList = []

        # decrypt chunks
        for i in chunkList:

            # skip if the chunk lenght is zero
            if(len(i) == 0):
                continue

            # sentinal is the object to return whenever the error is detacted , here it is None
            decodedBytesChunk = cipherPrivate.decrypt(i , None)

            decodedBytesList.append(decodedBytesChunk)


        # combine decrypted chunks and return
        decipher_text = b''.join(decodedBytesList)

        return decipher_text




if __name__ == "__main__":

    dbObj = SqliteCipher(dataBasePath="iChatterData/iChatterData.db" , checkSameThread=False , password="helloboi")


    colList , resultList = dbObj.getDataFromTable("pubpirKeys" , omitID=True)


    exportedPublicKey = resultList[0][0]
    exportedPrivateKey = resultList[0][1]

    obj = Enc_dec_handler(exportedPublicKey , exportedPrivateKey)

    enc = obj.encryptor_str("x"*(2048))
    print(enc , type(enc))

    dec = obj.decryptor_str(enc)
    print(dec , type(dec))



    with open("images/Group7.svg" , "rb") as file:
        data = bytes(file.read())


    enc = obj.encryptor_byte(data)

    dec = obj.decryptor_byte(enc)

    with open("images/newTestedGroup7.svg" , "wb") as file:
        file.write(dec)


    


    


    

    
        

