
questions ={"What is V's bith date?:" : "C",
            "What date was Kamuran's first interview?" :"D",
            "Roughly, how many times in a day Ahmed is having computer issues?": "B",
            }
answers =[["A. July 15, 1789", "B. Yesterday", "C. Even she does not know her birth date", "D. Who is V?"],
          ["A. Last week", "B. Feb 23, 2022", "C. There was not any", "D. March 23, 2022"],
          ["A. 2-3", "B. 3-4", "C. That is a MAC never gives an issue", "D. It is a Mac all the time gives issues"]]
          
def new_game():
  cevaplar=[]
  global correct_guesses
  correct_guesses = 0
  question_num=0
  guess= None
  for key in questions:
    print()
    print(key)
    for i in answers[question_num]:
      print(i)     
    question_num = question_num +1
    while guess not in("A", "B","C","D"):
      guess=input("Please enter A, B, C or D       :").upper()
    cevaplar.append(guess)
    
    
    correct_guesses += check_answer(questions.get(key), guess)
    guess=None
  display_score(correct_guesses, cevaplar)
  

def check_answer(x, y):
  if x==y:
    print("correct")    
    return 1
  else:
    print("wrong")
    return 0
def display_score(a, b):
  print("-------------------------------------------------------------------------------------------------------------------------------------")
  print("results")
  print("Answer key:", end=" ")
  for key in questions:
    print(questions.get(key), end=" ")
  print()
  print("Your Answer: ", end=" ")  
  for i in b:
    print(i, end=" ")
  print()
  score =  (correct_guesses*100)/len(questions)
  print("your score is :", score)

def play_again():
  x= input("Do you want to play again?  yes/no  :").lower()
  if x == "yes":
    return True
  else:
    return False




new_game()

while  play_again():
  new_game()

print("thanks for playing")