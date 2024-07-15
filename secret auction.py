print("Welcome to the secret auction program!")

bid_completed = False
bids = {}


def highest_bid(bid_records):
    bid_price = 0
    winner = ""
    for bidder in bid_records:
        highest_price = bid_records[bidder]
        if highest_price > bid_price:
            bid_price = highest_price
            winner = bidder
    print(f"The winner is {winner} with bid of Rs.{bid_price}")


while not bid_completed:
    bidder_name = input("What's your name? ")
    bid_amount = int(input("What's your bid? Rs."))
    bids[bidder_name] = bid_amount
    other_bidder = input("Are there any other bidders? Type 'yes' or 'no' \n")
    if other_bidder == "no":
        bid_completed = True
        highest_bid(bids)
