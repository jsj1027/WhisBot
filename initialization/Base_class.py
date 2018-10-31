# Whisbot by jsj1027/kaloshade

import configparser
from log_sys.log_system import *


class Base:
    # config for token credit to https://github.com/nh-server/Kurisu
    config = configparser.ConfigParser()

    log_location = 'initialization'

    training_programs = [
        'cogs.events.bot_events',
        'cogs.events.announcement_events',
        'cogs.commands.bot_commands'  # ,
        #  'cogs.mod_commands',
        #  'moderation.message_events'
    ]

    failed_training_programs = []

    def get_log_location(self):
        return self.log_location

    def get_config(self):
        return self.config

    def load_config(self, file_location):
        self.config.read(file_location)

    def get_training_programs(self):
        return self.training_programs

    def get_failed_training_programs(self):
        return self.failed_training_programs

    def set_failed_training_programs(self, failed_programs):
        self.failed_training_programs = failed_programs

    def get_conifg_id(self, group, item):
        config_item = self.config[group][item]
        if config_item.isdigit():
            return int(config_item)
        else:
            return config_item
