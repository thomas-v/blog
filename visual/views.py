from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from visual.models import Theme, Tutorial
from datetime import datetime, timedelta

def index(request):

    themes = Theme.objects.all()

    context = {
        'themes':themes
    }
    return render(request, 'visual/index.html', context)

def listTutorials(request, id):

    themes = Theme.objects.all()
    theme = Theme.objects.get(pk=id)
    tutorials = Tutorial.objects.filter(theme=id)

    week_ago = datetime.now() - timedelta(days=7)

    context = {
        'themes':themes,
        'currentTheme':theme,
        'tutorials':tutorials,
        'week_ago':week_ago
    }

    return render(request, 'visual/list.html', context)

def detailTutorial(request, id):

    themes = Theme.objects.all()
    tutorial = Tutorial.objects.get(pk=id)
    context = {
        'themes':themes,
        'tutorial':tutorial
    }
    return render(request, 'visual/detail.html', context)