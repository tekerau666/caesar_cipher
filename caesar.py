import re

alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя".upper()


def removeSpecialCharacters(text) -> str:
    return re.sub('\W+', '', text)


def Encrypt(plainText, key):
    key = int(key)
    plainText = removeSpecialCharacters(plainText).upper()
    cipherText = ''
    for i in range(len(plainText)):
        index = alphabet.index(plainText[i])
        cipherIndex = (index + key) % 33
        cipherChar = alphabet[cipherIndex]
        cipherText = cipherText + cipherChar
    return cipherText

def Decrypt(cipherText):
    with open('decipher.txt', 'w') as file:
        for i in range(1, 33):
            for char in cipherText:
                file.write(alphabet[(alphabet.index(char) - i) % 33])
            file.write('\n')