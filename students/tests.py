from django.test import TestCase

class BasicTestCase(TestCase):
    def test_1eq1(self):
        self.assertTrue(1 == 1)