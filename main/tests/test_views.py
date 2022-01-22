from django.test import TestCase
from django.urls import reverse
from main import forms


class TestPage(TestCase):
    def test_home_page_works(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')
        self.assertContains(resp, 'BookTime')
        
    def test_about_us_page_works(self):
        resp = self.client.get(reverse('about_us'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'about_us.html')
        self.assertContains(resp, 'BookTime')

    def test_contact_us_page_works(self):
        response = self.client.get(reverse("contact_us"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "contact_form.html")
        self.assertContains(response, "BookTime")
        self.assertIsInstance(
            response.context["form"], forms.ContactForm
        )