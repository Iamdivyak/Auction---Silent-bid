from replit import clear
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)

auction = {}

people_present = True
while people_present:
  name = input("What's your name?: ")
  bid = int(input("What's your bid: $"))
  auction[name] = bid
  should_continue = input("Are there any oher bidders? Type 'Y' for yes or 'N' for no\n").lower()
  if should_continue == "n":
    people_present=False
  elif should_continue == "y":
    clear()

highest_bid = 0
winer = ''
for bidder in auction:
  if highest_bid < auction[bidder]:
    highest_bid = auction[bidder]
    winer = bidder
print(f"Highest bidder is {winer}. highest bid is {highest_bid}")