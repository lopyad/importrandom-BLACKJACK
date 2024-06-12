import display

def save_result(userName, result):
    try: 
        file = open(f"record/{userName}.txt","a")

        #data = f"---\n{result[0]}\n{result[1]}\n{result[2]}\n---\n"
        data = "---\n"
        for msg in result:
            data +=f"{msg}\n"
        data += "---\n"

        file.write(data)
    finally:
        file.close()

def read_game_record(userName):
    try: 
        file = open(f"record/{userName}.txt","r")
        #print(file)
        for line in file.readlines():
            print(line, end="")
    finally:
        file.close()
    
    _ = input("press enter to continue...")

def show_ranking(userName, members):
    display.default("Ranking")
    
    copiedMembers = members.copy()
    copiedMembers = sorted(copiedMembers.items(), key = lambda x: x[1][3], reverse=True)
    
    print("| %4s | %10s | %7s | %6s | %5s |"%("rank", "userName", "playCnt", "winCnt", "chips"))
    idx = 1
    for member in copiedMembers:
        print("| %4d | %10s | %7s | %6s | %5s |"%(idx, member[0], member[1][1], member[1][2], member[1][3]))
        idx += 1

    print()
    _ = input("press enter to continue...")

# result -> 승패여부, 유저 손패, 딜러 손패
#save_result("lopyad", "")