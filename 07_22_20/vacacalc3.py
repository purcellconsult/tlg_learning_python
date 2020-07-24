# Demo of if/elif statement from alta3 courseware

print('How long have you been an employee? ')
emyears = int(input('Enter the years '))
if emyears >= 30:
    vacadays = emyears * 3
elif emyears >= 20:
    vacadays = emyears * 2
else:
    vacadays = emyears * 1.5
print('You have {} vacation days'.format(vacadays))

