from django.shortcuts import render
from django.views.generic import TemplateView

'''def home(request):
    context = {}
    return render(request, 'performance/home.html', context)
'''


class Home(TemplateView):
    template_name = 'actualtest/test.html'
    man = 'Ade'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['man'] = 'Ade'
        return context




