from django.db import models

# Create your models here.
class Backpack(models.Model):
    id = models.AutoField(primary_key = True) # 自動生成ID
    p_type = models.CharField(max_length = 10)
    p_name = models.CharField(max_length = 20)
    p_count = models.IntegerField(default = 0)