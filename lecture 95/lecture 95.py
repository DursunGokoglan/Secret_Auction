import os
from art import logo

print(logo)
print("Welcome to the secret auction program.")

max_bid = 0
max_bidder = ""
bid_log = {}
keep_on = True

while keep_on:

    name = input("What's your name? ")
    bid = input("What's your bid? $")

    bid_log[name] = bid

    more = input("Are there any other bidders? Type 'yes' or 'no': ")

    if more == "yes":
        os.system("cls")

    if more == "no":
        keep_on = False

for one in bid_log:
    if int(bid_log[one]) > max_bid:
        max_bid = int(bid_log[one])
        max_bidder = one

os.system("cls")

print(f"The winner is {max_bidder} with a bid of ${max_bid}.")