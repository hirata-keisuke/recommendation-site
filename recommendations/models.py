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
