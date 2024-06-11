import display
import membermgmt
import blackjack

def play_blackjack():
	display.blackjack()
	_ = input()

def play_minigames():
	display.minigame()
	_ = input()

def show_game_record():
	display.blackjack()
	_ = input()

def show_ranking():
	display.blackjack()
	_ = input()

def login(members):
	display.login_menu("Hi, there!")
	global isLogined

	name = input("username: ")
	passwd = input("password: ")

	isLogined = membermgmt.try_login(name, passwd, members)

	global userName
	userName = name	
	_ = input("enter any key to continue...")

def main():
	global isLogined
	global userName
	isLogined = False
	members = membermgmt.load_members()

	while True:
		if isLogined:
			display.main_menu()

			userInput = input(":")
			if not userInput in ["1", "2", "3", "4", "5"] or len(userInput)!=1:
				continue
			userInput = int(userInput)

			if userInput == 1:
				blackjack.blackjack_game(userName, members)
			elif userInput == 2:
				play_minigames()
			elif userInput == 3:
				show_game_record()
			elif userInput == 4:
				show_ranking()
			elif userInput == 5:
				isLogined = False
		else:
			login(members)

main()

