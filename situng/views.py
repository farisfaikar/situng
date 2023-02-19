from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello world, anda berada dalam laman home SITUNG")