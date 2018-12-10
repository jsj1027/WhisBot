import datetime
from pathlib import Path
import os


log_folder = Path(Path.cwd().as_posix() + '/log_files')
log_folder.mkdir(exist_ok=True)
initialization_log_filename = log_folder / "initialization_log.txt"
user_command_log_filename = log_folder / "user_command_log.txt"
user_event__log_filename = log_folder / "user_event_log.txt"
mod_command_log_filename = log_folder / "mod_command_log.txt"
bot_moderation_log_filename = log_folder / "bot_moderation_log.txt"
bot_event_log_filename = log_folder / "bot_event_log.txt"

def switch(destination):
    return {
        "initialization": initialization_log_filename,
        "user_command": user_command_log_filename,
        "user_event": user_event__log_filename,
        "mod_command": mod_command_log_filename,
        "bot_moderation": bot_moderation_log_filename,
        "bot_event": bot_event_log_filename
    }[destination]


def send_log(log_message, destination):
    filename = switch(destination)
    f = open(filename, "a+")
    f.write(log_message+f"    , DateTime: {datetime.datetime.now()}\n")


def create_log_files():
    log_msg=""
    if not initialization_log_filename.exists():
        initialization_log_filename.touch()
        log_msg += f"Initialization logfile was created"
    if not user_command_log_filename.exists():
        user_command_log_filename.touch()
        log_msg += f"UserCommand logfile was created "
    if not user_event__log_filename.exists():
        user_event__log_filename.touch()
        log_msg += f"UserEvent logfile was created "
    if not mod_command_log_filename.exists():
        mod_command_log_filename.touch()
        log_msg += f"ModCommand logfile was created "
    if not bot_moderation_log_filename.exists():
        bot_moderation_log_filename.touch()
        log_msg += f"BotModeration logfile was created "
    if not bot_event_log_filename.exists():
        bot_event_log_filename.touch()
        log_msg += f"BotEvent logfile was created "
    log_msg = f"Logging is online."
    send_log(log_msg, "initialization")
