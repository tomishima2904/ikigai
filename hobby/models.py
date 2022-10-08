from django.db import models


# テスト用のテーブル(藤田君用)
class HobbiesTmp(models.Model):
    hobby = models.CharField(max_length=30, blank=True, null=True)
    outdoor = models.IntegerField(blank=True, null=True)
    team = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hobbies_tmp'
