from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve
from .forms import CustomUserCreationForm
from .views import SignUpView


class CustomUserTest(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='mahdi',
            email='abbasimahdi782@gmail.com',
            password='miai09362092181'
        )
        self.assertEqual(user.username, 'mahdi')
        self.assertEqual(user.email, 'abbasimahdi782@gmail.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='mahdi',
            email='abbasimahdi782@gmail.com',
            password='miai09362092181'
        )
        self.assertEqual(admin_user.username, 'mahdi')
        self.assertEqual(admin_user.email, 'abbasimahdi782@gmail.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


class SignUpTest(TestCase):
    """Sign Up needs to be tested, but login and logout don't because they have built-in functions."""

    def setUp(self) -> None:
        self.response = self.client.get(reverse('signup'))

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'registration/signup.html')
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(self.response, 'bluh bluh bluh')

    def test_signup_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_sign_up(self):
        view = resolve('/accounts/signup/')
        self.assertEqual(view.func.__name__, SignUpView.as_view().__name__)
