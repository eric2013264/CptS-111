import string

def cleanup(phrase):
    phrase = phrase.replace(' ','')                            
    phrase = phrase.lower();                                  
    for letter in phrase:                                   
        if letter in string.punctuation:
            phrase = phrase.replace(letter, '')
    return phrase

def encrypt(phrase, en_key):
    output = ""
    key_spot = 0

    for position,c in enumerate(phrase):                      
        shift_amount = ord(en_key[key_spot])-96                
        en_char = ord(phrase[position])-96+shift_amount        
        if en_char > 26:                                      
            en_char = en_char - 26

        output += str(chr(en_char+96))                        

        key_spot += 1                                         
        if key_spot >= len(en_key):
             key_spot = 0

    return output                                              

def generate_decryption_key(en_key):                          
    dec_key = ""
    for c in en_key.upper():
        dec_key += chr(90 - (ord(c) - 64)%26)                  
    return dec_key.lower()                                     

def decrypt(phrase, dec_key):
    return encrypt(phrase, generate_decryption_key(dec_key))                                            

def crack(phrase):
    """coming soon"""
    return 0

while True: 

    choice = str(raw_input("Do you wish to encrypt or decrypt(e/d): "))
    if choice == 'e':
        phrase = str(raw_input("Input a phrase to encrypt: "))
        phrase = cleanup(phrase)
        en_key = str(raw_input("Input a key: "))
        en_key = cleanup(en_key)

        print encrypt(phrase, en_key)
        print "Encrypt using %s, or decrypt using %s" % (generate_decryption_key(en_key), en_key)
    else:
        phrase = str(raw_input("Input a phrase to decrypt: "))
        phrase = cleanup(phrase)
        en_key = str(raw_input("Input a key: "))
        en_key = cleanup(en_key)

        print decrypt(phrase, en_key)

    again = str(raw_input("Go again? y/n"))
    if again == "n":
        quit()
