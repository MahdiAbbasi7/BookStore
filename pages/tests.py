from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import HomePageView


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
