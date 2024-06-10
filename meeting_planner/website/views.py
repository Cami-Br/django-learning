from django.shortcuts import render
from django.http import HttpResponse
from meetings.models import Meeting


def welcome(request):
    if request.user.is_authenticated:
        context = {"meetings": Meeting.objects.all()}
    else:
        context = {}
    return render(
        request,
        template_name="website/welcome.html",
        context=context,
    )


def about_page(request):
    return HttpResponse("Hello, my name is Cami!")
