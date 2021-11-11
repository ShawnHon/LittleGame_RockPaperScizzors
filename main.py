# Rock Paper Scizzors by Shawn Hon
print('Welcome to Rock Paper Scizzors!!!!')
import random

while True:

    while True:

          human=input()
          if human=='R':
                   print('HumaG'
                         'n: Rock!')
                   break
          elif human=='P':
                   print('Human: Paper!')
                   break
          elif human=='S':
                   print('Human: Sizzors!')
                   break
          elif human=='E':
                   quit()
          else:
                   print('Please type R or P or S only; Type E to Exit')

    while True:
          numberS = random.randrange(1,4)

          if numberS==1:
                   print('Computer: Rock!')
                   break
          elif numberS==2:
                   print('Computers: Paper!')
                   break
          else:
                   print('Computers: Sizzors!')
                   break

    while True:
           if numberS==1 and human=='R' or numberS==2 and human=='P'or numberS==3 and human=='S':
                   print('Draw!')
                   break
           elif numberS==1 and human=='P'or numberS==2 and human=='S'or numberS==3 and human=='R':
                   print('You Win!!!')
                   break
           else:
                   print('You Lose!!!')
                   break
