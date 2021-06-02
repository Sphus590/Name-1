# The following is a provision given for user to see if he needed instructions or not
def instructions():
    inst=input("Do you need instructions to play the Quiz? Enter y for yes or n for no : ")
    if inst == "y":
        print("You will be given 5 questions which will have three options. Only one of the options will be correct. You will be given a score of 1 for each correct answer. There are no minus points for wrong answers.")
    else:
        print("Welcome to the Quiz")

instructions()
