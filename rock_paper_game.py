#import random, card game rock paper scissors game

# x= random.randint(1,6)
# y = random.random()
#cards =[1,2,3,4,5,6,7,8,9, "J", "Q","K","A"]
# random.shuffle(cards)
# print(cards)
import random
n=0
mylist = ['rock', 'paper', 'scissors']
comp=0
user=0
player = None
while n <10:
    computer = random.choice(mylist)
    while player not in ("1","2","3"):
        player = input("for rock select '1', for paper select '2',  for scissors select '3'?:")
    print("computer:" + computer)
    print("player:" + player)

    if computer == "rock" and player == "1":
        pass
    elif computer == "rock" and player == "2":
        user = user + 1
    elif computer == "rock" and player == "3":
        comp = comp + 1
    elif computer == "paper" and player == "1":
        comp = comp + 1
    elif computer == "paper" and player == "2":
        pass
    elif computer == "paper" and player == "3":
        user = user + 1
    elif computer == "scissors" and player == "1":
        user = user + 1
    elif computer == "scissors" and player == "2":
        comp = comp + 1
    else:
        pass
    n = n + 1
    player= None
    print("computer =", comp)
    print("player :", user)


if comp > user:
    print("Computer won")
else:
    print("player  won")
