from django.urls import path, include
from django.views.generic import TemplateView
from .views import ContactFormView
from . import views

urlpatterns = [
    path(r'', ContactFormView.as_view(), name='contact'),
    path(r'thanks/', TemplateView.as_view(template_name='contact/thanks.html'), name='thanks'),
]
