from django.conf import settings
from django.db import models
from django.core.validators import MinValueValidator

class BeerStyle(models.Model):
    name = models.CharField("ビアスタイル", max_length=15)
    birth_place = models.CharField("発祥地", max_length=10)
    fermentation = models.IntegerField(
        "発酵方法", choices=((1,"上面発酵"),(2,"下面発酵"))
    )
    description = models.TextField("説明")

    def __str__(self):
        return self.name

class BeerBrand(models.Model):
    name = models.CharField("ビール銘柄", max_length=15)
    degree = models.FloatField("アルコール度数", validators=[MinValueValidator(0)])
    color = models.CharField("ビールの色", max_length=10)
    bitterness = models.FloatField("IBU", validators=[MinValueValidator(0)])
    style = models.ForeignKey(BeerStyle, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class BeerReview(models.Model):
    review = models.TextField("ユーザの感想")
    review_to = models.ForeignKey(
        BeerBrand, 
        verbose_name="感想対象", on_delete=models.CASCADE
    )
    reviewed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="投稿者", on_delete=models.CASCADE
    )
    reviewed_at = models.DateTimeField("投稿日", auto_now_add=True)
    updated_at = models.DateTimeField("更新日", auto_now=True)

    def __str__(self):
        return self.review_to.name + "に対する" + self.reviewed_by.username + "の感想"
