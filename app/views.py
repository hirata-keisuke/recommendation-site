from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

from .models import BeerBrand, BeerReview

class TopList(ListView):
    ...

class StyleList(ListView):
    ...

class StyleDetail(DetailView):
    ...

class BrandSearch():
    ...

class BrandDetail(DetailView):
    template_name = "app/brand_detail.html"
    model = BeerBrand

class ReviewCreate(CreateView):
    template_name = "app/review_create.html"
    model = BeerReview
    fields = ("user", "brand", "review", "rate")
    success_url = reverse_lazy("app:brand_list")

class CreateCheck():
    ...

class CreateComplete():
    ...

class ReviewDelete(DeleteView):
    ...

class DeleteComplete():
    ...

class ReviewUpdate(UpdateView):
    ...

class UpdateCheck():
    ...

class UpdateComplete():
    ...

class Login():
    ...

class Logout():
    ...

class Error():
    ...

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
