from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
rooms = [
    {'id': '1', 'name': 'Let learn python'},
    {'id': '2', 'name': 'Design with me'},
    {'id': '3', 'name': 'Front end developer'}
]


def home(request):
    context = {'rooms': rooms}
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html')

