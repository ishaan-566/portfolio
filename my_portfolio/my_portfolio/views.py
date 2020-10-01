from django.shortcuts import render
from myapp.models import Project, Language


def cv(request):
    projects = Project.objects.all().order_by('-id')[:4]
    languages = Language.objects.all()
    context = {
        'projects': projects,
        'languages': languages
    }
    return render(request, 'portfolio/ind.html',context)

