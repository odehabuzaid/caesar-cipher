

def arrange(char,key):
    if not char.isdigit():
        char_num = ord(char) 

        offset = 65 if char == char.upper() else 97
        
        shifted_num = char_num + key - offset
        
        mod_num = shifted_num % 26 + offset

        return mod_num


def encrypt(text:str,key:int):

    words = text.split()
    cipher_words = []
    for word in words:
        cipher = ""
        for char in word:
            mod_num = arrange(char,key)
            cipher += chr(mod_num)
        cipher_words.append(cipher)
    return " ".join(cipher_words)
    
print(encrypt('apple',20))
def decrypt(text:str,key:int):
    return encrypt(text, -key)

    
def crack(test:str,key:int):
    pass
