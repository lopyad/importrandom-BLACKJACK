import os
import platform
def clear_terminal():
    mySystem = platform.system()
    if mySystem == "Windows":
        os.system("cls")
    else:
        os.system("clear")

text_irblackjack = """
  _____ ______  _       ______  _       ___   _____  _   __   ___   ___   _____  _   __
 |_   _|| ___ \\( )      | ___ \\| |     / _ \\ /  __ \\| | / /  |_  | / _ \\ /  __ \\| | / /
   | |  | |_/ /|/  ___  | |_/ /| |    / /_\\ \\| /  \\/| |/ /     | |/ /_\\ \\| /  \\/| |/ / 
   | |  |    /    / __| | ___ \\| |    |  _  || |    |    \\     | ||  _  || |    |    \\ 
  _| |_ | |\\ \\    \\__ \\ | |_/ /| |____| | | || \\__/\\| |\\  \\/\\__/ /| | | || \\__/\\| |\\  \\
  \\___/ \\_| \\_|   |___/ \\____/ \\_____/\\_| |_/ \\____/\\_| \\_/\\____/ \\_| |_/ \\____/\\_| \\_/
"""

text_blackjack = """
______  _       ___   _____  _   __   ___   ___   _____  _   __
| ___ \\| |     / _ \\ /  __ \\| | / /  |_  | / _ \\ /  __ \\| | / /
| |_/ /| |    / /_\\ \\| /  \\/| |/ /     | |/ /_\\ \\| /  \\/| |/ / 
| ___ \\| |    |  _  || |    |    \\     | ||  _  || |    |    \\ 
| |_/ /| |____| | | || \\__/\\| |\\  \\/\\__/ /| | | || \\__/\\| |\\  \\
\\____/ \\_____/\\_| |_/ \\____/\\_| \\_/\\____/ \\_| |_/ \\____/\\_| \\_/
"""

text_play = """
______  _       ___  __   __  _  _  _ 
| ___ \\| |     / _ \\ \\ \\ / / | || || |
| |_/ /| |    / /_\\ \\ \\ V /  | || || |
|  __/ | |    |  _  |  \\ /   | || || |
| |    | |____| | | |  | |   |_||_||_|
\\_|    \\_____/\\_| |_/  \\_/   (_)(_)(_)
"""

text_minigame = """
___  ___ _         _   _____                         
|  \\/  |(_)       (_) |  __ \\                        
| .  . | _  _ __   _  | |  \\/  __ _  _ __ ___    ___ 
| |\\/| || || '_ \\ | | | | __  / _` || '_ ` _ \\  / _ \\
| |  | || || | | || | | |_\\ \\| (_| || | | | | ||  __/
\\_|  |_/|_||_| |_||_|  \\____/ \\__,_||_| |_| |_| \\___|
"""

def default(msg):
    clear_terminal()
    print(text_blackjack)
    print("[ " + msg + " ]")

myMenu = ["game start", "play minigames", "show my game record", "show user ranking", "log out", ""]
def main_menu(userName, userInfo):
    clear_terminal()
    print(text_blackjack)
    print(f"[{userName}, ◉ {userInfo[3]}]")
    
    myMenuLength = len(myMenu)
    for i in range(myMenuLength-1):
        print(str(i+1)+". "+myMenu[i])
    print(myMenu[myMenuLength-1])

def blackjack():
    clear_terminal()
    print(text_play)

def minigame():
    clear_terminal()
    print(text_minigame)