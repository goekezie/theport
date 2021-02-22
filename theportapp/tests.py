from django.test import TestCase
from .models import Project
from .models import Messenger

class ProjectTest(TestCase):
    def setUp(self):
        Project.objects.create(title="Tester", content="the Rolling Test")


    def Project_ws_Field_label(self):
        #The post can upload
        Project.objects.get(title="Tester")
        field_label = Project._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_date_of_post(self):
        Project.objects.get(title="Tester")
        field_label = Project._meta.get_field('created_on').verbose_name
        self.assertEqual(field_label, 'created on')

    def title_name_max_length(self):
        Project.objects.get(title="Tester")
        max_length = Project._meta.get_field('title').max_length
        self.assertEqual(max_length, 200)


class MessengerTest(TestCase):
    def setUp(self):
        Messenger.objects.create(name="Tes", message="the Test offer")


    def Messenger_ws_Field_label(self):
        #The post can upload
        Messenger.objects.get(name="Tes")
        field_label = Messenger._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_date_of_message(self):
        Messenger.objects.get(name="Tes")
        field_label = Messenger._meta.get_field('created_on').verbose_name
        self.assertEqual(field_label, 'created on')

    def title_name_max_length(self):
        Messenger.objects.get(name="Tes")
        max_length = Messenger._meta.get_field('name').max_length
        self.assertEqual(max_length, 200)