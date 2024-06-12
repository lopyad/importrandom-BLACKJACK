import random
import blackjack
from time import perf_counter

def minigame_game(name, members):
    game_num = members[name][1]
    wins = members[name][2]
    chips = members[name][3]
    answer = ''
    print('=========Minigame=========')
    print('You can get 1~5 chips')
    print('Wirte target word as fast as you can\n(If you want to back to the menu, write "out")')
    input('Ready? Press enter...')
    print()
    while True:
        word = chr(random.randrange(97, 123))
        print('Target word : ' + word)
        print('(Exit : "out")')
        start = perf_counter()
        answer = input('Answer : ')
        if answer == 'out':
            break
        finish = perf_counter()
        gain = int(5 / (finish*2 - start*2))
        if gain > 5:
            gain = 5
        elif gain <= 0:
            print("It's too late...\n")
            continue
        
        if answer == word:
            print('Correct! You got ' + str(gain) + ' chips!\n')
            chips += gain
        else:
            print('Wrong...\n')
    members[name] = (members[name][0], game_num, wins, chips)
    blackjack.rewrite(members)
    print('==========Result==========')
    print('Your total chips : ' + str(chips))
    input('Good bye')
    #print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    return

