from django.test import TestCase
from django.urls import resolve
from recommendations import views

class TopTest(TestCase):
    def test_resolve_correct_url(self):
        found = resolve("/")
        self.assertEqual(views.top, found.func)

    def test_use_correct_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "recommendations/top.html")

class RegistStyleTest(TestCase):
    def test_resolve_correct_url(self):
        found = resolve("/recommendations/style/regist/")
        self.assertEqual(views.regist_style, found.func)

    def test_use_correct_template(self):
        response = self.client.get("/recommendations/style/regist/")
        self.assertTemplateUsed(response, "recommendations/regist_style.html")

class DetailStyleTest(TestCase):
    def test_resolve_correct_url(self):
        found = resolve("/recommendations/style/1/")
        self.assertEqual(views.detail_style, found.func)

    def test_use_correct_template(self):
        response = self.client.get("/recommendations/style/1/")
        self.assertTemplateUsed(response, "recommendations/detail_style.html")

class EditStyleTest(TestCase):
    def test_resolve_correct_url(self):
        found = resolve("/recommendations/style/1/edit/")
        self.assertEqual(views.edit_style, found.func)

    def test_use_correct_template(self):
        response = self.client.get("/recommendations/style/1/edit/")
        self.assertTemplateUsed(response, "recommendations/edit_style.html")
