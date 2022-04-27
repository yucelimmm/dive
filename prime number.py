#prime number
x = int(input("enter a number  :"))
n=0
empty=[]
for i in range(1,x+1):
   if x%i==0:
     n= n+1
     empty.append(i)
print(empty)     

if n==2:
  print("prime")
else:
  print("This is not a prime number")     