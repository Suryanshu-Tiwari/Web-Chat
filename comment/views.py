from django.shortcuts import render
from .models import comment, spams
from comment import views
from django.http import HttpResponse
# Create your views here.

def homepage(request):
    return render(request, 'homepage.html')

def suryanshu(request):
    SpamComments = comment.objects.filter(isSpam='True')
    NonSpamComments = comment.objects.filter(isSpam='False')
    check = 'null'
    isSpam = 'False'
    if request.method=='POST':
        CurrentUsername = 'suryanshu'
        comment1 = request.POST.get('comment')
        CommentWords = comment1.split()
        for commentword in CommentWords:
            try:
                check = spams.objects.get(words=commentword)
                if check!='null':
                    isSpam = 'True'
            except:
                isSpam = 'False'     
        post = comment()
        post.name = CurrentUsername
        post.comment = comment1
        post.isSpam = isSpam
        post.save()
        return render(request, 'suryanshu.html', {"SpamComments": SpamComments , "NonSpamComments": NonSpamComments})

    else:
        return render(request, 'suryanshu.html',{"SpamComments": SpamComments, "NonSpamComments": NonSpamComments})


def vikas(request):
    SpamComments = comment.objects.filter(isSpam='True')
    NonSpamComments = comment.objects.filter(isSpam='False')
    check = 'null'
    isSpam = 'False'
    if request.method=='POST':
        CurrentUsername = 'vikas'
        comment1 = request.POST.get('comment')
        CommentWords = comment1.split()
        for commentword in CommentWords:
            try:
                check = spams.objects.get(words=commentword)
                if check!='null':
                    isSpam = 'True'
            except:
                isSpam = 'False'  
        post = comment()
        post.name = CurrentUsername
        post.comment = comment1
        post.isSpam = isSpam
        post.save()
        return render(request, 'vikas.html', {"SpamComments": SpamComments, "NonSpamComments": NonSpamComments})

    else:
        return render(request, 'vikas.html', {"SpamComments": SpamComments, "NonSpamComments": NonSpamComments})

def ritik(request):
    SpamComments = comment.objects.filter(isSpam='True')
    NonSpamComments = comment.objects.filter(isSpam='False')
    check = 'null'
    isSpam = 'False'
    if request.method=='POST':
        CurrentUsername = 'ritik'
        comment1 = request.POST.get('comment')
        CommentWords = comment1.split()
        for commentword in CommentWords:
            try:
                check = spams.objects.get(words=commentword)
                if check!='null':
                    isSpam = 'True'
            except:
                isSpam = 'False'  
        post = comment()
        post.name = CurrentUsername
        post.comment = comment1
        post.isSpam = isSpam
        post.save()
        return render(request, 'ritik.html', {"SpamComments": SpamComments, "NonSpamComments": NonSpamComments})

    else:
        return render(request, 'ritik.html', {"SpamComments": SpamComments, "NonSpamComments": NonSpamComments})


def ved(request):
    SpamComments = comment.objects.filter(isSpam='True')
    NonSpamComments = comment.objects.filter(isSpam='False')
    check = 'null'
    isSpam = 'False'
    if request.method=='POST':
        CurrentUsername = 'ved'
        comment1 = request.POST.get('comment')
        CommentWords = comment1.split()
        for commentword in CommentWords:
            try:
                check = spams.objects.get(words=commentword)
                if check!='null':
                    isSpam = 'True'
            except:
                isSpam = 'False'  
        post = comment()
        post.name = CurrentUsername
        post.comment = comment1
        post.isSpam = isSpam
        post.save()
        return render(request, 'ved.html', {"SpamComments": SpamComments, "NonSpamComments": NonSpamComments})

    else:
        return render(request, 'ved.html', {"SpamComments": SpamComments, "NonSpamComments": NonSpamComments})