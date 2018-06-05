def command_parse(commands):
    fixed_command_list = []
    for command in commands:
        if '@' not in command:
            fixed_command_list.append(command)
    return fixed_command_list
