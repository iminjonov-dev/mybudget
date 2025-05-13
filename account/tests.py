from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


class UserAuthTest(TestCase):
    def test_user_register(self):
        response = self.client.post(reverse('register'), {
            'firstname': '',
            'lastname': '',
            'username': '',
            'email': '',
            'phone': '',
            'password': ''
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='').exists())

    def test_user_login(self):
        user = User.objects.create_user(username='', password='', is_active=True)
        response = self.client.post(reverse('login'), {
            'username': 'ali123',
            'password': 'testpass123'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(int(self.client.session['_auth_user_id']), user.id)

    def test_otp_verification(self):
        user = User.objects.create_user(
            username='ali123',
            email='ali@example.com',
            password='testpass123',
            is_active=False,
            verification_code='123456'
        )
        session = self.client.session
        session['user_email'] = 'ali@example.com'
        session.save()

        response = self.client.post(reverse('verify_code'), {
            'otp': '123456'
        })
        user.refresh_from_db()
        self.assertTrue(user.is_active)
        self.assertEqual(user.verification_code, '')
        self.assertEqual(response.status_code, 302)


class ProfileUpdateTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='ali123',
            password='testpass123',
            first_name='Ali',
            last_name='Valiyev',
            phone='998901234567'
        )
        self.client.login(username='ali123', password='testpass123')

    def test_update_profile(self):
        response = self.client.post(reverse('account_update'), {
            'firstname': 'Alisher',
            'lastname': 'Qodirov',
            'phone': '998909999999'
        })
        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, 'Alisher')
        self.assertEqual(self.user.last_name, 'Qodirov')
        self.assertEqual(self.user.phone, '998909999999')
        self.assertEqual(response.status_code, 302)



class LogoutTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='ali123', password='testpass123')
        self.client.login(username='ali123', password='testpass123')

    def test_logout(self):
        response = self.client.get(reverse('logout'))
        self.assertNotIn('_auth_user_id', self.client.session)
        self.assertEqual(response.status_code, 302)

