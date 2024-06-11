import csv
import hashlib

def hash_passwd(passwd):
    return hashlib.sha256(passwd.encode()).hexdigest()

""" example
username: test
passwd: test 
"""
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
    
    return inputName, loginSuccess

def load_members():
    file = open("members.csv","r")
    members = {}
    for line in file:
        name, passwd, trys, wins, chips= line.strip('\n').split(',')
        members[name] = (passwd, int(trys), int(wins), int(chips))
    file.close()
    return members

#print(hash_passwd("test"))