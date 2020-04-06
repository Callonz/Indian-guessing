while(1):
    print("Let's play an Indian guessing game!")
    playerguess = float(input("> "))
    guess = 500000.0
    allowedDivert = 0.001
    lastChange = 500000.0
    guessed = 0
    for round in range(1,31, 1):
        if guess > playerguess:
            print(str(round) + " I guess: " + str(guess) + "   Too big!")
            guess -= lastChange /2
        else:
            print(str(round) + " I guess: " + str(guess) + "   Too small!")
            guess += lastChange / 2
        lastChange = lastChange / 2

        if (guess-allowedDivert<=playerguess<=guess+allowedDivert):
            print(str(round+1) + " I guess: " + str(guess) + "   Close enough! ;) I got you this time!")
            guessed =1
            break
    if(not guessed):
        print("You have beaten me. Here you go: midnight{rice_and_cu^H^Hsoju}")
