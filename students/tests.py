from django.test import TestCase
from students.models import StudentSignup

class BasicTestCase(TestCase):
    def test_1eq1(self):
        self.assertTrue(1 == 1)

class StudentSignUpTestCase(TestCase):
    def setUp(self):
        StudentSignup.objects.create(phone_number="1234567890", classes="CS 3240")

    def test_students(self):
        student = StudentSignup.objects.get(phone_number="1234567890")
        self.assertEqual(student.classes, "CS 3240")