from django.test import TestCase
from tutors.models import TutorSignup

class TutorSignUpEquivalenceTestCase(TestCase):
    def setUp(self):
        TutorSignup.objects.create(phone_number="555-555-1234", classes="CS 3240", subjects="science", pay="10", payment_method="venmo")
        
    def test_tutor(self):
        tutor = TutorSignup.objects.get(phone_number="555-555-1234")
        self.assertEqual(tutor.classes, "CS 3240")
        self.assertEqual(tutor.subjects, "science")
        self.assertEqual(tutor.pay, "10")
        self.assertEqual(tutor.payment_method, "venmo")
        

class TutorSignUpBoundaryTestCase(TestCase):
    def setUp(self):
        TutorSignup.objects.create(phone_number="", classes="none", subjects="", pay="0", payment_method="")

    def test_tutor(self):
        bad = TutorSignup.objects.get(phone_number="")
        self.assertEqual(bad.classes, "none")
        self.assertEqual(bad.subjects, "")
        self.assertEqual(bad.pay, "0")
        self.assertEqual(bad.payment_method, "")

class GPSTestCase(TestCase):
    def setUp(self):
        TutorSignup.objects.create(phone_number="555-555-5555", classes="CS 2150", subjects="science", pay="1", payment_method="venmo")
        tutor = TutorSignup.objects.get(phone_number="555-555-5555")
        tutor.longitude=5.5
        tutor.latitude=4.4
        tutor.save()

    def test_gps(self):
        tutor = TutorSignup.objects.get(phone_number="555-555-5555")
        self.assertEqual(tutor.longitude,5.5)
        self.assertGreater(tutor.latitude,4.39)
        self.assertGreater(4.41,tutor.latitude)

class ActiveTestCase(TestCase):
    def setUp(self):
        TutorSignup.objects.create(phone_number="2", classes="CS1", subjects="science", pay="2", payment_method="venmo")
        tutor = TutorSignup.objects.get(phone_number="2")
        tutor.status=True
        tutor.save()

    def test_active(self):
        tutor = TutorSignup.objects.get(phone_number="2")
        self.assertTrue(tutor.status)

class InactiveTestCase(TestCase):
    def setUp(self):
        TutorSignup.objects.create(phone_number="3", classes="CS1", subjects="science", pay="2", payment_method="venmo")
    
    def test_inactive(self):
        tutor = TutorSignup.objects.get(phone_number="3")
        self.assertFalse(tutor.status)