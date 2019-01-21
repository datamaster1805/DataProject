from django.db import models

# Create your models here.


class Products(models.Model):

    p_code = models.IntegerField(unique=True, blank=True, null=True)
    p_name = models.TextField(blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    earning = models.FloatField(blank=True, null=True)
    earn_7d = models.FloatField(blank=True, null=True)
    earn_14d = models.FloatField(blank=True, null=True)
    earn_28d = models.FloatField(blank=True, null=True)
    earn_35d = models.FloatField(blank=True, null=True)
    path_1m = models.FloatField(blank=True, null=True)
    path_3m = models.FloatField(blank=True, null=True)
    path_6m = models.FloatField(blank=True, null=True)
    path_1y = models.FloatField(blank=True, null=True)
    strat_money = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'products'
