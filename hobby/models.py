from django.db import models


# テスト用のテーブル(藤田君用)
class HobbiesTmp(models.Model):
    hobby = models.CharField(max_length=30, blank=True, null=True)
    outdoor = models.IntegerField(blank=True, null=True)
    team = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hobbies_tmp'


# 本番用のテーブル (ver.1)
class Hobbies(models.Model):
    hobby = models.CharField(max_length=30)
    outdoor = models.IntegerField(blank=True, null=True, default=0)
    skill = models.IntegerField(blank=True, null=True, default=0)
    group = models.IntegerField(blank=True, null=True, default=0)
    cost = models.IntegerField(blank=True, null=True, default=0)

    class Meta:
        managed = False
        db_table = 'hobbies'


# 本番用のテーブル (ver.2)
class HobbiesSecond(models.Model):
    hobby = models.CharField(max_length=30)
    outdoor = models.IntegerField(blank=True, null=True)
    skill = models.IntegerField(blank=True, null=True)
    group = models.IntegerField(blank=True, null=True)
    cost = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hobbies_second'