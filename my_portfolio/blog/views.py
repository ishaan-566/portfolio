from django.shortcuts import render
from.models import *
from .forms import CommentForm
from django.core.mail import EmailMessage

def map(request):
    return render(request, "blog/map.html")

def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    categories = Category.objects.all()
    temp = []
    class Temp_Category:
        def __init__(self, name, count):
            self.name = name
            self.count = count
    for c in categories:
        post = Post.objects.filter(categories__name__contains=c.name)
        temp.append(Temp_Category(c.name, len(post)))
    context = {
        "posts": posts,
        "categories": temp
    }
    return render(request, "blog/blog_index.html", context)



def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by('-created_on')
    categories = Category.objects.all()
    temp = []
    class Temp_Category:
        def __init__(self, name, count):
            self.name = name
            self.count = count
    for c in categories:
        post = Post.objects.filter(categories__name__contains=c.name)
        if not c.name == category:
            temp.append(Temp_Category(c.name, len(post)))
    context = {
        "category": category,
        "posts": posts,
        "categories": temp
    }
    return render(request, "blog/blog_category.html", context)


def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post).order_by('-id')
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()
            body = "Hello me,<br>{}<br> just post a comment on your Blog {}<br>.\"<i>{}</i>\"".format(form.cleaned_data["author"], post.title, form.cleaned_data["body"])
            email = EmailMessage(
                'Comment on Blog',
                body,
                '',
                ['ishaanaggarwal566@gmail.com'],
            )
            email.content_subtype = "html"
            email.send()
    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }

    return render(request, "blog/blog_detail.html", context)
