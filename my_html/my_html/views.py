from django.shortcuts import render


def index(request):
    return render(request, 'main.html')


def static_media(request):
    return render(request, 'static-media.html')