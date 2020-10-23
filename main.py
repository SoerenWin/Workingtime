import datetime
import mysql.connector

mydb = mysql.connector.connect(host="<your host>",
                               user="<your username>",
                               password="<your password>",
                               database='<your database>'
                               )
mycursor = mydb.cursor()


def calcminutes(starttime, endtime):
    if (int(endtime[0:2]) - int(starttime[0:2])) == 0:
        return int(endtime[3:5]) - int(starttime[3:5])
    else:
        return (int(endtime[0:2]) - int(starttime[0:2])) * 60 + int(endtime[3:5]) - int(starttime[3:5])


def getstarttime():
    return lines[1][7:12]

def getendtime():
    return lines[len(lines)-2][14:19]


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

# open text file and setup "file" variable
with open(f'workingtime_{datetime.date.today()}.txt', 'a+') as file:
    file.seek(0)
    lines = file.readlines()

# first time on that day opening a document
if len(lines) == 0:
    username = input('What is your name? ')
    lines.append(f'Good morning {username}\n')
    print(f'Good morning {username}')
else:
    username = lines[0][13:len(lines[0]) - 1]

# putting in fixed rows
if len(lines) == 1:
    start = input('\nWhen did you start working? [hh:mm] ')
    lines.append(f'Start: {start}\n')
    lines.append("Day finished: False\n")
    lines.append("Data committed: False")
    committed=False
    print(f'{username}, you started working at {start}\n')
# day has already been ended once
elif lines[len(lines) - 2][14:19] != 'False':
    print(
        '\nYou already finished your day at {0} with {1:.4} hours of working time and {2} minutes of breaks.'.format(lines[len(lines) - 2][14:19],
                                                                                           lines[len(lines) - 2][
                                                                                           25:30], getbreakduration()))
    # data has already been committed
    if lines[len(lines) - 1][16:20] == 'True':
        print('Data has already been committed to the database, but you can still change it if you like.\n')
    else:
        print('Data isn\'t committed yet.\n')
else:
    print(
        f'\nGood morning {username}\nToday, you started working at {getstarttime()} and already made {getbreakduration()} minutes of breaks.\n')

# main part
while True:
    if len(lines) > 1:
        next = input(
            'What do you want to do next? Add break (b) | Finish day (f) | change start time (s) | exit (e) ')
        if next == 'b':
            next = input('What do you want to do next? Add break duration (d) | Add break times (t) ')
            if next == 'd':
                breaktime = input('\nHow long did your break last? [mm] ')
                if len(breaktime)==1:
                    insertline(f'break: 0{breaktime} minutes', len(lines) - 2)
                else:
                    insertline(f'break: {breaktime} minutes', len(lines) - 2)
                print(f'Your break lasted {breaktime} minutes\n')
            elif next == 't':
                breaktime = calcminutes(input('When did you start your break? [hh:mm] '),
                                        input('When did you end your break? [hh:mm] '))
                if breaktime < 10:
                    insertline(f'break: 0{breaktime} minutes', len(lines) - 2)
                else:
                    insertline(f'break: {breaktime} minutes', len(lines) - 2)
                print(f'Yor break lasted {breaktime} minutes\n')
            else:
                print(f'Please check your input "{next}".')
        elif next == 's':
            start = input('When did you start working? [hh:mm] ')
            changeline(f'Start: {start}', 1)
            print(f'Start time changed to {start}')
        elif next == 'f':
            end = input('When did you finish your day? (hh:mm) ')
            start = getstarttime()
            workingtime = calcminutes(start, end) - getbreakduration()
            print('Day finished. Today, you worked {0:.3} hours.'.format(workingtime / 60))
            changeline('Day finished: {0} with {1:.3} hours of working time and {2} minutes of breaks'.format(end, workingtime / 60, getbreakduration()),
                       len(lines) - 2)
            next = input('Do you want to commit your data to the database? (y/n) ')
            if next == 'y':
                sql = f"Delete FROM workingtime WHERE date='{datetime.date.today()}'"
                mycursor.execute(sql)
                mydb.commit()
                sql = "INSERT INTO workingtime (date, starttime, endtime, effectivetime, breaktime, workingtime) VALUES (%s,%s,%s,%s,%s,%s)"
                val = (
                    datetime.date.today(), getstarttime(), end, '{0:.3}'.format(workingtime / 60), getbreakduration(),
                    '{0:.3}'.format(calcminutes(start, end) / 60))
                mycursor.execute(sql, val)
                mydb.commit()
                print(f'Data of the day successfully added to the database. day_id: {mycursor.lastrowid}\n')
                changeline('Data committed: True', len(lines) - 1)
            else:
                print('Remember to upload your data to the database.\n')
                changeline('Data committed: False', len(lines) - 1)
        elif next == 'e':
            # day finished but not committed
            if lines[len(lines) - 2][14:19] != 'False' and lines[len(lines) - 1][16:21] == 'False':
                next=input('You finished your day but your data is not committed yet. Do you want to commit your data now? (y/n) ')
                if next=='y':
                    # delete data from today in database, when already committed
                    sql = f"Delete FROM workingtime WHERE date='{datetime.date.today()}'"
                    mycursor.execute(sql)
                    mydb.commit()
                    # add new row in database
                    sql = "INSERT INTO workingtime (date, starttime, endtime, effectivetime, breaktime, workingtime) VALUES (%s,%s,%s,%s,%s,%s)"
                    val = (
                        datetime.date.today(), getstarttime(), getendtime(), '{0:.3}'.format(calcminutes(getstarttime(),getendtime())-getbreakduration()/60),
                        getbreakduration(),
                        '{0:.3}'.format(calcminutes(getstarttime(), getendtime()) / 60))
                    mycursor.execute(sql, val)
                    mydb.commit()
                    print(f'Data of the day successfully added to the database. day_id: {mycursor.lastrowid}\n')
                    changeline('Data committed: True', len(lines) - 1)
            # print information in text file
            with open(f'workingtime_{datetime.date.today()}.txt', 'a+') as file:
                file.seek(0)
                file.truncate()
                for line in lines:
                    file.write(line)
            print('\nBye Bye')
            break
        else:
            print(f'Please check your input "{next}".')
