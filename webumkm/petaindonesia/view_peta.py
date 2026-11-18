from django.shortcuts import render


def petasatu(request):
    # render peta indonesia
    return render(request, 'petaindonesia/petasatu.html')


def petadua(request):
    # render peta jabodetabek geojson
    return render(request, 'petaindonesia/petadua.html')
