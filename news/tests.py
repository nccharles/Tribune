from django.test import TestCase
from .models import Editor,Article,tags

# Create your tests here.
class EditorTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.charles= Editor(first_name = 'Charles', last_name ='NDAYISABA', email ='charles.ndayisaba@moringaschool.com')
# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.charles,Editor))