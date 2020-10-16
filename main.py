import datetime


def calcminutes(starttime, endtime):
    if (int(endtime[0:2]) - int(starttime[0:2])) == 0:
        return int(endtime[3:5]) - int(starttime[3:5])
    else:
        return (int(endtime[0:2]) - int(starttime[0:2])) * 60 + int(endtime[3:5]) - int(starttime[3:5])


def getstarttime():
    return lines[1][7:12]


def getbreakduration():
    breakduration = 0
    for i in range(2, len(lines) - 2):
        breakduration += int(lines[i][7:10])
    return breakduration


def changeline(content, line):
    lines[line] = content + '\n'


def insertline(content, line):
    lines.append('added')
    for i in range(len(lines) - 1, line, -1):
        lines[i] = lines[i - 1]
    lines[line] = content + '\n'


with open(f'workingtime_{datetime.date.today()}.txt', 'a+') as file:
    file.seek(0)
    lines = file.readlines()


if len(lines) == 0:
    username = input('What is your name? ')
    lines.append(f'Good morning {username}\n')
    print(f'Good morning {username}')
else:
    username = lines[0][13:len(lines[0]) - 1]

if len(lines) == 1:
    start = input('\nWhen did you start working? [hh:mm] ')
    lines.append(f'Start: {start}\n')
    lines.append("Day finished: False\n")
    lines.append("Data commited: False")
    print(f'{username}, you started working at {start}\n')
else:
    print(
        f'\nGood morning {username}\nToday, you started working at {getstarttime()} and already made {getbreakduration()} minutes of breaks.\n')

while True:
    if len(lines) > 1:
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
            workingtime = calcminutes(start, end) - getbreakduration()
            print('Day finished. Today you worked {0:.3} hours.'.format(workingtime / 60))
            changeline('Day finished: {0} with {1:.3} hours of working time'.format(end, workingtime / 60), len(lines) - 2)
        elif next == 'e':
            with open(f'workingtime_{datetime.date.today()}.txt', 'a+') as file:
                file.seek(0)
                file.truncate()
                for line in lines:
                    file.write(line)
            print('Bye Bye')
            break
        else:
            print(f'Please check your input "{next}".')
