from caesar_cipher.caesar_cipher import decrypt, encrypt
from caesar_cipher.crack import crack

"""
TODO:[X] encrypt a string with a given shift
TODO:[X] decrypt a previously encrypted string with the same shift
TODO:[X] encryption should handle upper and lower case letters
TODO:[X] encryption should allow non-alpha characters but ignore them, including white space
TODO:[X] decrypt encrypted version of It was the best of times, it was the worst of times. WITHOUT knowing the shift used.
TODO:[X] refer to supplied unit tests.
"""

def test_encrypt_a_string_with__given_shift():
    
    actual = encrypt("apple", 1)
    expected = "bqqmf"
    
    results = [actual == expected]
    
    actual = encrypt("apple", 20)
    expected = "ujjfy"
    
    results+= [actual == expected]
    
    assert all(results)

def test_decrypt_string_with_same_shift():

    actual = decrypt("bqqmf", 1)
    expected = "apple"

    results = [actual == expected]
    
    actual = decrypt("ujjfy", 20)
    expected = "apple"
    
    results.append(actual == expected)
    
    assert all(results)

def test_encryption_handle_upper_lower_cahar_same_shift():
    actual = encrypt("BANANA", 10)
    expected = "LKXKXK"
    assert actual == expected

def test_ignore_nonalpha_chars():
    actual = encrypt("apples and bananas", 1)
    expected = "bqqmft boe cbobobt"
    
    results = [actual == expected]
    
    actual = encrypt("Gimme a 1!", 1)
    expected = "Hjnnf b 1!"
    
    results.append(actual == expected)
    
    assert all(results)
   
def test_round_trip():
    original = "Gimme a 1!"
    shift = 5
    encrypted = encrypt(original, shift)
    actual = decrypt(encrypted, shift)
    expected = original
    assert actual == expected

def test_decrypt_string_without_shift():
    phrase = "It was the best of times, it was the worst of times."
    encrypted = encrypt(phrase, 10)
    actual = crack(encrypted)
    expected = phrase
    assert actual == expected

def test_crack_nonsense():
    phrase = "Ix fhw txe fofg of ndhrl, it nad tho hndrk of allkd."
    encrypted = encrypt(phrase, 10)
    actual = crack(encrypted)
    expected = None
    assert actual == expected
