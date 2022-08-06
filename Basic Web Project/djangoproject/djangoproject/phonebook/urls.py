from django.urls import path
from djangoproject.phonebook.views import landing_page

urlpatterns = [
    path('', landing_page, name='landing-page')
]
