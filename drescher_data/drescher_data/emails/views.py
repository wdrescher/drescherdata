from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView

from .forms import ContactForm
from .models import Contact

# Create your views here.
class ContactFormView(FormView):
    template_name = 'pages/contact.html'
    form_class = ContactForm
    model = Contact
    success_url = '/getback/'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return redirect(reverse_lazy('emails:getback'))
