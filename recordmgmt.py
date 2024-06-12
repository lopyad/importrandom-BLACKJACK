import display

def save_result(userName, result):
    pass

def show_ranking(userName, members):
    display.default("Ranking")
    
    copiedMembers = members.copy()
    copiedMembers = sorted(copiedMembers.items(), key = lambda x: x[1][3], reverse=True)
    
    print("| %4s | %10s | %7s | %7s | %5s |"%("rank", "userName", "playCnt", "winRate", "chips"))
    idx = 1
    for member in copiedMembers:
        print("| %4d | %10s | %7s | %7s | %5s |"%(idx, member[0], member[1][1], member[1][2], member[1][3]))
        idx += 1

    print()
    _ = input("press enter to continue...")

# result -> 승패여부, 유저 손패, 딜러 손패