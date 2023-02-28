from django.shortcuts import render
from ml_codes.studentscore_reg import StudentPerformance
from .forms import PerformanceForm
from django.views.generic import TemplateView
from django.http import JsonResponse


def home(request):
    form = PerformanceForm()
    '''first_grade = 0
    second_grade = 0
    fathers_education = 0
    mothers_education = 0
    study_time = 0
    sex = 0


    explanatory = [[]]
    result = None
    percent_result = 0
    '''

    '''if request.method == 'GET':
        form = PerformanceForm(request.GET)
        if form.is_valid():
            first_grade = request.GET.get('first_grade')
            second_grade = request.GET.get('second_grade')
            fathers_education = request.GET.get('fathers_education')
            mothers_education = request.GET.get('mothers_education')
            study_time = request.GET.get('study_time')
            sex = request.GET.get('sex')

            explanatory = [
                first_grade,
                second_grade,
                fathers_education,
                mothers_education,
                study_time,
                sex
            ]

            performance = StudentPerformance()

            explanatory = [[float(x) for x in explanatory]]

            result = performance.predictPerformance(explanatory)
            percent_result = round(result['score']/20 * 100, 2)

            print(result)'''

    '''context = {'result': result, 'percent_result': percent_result, 'form': form}'''
    context = {'form': form}
    return render(request, 'home/home.html', context)


class About(TemplateView):
    template_name = 'home/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'femi'
        return context


class Contact(TemplateView):
    template_name = 'home/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'mike'
        return context


def result(request):
    is_ajax = request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
    form = PerformanceForm()
    if is_ajax:
        print(request.GET)
        first_grade = request.GET.get('first_grade')
        second_grade = request.GET.get('second_grade')
        fathers_education = request.GET.get('fathers_education')
        mothers_education = request.GET.get('mothers_education')
        study_time = request.GET.get('study_time')
        sex = request.GET.get('sex')

        explanatory = [
            first_grade,
            second_grade,
            fathers_education,
            mothers_education,
            study_time,
            sex
        ]

        performance = StudentPerformance()

        explanatory = [[float(x) for x in explanatory]]

        result = performance.predictPerformance(explanatory)
        percent_result = round(result['score'] / 20 * 100, 2)

        print(result)

        context = {'result': result, 'percent_result': percent_result}
        return JsonResponse(context)
