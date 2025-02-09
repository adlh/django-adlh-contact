from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from datetime import datetime
from .forms import ContactForm


class ContactFormView(FormView):
    template_name= 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('thanks')

    def form_valid(self, form):
        name = form.cleaned_data['name']
        message = form.cleaned_data['message']
        from_email = form.cleaned_data['email']
        tel = form.cleaned_data['tel']
        cc_myself = form.cleaned_data['cc_myself']

        msg_tel = ''
        if tel:
            msg_tel = u'\n\n%s: %s' % (_(u'Telefon'), tel)

        body = _(u'Am %(date)s %(name)s schrieb:') % {
                'date': datetime.now().strftime('%d.%m.%Y um %H:%M'),
                'name': name} + '\nEmail: %s\n\n%s' % (from_email,
                                                        message + msg_tel)

        # set managers as recipients
        recipients = [e for n, e in settings.MANAGERS]
        subject = u'%s%s' % (settings.EMAIL_SUBJECT_PREFIX, _(u'Kontakt'))
        try:
            if cc_myself:
                send_mail( subject,
                    _(u'Kopie Ihrer Nachricht:') + '\n\n%s' % body,
                    settings.SERVER_EMAIL, [from_email])
            send_mail(subject, body, settings.SERVER_EMAIL, recipients)
        except BadHeaderError:
            return HttpResponse(_(u'Falsches Header. Bitte eine gültige '
                'Emailadresse angeben.'))
        return super(ContactFormView, self).form_valid(form)


def thanks(request):
    return render(request, 'thanks.html', {})

