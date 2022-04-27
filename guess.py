import random
num =random.randint(0, 85)
while 1==1:
  gus = input('Enter your guess: ') 
  if not gus.isdigit():
      print(f'You\'ve enetered {gus}. This is an invalid input!')
  else:
    gus=int(gus)
    if gus< num:
      print("go higer")
    elif gus>num:
      print("go lower")
    else:
      print("wow")
      break