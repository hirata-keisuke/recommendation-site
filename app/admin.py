from django.contrib import admin
from .models import Member, BeerBrand, BeerStyle, BeerReview

admin.site.register(Member)
admin.site.register(BeerBrand)
admin.site.register(BeerStyle)
admin.site.register(BeerReview)
