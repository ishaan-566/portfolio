from django.shortcuts import render
from .models import Project, Comment
from blog.forms import CommentForm
from django.core.mail import EmailMessage
from django.http import Http404


def project_index(request):
    projects = Project.objects.all().order_by('-id')
    context = {
        'projects': projects,
    }
    return render(request, template_name='portfolio/project_index.html', context=context)


def project_detail(request, pk):
    try:
        project = Project.objects.get(pk=pk)
    except Project.DoesNotExist:
        raise Http404("No Project matches the given query.")
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
            body = "Hello me,<br>{}<br> just post a comment on your project {}<br>.<i>\"{}\"</i>".format(
                form.cleaned_data["author"], project.title, form.cleaned_data["body"])
            try:
                email = EmailMessage(
                    'Comment on project',
                    body,
                    '',
                    ['ishaanaggarwal566@gmail.com'],
                )
                email.content_subtype = "html"
                email.send()
            except:
                pass

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
