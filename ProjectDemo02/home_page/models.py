from django.db import models

# Create your models here.


class Products(models.Model):

    p_code = models.CharField(max_length=15, blank=True, null=True)
    p_name = models.CharField(max_length=30, blank=True, null=True)
    start_date = models.CharField(max_length=20, blank=True, null=True)
    earning = models.CharField(max_length=20, blank=True, null=True)
    earn_7d = models.CharField(max_length=20, blank=True, null=True)
    earn_14d = models.CharField(max_length=20, blank=True, null=True)
    earn_28d = models.CharField(max_length=20, blank=True, null=True)
    earn_35d = models.CharField(max_length=20, blank=True, null=True)
    path_1m = models.CharField(max_length=20, blank=True, null=True)
    path_3m = models.CharField(max_length=20, blank=True, null=True)
    path_6m = models.CharField(max_length=20, blank=True, null=True)
    path_1y = models.CharField(max_length=20, blank=True, null=True)
    start_money = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'products'
