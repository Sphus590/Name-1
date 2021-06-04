print ("***************WELCOME TO THE QUIZ******************")
# initial score
Q1 ='A'
Q2 ='C'
Q3 ='B'
Q4 ='A'
Q5 ='B'






score = 0

#Asking for user details, name
def greet():
    global name
    while True:
        name = input("Please enter your name : ")
        if name.isalpha():
            break
        print("Please enter your name using alphabets only : ")
        
      
greet()


#Ask if they are ready to take the quiz
status = input("Are you ready to take the quiz :{}?: \na. Yes \nb. No \n=>".format( name))




#What if the user is ready
def inst():
    inst = input ("Would you like instructions for the quiz? :{}? \na. Yes \nb. No \n=>")
    if inst == 'yes' or inst == 'Yes' or inst == 'y' or inst == 'Y' or inst == 'a' or inst == 'A':
        print("*********************")
        print("Welcome to the quiz.")
        print("*********************")
        print("Here are the instructions to the quiz")
        print("You will be given 5 questions which will have three options")
        print("Only one of the questions will be correct ")
        print("Lets see how many you get correct.")
# what if the user in not ready 
    elif inst == 'No' or inst == 'no' or inst == 'N' or inst == 'n':
        print("Thats fine here are the questions ")
       
  

inst()



#question 1
print("\nQuestion: 1|score:{}".format(score))
ans=input("who hit the last shot to win the 2011 cricket world cup?\na.Ms dhoni\nb.Sachin tendulkar\nc.Yuvraj singh \nYour answer : ")
if ans == 'MS dhoni' or ans == 'ms dhoni' or ans =='A' or ans == 'a':
    print("Correct")
    score+=1
    print("Your score is",score)
else:
    print("Sorry this answer is incorrect the correct answer is MS dhoni" )
    if score <=0:
        score = 0
        print("Your score is",score)

# question 2

print("\nQuestion: 2|score:{}".format(score))
ans=input("The Lakers and New york Nicks play which sport?\na.Baseball\nb.Football\nc.Basketball\nYour answer : ")
if ans == 'Basketball' or ans == 'basketball' or ans =='C' or ans == 'c':
    print("Correct")
    score+=1
    print("Your score is",score)
else:
    print("Sorry this answer is incorrect the correct answer is Basketball" )
    if score <=0:
        score = 0
        print("Your score is",score)


# question 3

print("\nQuestion: 3|score:{}".format(score))
ans=input("Who holds the womens 100m record?\na.Usain Bolt\nb.Florence Griffith-Joyner\nc.Angela Matthews\nYour answer : ")
if ans == 'Florence griffith joyner' or ans == 'florence griffith joyner' or ans =='B' or ans == 'b':
    print("Correct")
    score+=1
    print("Your score is",score)
else:
    print("Sorry this answer is incorrect the correct answer is Florence Griffith-Joyner" )
    if score <=0:
        score = 0
        print("Your score is",score)
    

# question 4

print("\nQuestion: 4|score:{}".format(score))
ans=input("Who is the current best ODI batsmen?\na.Babar azam\nb.Virat kohli\nc.Kane williamson\nYour answer : ")
if ans == 'Babar azam' or ans == 'babar azam' or ans =='A' or ans == 'a':
    print("Correct")
    score+=1
    print("Your score is",score)
else:
    print("Sorry this answer is incorrect the correct answer is Babar azam" )
    if score <=0:
        score = 0
        print("Your score is",score)


# question 5

print("\nQuestion: 5|score:{}".format(score))
ans=input("Which ball is used in an ODI?\na.Red\nb.White\nc.Pink\nYour answer : ")
if ans == 'White' or ans == 'white' or ans =='B' or ans == 'b':
    print("Correct")
    score+=1
    print("Your score is",score)
else:
    print("Sorry this answer is incorrect the correct answer is White" )
    if score <=0:
        score = 0
        print("Your score is",score)
