"""addressbook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import contacts.views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$',
        contacts.views.ListContactView.as_view(),
        name='contacts-list',),
    url(r'^organisations-list$',
        contacts.views.ListOrganisationView.as_view(),
        name='organisations-list',),
    url(r'^(?P<pk>\d+)/$',
        contacts.views.ContactView.as_view(),
        name='contacts-view',),
    url(r'^organisation(?P<pk>\d+)/$',
        contacts.views.OrganisationView.as_view(),
        name='organisations-view',),
    url(r'^new$',
        contacts.views.CreateContactView.as_view(),
        name='contacts-new',),
    url(r'^new-organisation$',
        contacts.views.CreateOrganisationView.as_view(),
        name='organisations-new',),
    url(r'^edit/(?P<pk>\d+)/$',
        contacts.views.UpdateContactView.as_view(),
        name='contacts-edit',),
    url(r'^edit/organisation(?P<pk>\d+)/$',
        contacts.views.UpdateOrganisationView.as_view(),
        name='organisations-edit',),
    url(r'^edit/(?P<pk>\d+)/addresses$',
        contacts.views.EditContactAddressView.as_view(),
        name='contacts-edit-addresses',),
    url(r'^edit/organisation(?P<pk>\d+)/addresses$',
        contacts.views.EditOrganisationAddressView.as_view(),
        name='organisations-edit-addresses',),
    url(r'^edit/organisation(?P<pk>\d+)/contacts(?P<fk>)$',
        contacts.views.EditOrganisationContactsView.as_view(),
        name='organisations-edit-contacts',),
    url(r'^delete/(?P<pk>\d+)/$',
        contacts.views.DeleteContactView.as_view(),
        name='contacts-delete',),
    url(r'^delete/organisation(?P<pk>\d+)/$',
        contacts.views.DeleteOrganisationView.as_view(),
        name='organisations-delete',),
]
urlpatterns += staticfiles_urlpatterns()