import random
import string

chars=" "+string.punctuation+string.digits+string.ascii_letters
chars=list(chars)
key=chars.copy()
key=list(key)
random.shuffle(key)


pt=input("enter your password : ")
cipher=""

for letter in pt:
    index = chars.index(letter)
    cipher += key[index]
print(f"password in letters:  {pt}")    
print(f"the encrypted code is: {cipher}")

cipher=input("enter the cipher code: ")
pt=""
for letter in cipher:
    index = key.index(letter)
    pt += chars[index]
print(f"the cipher code is:{cipher}")
print(f"the message is:{index}")