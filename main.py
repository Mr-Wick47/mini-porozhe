import random


player=input('rock, paper ,sclssors...?')
rand_num=random.randint(0,2)

if rand_num==0:
    computer='rock'
elif rand_num==1:
    computer='paper'
else:
    computer='sclssors'
print(player)
print(computer)
if player==computer:
    print("its a tie")
elif player=='rock':
    if computer=='sclssors':
        print('player wins')
    else:
        print('computer wins')
elif player=='paper':
    if computer=='rock':
        print('player wins')
    else:
        print('computer wins')
elif player=='sclssors':
    if computer=='paper':
        print('player wins')
    else:
        print('computer wins')
else:
    print('something wrong')

