Player1=input('Player 1, Please Enter Your Reponse:')
Player2=input('Player 2, Please Enter Your Reponse:')

Options=['R', 'P', 'S']

if Player1 in Options and Player2 in Options:
    if Player1=='R' and Player2=='S' or Player1=='P' and Player2=='R' or Player1=='S' and Player2=='P':
        print('Player1 is the winner.')
    elif Player1==Player2:
        print("Draw.")
    else:
        print('Player2 is the winner.')
else:
    print('Invalid Input.')
