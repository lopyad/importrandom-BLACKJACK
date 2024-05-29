import csv
import hashlib

def hash_passwd(passwd):
    return hashlib.sha256(passwd.encode()).hexdigest()

def try_login(inputName, inputPasswd, members):
    loginSuccess = False

    for name in members.keys():
        if name == inputName:
            if members[name][0] == hash_passwd(inputPasswd):
                loginSuccess = True
            else:
                print("incorrect passwd")
            break
            
    if loginSuccess:
        print("Welcome", inputName)
    else:
        print(inputName + " is not member in BLACKJACK")
    
    return loginSuccess

def load_members():
    #file = open("/home/jmlee/Documents/Python-code/blackjack+/members.csv","r")
    file = open("members.csv","r")
    members = {}
    for line in file:
        name, passwd, chips = line.strip('\n').split(',')
        members[name] = (passwd, int(chips))
    file.close()
    return members

#print(hash_passwd("test"))