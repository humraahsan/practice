# from replit import clear
# HINT: You can call clear() to clear the output in the console.

from art import logo

print(logo)
bids_dict = {}
stop_bidding = False


def highest_bidder(bids):
    highest_bid = 0
    highest_bidder = ""
    for bidder in bids_dict:
        bidding_price = bids_dict[bidder]
        if bidding_price > highest_bid:
            highest_bid = bidding_price
            highest_bidder = bidder
    print(f" highest bidding price is {highest_bid} bid by {highest_bidder}")


while not stop_bidding:
    name = input("What is your name: ")
    price = int(input("What is the bid price: "))
    bids_dict[name] = price
    continue_bidding = input("Are there any other bidders? Type Yes or No \n")
    if continue_bidding == "No":
        stop_bidding = True
        highest_bidder(bids_dict)
    else:
        stop_bidding = False
