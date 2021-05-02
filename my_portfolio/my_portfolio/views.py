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
    if l%4 != 0:
        for i in range(4-(l%4)):
            certificates.append(None)
        l += 4-(l%4)

    certificate_list = [[],[],[],[]]
    i=0
    while i<l:
        certificate_list[0].append(certificates[i])
        certificate_list[1].append(certificates[i+1])
        certificate_list[2].append(certificates[i+2])
        certificate_list[3].append(certificates[i+3])
        i+=4

    context = {
        'certificates': certificate_list
    }
    return render(request, 'portfolio/certi.html',context)