from unittest import TestCase
from helpers.dictionary import *


class TestDictionary(TestCase):

    def setUp(self):
        return

    def tearDown(self):
        return

    def test_get_black_list(self):
        t = get_black_list()
        self.assertEqual(black_list, t)

    def test_get_white_list(self):
        t = get_white_list()
        self.assertEqual(white_list, t)

    def test_get_users(self):
        t = get_users()
        self.assertEqual(users, t)

    def test_user_in_database(self):
        expected = [[], 0, 0]
        self.assertEqual(check_user_database('00'), expected, msg="Was not the right person")

    def test_user_not_in_database(self):
        self.assertEqual(check_user_database('000'), False, msg="Was in the database or it borked")

    def test_add_user_to_user_database(self):
        mock_database = get_users()
        add_user_to_user_database('01234', [], 0)
        self.assertIn('01234', mock_database, msg='The user was not found in the database')

    def test_fail_to_add_user_to_user_database(self):
        with self.assertRaises(ValueError,  msg='The user was somehow found in the database'):
            add_user_to_user_database('00', [], 0)

    def test_check_black_list_database(self):
        expected = 0.5
        self.assertEqual(expected, check_black_list_database('arian'))

    def test_check_not_in_black_list_database(self):
        expected = False
        self.assertEqual(expected, check_black_list_database('return'))

    def test_check_black_list_intersection(self):
        message = "Jake is an arian".split()
        message_set = {}
        for word in message:
            message_set[word] = word
        intersection = check_black_list_intersection(message_set)
        self.assertEqual({"arian"}, intersection)

    def test_check_no_black_list_intersection(self):
        message = "Jake is a nice guy".split()
        message_set = {}
        for word in message:
            message_set[word] = word
        intersection = check_black_list_intersection(message_set)
        self.assertEqual(set(), intersection)