from finalweb.models import *
from django.views.generic import TemplateView, FormView
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from finalweb.forms import EmailForm
from finalst import settings
from django import forms


class IndexView(TemplateView):
    queryset_one = Quote.objects.all()
    queryset_two = Reference.objects.order_by('-complexity')[:3]
    queryset_three = Reference.objects.filter(newest=True).first()
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['quotes'] = self.queryset_one
        context['top_three'] = self.queryset_two
        context['newest'] = self.queryset_three
        return context


class ContactView(TemplateView):
    template_name = 'contact.html'


class ReferencesView(TemplateView):
    queryset = Reference.objects.order_by('-complexity')
    context_object_name = 'references_list'
    template_name = 'reference.html'

    def get_context_data(self, **kwargs):
        context = super(ReferencesView, self).get_context_data(**kwargs)
        context['references_list'] = self.queryset
        return context


class SingleReferenceView(TemplateView):
    template_name = 'single_reference.html'

    def get_context_data(self, **kwargs):
        context = super(SingleReferenceView, self).get_context_data(**kwargs)
        context['data'] = Reference.objects.get(pk=self.kwargs.get('id', None))
        context['images'] = RefImages.objects.filter(reference__pk=self.kwargs.get('id', None))
        return context


class SendMail(TemplateView, FormView):
    form_class = EmailForm
    template_name = 'contact.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']

            try:
                send_mail(name + " <" + email + ">", message + ' telefon:' + phone, email, [settings.EMAIL_HOST_USER])
            except forms.ValidationError:
                pass

            return HttpResponseRedirect('/contact/')

        return HttpResponseRedirect('/contact/')

