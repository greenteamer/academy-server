from django.shortcuts import render

# Create your views here.
def index(request):
    context = {'title': 'Academy Home Page'}
    return render(request, 'main/index.html', context)
