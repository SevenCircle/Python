import os

def closeProg():
    c = ' '
    while c[0] != 'y' and c[0] != 'n':
        c = input("Add more bids? (y)es or (n)o: ").lower()
    return c[0] == 'n'

def game():
    bids = {}
    close = False
    os.system('cls' if os.name == 'nt' else 'clear')
    while not close:
        bid = input("What is the bid: ")
        minVal = 0
        if(len(bids) > 0):
            minVal = max(bids,key=bids.get)
        
        if(bid.isdecimal() and (minVal == 0 or bid > bids[minVal])):
            nBid = input("Bid from: ")
            bids[nBid] = bid
            close=closeProg()
            os.system('cls' if os.name == 'nt' else 'clear')
            
        else: print("Bid needs to be a number and bigger than "+ str(minVal) + " of value "+str(bids[minVal]))
    max_key = max(bids, key=bids.get)
    print("Highest bidder: " + max_key + " of value "+ bids[max_key])

game()