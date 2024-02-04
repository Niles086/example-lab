import string

def encrypt(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def crack(ciphertext):
    english_words = ["it", "was", "the", "best", "of", "times", "worst"]
    
    for shift in range(26):
        decrypted_text = decrypt(ciphertext, shift)
        words = decrypted_text.split()
        if all(word.lower() in english_words for word in words):
            return decrypted_text
    return ""