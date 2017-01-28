from django.test import LiveServerTestCase
from django.test import TestCase
from django.test.client import Client
from django.test.client import RequestFactory

from selenium import webdriver

from contacts.models import Contact
from contacts.views import ListContactView
# #######################################################
#  models tests
# #######################################################
class ContactTests(TestCase):
    """Contact Model getting tested """
    def test_str(self):
        """do we get string representation correct"""
        contact = Contact(first_name='An',
                          last_name='Person')
        self.assertEquals(str(contact), 'An Person')

# #######################################################
#  views tests
# #######################################################
class ContactListViewTests(TestCase):
    """working view for list of contacts?"""
    def test_contacts_in_the_client(self):
        client = Client()
        response = client.get('/')
        # should have empty lsit before creating a Contact
        self.assertEquals(list(response.context['object_list']), [])
        # now create a Contact and make sure it is where we expect
        Contact.objects.create(first_name='Django', last_name='Reinhardt')
        response = client.get('/')
        self.assertEquals(response.context['object_list'].count(), 1)

    def test_contacts_in_the_requestfactory(self):
        factory = RequestFactory()
        request = factory.get('/')
        response = ListContactView.as_view()(request)
        self.assertEquals(list(response.context_data['object_list']), [])
        Contact.objects.create(first_name='Lancelot', last_name='the Brave')
        response = ListContactView.as_view()(request)
        self.assertEquals(response.context_data['object_list'].count(), 1)
        
# #######################################################
#  integration tests
# #######################################################
class ContactListIntegrationTests(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Firefox()
        super(ContactListIntegrationTests, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super(ContactListIntegrationTests, cls).tearDownClass()

    def test_contact_listed(self):
        # create a test contact
        Contact.objects.create(first_name='foo', last_name='bar')
        # make sure it's listed as <first> <last> on the list
        self.browser.get('{}{}'.format(self.live_server_url, '/'))
        self.assertEqual(
            self.browser.find_elements_by_css_selector('.contact')[0].text,
            'foo bar'
        )
    
    def test_add_contact_linked(self):

        self.assert_(
            self.browser.find_element_by_link_text('add contact')
        )

    def test_add_contact(self):

        self.browser.get('{}{}'.format(self.live_server_url, '/'))
        self.browser.find_element_by_link_text('add contact').click()

        self.browser.find_element_by_id('id_first_name').send_keys('test')
        self.browser.find_element_by_id('id_last_name').send_keys('contact')
        self.browser.find_element_by_id('id_email').send_keys('test@example.com')

        self.browser.find_element_by_id("save_contact").click()
        self.assertEqual(
            self.browser.find_elements_by_css_selector('.contact')[-1].text,
            'test contact'
        )