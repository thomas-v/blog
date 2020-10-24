from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from visual.models import Theme

def index(request):

    themes = Theme.objects.all()

    context = {
        'themes':themes
    }
    return render(request, 'visual/index.html', context)