from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def home_page(request):
    return render(request, 'index.html')
    # return HttpResponse("这是主页！")

def play_video(request):
    return render(request, 'player.html')

def page1(request):
    return render(request, 'page1.html')

def login(request):
    return render(request, 'login.html')

def cake(request):
    return render(request, 'BirthdayCake.html')

def memo(request):
    return render(request, 'Memories.html')
