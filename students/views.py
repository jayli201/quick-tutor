from django.http import HttpResponse


def landing(request):
    return HttpResponse("Hello, world. You're at the Quick Tutor home page.")


def home(request):
    return HttpResponse("Hello, world. You're at the students home page.")