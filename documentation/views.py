from django.shortcuts import render


def index(request):
    return render(request, "documentation/index.html", context={})

def about(request):
    return render(request, "documentation/about.html", context={})

def how(request):
    return render(request, "documentation/how.html", context={})