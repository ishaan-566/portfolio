from django.shortcuts import render
from myapp.models import Project, Language, Certificate


def sitemap(request):
    return render(request, 'portfolio/sitemap.xml')


def cv(request):
    projects = Project.objects.all().order_by('-id')[:3]
    languages = Language.objects.all()

    context = {
        'projects': projects,
        'languages': languages
    }
    return render(request, 'portfolio/ind.html', context)


def certificate(request):
    certificates = list(Certificate.objects.all().order_by('-id'))
    l = len(certificates)
    l += 4 - (l % 4)
    certificate_list = []
    for i in range(0, l, 4):
        certificate_list.append(certificates[i:i + 4])
    context = {
        'certificates': certificate_list
    }
    return render(request, 'portfolio/certi.html', context)
