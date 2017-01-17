from Crypto.Cipher import AES
import string
import base64
import time
import os
#crypto method
PADDING = '{'
BLOCK_SIZE = 32
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
#encryption and decryption variables
EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)

loop=5
while loop==5:
    os.system('clear')
    print "                           .           "
    print "                           .           "
    print "           ,(              #%.         "
    print "       /%(/,,.             .*(#%&      "
    print "      /**......            ,.,,,//.    "
    print "     ,                     ..   ..(    "
    print "                                  .,   "
    print "    .     SKUL01TEXTCRYPT.py      .    "
    print "                                    .  "
    print "    .  ___ _        _    __   _    .   "
    print "  .   / __| |___  _| |  /  \ / |   .  ."
    print "  .   \__ \ / / || | |_| ()  | |   .   "
    print "      |___/_\_\\_,_|____\__/ |_|     . "
    print "                                  ..   "
    print " .....  Encryption / Decryption      ..."
    print "                                       "
     
    option=raw_input("Would you like to encrypt or decrypt?\n[a] Encrypt\n[b] Decrypt\n\nMY Ch0ice: ")
    if option=='a':
        letter=3
        while letter==3:
            secret = raw_input("Please Enter An Encryption Key {must be 16 characters long}\nKEY: ")
            countTotal= (len(secret))
            if countTotal==16:
                cipher = AES.new(secret)
                letter=0
            else:
                print "Please Ensure The Key You Entered Is 16 Characters In Length\n"
                letter=3

        data=raw_input("Please Enter Text You'd Like Encrypted\nText:")
        encoded = EncodeAES(cipher, data)
        print '\n[Successfully Encrypted]...\n'
        time.sleep(1)
        print 'Encrypted string:', encoded
        print '\nYou can now copy the encoded text and send it.'
        raw_input()
        options=raw_input("Would You Like To Encrypt/Decrypt Again? [y/n]\nMY CH0ICE: ")
        if options=='y':
            loop=5
        if options=='n':
            loop=0
          
    if option=='b':
      
        encoded=raw_input("Please Enter The Encoded String\nString:")
        letter=3
        while letter==3:
            secret=raw_input("Please Enter The Decryption Key\nKey:")
            countTotal= (len(secret))
         
            if countTotal==16:
                cipher = AES.new(secret)
                letter=0
                decoded = DecodeAES(cipher, encoded)
                time.sleep(1)
                print '\n[Successfully Decrypted]...\n'
                time.sleep(1)
                print 'Decrypted string:', decoded
                print '\nYou can now Copy the decoded text And save it.'
                raw_input()
                options=raw_input("Would You Like To Encrypt/Decrypt Again? [y/n]\nMY CH0ICE: ")
                if options=='y':
                    loop=5
                if options=='n':
                    loop=0
            else:
                print "Exiting due to invalid key."
                time.sleep(1)
                print "Please Ensure The Key You Entered Is 16 Characters In Length\n"
                exit
              
if loop==0:
    os.system('clear')
    print "Keep Your Text Safe. -SkuL01"
    time.sleep(2)
    exit
