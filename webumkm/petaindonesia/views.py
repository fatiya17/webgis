from django.http import HttpResponse


def welcome(request):
    # route halaman welcome / root
    return HttpResponse("<h1>Selamat Datang di Situs Kami!</h1>")
