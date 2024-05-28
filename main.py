import display 

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

isLogined = False
while True:
	if isLogined:
		display.main_menu()

		userInput = input()
		if not userInput in ["1", "2", "3", "4", "5"] or len(userInput)!=1:
			continue
		userInput = int(userInput)

		if userInput == 1:
			play_blackjack()
		elif userInput == 2:
			play_minigames()
		elif userInput == 3:
			show_game_record()
		elif userInput == 4:
			show_ranking()
		elif userInput == 5:
			isLogined = False
	else:
		display.login_menu()

		## make login code
		_ = input()
		isLogined = True
		##
    


