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
