import datetime
from pathlib import Path

log_folder = Path("log_files/")
initialization_log_filename = log_folder / "initialization_log.txt"
user_command_log_filename = log_folder / "user_command_log.txt"
user_event__log_filename = log_folder / "user_event_log.txt"
mod_command_log_filename = log_folder / "mod_command_log.txt"
bot_moderation_log_filename = log_folder / "bot_moderation_log.txt"
bot_event_log_filename = log_folder / "bot_event_log.txt"

def send_log(log_message, destination):
    filename = ""
    if destination == "initialization":
        filename = initialization_log_filename
    elif destination == "user_command":
        filename = user_command_log_filename
    elif destination == "user_event":
        filename = user_event__log_filename
    elif destination == "mod_command":
        filename = mod_command_log_filename
    elif destination == "bot_moderation":
        filename = bot_moderation_log_filename
    elif destination == "bot_event":
        filename = bot_event_log_filename
    with filename.open() as f:
        f.write(log_message+f"    , DateTime: {datetime.datetime.now()}\n")


def create_log_files():
    log_msg=""
    if not initialization_log_filename.exists():
        with initialization_log_filename.open() as f: f.close()
        log_msg += f"Initialization logfile was created "
    if not user_command_log_filename.exists():
        with user_command_log_filename.open() as f: f.close()
        log_msg += f"UserCommand logfile was created "
    if not user_event__log_filename.exists():
        with user_event__log_filename.open() as f: f.close()
        log_msg += f"UserEvent logfile was created "
    if not mod_command_log_filename.exists():
        with mod_command_log_filename.open() as f: f.close()
        log_msg += f"ModCommand logfile was created "
    if not bot_moderation_log_filename.exists():
        with bot_moderation_log_filename.open() as f: f.close()
        log_msg += f"BotModeration logfile was created "
    if not bot_event_log_filename.exists():
        with bot_event_log_filename.open() as f: f.close()
        log_msg += f"BotEvent logfile was created "
    log_msg = f"Logging is online."
    send_log(log_msg, "initialization")

