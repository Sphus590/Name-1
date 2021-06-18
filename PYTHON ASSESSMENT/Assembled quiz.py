from random import shuffle
print ("***************WELCOME TO THE GENERAL SPORTS QUIZ Developed by Guransh******************")


 

#Asking for user details, name
def greet():
    global name
    while True:
        name = input("Please enter your name : ")
        if name.replace(' ','').isalpha():
            break
        print("Please enter your name using alphabets only  ")
        
      
greet()

#Asking for user details, age
def age():
    while True:
        age = input("Please enter your age : ")
        if age.replace(' ','').isnumeric():#using replace to allow spaces after the answer
            if 5< int(age)<99: #allowing age till 7 to 100 only
                break
            else:
                print('You need to be 5 to 99 to play the quiz')
                exit()
       
            

age()





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
    global r ,total
    while True:
        try:
            r = int(input("\nPlease enter how many questions you want to answer : "))
            if 0<r<=10:
                break
            else:
                print("please enter the amount of questions from 1 to 10 only")
        except:
            print('please enter questions in numbers only (The maximum number of questions is 5 )')


    total = r

questions()



# initial score
Q1 ='A'
Q2 ='C'
Q3 ='B'
Q4 ='A'
Q5 ='A'
Q6 ='B'
Q7 ='C'
Q8 ='B'
Q9 ='C'
Q10 ='A'

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
    "What does wwe stand for?",
    {'answer':'a','option':'a)World Wrestling Entertainment\nb)Wery Wery easy\nc)Wall Want Elephant\n'}
    ],
[
    "Is Ultimate frisbee an international sport or no?",
    {'answer':'b','option':'a)No\nb)Yes\nc)Maybe\n'}
    ],
[
    "What is Muhammed Ali's real name?",
    {'answer':'c','option':'a)Muhammed Ali\nb)Micheal Jordan\nc)Cassius Marcellus Clay Jr.\n'}
    ],
[
    "At which olympics did Kelly Holmes win two gold medals?",
    {'answer':'b','option':'a)Tokyo Olympics\nb)Athens Olympics\nc)China Olympics\n'}
    ],
[
    "The Chicago Cubs and Boston Red Sox play which sport?",
    {'answer':'c','option':'a)Golf\nb)Swimming\nc)Baseball\n'}
    ],
[
    "Which country are the current world cup holders for Netball?",
    {'answer':'a','option':'a)New Zealand\nb)Austrailia\nc)India\n'}
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
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print("End of quiz summary")
print("Your final score is", score,"out of",total)
print("That means you answered", (round(score/total*100,2)),"% of the questions correctly!")
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
exit()


