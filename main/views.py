from django.shortcuts import render


def index(request):
    context = {"title": "Academy Home Page"}
    return render(request, "main/index.html", context)
