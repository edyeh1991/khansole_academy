from random import randint
count = 1

while count <= 3:
    x1 = randint(1,100)
    x2 = randint(1,100)
    q = int(input(f'What is {x1} + {x2}? '))
    if q == x1 + x2:
        print (f'You got it! The answer is {x1 + x2} You got {count} correct in a row')
        count= count + 1
    else:
            print (f'Wrong! The answer is {x1 + x2}')
            x1 = randint(1,100)
            x2 = randint(1,100)
            count = 1