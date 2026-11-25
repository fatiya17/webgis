from django.shortcuts import render


def petasatu(request):
    # render peta indonesia
    return render(request, 'petaindonesia/petasatu.html')


def petadua(request):
    # render peta jabodetabek geojson
    return render(request, 'petaindonesia/petadua.html')

def petakampus(request):
    return render(request, 'petaindonesia/petakampus.html')

def peta_provinsi(request):
    return render(request, "petaindonesia/peta_provinsi.html")

def petani_jawa(request):
    return render(request, "petaindonesia/petani_jawa.html")