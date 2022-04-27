#bigges numbers
n=int(input("number :"))
list=[]
for j in range(0,n+1):
  list.append(int(j))
list.sort()
print(list)
print("the biggeest number is ",list[-1])