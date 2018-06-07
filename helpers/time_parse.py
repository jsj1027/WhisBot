from datetime import timedelta


def time_parse(commands):
    weeks, days, hours, minutes, seconds, counter, num = 0, 0, 0, 0, 0, 0, 0
    for command in commands:
        if command.isdigit():
            num = command
        elif isinstance(command, str):
            element = command.lower()
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
    later = timedelta(weeks=weeks, days=days, hours=hours, minutes=minutes, seconds=seconds)
    return later.total_seconds()
