#import random, card game rock paper scissors game
import random
x= random.randint(1,6)
y = random.random()
mylist=['rock', 'paper', 'scissors']
z= random.choice(mylist)
print(z)
cards =[1,2,3,4,5,6,7,8,9, "J", "Q","K","A"]
random.shuffle(cards)
print(cards)
