from django.shortcuts import render
from django.http import HttpResponse

from .models import BeerBrand

def index(request):
    return HttpResponse("Hello, world. You're at the app index.")

def overview(request):
    brand_list = BeerBrand.objects.all()
    context = {"brand_list":brand_list}
    return render(request, "app/overview.html", context)
