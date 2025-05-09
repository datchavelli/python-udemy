import random
import os
import sys

clubs = {
    'A': '''
         _________
        |A        |
        |♣   *    |
        |    !    |
        |  *-♣-*  |
        |    |    |
        |   ~~~  ♣|
        |        V|
         ~~~~~~~~~
         '''
    ,
    'K': '''
         _________
        |K |/|\|  |
        |♣ /o,o\  |
        |  \ _-_/ |
        | ~-_-~-_ |
        |  /~-~\  |
        |  \o`o/ ♣|
        |  |\ |/ X|
         ~~~~~~~~~~
         '''
    ,
    'Q': '''
         _________
        |Q |~~~|  |
        |♣ /o,o\  |
        |  \ _-_/ |
        | _-~♣_-~ |
        |  /~-~\  |
        |  \o`o/ ♣|
        |  |___| Q|
         ~~~~~~~~~
         '''
    ,
    'J': '''
         _________
        |J /~~|_  |
        |♣ | o`,  |
        |  | -|   |
        | =~)♣(_= |
        |   |- |  |
        |  `.o | ♣|
        |  ~|__/ P|
         ~~~~~~~~~
         '''
    ,
    '10': '''
         _________
        |10♣   ♣  |
        |♣   ♣    |
        |  ♣   ♣  |
        |         |
        |  ♣   ♣  |
        |    ♣   ♣|
        |  ♣   ♣0l|
         ~~~~~~~~~
         '''
    ,
    '9': '''
         _________
        |9 ♣   ♣  |
        |♣        |
        |  ♣   ♣  |
        |    ♣    |
        |  ♣   ♣  |
        |        ♣|
        |  ♣   ♣ 6|
         ~~~~~~~~~
         '''
    ,
    '8': '''
         _________
        |8 ♣   ♣  |
        |♣        |
        |  ♣   ♣  |
        |         |
        |  ♣   ♣  |
        |        ♣|
        |  ♣   ♣ 8|
         ~~~~~~~~~
         '''
    ,
    '7': '''
         _________
        |7        |
        |♣ ♣   ♣  |
        |    ♣    |
        |  ♣   ♣  |
        |         |
        |  ♣   ♣ ♣|
        |        L|
         ~~~~~~~~~
         '''
    ,
    '6': '''
         _________
        |6        |
        |♣ ♣   ♣  |
        |         |
        |  ♣   ♣  |
        |         |
        |  ♣   ♣ ♣|
        |        9|
         ~~~~~~~~~
         '''
    ,
    '5': '''
         _________
        |5        |
        |♣        |
        |  ♣   ♣  |
        |    ♣    |
        |  ♣   ♣  |
        |        ♣|
        |        S|
         ~~~~~~~~~
         '''
    ,
    '4': '''
         _________
        |4        |
        |♣        |
        |  ♣   ♣  |
        |         |
        |  ♣   ♣  |
        |        ♣|
        |        b|
         ~~~~~~~~~
         '''
    ,
    '3': '''
         _________
        |3        |
        |♣   ♣    |
        |         |
        |    ♣    |
        |         |
        |    ♣   ♣|
        |        E|
         ~~~~~~~~~
         '''
    ,
    '2': '''
         _________
        |2        |
        |♣        |
        |    ♣    |
        |         |
        |    ♣    |
        |        ♣|
        |        Z|
         ~~~~~~~~~
         '''
}

