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

    def test_point_assignment(self):
        message_set = {'You','are','a','faggy', 'arian'}
        expected_point_total = 1
        self.assertEqual(point_assignment(message_set), expected_point_total)

    def test_add_points_none_existing_user(self):
        #this only tests if it returns total but not if it added it correctly or if it appened right to a existing user
        self.assertEqual(add_points('000', 1, {'arian','faggy'}), 1)

    def test_add_points_existing_user(self):
        #this only tests if it returns total but not if it added it correctly or if it appened right to a existing user
        self.assertEqual(add_points('00', 1, {'arian','faggy'}), 1)