from django.test import SimpleTestCase 
from django.urls import reverse

# Create your tests here.

class HomePageTest(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    def test_url_available_by_name(self):
        response =self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
    def test_template_name_correct(self):
        response = self.client.get(reverse("index"))
        self.assertTemplateUsed(response, "index.html")
    def test_template_content(self):
        response = self.client.get(reverse("index"))
        self.assertContains(response, "<h1>Home</h1>")

class AboutPageTest(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)
    def test_url_available_by_name(self):
        response =self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)
    def test_template_name_correct(self):
        response = self.client.get(reverse("about"))
        self.assertTemplateUsed(response, "about.html")
    def test_template_content(self):
        response = self.client.get(reverse("about"))
        self.assertContains(response, "<h1>About</h1>")