diamonds = {
    'A': '''
         _________
        |A        |
        |♦  /~\   |
        |  / ^ \  |
        | (  ) ( )|
        |  \  v / |
        |   \ _/ ♦|
        |        V|
         ~~~~~~~~~
         '''
    ,
    'K': '''
         _________
        |K |/|\|  |
        |♦ |♦.♦|  |
        |   \ v/  |
        |  XXXXX  |
        |   /^\   |
        |  |♦`♦| ♦|
        |  |\ |/ X|
         ~~~~~~~~~
         '''
    ,
    'Q': '''
         _________
        |Q |~~~|  |
        |♦ |♦.♦|  |
        |   \ v/  |
        |  XX♦XX  |
        |   /^\   |
        |  |♦`♦| ♦|
        |  |___| Q|
         ~~~~~~~~~
         '''
    ,
    'J': '''
         _________
        |J /~~|_  |
        |♦ ( ♦\   |
        |  ! \ l  |
        | ^^^Xvvv |
        |   l\  I |
        |   \♦ ) ♦|
        |  ~|__/ P|
         ~~~~~~~~~
         '''
    ,
    '10': '''
         _________
        |10♦   ♦  |
        |♦   ♦    |
        |  ♦   ♦  |
        |         |
        |  ♦   ♦  |
        |    ♦   ♦|
        |  ♦   ♦0l|
         ~~~~~~~~~
         '''
    ,
    '9': '''
         _________
        |9 ♦   ♦  |
        |♦        |
        |  ♦   ♦  |
        |    ♦    |
        |  ♦   ♦  |
        |        ♦|
        |  ♦   ♦ 6|
         ~~~~~~~~~
         '''
    ,
    '8': '''
         _________
        |8 ♦   ♦  |
        |♦        |
        |  ♦   ♦  |
        |         |
        |  ♦   ♦  |
        |        ♦|
        |  ♦   ♦ 8|
         ~~~~~~~~~
         '''
    ,
    '7': '''
         _________
        |7        |
        |♦ ♦   ♦  |
        |    ♦    |
        |  ♦   ♦  |
        |         |
        |  ♦   ♦ ♦|
        |        L|
         ~~~~~~~~~
         '''
    ,
    '6': '''
         _________
        |6        |
        |♦ ♦   ♦  |
        |         |
        |  ♦   ♦  |
        |         |
        |  ♦   ♦ ♦|
        |        9|
         ~~~~~~~~~
         '''
    ,
    '5': '''
         _________
        |5        |
        |♦        |
        |  ♦   ♦  |
        |    ♦    |
        |  ♦   ♦  |
        |        ♦|
        |        S|
         ~~~~~~~~~
         '''
    ,
    '4': '''
         _________
        |4        |
        |♦        |
        |  ♦   ♦  |
        |         |
        |  ♦   ♦  |
        |        ♦|
        |        b|
         ~~~~~~~~~
         '''
    ,
    '3': '''
         _________
        |3        |
        |♦   ♦    |
        |         |
        |    ♦    |
        |         |
        |    ♦   ♦|
        |        E|
         ~~~~~~~~~
         '''
    ,
    '2': '''
         _________
        |2        |
        |♦        |
        |    ♦    |
        |         |
        |    ♦    |
        |        ♦|
        |        Z|
         ~~~~~~~~~
         '''
}

