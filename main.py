# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import datetime


def calcminutes(starttime, endtime):
    if (int(endtime[0:2]) - int(starttime[0:2])) == 0:
        return int(endtime[3:5]) - int(starttime[3:5])
    else:
        return (int(endtime[0:2]) - int(starttime[0:2])) * 60 + int(endtime[3:5]) - int(starttime[3:5])


file = open(f'workingtime_{datetime.date.today()}.txt', 'a+')
file.seek(0)
lines = file.readlines()
n = len(lines)

if n == 0:
    username = input('What is your name? ')
    file.write(f'Good morning {username}\n')
    print(f'Good morning {username}')
    n = n + 1
else:
    username = lines[0][13:len(lines[0]) - 1]

if n == 1:
    start = input('\nWhen did you start working? [hh:mm] ')
    file.write(f'Start: {start}\n')
    print(f'{username}, you started working at {start}\n')
    n += 1
else:
    file.seek(0)
    start = file.readlines()[1][7:12]
    print(f'\nGood morning {username}\nToday, you started working at {start} and already made minutes of breaks.\n')

while True:
    if n > 1:
        next = input(
            'What do you want to do next? Add break (b) | Finish day (f) | change start time (s) | exit (e) ')
        if next == 'b':
            next = input('What do you want to do next? Add break duration (d) | Add break times (t) ')
            if next == 'd':
                breaktime = input('\nHow long did your break last? [mm] ')
                file.write(f'break: {breaktime} minutes\n')
                print(f'Yor break lasted {breaktime} minutes\n')
            elif next == 't':
                breaktime = calcminutes(input('When did you start your break? [hh:mm] '),
                                        input('When did you end your break? [hh:mm] '))
                file.write(f'break: {breaktime} minutes\n')
                print(f'Yor break lasted {breaktime} minutes\n')
            else:
                print(f'Please check your input "{next}".')
        elif next == 's':
            start = input('When did you start working? [hh:mm] ')
            file.seek(0)
            lines = file.readlines()
            lines[1] = f'Start: {start}\n'
            file.truncate(0)
            for i in range(len(lines)):
                file.write(lines[i])
            print(f'Starting time changed to {start}')
        elif next == 'e':
            break
        else:
            print(f'Please check your input "{next}".')

file.close()
