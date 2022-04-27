#fibonacci numbers
empty = []
i = 0
b =1
last =0
empty.append(i)
empty.append(b)
n=int(input("Please enter a number:"))


for i in range(n):
  last =(empty[-1]+empty[-2])
  empty.append(last)
  
print("fibonacci",empty)