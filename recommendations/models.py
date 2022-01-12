from django.db import models

class BeerStyle(models.Model):
    name = models.CharField("ビアスタイル", max_length=15)
    birth_place = models.CharField("発祥地", max_length=10)
    fermentation = models.IntegerField(
        "発酵方法", choices=((1,"上面発酵"),(2,"下面発酵"))
    )
    description = models.TextField("説明")

    def __str__(self):
        return self.name
