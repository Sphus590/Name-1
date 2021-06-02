#Ask if they are ready to take the quiz
status = input("Are you ready to take the quiz :{}?: \na. Yes \nb. No \n=>")

#What if the user is not ready
if status == 'No' or status == 'no' or status == 'n' or status == 'N' : 
    print(" Thats ok take your time see you next time.")
    
#what if the user is ready
if status == 'yes' or status == 'Yes' or status == 'y' or status == 'Y' or status == 'a' or status == 'A':
    print("Welcome to the quiz.")
    print("These are the instructions on the quiz")
    print("You will be given 5 questions and you must answer them correctly to earn points")
    print("Lets see how many points you can get :)")
