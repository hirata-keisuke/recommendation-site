from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

from .models import BeerBrand, BeerReview

#def Top(request):
#    return render(request, "app/top.html")

class BrandList(ListView):
    template_name = "app/brand_list.html"
    model = BeerBrand

class BrandDetail(DetailView):
    template_name = "app/brand_detail.html"
    model = BeerBrand

class ReviewCreate(CreateView):
    template_name = "app/review_create.html"
    model = BeerReview
    fields = ("user", "brand", "review", "rate")
    success_url = reverse_lazy("app:brand_list")

class BrandDelete(DeleteView):
    template_name = "app/brand_delete.html"
    model = BeerBrand
    success_url = reverse_lazy("app:brand_list")

class BrandUpdate(UpdateView):
    template_name = "app/brand_update.html"
    model = BeerBrand
    fields = ("name", "degree", "color", "srm", "bitterness", "style")
    success_url = reverse_lazy("app:brand_list")

#def login(request):
#    form = LoginForm()

#    return render(request, "app/login.html", {"form" : form})

#def login_check(request):

#    if request.method == "POST":
#        form = LoginForm(request.POST)
#        if form.is_valid():
#            return HttpResponse("app/logout.html")

#    else:
#        form = LoginForm()

#    return render(request, "app/login.html", {"form" : form})


#def logout(request):
#    return render(request, "app/logout.html")
