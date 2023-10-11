from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import HomePageView, AboutPageView


class HomepageTests(SimpleTestCase):

    def setUp(self):
        """This function written because we don't write again code."""
        url = reverse('home')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        """For exists homepage."""
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        """For exists homepage template."""
        self.assertTemplateUsed(self.response, 'home.html')

    def test_homepage_contains_correct_html(self):
        """Check correct medias in file."""
        self.assertContains(self.response, 'Homepage')

    def test_homepage_does_not_contains_incorrect_html(self):
        """Check incorrect medias in file."""
        self.assertNotContains(self.response, 'blah blah blah blah')

    def test_homepage_url_resolves_homepage(self):
        """Check that homepage in correct url and path or not"""
        view = resolve('/')
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)


class AboutPageTests(SimpleTestCase):  # new
    def setUp(self):
        url = reverse('about')
        self.response = self.client.get(url)

    def test_aboutpage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_aboutpage_template(self):
        self.assertTemplateUsed(self.response, 'about.html')

    def test_aboutpage_contains_correct_html(self):
        self.assertContains(self.response, 'About Page')

    def test_aboutpage_does_not_contain_incorrect_html(self):
        self.assertNotContains(
            self.response, 'Hi there! I should not be on the page.')

    def test_aboutpage_url_resolves_aboutpageview(self):
        view = resolve('/about/')
        self.assertEqual(
            view.func.__name__,
            AboutPageView.as_view().__name__
        )
