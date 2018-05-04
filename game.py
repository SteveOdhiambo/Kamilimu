import random

gameChoices = ['rock','paper','scissors']

computerMove = random.choice(gameChoices)

challengerMove = True

while challengerMove is True:
    challengerMove = str(input("Rock, Paper or Scissors?")).lower()
    if challengerMove == computerMove:
        print('It is a TIE')
    elif challengerMove == 'rock' and computerMove == 'paper':
        print('Computer wins it picked {}'.format(computerMove))
    elif challengerMove == 'paper' and computerMove == 'rock':
        print('You win computer picked {}'.format(computerMove))
    elif challengerMove == 'scissors' and computerMove == 'paper':
        print('You win computer picked {}'.format(computerMove))
    elif challengerMove == 'paper' and computerMove == 'scissors':
        print('Computer wins it picked {}'.format(computerMove))
    elif challengerMove == 'scissors' and computerMove == 'rock':
        print('Computer wins it picked {}'.format(computerMove))
    elif challengerMove == 'rock' and computerMove == 'scissors':
        print('You win computer picked {}'.format(computerMove))

challengerMove = False