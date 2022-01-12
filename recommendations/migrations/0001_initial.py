# Generated by Django 3.2 on 2022-01-11 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BeerStyle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, verbose_name='ビアスタイル')),
                ('birth_place', models.CharField(max_length=10, verbose_name='発祥地')),
                ('fermentation', models.IntegerField(choices=[(1, '上面発酵'), (2, '下面発酵')], verbose_name='発酵方法')),
                ('description', models.TextField(verbose_name='説明')),
            ],
        ),
    ]
