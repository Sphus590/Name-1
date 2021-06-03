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
    "The lakers and new york nicks play which sport?",
    {'answer':'c','option':'a)Baseball\nb)Football\nc)Basketball\n'}
    ],
[
    "Who holds the womens 100m record?",
    {'answer':'b','option':'a)Usain Bolt\nb)Florence Griffith Joyner\nc)Angela Mathews\n'}
    ],
[
    "Who is the current best ODI batsmen?",
    {'answer':'a','option':'a)Babar azam\nb)Virat kohli\nc)Kane williamson\n'}
    ],
[
    "Which ball is used in an ODI?",
    {'answer':'b','option':'a)Red\nb)White\nc)Pink\n'}
    ],
   
]



