sea= open("D:\python\\fishes.txt", "r")

print(sea.read())
sea.seek(0)
print()
print(sea.readline(12))
print(sea.readline(12))
print(sea.readline(12))
print(sea.readline(56))  #---------------->
print(sea.tell())



