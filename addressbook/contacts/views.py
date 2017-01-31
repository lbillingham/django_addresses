from django.core.urlresolvers import reverse
# # from django.forms import ModelForm
# from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView

from contacts.models import Contact, Organisation
from contacts import forms

# Create your views here.
class ListOrganisationView(ListView):
    model = Organisation
    template_name = 'organisation_list.html'

class ListContactView(ListView):
    model = Contact
    template_name = 'contact_list.html'


class AbstractCreateView(CreateView):
    html_slug = 'ERROR-ABSTRACT'

    class Meta:
        abstract = True

    @property
    def template_name(self):
        return 'edit_{}.html'.format(self.html_slug)

    def get_success_url(self):
        return reverse('{}s-list'.format(self.html_slug))

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['action'] = reverse('{}s-new'.format(self.html_slug))

        return context

class CreateContactView(AbstractCreateView):
    model = Contact
    html_slug = 'contact'
    form_class = forms.ContactForm

class CreateOrganisationView(AbstractCreateView):
    model = Organisation
    html_slug = 'organisation'
    form_class = forms.OrganisationForm


class AbstractUpdateView(UpdateView):

    html_slug = 'ERROR-ABSTRACT'

    class Meta:
        abstract = True

    def get_success_url(self):
        return reverse('{}s-list'.format(self.html_slug))

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['action'] = reverse('{}s-edit'.format(self.html_slug),
                                    kwargs={'pk': self.get_object().id})
        return context

class UpdateContactView(AbstractUpdateView):
    model = Contact
    html_slug = 'contact'
    template_name = 'edit_{}.html'.format(html_slug)
    form_class = forms.ContactForm


class UpdateOrganisationView(AbstractUpdateView):
    model = Organisation
    html_slug = 'organisation'
    template_name = 'edit_{}.html'.format(html_slug)
    form_class = forms.OrganisationForm


class DeleteContactView(DeleteView):

    model = Contact
    template_name = 'delete_contact.html'

    def get_success_url(self):
        return reverse('contacts-list')

class DeleteOrganisationView(DeleteView):

    model = Organisation
    template_name = 'delete_organisation.html'

    def get_success_url(self):
        return reverse('organisations-list')

class ContactView(DetailView):
    model = Contact
    template_name = 'contact.html'

class OrganisationView(DetailView):
    model = Organisation
    template_name = 'organisation.html'


class EditContactAddressView(UpdateView):

    model = Contact
    template_name = 'edit_addresses.html'
    form_class = forms.ContactAddressFormSet

    def get_success_url(self):

        # redirect to the Contact view.
        return self.get_object().get_absolute_url()