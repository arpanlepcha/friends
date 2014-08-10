from django.test import TestCase
from django.test.utils import setup_test_environment
import json

setup_test_environment()

class SocialGraphTests(TestCase):
    fixtures = ['/graph/fixtures/data.json']

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Simple home page listing the apis")

    def test_friends(self):
        response = self.client.get('/friends/1', follow=True)
        self.assertEqual(response.status_code, 200)
        json_string = response.content
        data = json.loads(json_string)
        self.assertEqual(2, data[0].get('id'))
        self.assertEqual('Rob', data[0].get('name'))

    def test_friends_of_friends(self):
        response = self.client.get('/friends/friends/3', follow=True)
        self.assertEqual(response.status_code, 200)
        json_string = response.content
        data = json.loads(json_string)
        self.assertEqual(7, len(data))

    def test_recommendations(self):
        response = self.client.get('/friends/recommendation/1', follow=True)
        self.assertEqual(response.status_code, 200)
        json_string = response.content
        data = json.loads(json_string)
        self.assertEqual(0, len(data))

        response = self.client.get('/friends/recommendation/5', follow=True)
        self.assertEqual(response.status_code, 200)
        json_string = response.content
        data = json.loads(json_string)
        self.assertEqual(20, data[0].get('id'))
        self.assertEqual('Katy', data[0].get('name'))
