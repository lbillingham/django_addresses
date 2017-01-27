from django.core.urlresolvers import reverse
# # from django.forms import ModelForm
# from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic import ListView

from contacts.models import Contact

# Create your views here.
class ListContactView(ListView):
    model = Contact
    template_name = 'contact_list.html'


class CreateContactView(CreateView):
    model = Contact
    template_name = 'edit_contact.html'
    fields = model.field_names()

    def get_success_url(self):
        return reverse('contacts-list')
