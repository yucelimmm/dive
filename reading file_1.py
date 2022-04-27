text="RODNEY HO: How are you doing?"

# with open('test.txt','w') as file:
#     print(file.write(text))
#     print(file.read())
# with open ("test.txt") as file:
#     print(file.read())
text_2="CHANG: Great. Well, if you could just give us a little more about the origin story of BNC - like, who launched it exactly?"

# with open("test.txt", "a") as file:
#     file.write(text_2)
def read():
  try:
    with open('test.txt') as f:
        a=(f.read())
    
  except FileNotFoundError:
    print("There is not such a file ot the path is incorrect")
  except:
    print("something went wrong")
  else:
     print(a)
  finally: 
    print("this is how I roll")

read()