hearts = {
    'A': '''
         _________
        |A        |
        |♥  _  _  |
        |  / \/ \ |
        |  \    / |
        |   \  /  |
        |    \/  ♥|
        |        V|
         ~~~~~~~~~
         '''
    ,
    'K': '''
         _________
        |K |/|\ | |
        |♥ |^_^|  |
        |   \ v/  |
        |  ♥ K ♥  |
        |   /^\   |
        |  |o_o| ♥|
        |  |\ |/|X|
         ~~~~~~~~~
         '''
    ,
    'Q': '''
         _________
        |Q |~~~|  |
        |♥ |o_o|  |
        |   \ v/  |
        |  ♥ Q ♥  |
        |   /^\   |
        |  |^_^| ♥|
        |  |___| Q|
         ~~~~~~~~~
         '''
    ,
    'J': '''
         _________
        |J /~~|_  |
        |♥ ( o\   |
        |  ! \ l  |
        | ^^^Xvvv |
        |   l\  I |
        |   \ o )♥|
        |  ~|__/ P|
         ~~~~~~~~~
         '''
    ,
    '10': '''
         _________
        |10♥   ♥  |
        |♥   ♥    |
        |  ♥   ♥  |
        |         |
        |  ♥   ♥  |
        |    ♥   ♥|
        |  ♥   ♥0l|
         ~~~~~~~~~
         '''
    ,
    '9': '''
         _________
        |9 ♥   ♥  |
        |♥        |
        |  ♥   ♥  |
        |    ♥    |
        |  ♥   ♥  |
        |        ♥|
        |  ♥   ♥ 6|
         ~~~~~~~~~
         '''
    ,
    '8': '''
         _________
        |8 ♥   ♥  |
        |♥        |
        |  ♥   ♥  |
        |         |
        |  ♥   ♥  |
        |        ♥|
        |  ♥   ♥ 8|
         ~~~~~~~~~
         '''
    ,
    '7': '''
         _________
        |7        |
        |♥ ♥   ♥  |
        |    ♥    |
        |  ♥   ♥  |
        |         |
        |  ♥   ♥ ♥|
        |        L|
         ~~~~~~~~~
         '''
    ,
    '6': '''
         _________
        |6        |
        |♥ ♥   ♥  |
        |         |
        |  ♥   ♥  |
        |         |
        |  ♥   ♥ ♥|
        |        9|
         ~~~~~~~~~
         '''
    ,
    '5': '''
         _________
        |5        |
        |♥        |
        |  ♥   ♥  |
        |    ♥    |
        |  ♥   ♥  |
        |        ♥|
        |        S|
         ~~~~~~~~~
         '''
    ,
    '4': '''
         _________
        |4        |
        |♥        |
        |  ♥   ♥  |
        |         |
        |  ♥   ♥  |
        |        ♥|
        |        b|
         ~~~~~~~~~
         '''
    ,
    '3': '''
         _________
        |3        |
        |♥   ♥    |
        |         |
        |    ♥    |
        |         |
        |    ♥   ♥|
        |        E|
         ~~~~~~~~~
         '''
    ,
    '2': '''
         _________
        |2        |
        |♥        |
        |    ♥    |
        |         |
        |    ♥    |
        |        ♥|
        |        Z|
         ~~~~~~~~~
         '''
}


spades = {
    'A': '''
         _________
        |A        |
        |♠   ^    |
        |   / \   |
        |  ( ♠ )  |
        |   \ /   |
        |    .   ♠|
        |        V|
         ~~~~~~~~~
         '''
    ,
    'K': '''
         _________
        |K |/|\|  |
        |♠ |^_^|  |
        |   \ ♠/  |
        |  ♠ K ♠  |
        |   /^\   |
        |  |o_o| ♠|
        |  | |/| X|
         ~~~~~~~~~
         '''
    ,
    'Q': '''
         _________
        |Q |~~~|  |
        |♠ |o_o|  |
        |   \ ♠/  |
        |  ♠ Q ♠  |
        |   /^\   |
        |  |^_^| ♠|
        |  |___| Q|
         ~~~~~~~~~
         '''
    ,
    'J': '''
         _________
        |J /~~|_  |
        |♠ ( o\   |
        |  ! \ l  |
        | ^^^Xvvv |
        |   l\  I |
        |   \o ) ♠|
        |  ~|__/ P|
         ~~~~~~~~~
         '''
    ,
    '10': '''
         _________
        |10♠   ♠  |
        |♠   ♠    |
        |  ♠   ♠  |
        |         |
        |  ♠   ♠  |
        |    ♠   ♠|
        |  ♠   ♠0l|
         ~~~~~~~~~
         '''
    ,
    '9': '''
         _________
        |9 ♠   ♠  |
        |♠        |
        |  ♠   ♠  |
        |    ♠    |
        |  ♠   ♠  |
        |        ♠|
        |  ♠   ♠ 6|
         ~~~~~~~~~
         '''
    ,
    '8': '''
         _________
        |8 ♠   ♠  |
        |♠        |
        |  ♠   ♠  |
        |         |
        |  ♠   ♠  |
        |        ♠|
        |  ♠   ♠ 8|
         ~~~~~~~~~
         '''
    ,
    '7': '''
         _________
        |7        |
        |♠ ♠   ♠  |
        |    ♠    |
        |  ♠   ♠  |
        |         |
        |  ♠   ♠ ♠|
        |        L|
         ~~~~~~~~~
         '''
    ,
    '6': '''
         _________
        |6        |
        |♠ ♠   ♠  |
        |         |
        |  ♠   ♠  |
        |         |
        |  ♠   ♠ ♠|
        |        9|
         ~~~~~~~~~
         '''
    ,
    '5': '''
         _________
        |5        |
        |♠        |
        |  ♠   ♠  |
        |    ♠    |
        |  ♠   ♠  |
        |        ♠|
        |        S|
         ~~~~~~~~~
         '''
    ,
    '4': '''
         _________
        |4        |
        |♠        |
        |  ♠   ♠  |
        |         |
        |  ♠   ♠  |
        |        ♠|
        |        b|
         ~~~~~~~~~
         '''
    ,
    '3': '''
         _________
        |3        |
        |♠   ♠    |
        |         |
        |    ♠    |
        |         |
        |    ♠   ♠|
        |        E|
         ~~~~~~~~~
         '''
    ,
    '2': '''
         _________
        |2        |
        |♠        |
        |    ♠    |
        |         |
        |    ♠    |
        |        ♠|
        |        Z|
         ~~~~~~~~~
         '''
}

