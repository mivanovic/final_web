from finalweb.models import *
from django.views.generic import TemplateView, FormView
from django.http import HttpResponse, HttpResponseBadRequest
from django.core.mail import send_mail
from finalweb.forms import EmailForm
from finalst import settings
from django.shortcuts import render, render_to_response
import json
from django.views.decorators.csrf import csrf_protect


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


class ReferencesView(TemplateView):
    queryset = Reference.objects.order_by('-complexity')
    context_object_name = 'references_list'
    template_name = 'reference.html'

    def get_context_data(self, **kwargs):
        context = super(ReferencesView, self).get_context_data(**kwargs)
        context[self.context_object_name] = self.queryset
        return context


class SingleReferenceView(TemplateView):
    template_name = 'single_reference.html'

    def get_context_data(self, **kwargs):
        context = super(SingleReferenceView, self).get_context_data(**kwargs)
        context['data'] = Reference.objects.get(pk=self.kwargs.get('id', None))
        context['images'] = RefImages.objects.filter(reference__pk=self.kwargs.get('id', None))
        return context


class ContactView(TemplateView, FormView):
    form_class = EmailForm
    template_name = 'contact.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']

            report = "Od: {0} '<{1}>'\r\nPoruka: {2}\r\nTelefon: {3}".format(name, email, message, phone)

            send_mail('Final-st.hr kontakt forma', report, email, [settings.EMAIL_HOST_USER])

            if request.is_ajax():
                return HttpResponse('OK')
            else:
                pass
        else:
            if request.is_ajax():
                errors_dict = {}
                if form.errors:
                    for error in form.errors:
                        e = form.errors[error]
                        errors_dict[error] = unicode(e)

                return HttpResponseBadRequest(json.dumps(errors_dict))
            else:
                pass

        return render(request, self.template_name, {'form': form})


class QuestionsView(TemplateView):
    template_name = 'questions.html'
    queryset = Questions.objects.all()

    def get_context_data(self, **kwargs):
        context = super(QuestionsView, self).get_context_data(**kwargs)
        context['questions'] = self.queryset
        return context

from django.core.context_processors import csrf
def my_view(request):
    c = {}
    c.update(csrf(request))
    c['questions'] = Questions.objects.all()

    return render_to_response('questions.html', c)


class MaterialsView(TemplateView):
    template_name = 'materials.html'


def search(request):
    template_name = 'questions.html'

    search_text = ''

    # def post(self, request, *args, **kwargs):
    if request.method == 'POST':
        search_text = request.POST['search_text']

    result = Questions.objects.filter(question__contains=search_text).filter(answer_contains=search_text)

    return render_to_response('ajax_search.html', {'result': result})




