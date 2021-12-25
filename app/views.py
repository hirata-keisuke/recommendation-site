from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import BeerBrand
from .forms import LoginForm

def top(request):
    return render(request, "app/top.html")

def overview(request):
    brand_list = BeerBrand.objects.all()
    context = {"brand_list":brand_list}
    return render(request, "app/overview.html", context)

def search(request):
    return render(request, "app/search.html")

def search_result(request):
    return render(request, "app/search_result.html")

def login(request):
    form = LoginForm()

    return render(request, "app/login.html", {"form" : form})

def login_check(request):

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            return HttpResponse("app/logout.html")

    else:
        form = LoginForm()

    return render(request, "app/login.html", {"form" : form})


def logout(request):
    return render(request, "app/logout.html")