cards = {
    "c": clubs,
    "s": spades,
    "h": hearts,
    "d": diamonds
}

def create_deck():
    ranks = ['A'] + [str(n) for n in range(2, 11)] + ['J', "Q", "K"]
    suits = ['c','d','h','s']
    deck = [(rank, suit) for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

def deal_card(deck):
    return deck.pop()

def get_ascii_card(rank,suit):
    return cards[suit][rank]

def deal_hand(deck, num_cards=2):
    hand = []
    for _ in range(num_cards):
        hand.append(deal_card(deck))
    return hand

def deal_new_card(deck,hand):
    card = deal_card(deck)
    hand.append(card)
    return hand

def calculate_score(hand):
    score = 0
    for value, suit in hand:
        if value in ["J", "Q", "K"]:
            score += 10
        elif value == "A":
            #can be 11 or 1
            if score + 11 > 21:
                score += 1
            else:
               score += 11
        else:
            score += int(value)
    return score

def print_hand(hand,skip_first=False):
    number = 0
    for i in hand:
        if skip_first and number == 0:
            print("Hidden")
            number += 1
            continue
        number += 1
        print(get_ascii_card(*i))
    return True

deck = create_deck()
player_lost = False
player_lost = True


dealer = deal_hand(deck)
player = deal_hand(deck)
dealer_score = calculate_score(dealer)
player_score = calculate_score(player)


print("Dealer: \n")
#print(dealer[0])
print_hand(dealer,True)
#print(dealer[1])

print("Player: \n")
print_hand(player)
print(f"Score: {player_score}")
if player_score == 21:
    print("BLACKJACK!")
#player = deal()
hit = "n"
while player_score < 21:
    hit = input("Hit? Yes/No (y/n): ").lower()
    if hit == "y":
        print("Dealer: \n")
        print_hand(dealer)
        print(f"Dealer Score: {dealer_score}")
        player = deal_new_card(deck, player)
        player_score = calculate_score(player)
        print("Player: \n")
        print_hand(player)
        print(f"Score: {player_score}")
    else:
        print("Dealer: \n")
        print_hand(dealer)
        if dealer_score not in [17,18,19,20]:
            dealer = deal_new_card(deck, dealer)
            dealer_score = calculate_score(dealer)
            print("Dealer: \n")
            print_hand(dealer)

    if dealer_score > 21 and player_score <= 21:
        print(f"dealer: {dealer_score}")
        print(f"player: {player_score}")
        print("You Win!")
        sys.exit()
    if dealer_score == 21 and player_score < 21:
        print(f"dealer: {dealer_score}")
        print(f"player: {player_score}")
        print("You Lose!")
        sys.exit()

    if player_score == 21:
        print(f"dealer: {dealer_score}")
        print(f"player: {player_score}")
        print("BLACKJACK!")
        sys.exit()

if player_score > 21:
    print(f"dealer: {dealer_score}")
    print(f"player: {player_score}")
    print("bust! you lose.")
    sys.exit()


#while player_lost is not True:
    

