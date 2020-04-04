from django.test import TestCase
from students.models import StudentSignup

class BasicTestCase(TestCase):
    def test_1eq1(self):
        self.assertTrue(1 == 1)

class StudentSignUpEquivalenceTestCase(TestCase):
    def setUp(self):
        StudentSignup.objects.create(phone_number="123-456-7890", classes="CS 3240")
        
    def test_student(self):
        student = StudentSignup.objects.get(phone_number="123-456-7890")
        self.assertEqual(student.classes, "CS 3240")

class StudentSignUpBoundaryTestCase(TestCase):
    def setUp(self):
        StudentSignup.objects.create(phone_number="5", classes="")
        
    def test_student(self):
        blank = StudentSignup.objects.get(phone_number="5")
        self.assertEqual(blank.classes, "")