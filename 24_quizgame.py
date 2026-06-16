questions = ("What is Parth's fav food",
             "What is Parth's fav celebrity",
             "What is Parth's fav singer")


options= (("A.Biryani","B.Paneer","C.Bhindi","D.Pizza"),
          ("A.Charlie Puth","B.Justin Bieber","C.Ajay Devgan","D.CR7"),
          ("A.Charlie Puth","B.Justin Bieber","C.Modi","D.BTS"))


answers = ("B","D","B")
guesses = []
score = 0
question_num= 0

for question in questions:
    print("----------------------------------------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess=input("Enter (A,B,C,D): ").upper()
    guesses.append(guess)
    # question_num+=1  
    if guess == answers[question_num]:
        score +=1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answers")   
    question_num += 1 


print("---------------------")  
print("     Result      ")
print("---------------------") 

print("answers: ",end=" ")
for answer in answers:
    print(answer)
print()

print("guesses: ",end=" ")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score/len(questions)*100)
print(f"Youre score is {score}")