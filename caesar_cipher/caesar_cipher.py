

def arrange(char,key):
    char_num = ord(char) 
    
    offset = 65 if char == char.upper() else 97
    
    shifted_num = char_num + key - offset
    
    mod_num = shifted_num % 26 + offset
    
    return mod_num

import re


def encrypt(text:str,key:int):
    
    words = text.split()
    cipher_words = []
    for word in words:
        
        cipher = ""
        for char in word:
            if not re.match(r'[^a-zA-Z]',char):
                mod_num = arrange(char,key)
                cipher += chr(mod_num)
            else:
                cipher += char
        cipher_words.append(cipher)    
    return " ".join(cipher_words)
    

def decrypt(text:str,key:int):
    return encrypt(text, -key)


