import random;
import os;

while True:
    while True:
        try:
            playerSel = int(input('Rock(1)\nPaper(2)\nScissors(3) > '))
        except ValueError():
            continue
        else:
            break

    computerSel = random.choice([1, 2, 3])

    if computerSel == 1 and playerSel == 3 or computerSel == 2 and playerSel == 1 or computerSel == 3 and playerSel == 2:
        print('Computer has won!')
    elif computerSel == playerSel:
        print('It\'s a tie!')
    else:
        print('Player has won!')

    again = input('Wanna play again?(y/n) > ')[0]
    if again == 'y':
        continue
    else:
        break