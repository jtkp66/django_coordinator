from django.shortcuts import render


def survey_new(request):

    return render(request, 'survey/survey-new.html')
