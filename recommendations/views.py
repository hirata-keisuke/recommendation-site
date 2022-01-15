from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET

from recommendations import models, forms

@require_GET
def top(request):
    styles = models.BeerStyle.objects.all()
    context = {"styles" : styles}

    return render(
        request, "recommendations/top.html",
        context
    )

def regist_style(request):

    if request.method == "POST":
        form = forms.BeerStyleForm(request.POST)
        if form.is_valid():
            style = form.save()
            return redirect(
                detail_style, style_id=style.pk
            )

    else:
        form = forms.BeerStyleForm()
    return render(
        request, "recommendations/regist_style.html",
        {"form" : form}
    )

def detail_style(request, style_id):
    style = get_object_or_404(models.BeerStyle, pk=style_id)
    brands = models.BeerBrand.objects.filter(style__id=style_id)
    context = {"style" : style, "brands" : brands}

    return render(
        request, "recommendations/detail_style.html",
        context
    )

def edit_style(request, style_id):
    style = get_object_or_404(models.BeerStyle, pk=style_id)

    if request.method == "POST":
        form = forms.BeerStyleForm(request.POST, instance=style)
        if form.is_valid():
            style = form.save()
            return redirect(
                detail_style, style_id=style.pk
            )

    else:
        form = forms.BeerStyleForm(instance=style)
    return render(
        request, "recommendations/edit_style.html",
        {"form" : form, "style_id" : style_id}
    )

def regist_brand(request):

    if request.method == "POST":
        form = forms.BeerBrandForm(request.POST)
        if form.is_valid():
            brand = form.save()
            return redirect(
                detail_brand, brand_id=brand.pk
            )

    else:
        form = forms.BeerBrandForm()
    return render(
        request, "recommendations/regist_brand.html",
        {"form" : form}
    )

def detail_brand(request, brand_id):
    brand = get_object_or_404(models.BeerBrand, pk=brand_id)
    reviews = models.BeerReview.objects.filter(review_to__id=brand_id)
    context = {"brand" : brand, "reviews" : reviews}

    return render(
        request, "recommendations/detail_brand.html",
        context
    )

@login_required
def review(request, brand_id):

    try:
        review = models.BeerReview.objects.get(
            review_to__id=brand_id, reviewed_by__id=request.user.id
        )
    except models.BeerReview.DoesNotExist:
        review = None

    if request.method != "POST":
        form = forms.ReviewForm(instance=review)
        return render(
            request,  "recommendations/review.html",
            {"form" : form, "brand_id" : brand_id}
        )

    form = forms.ReviewForm(request.POST, instance=review)

    if form.is_valid:
        review = form.save(commit=False)
        brand = models.BeerBrand.objects.get(pk=brand_id)
        review.review_to = brand
        
    else:
        return render(
            request,  "recommendations/review.html",
            {"form" : form, "brand_id" : brand_id}
        )

    review.reviewed_by = request.user

    review.save()

    return redirect(
        "detail_brand", brand_id=brand_id
    )
