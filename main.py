import display
import membermgmt
import blackjack
import minigame

def show_ranking(members):
	display.default("Ranking")
	print("check")
	print("%")
	for name in members.keys():
		print(name, members[name])
	_ = input()

def main():
	#setup
	global isLogined, userName
	isLogined = False
	members = membermgmt.load_members()

	#loop
	while True:
		if isLogined:
			display.main_menu(userName, members[userName])

			userInput = input(":")
			if not userInput in ["1", "2", "3", "4", "5"] or len(userInput)!=1:
				continue
			userInput = int(userInput)

			if userInput == 1:
				display.blackjack()
				blackjack.blackjack_game(userName, members)
				members = membermgmt.load_members()
			elif userInput == 2:
				display.minigame()
				minigame.minigame_game(userName, members)
				members = membermgmt.load_members()
			elif userInput == 3:
				display.default()
				_ = input()
			elif userInput == 4:
				show_ranking(members)
			elif userInput == 5:
				isLogined = False
		else:
			isLogined, userName = membermgmt.login(members)

main()

