


def encrypt(text:str,key:int):
    offset = 65
    words = text.split()
    cipher_words = []
    for word in words:
        cipher = ""
        for char in word:
            char_num = ord(char.upper()) if char.upper() else ord(char.lower())
            shifted_num = char_num + key - offset
            mod_num = shifted_num % 26 + offset
            cipher += chr(mod_num)
        cipher_words.append(cipher)
    return " ".join(cipher_words).lower()
    

def decrypt(text:str,key:int):
    return encrypt(text, -key)

    
def crack(test:str,key:int):
    pass
