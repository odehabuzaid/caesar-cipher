import re

import enchant

from .caesar_cipher import decrypt

english = enchant.Dict("en_US")
def crack(text: str):
    for i in range(1, 27):
        # if i == 10:
        decrypted = decrypt(text, i)
        clean_text = re.sub(r"[^a-zA-Z0-9 \n\.]", "", decrypted)
        list_of_words = clean_text.split()
        true_words = list()
        for word in list_of_words:
            if english.check(word):
                true_words.append(word)
            
            if len(true_words) == len(list_of_words):
                return "".join(decrypted)
                    

