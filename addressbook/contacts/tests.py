from django.test import TestCase

from contacts.models import Contact
# Create your tests here.

class ContactTests(TestCase):
    """Contact Model getting tested """
    def test_str(self):
        """do we get string representation correct"""
        contact = Contact(first_name='An',
                          last_name='Person')
        self.assertEquals(str(contact), 'An Person')

