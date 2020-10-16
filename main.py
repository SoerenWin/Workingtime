# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import datetime


def calcminutes(starttime, endtime):
    if (int(endtime[0:2]) - int(starttime[0:2])) == 0:
        return int(endtime[3:5]) - int(starttime[3:5])
    else:
        return (int(endtime[0:2]) - int(starttime[0:2])) * 60 + int(endtime[3:5]) - int(starttime[3:5])


def getstarttime():
    file.seek(0)
    return file.readlines()[1][7:12]


def getbreakduration():
    file.seek(0)
    lines = file.readlines()
    breakduration = 0
    for i in range(2, len(lines) - 2):
        breakduration += int(lines[i][7:10])
    return breakduration


def changeline(content, line):
    file.seek(0)
    lines = file.readlines()
    lines[line] = content + '\n'
    file.truncate(0)
    for i in range(len(lines)):
        file.write(lines[i])


def insertline(content, line):
    file.seek(0)
    lines = file.readlines()
    lines.append('added')
    for i in range(len(lines) - 1, line, -1):
        lines[i] = lines[i - 1]
    lines[line] = content + '\n'
    file.truncate(0)
    for i in range(len(lines)):
        file.write(lines[i])


file = open(f'workingtime_{datetime.date.today()}.txt', 'a+')
file.seek(0)
lines = file.readlines()
n = len(lines)

# TODO messed up row order when inserting all information in one turn
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
    file.write("Day finished: False\n")
    file.write("Data commited: False")
    print(f'{username}, you started working at {start}\n')
    n += 1
else:
    print(
        f'\nGood morning {username}\nToday, you started working at {getstarttime()} and already made {getbreakduration()} minutes of breaks.\n')

file.close()
file = open(f'workingtime_{datetime.date.today()}.txt', 'a+')
file.seek(0)
lines = file.readlines()

while True:
    if n > 1:
        next = input(
            'What do you want to do next? Add break (b) | Finish day (f) | change start time (s) | exit (e) ')
        if next == 'b':
            next = input('What do you want to do next? Add break duration (d) | Add break times (t) ')
            if next == 'd':
                breaktime = input('\nHow long did your break last? [mm] ')
                insertline(f'break: {breaktime} minutes', len(lines) - 2)
                print(f'Yor break lasted {breaktime} minutes\n')
            elif next == 't':
                breaktime = calcminutes(input('When did you start your break? [hh:mm] '),
                                        input('When did you end your break? [hh:mm] '))
                insertline(f'break: {breaktime} minutes', len(lines) - 2)
                print(f'Yor break lasted {breaktime} minutes\n')
            else:
                print(f'Please check your input "{next}".')
        elif next == 's':
            start = input('When did you start working? [hh:mm] ')
            changeline(f'Start: {start}', 1)
            print(f'Start time changed to {start}')
        elif next == 'f':
            end = input('When did you end your day? (hh:mm) ')
            start = getstarttime()
            workingtime = calcminutes(start, end)
            print('{0:.3}'.format(workingtime / 60))
        elif next == 'e':
            print('Bye Bye')
            break
        else:
            print(f'Please check your input "{next}".')

file.close()
