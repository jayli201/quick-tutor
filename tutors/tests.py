from django.test import TestCase
from tutors.models import TutorSignup
from django.contrib.auth.models import User

class TutorSignUpEquivalenceTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user('test', 'test@test.com', 'password')
        TutorSignup.objects.create(phone_number="555-555-1234", classes="CS 3240", subjects="science", pay="10", payment_method="venmo", user=user)
        blank = User.objects.create_user('blank', 'blank@gmail.com', 'pass')
        TutorSignup.objects.create(phone_number="", classes="none", subjects="", pay="0", payment_method="", user=blank)

    def test_tutor_equivalence(self):
        tutor = TutorSignup.objects.get(phone_number="555-555-1234")
        self.assertEqual(tutor.classes, "CS 3240")
        self.assertEqual(tutor.subjects, "science")
        self.assertEqual(tutor.pay, "10")
        self.assertEqual(tutor.payment_method, "venmo")

    def test_tutor_boundary(self):
        bad = TutorSignup.objects.get(phone_number="")
        self.assertEqual(bad.classes, "none")
        self.assertEqual(bad.subjects, "")
        self.assertEqual(bad.pay, "0")
        self.assertEqual(bad.payment_method, "")

    def test_tutor_edit(self):
        tutor = TutorSignup.objects.get(phone_number="555-555-1234")
        tutor.phone_number="5"
        tutor.classes="CS 2150"
        tutor.save()
        self.assertEqual(tutor.phone_number,"5")
        self.assertEqual(tutor.classes,"CS 2150")

class GPSTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user('test', 'test@test.com', 'password')
        TutorSignup.objects.create(phone_number="555-555-5555", classes="CS 2150", subjects="science", pay="1", payment_method="venmo", user=user)
        tutor = TutorSignup.objects.get(phone_number="555-555-5555")
        tutor.longitude=5.5
        tutor.latitude=4.4
        tutor.save()

    def test_gps(self):
        tutor = TutorSignup.objects.get(phone_number="555-555-5555")
        self.assertEqual(tutor.longitude,5.5)
        self.assertGreater(tutor.latitude,4.39)
        self.assertGreater(4.41,tutor.latitude)

    def test_change_gps(self):
        tutor = TutorSignup.objects.get(phone_number="555-555-5555")
        tutor.longitude = 7
        tutor.latitude = 2
        tutor.save()
        self.assertEqual(tutor.longitude,7)
        self.assertEqual(tutor.latitude, 2)

class ActiveTestCase(TestCase):
    def setUp(self):
        active = User.objects.create_user('test', 'test@test.com', 'password')
        TutorSignup.objects.create(phone_number="2", classes="CS1", subjects="science", pay="2", payment_method="venmo", user=active)
        inactive = User.objects.create_user('test2', 'test2@test.com', 'password2')
        TutorSignup.objects.create(phone_number="3", classes="CS1", subjects="science", pay="2", payment_method="venmo", user=inactive)
        tutor = TutorSignup.objects.get(phone_number="2")
        tutor.status=True
        tutor.save()

    def test_active(self):
        tutor = TutorSignup.objects.get(phone_number="2")
        self.assertTrue(tutor.status)
        
    def test_inactive(self):
        tutor = TutorSignup.objects.get(phone_number="3")
        self.assertFalse(tutor.status)