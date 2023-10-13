def encrypt_text(text):
    encrypted = ""
    for e in text:
        if 'a' <= e <= 'z':
            if e == 'z':
                encrypted += 'A'
            else:
                encrypted += chr(ord(e.lower()) + 1).upper()
        elif 'A' <= e <= 'Z':
            if e == 'Z':
                encrypted += 'a'
            else:
                encrypted += chr(ord(e.lower()) + 1).lower()
        else:
            encrypted += e
    return encrypted

def decrypt_text(text):
    decrypted = ""
    for e in text:
        if 'a' <= e <= 'z':
            if e == 'a':
                decrypted += 'Z'
            else:
                decrypted += chr(ord(e.lower()) - 1).upper()
        elif 'A' <= e <= 'Z':
            if e == 'A':
                decrypted += 'z'
            else:
                decrypted += chr(ord(e.lower()) - 1).lower()
        else:
            decrypted += e
    return decrypted


text = "Python is a great choise!"

encrypted = encrypt_text(text)
print(encrypted)

decrypted = decrypt_text(encrypted)
print(decrypted)

encrypt_text(text)
decrypt_text(text)