#!/usr/bin/env python
# coding: utf-8

# In[3]:


sea = open("fishes.txt", 'r')

print(sea.readline())
print(sea.readlines())
sea.close()


# In[1]:


with open ('fishes.txt') as file:
    print(file.read())
file.close()


# In[32]:


text="RODNEY HO: How are you doing?"

with open('fishes.txt','r', encoding="utf-8") as file:

    print(file.read())


# In[22]:


sea = open("fishes.txt", 'r')

print(sea.readline())
print(sea.readlines())
sea.close()


# In[29]:


with open ("dummy.txt", 'w', encoding="utf-8") as file:
    file.write("this is my first dummy")
    
    
    
with open ("dummy.txt", 'r') as file:
    print(file.read())
   

    


# In[34]:


with open("dummy_file.txt", 'w', encoding="utf-8") as file:
    file.write('My first sentence')
    file.write('My second sentence,')
    file.write('My third sentence\n')
    file.write('My fourth sentence ')
    file.write('My last sentence')

with open("dummy_file.txt", 'r', encoding="utf-8") as file:
    print(file.read())


# In[44]:


fruits = ['Banana', 'Orange', 'Apple', 'Strawberry', 'Cherry']
fruits= str(fruits)
with open("new.txt", "w") as file:
    file.write(fruits)
    
with open("new.txt", "r") as file:
    a=("".join(file))
    print(file.read(a))


# In[45]:


flowers = ["Jasmine", "Rose", "Lilly", "Daisy", "Tulip"]

with open("new1.txt", "w") as file:
    for i in range(len(flowers)):
        file.write(str(i+1)+". " + (flowers[i]+'\n'+"\n"))
        
with open("new1.txt", "r") as file:
    print(file.read())


# In[49]:


flowers = ["Jasmine\n", "Rose\n", "Lilly\n", "Daisy\n", "Tulip\n"]

with open("new1.txt", "w") as file:
        file.writelines(flowers)
        
with open("new1.txt", "r") as file:
    print(file.read())


# In[51]:


chart = ['''no,fruit,amount
1,Banana,4 lb
2,Orange,5 lb
3,Apple,2 lb
4,Strawberry,6 lb
5,Cherry,3 lb''']

with open('fruits.csv', 'w') as f:
    f.writelines(chart)

with open('fruits.csv', 'r') as f:
    print(f.read())


# In[54]:


chart = ['''0,yucel,onal, 85
1,yucel1,onal, 86
2,yucel2,onal, 87
3,yucel3,onal, 88
4,yucel4,onal, 89
5,yucel5,onal, 90''']

with open('people.csv', 'w') as f:
    f.writelines(chart)
with open('people.csv', 'r') as f:
    print(f.read())


# In[56]:


import csv
with open('people.csv', 'r') as f:
    csv_rows=csv.reader(f)
    
    print(csv_rows)
    print()
    for row in csv_rows:
        print(row)

