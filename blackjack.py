#import membermgmt
import random
import recorder
#import main

def fresh_deck():
    suits = { 'Spade', "Heart", 'Diamond', 'Club'}
    ranks = { 2,3,4,5,6,7,8,9,10,'J','Q','K','A'}
    deck = []
    for i in suits:
        for j in ranks:
            deck.append((i,j))
    random.shuffle(deck)
    return deck

def count_score(cards):
    score = 0
    number_of_ace = 0
    for card in cards:
        rank = card[1]
        if rank == 'A':
            rank = 11
            number_of_ace += 1
        elif rank in ['J','Q','K']:
            rank = 10
        score += rank
    while score > 21 and number_of_ace > 0:
        score -= 10
        number_of_ace -= 1
    return score

def draw_card(deck):
    if deck == []:
        deck = fresh_deck()
    return (deck[0], deck[1:])

    
        
def start_blackjack():
    deck = fresh_deck()
    user = []
    user_h = 'User : '
    dealer = []
    dealer_h = 'Dealer : '
    for i in range(2):
        draw, deck = draw_card(deck)
        user.append(draw)
        user_h += str(draw) + ' '
        draw, deck = draw_card(deck)
        dealer.append(draw)
        dealer_h += str(draw) + ' '
    position = dealer_h.find("('")
    position = dealer_h.find("('", position+1)
    print('Dealer : (****,**) ' + dealer_h[position:])
    print(user_h)
    while True:
        answer = input('hit? (Y/N)\n')
        while not(answer in ['Y', 'N']):
            answer = input('hit? (Y/N)\n')
        if answer == 'Y':
            draw, deck = draw_card(deck)
            user.append(draw)
            user_h += str(draw) + ' '
            print(user_h)
            score = count_score(user)
            if score > 21 :
                print('Bust!')
                input('Press enter...\n')
                return -1
            elif score == 21:
                print('Black jack!')
                input('Press enter...\n')
                return 2
            else:
                continue
        else:
            score = count_score(user)
            break
    print("\nDealer's turn\n")
    d_score = count_score(dealer)
    while d_score < 16 :
        draw, deck = draw_card(deck)
        dealer.append(draw)
        dealer_h += str(draw) + ' '
        d_score = count_score(dealer)
        print('Dealer : (****,**) ' + dealer_h[position:])
        input('Press enter...\n')
    print('Result')
    print(dealer_h)
    print(user_h)
    input('Press enter...\n')

    #recorder.save_result()

    if d_score > 21:
        print('You win!')
        return 1
    else:
        if score > d_score:
            print('You win!')
            return 1
        elif score == d_score:
            print('Deuce')
            return 0
        else:
            print('You lose...')
            return -1
        
def rewrite(members):
    content = ''
    for i in members:
        content += str(i)
        for j in members[i]:
            content += ',' + str(j)
        content += '\n'
    file = open('members.csv','w')
    file.write(content)
    file.close()
        
def blackjack_game(member, members):
    #members = membermgmt.load_members() #{이름:(비밀번호,칩(정수)),...} 의 딕셔너리의 형태로 유저 정보 추출
    game_num = members[member][1]
    wins = members[member][2]
    chips = members[member][3]
    answer = 'Y'
    while answer == 'Y':
        if chips <= 0:
            members[member] = (members[member][0], game_num, wins, chips)
            rewrite(members)
            print('Not enough chips')
            input('Press enter...\n')
            return 
        else:
            game_num += 1
            while True:
                try:
                    print('\nYour chips : ' + str(chips) + ' left')
                    bet = int(input('Bet your chips\n'))
                    assert bet <= chips
                except ValueError:
                    print('Not a number')
                except AssertionError:
                    print('Not enough chips')
                else:
                    print('\nYou bet ' + str(bet) + ' chips!')
                    break
        result = start_blackjack()
        
        

        if result > 0:
            wins += 1
        chips += int(bet)*result
        if chips < 0:
            chips = 0
        print('Your chips : ' + str(chips) + ' left')
        answer = input('Want to play more? (Y/N)\n')
        while not(answer in ['Y', "N"]):
            answer = input('Want to play more? (Y/N)\n')
    members[member] = (members[member][0], game_num, wins, chips)
    rewrite(members)
    print('Good bye\n')
    return 
    
    

#blackjack_game('test')