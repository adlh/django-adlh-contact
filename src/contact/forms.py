from django.utils.translation import gettext_lazy as _
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label=_(u'Name'), max_length=50)
    message = forms.CharField(label=_(u'Nachricht'), widget=forms.Textarea)
    tel = forms.CharField(label=_(u'Telefon'), max_length=20, required=False)
    email = forms.EmailField(label=_(u'Email'))
    cc_myself = forms.BooleanField(label=_(u'Eine Kopie an meine Email-Adresse verschicken'), required=False)

