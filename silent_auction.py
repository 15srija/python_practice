import os
def find_winner(bidder_details):
   highest_bid=0
   for bidder in bidder_details:
      bidding_price=bidder_details[bidder]
      if bidding_price>highest_bid:
         highest_bid=bidding_price
         winner=bidder
   print(f"The winner of the auction is {winner} with price {highest_bid}")

auction={}
more_bidders='yes'
while more_bidders!='no':
   name=input("Enter name:")
   bid_price=int(input("Enter the bid price:"))
   auction[name]=bid_price
   more_bidders=input("Are there more bidders? yes or no:").lower()
   if more_bidders=='no':
    find_winner(auction)
   elif more_bidders=='yes':
    os.system('cls')
