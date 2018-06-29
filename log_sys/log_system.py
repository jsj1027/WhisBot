import datetime


def send_log(log_message, destination):
    file = open(f"log_files/{destination}_log.txt", "a+")
    file.write(log_message+f"    , DateTime: {datetime.datetime.now()}\n")
    file.close()


def create_log_files():
    initialization = open("log_files/initialization_log.txt","a+")
    user_command = open("log_files/user_command_log.txt","a+")
    user_event = open("log_files/user_event_log.txt","a+")
    mod_command = open("log_files/mod_command_log.txt","a+")
    bot_event = open("log_files/bot_event_log.txt","a+")
    bot_moderation = open("log_files/bot_moderation_log.txt","a+")
    initialization.close()
    user_command.close()
    user_event.close()
    mod_command.close()
    bot_event.close()
    bot_moderation.close()
    log_msg = f"Logging was set up properly."
    send_log(log_msg, "initialization")

