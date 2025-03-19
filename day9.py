import os

gravel_art = '''
           ___________
           \         /
            )_______(
            |"""""""|_.-._,.---------.,_.-._
            |       | | |               | | ''-.
            |       |_| |_             _| |_..-'
            |_______| '-' `'---------'` '-'
            )"""""""(
           /_________\
           `'-------'`
         .-------------.
        /_______________\
'''
print(gravel_art)
print("Welcome to the secret auction program!")
program_end = False
bids = {}
clear = lambda: os.system('clear')

while program_end == False:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bids[name] = bid
    next_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if next_bidders == "no":
        program_end = True
    clear()

def find_highest_bidder(bidding_dictionary):
    top_bid = 0
    top_bidder = ""
    # Mozemo koristiti i max() f-ju
    # max(disct, key=dict.get)
    for bidder in bidding_dictionary:
        if bids[bidder] > top_bid:
            top_bid = bids[bidder]
            top_bidder = bidder

    print(f"The winner is {top_bidder} with a bid of ${top_bid}")

find_highest_bidder(bids)

