#Player Names
name1 = input("Enter p1 name: ")
name2 = input("Enter p2 name: ")

#Players can input rock paper or scissor
p1 = input("p1 choose: Rock, paper or scissor? ")
p2 = input("p2 choose: Rock, paper or scissor? ")
#if both players enter same 
if p1 == p2:
    print("draw")
#player 1 choose rock and player 2 chooses paper
if p1 == "rock" and p2 == "paper":
    print(name1 ,"wins")
#p1 choose paper and p2 choose rock
elif p1 == "paper" and p2 == "rock":
    print(name2, "wins")
#p1 choose rock and p2 choose scissor
if p1 == "rock" and p2 == "scissor":
    print(name1, "wins")
#p1 choose scissor and p2 choose rock
elif p1 == "scissor" and p2 == "rock":
    print(name2, "wins")
#p1 choose scissor and p2 choose paper
if p1 == "scissor" and p2 == "paper":
    print(name1, "wins")
#p1 choose paper and p2 choose scissor
elif p1 == "paper" and p2 == "scissor":
    print(name2, "wins")
