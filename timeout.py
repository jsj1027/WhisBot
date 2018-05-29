import datetime
from datetime import timedelta

def user_parse(commands):
    person=''
    command_list = commands.split(" ")
    commandstring = ''
    for x in range(0, len(command_list)):
        if '@' not in command_list[x] and x == (len(command_list)-1):
            commandstring += (command_list[x])
        elif '@' not in command_list[x] and x != (len(command_list)-1):
            commandstring += (command_list[x] + ' ')
        else:
            person = command_list[x].replace("@", "", 1)
            person = person.replace("<", '')
            person = person.replace(">", '')
    return commandstring, person

def timeout_parse(commands):
    command_list = commands.split(" ")
    weeks, days, hours, minutes, seconds, counter, num = 0, 0, 0, 0, 0, 0, 0
    element = ''
    command_length = int(len(command_list) + (len(command_list)/2))
    for x in range(0, command_length):
        if counter == 0:
            num = command_list[x]
            counter += 1
        elif counter == 1:
            element = command_list[x].lower()
            counter += 1
        elif counter == 2:
            if element == 'wk':
                weeks = int(num)
            elif element == 'dy':
                days = int(num)
            elif element == 'hr':
                hours = int(num)
            elif element == 'min':
                minutes = int(num)
            elif element == 'sec':
                seconds = int(num)
            counter = 0
    later = timedelta(weeks=weeks, days=days, hours=hours, minutes=minutes, seconds=seconds)
    return later.total_seconds()
