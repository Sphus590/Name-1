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
