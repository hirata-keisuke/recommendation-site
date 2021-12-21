from django.db import models

class Member(models.Model):

    SEX = [("M", "男性"),["F", "女性"]]

    name = models.CharField("会員の名前", max_length=20)
    user_name = models.CharField("会員のユーザー名", max_length=20)
    sex = models.CharField("会員の性別", max_length=1, choices=SEX)
    password = models.CharField("会員のパスワード", max_length=15)
    address = models.CharField("会員の出身地", max_length=30)
    birth_date = models.DateField("会員の生年月日")
    mail = models.EmailField("会員のeメールアドレス")

    def __str__(self):
        return self.name

class BeerStyle(models.Model):

    style = models.CharField("ビアスタイルの名称", max_length=20)
    birthplace = models.CharField("ビアスタイルの発祥地", max_length=20)
    fermentation = models.CharField("醸造方法", max_length=10)
    desciption = models.TextField()

    def __str__(self):
        return self.style

class BeerBrand(models.Model):

    name = models.CharField("ビールの銘柄", max_length=15)
    degree = models.FloatField("アルコール度数")
    color = models.CharField("ビールの色", max_length=10)
    srm = models.FloatField("米国醸造化学者学会によるビールの色の数値指標")
    bitterness = models.FloatField("ビールの苦味IBU")
    style = models.ForeignKey(BeerStyle, on_delete=models.RESTRICT)

    def __str__(self):
        return self.name

class BeerReview(models.Model):

    user = models.ForeignKey(Member, on_delete=models.CASCADE)
    brand = models.ForeignKey(BeerBrand, on_delete=models.CASCADE)
    review = models.TextField("ビール銘柄に関するレビュー文")
    rate = models.IntegerField("会員の好み", choices=[(1, "好き"),(-1, "イマイチ")])
