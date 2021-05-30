#Ask if they are ready to take the quiz
while True:
    status = input("Are you ready to take the quiz :{}?: \na. Yes \nb. No \n=>")

#What if the user is ready

    if status == 'yes' or status == 'Yes' or status == 'y' or status == 'Y' or status == 'a' or status == 'A':
        print("Welcome to the quiz.")
        print("Here are the instructions to the quiz")
        print("You will be given 5 questions which will have three options")
        print("Only one of the questions will be correct ")
        print("Lets see how many you get correct.")
    # what if the user in not ready 
    elif status == 'No' or status == 'no' or status == 'N' or status == 'n':
        print("Thank you welcome to the quiz")
    else:
        print("Please enter your answer in y/n only")
