import csv
import hashlib
import display 

def hash_passwd(passwd):
    return hashlib.sha256(passwd.encode()).hexdigest()

""" example
username: test
passwd: test 
"""

def login(members):
    display.default("Hi, there! (If you have no account, plz input 'register' instead name)")

    name = input("username: ")

    if name == "register":
        add_newMember(members)
        return False, None
    
    passwd = input("password: ")

    

    isLogined = try_login(name, passwd, members)

    _ = input("press enter to continue...")

    return isLogined, name

def try_login(inputName, inputPasswd, members):
    loginSuccess = False
    passwdFailed = False

    for name in members.keys():
        if name == inputName:
            if members[name][0] == hash_passwd(inputPasswd):
                loginSuccess = True
            else:
                passwdFailed = True
                print("incorrect passwd")
            break
            
    if loginSuccess:
        print("Welcome", inputName)
    elif not passwdFailed:
        print(inputName + " is not member in BLACKJACK")
    
    return loginSuccess

def load_members():
    try: 
        file = open("members.csv","r")
        members = {}
        for line in file:
            name, passwd, trys, wins, chips= line.strip('\n').split(',')
            members[name] = (passwd, int(trys), int(wins), int(chips))
    finally:
        file.close()
    return members

def add_newMember(members):
    display.default("Input new member's name and passwd")

    name = input("username(only alphabet): ")
    passwd = input("password: ")

    if name in ["", "register"] or name.isalpha()==False:
        print(f"You can't use '{name}' in BLACKJACK")
        _ = input("press enter to continue...")
        return
    elif members.get(name) != None:
        print(f"{name} is already exist in BLACKJACK")
        _ = input("press enter to continue...")
        return
    elif len(name) > 10:
        print(f"'{name}' is too long (max length is 10)")
        _ = input("press enter to continue...")
        return
    
    if passwd == "":
        print("plz input password")
        _ = input("press enter to continue...")
        return

    try:
        file = open("members.csv","a")
        data = f"{name},{hash_passwd(passwd)},0,0,5000\n"
        print(data, type(data))
        file.write(data)
        print("Successfully add newMember")
    finally:
        file.close()


    _ = input("press enter to continue...")

#print(hash_passwd("test"))
#add_newMember()