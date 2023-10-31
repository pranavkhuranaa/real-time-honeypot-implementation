import hashlib 
import json
import sys
import getch
secret_key = "s3cr3t"

def hash256(text,salt):
    text = text.encode()
    salt = salt.encode()
    return hashlib.sha256(text+salt).hexdigest()

def password(plaintext,salt):
    salt1 = hash256(secret_key,salt)
    hsh = hash256(plaintext,salt1)
    return "".join((salt1,hsh))

def generatepassword(plaintext,salt,alp,length=10):
    alphabet = ('abcdefghijklmnopqrstuvwxyz'
            'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            '0123456789')
    if(alp == 1):
        alphabet = alphabet + '!@#$%^&*()-_'

    hexdig = password(plaintext,salt)
    num = int(hexdig,16)

    num_chars = len(alphabet)

    chars = []
    while len(chars) < length:
        num, idx = divmod(num, num_chars)
        chars.append(alphabet[idx])

    return ''.join(chars)

def writeToJSONFile(path, fileName, data):
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'a') as fp:
        #json.dump("data=",fp)
        json.dump(data, fp)

a=input("\nEnter username: ")
# pw = input("Enter password: ");
print("\nEnter password: ", end=" ")

passwor = ''
while True:
    x = getch.getch()
    # x = msvcrt.getch().decode("utf-8")
    if x == '\r' or x == '\n':
        break
    print('*', end='', flush=True)
    passwor +=x


b=input("\n\nEnter website name that will be redirected after successful login: ")
c=int(input("\nFor hash conversion:\nEnter 1 if you want special character or else enter 0: "))
d=generatepassword(a,b,c)

path = './'
fileName='data'
data = {}
data['username1'] = a
# data['password1'] = pw
data['password1'] = passwor
data['hash_password'] = d
 
writeToJSONFile(path,fileName,data)

print("\nCredentials created successfully and stored in 'data.json' file.\n\nFollowing are the details:\n")
print("\nUsername: ", a, "\nPassword: ",passwor, "\nHash password: ",d,"\nWebsite after successful login: ",b+"\n")






