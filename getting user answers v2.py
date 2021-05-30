if ans == 'MS dhoni' or ans == 'ms dhoni' or ans =='A' or ans == 'a':
        print("Correct")
        score+=1
        print("Your score is",score)
    else:
        print("Sorry this answer is incorrect the correct answer is Ms dhoni" )
        if score <=0:
            score = 0
            print("Your score is",score)

