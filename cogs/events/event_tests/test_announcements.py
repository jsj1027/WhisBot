from unittest import TestCase
import discord
from discord.ext import commands
import configparser

config = configparser.ConfigParser()
config.read("../../../config.ini")


class TestAnnouncements(TestCase):
    def setUp(self):
        return

    def test_message_same_channel(self):
        bot = commands.Bot(command_prefix="!")
        message = discord.Message
        message.channel = bot.get_channel(id=config['channel_text']['announcement_channel_text'])
        announcement_channel = bot.get_channel(id=config['channel_text']['announcement_channel_text'])
        message.channel.id
        announcement_channel.channel.id
        self.assertEqual(message.channel.id, announcement_channel.channel.id)

