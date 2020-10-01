from django.shortcuts import render
from .models import Project, Comment
from blog.forms import CommentForm

def project_index(request):
    projects = Project.objects.all().order_by('-id')
    context = {
        'projects': projects,
    }
    return render(request, template_name='portfolio/project_index.html', context=context)


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    comments = Comment.objects.filter(project=project).order_by('-created_on')
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                project=project
            )
            comment.save()

    context = {
        'project': project,
        'comments': comments,
        'form': form,
    }
    return render(request, template_name='portfolio/project_detail.html', context=context)

def project_tech(request, tech):
    project = Project.objects.filter(
        technology__name=tech
    )

    context = {
        "tech": tech,
        "project": project
    }
    return render(request, "portfolio/project_tech.html", context)

