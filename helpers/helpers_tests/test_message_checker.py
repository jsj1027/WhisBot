from unittest import TestCase
from helpers.dictionary import *
from helpers.message_checker import *
import discord


class TestMessageChecker(TestCase):

    def setUp(self):
        return

    def tearDown(self):
        return

    def test_check_contents(self):
        message = discord.Message
        message.content = "This is a arian test aplaceholder. Boom."
        expected = {'arian'}
        self.assertEqual(expected, check_contents(message), msg="It didn't parse everything out")

    def test_check_contents_nothing_inside(self):
        message = discord.Message
        message.content = "This is a test. Boom."
        expected = set()
        self.assertEqual(expected, check_contents(message), msg="It didn't parse everything out")
