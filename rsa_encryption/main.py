'''
Created on Sep 22, 2012

@author: Joseph Lee
'''
from encryption import Encryption

def main():
    enc = Encryption()
    print("Encrypting message: The Queen Can't Roll When Sand is in the Jar.")
    message = "The Queen Can't Roll When Sand is in the Jar."
    message = enc.encrypt(message)
    print(message)
    print()
    print("Decrypting message:")
    message = enc.decrypt(message)
    print(message)
    
    input("--Press any key to end--")

if __name__ == '__main__':
    main()