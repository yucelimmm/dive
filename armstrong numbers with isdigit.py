while 1==1:
  a = input("please enter a positive number:  ")

  if not a.isdigit():
    print(f"It is an invalid entry. Don't use non-numeric, float, or negative values! {a} is not a vaid number")
  else:
    a=int(a)
    x = str(a) #convert int to str
    y = list(x)  #covert str to lis
    #print(y)
    t =len(y)#gets the caracter's numbers from the list
    b=len(y)#gets the caracter's numbers from the list
    n = 0
    total = 0
    empty =[]
    for i in range(0, len(y)): # converts str_list items to int to make calculations
        y[i] = int(y[i])
    #print(y)
    while t>0 :
      empty.append(y[t-t+n]**b)#MAkes the calculation in here. Puts each number in enptylist
      t= t-1
      n = n+1
    #print(empty)
    for i in range(0,len(empty)):#Gets  numbers and adds them together.
      total = total + empty[i]
    if total == a:
      print(f"{a} is an \"Armstrong\" Number")
    else:
      print(f"{a} is not an Armstrong Number")
    break
