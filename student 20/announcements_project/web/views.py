from django.views.generic import TemplateView
from django.shortcuts import render

class HomePageView(TemplateView):
    template_name = 'web/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['welcome_message'] = 'Hi there, hello'
        return context