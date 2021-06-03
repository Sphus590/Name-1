from random import shuffle
print ("***************WELCOME TO THE GENERAL SPORTS QUIZ******************")


 

#Asking for user details, name
def greet():
    global name
    while True:
        name = input("Please enter your name : ")
        if name.replace(' ','').isalpha():
            break
        print("Please enter your name using alphabets only  ")
        
      
greet()


#Ask if they are ready to take the quiz
status = input("Are you ready to take the quiz {} ? If you enter anything other than Y the quiz will end: \na. Yes \nb. No \n=>".format( name)).lower()

# what is they are not ready
if status == 'yes' or status == 'y' or status == 'b':
    pass
else:
    print("Thank you for coming please come back later")
    exit()





#What if the user is ready
def inst():
    inst = input ("Would you like instructions for the quiz? : \na. Yes \nb. No \n=>")
    if inst == 'yes' or inst == 'Yes' or inst == 'y' or inst == 'Y' or inst == 'a' or inst == 'A':
        print("*********************")
        print("Welcome to the quiz.")
        print("*********************")
        print("Here are the instructions to the quiz")
        print("You will be given 5 questions which will have three options")
        print("Only one of the options will be correct ")
        print("Lets see how many you get correct.")
# what if the user in not ready 
    elif inst == 'No' or inst == 'no' or inst == 'N' or inst == 'n':
        print("Thats fine here are the questions ")

    
inst()


#asking how many questions they would like to answer
def questions():
    global r
    while True:
        try:
            r = int(input("\nPlease enter how many questions you want to answer : "))
            if 0<r<=5:
                break
            else:
                print("please enter the amount of questions from 1 to 5 only")
        except:
            print('please enter questions in numbers only (The maximum number of questions is 5 )')

questions()



# initial score
Q1 ='A'
Q2 ='C'
Q3 ='B'
Q4 ='A'
Q5 ='B'

score = 0

# dictionary for the question and the correct answer
questions=[
[
    "Who hit the last shot to win the 2011 cricket world cup?",
    {'answer':'a','option':'a)Ms Dhoni\nb)Sachin tendulkar\nc)Yuvraj singh\n'}
    ],
[
    "The lakers and New york nicks play which sport?",
    {'answer':'c','option':'a)Baseball\nb)Football\nc)Basketball\n'}
    ],
[
    "Who holds the womens 100m record?",
    {'answer':'b','option':'a)Usain Bolt\nb)Florence Griffith Joyner\nc)Angela Mathews\n'}
    ],
[
    "Who is the current best One Day International batsmen?",
    {'answer':'a','option':'a)Babar azam\nb)Virat kohli\nc)Kane williamson\n'}
    ],
[
    "Which ball is used in a One Day International Cricket match?",
    {'answer':'b','option':'a)Red\nb)White\nc)Pink\n'}
    ],
   
]

shuffle(questions)
while r>0:
    data = questions[0]
    q = data[0]
    data =data[1]
    answer = data['answer']
    option = data['option']

    print(q)
    print(option)
    while True:
        user_answers = input("Please enter your answer here : ").lower().replace(' ','')
        if user_answers =='a' or user_answers == 'b' or user_answers == 'c': 
            if user_answers == answer:
                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                print("Well done thats correct keep going ")
                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                score +=1
                print("^^^^^^^^^^^^^")
                print("your score is",score)
                print("^^^^^^^^^^^^^")
            else:
                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                print("Sorry your answer is incorrect, The correct answer is ",answer)    
                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                print("^^^^^^^^^^^^^")
                print("your score is",score)
                print("^^^^^^^^^^^^^")

            del questions[0]
            r-=1
            break
        else:
            print("please enter the alphabet for the chosen option")
            
#end of quiz summary
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print("End of quiz summary")
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print("Thank you for playing my quiz I hope you enjoyed it.")
print("Your final score was",score)
print("Make sure you come back again to give it a go")
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
