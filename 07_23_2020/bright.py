
# nested if statement
answer = 'bright'
print('Finish this sentence. Always look on the __ side of life.')
uanswer = input('Complete the phrase ')
if uanswer == answer:
    print('That is correct!')
else:
    print('2 tries left. Guess again. ')
    uanswer = input('Complete the phrase ')
    if uanswer == answer:
        print('That is correct!')
    else:
        print('1 try left. Guess again.')
        uanswer = input()
        if uanswer == answer:
            print('That is correct!')
        else:
            print('Sorry. The correct answer is {}'.format(answer))
            print('Thanks for playing!')