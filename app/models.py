from django.contrib.auth.models import User
from django.db import models

class Member(models.Model):

    SEX = [("M", "男性"),["F", "女性"]]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sex = models.CharField("会員の性別", max_length=1, choices=SEX)
    post_code = models.CharField("会員の郵便番号", max_length=10)
    address = models.CharField("会員の住所", max_length=30)
    birth_date = models.DateField("会員の生年月日")

    def __str__(self):
        return self.name

class BeerStyle(models.Model):

    style = models.CharField("ビアスタイルの名称", max_length=20)
    birthplace = models.CharField("ビアスタイルの発祥地", max_length=20)
    fermentation = models.CharField("醸造方法", max_length=10)
    description = models.TextField("ビアスタイルの説明")

    def __str__(self):
        return self.style

class BeerBrand(models.Model):

    name = models.CharField("ビールの銘柄", max_length=15)
    degree = models.FloatField("アルコール度数")
    color = models.CharField("ビールの色", max_length=10)
    bitterness = models.FloatField("ビールの苦味IBU")
    style = models.ForeignKey(BeerStyle, on_delete=models.RESTRICT)

    def __str__(self):
        return self.name

class BeerReview(models.Model):

    user = models.ForeignKey(Member, on_delete=models.CASCADE)
    brand = models.ForeignKey(BeerBrand, on_delete=models.CASCADE)
    review = models.TextField("ビール銘柄に関するレビュー文")
    preference = models.IntegerField("会員の好み", choices=[(1, "好き"),(-1, "嫌い")])
