from django.test import TestCase
from tutors.models import TutorSignup

class TutorSignUpTestCase(TestCase):
    def setUp(self):
        TutorSignup.objects.create(phone_number="555-555-1234", classes="CS 3240", subjects="science", pay="10", payment_method="venmo")
        TutorSignup.objects.create(phone_number="", classes="none", subjects="", pay="0", payment_method="")

    def test_students(self):
        tutor = TutorSignup.objects.get(phone_number="555-555-1234")
        self.assertEqual(tutor.classes, "CS 3240")
        self.assertEqual(tutor.subjects, "science")
        self.assertEqual(tutor.pay, "10")
        self.assertEqual(tutor.payment_method, "venmo")
        bad = TutorSignup.objects.get(phone_number="")
        self.assertEqual(bad.classes, "none")
        self.assertEqual(bad.subjects, "")
        self.assertEqual(bad.pay, "0")
        self.assertEqual(bad.payment_method, "")