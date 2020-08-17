import random, sys

loss =0
win=0
tie=0

while True:
    print("%s wins, %s Losses, %s Ties" % (win, loss, tie))
    while True:
        print('choose (r)ock or (p)aper or (s)cissors or (q)uit')
        playermove= input()
        if playermove == "q":
            sys.exit()
        if playermove == 'r' or playermove == "p" or playermove == 's':
            break
        print("choose (r)ock or (p)aper or (s)cissors or (q)uit")
    
    if playermove == "r":
        print('Rock VS ...')
    elif playermove == "p":
        print("Paper VS ...")
    elif playermove == "s":
        print("Scissors VS ...")

    randomnumber = random.randint(1,3)
    if randomnumber == 1:
        compmove='r'
        print("Rock")

    elif randomnumber == 2:
        compmove = "p"
        print("Paper")

    elif randomnumber == 3:
        compmove = 's'
        print("Scissors")

    # the rules (player wins)
    if playermove == 'r' and compmove == 's':
        win = win + 1
    elif playermove == 's' and compmove == 'p':
        win = win +1
    elif playermove == 'p' and compmove == 'r':
        win = win +1

    # loss rule
    elif playermove == 'r' and compmove == 'p':
        loss = loss + 1
    elif playermove == 's' and compmove == 'r':
        loss = loss +1
    elif playermove == 'p' and compmove == 's':
        loss = loss +1

    elif compmove == playermove:
        tie = tie + 1

    