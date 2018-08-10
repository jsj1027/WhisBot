from unittest import TestCase
import discord

class TestMessageEvents(TestCase):
    def test_on_message(self):
        from moderation.message_events import MessageEvents
        message = discord.Message
        message.content = "arian"
        self.assertTrue(MessageEvents.on_message(message))
