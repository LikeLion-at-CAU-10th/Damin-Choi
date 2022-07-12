from django.db import models

# Create your models here.
class  Introduce(models.Model):
  # id      = 자동생성 -->장고에서 식별을 위해 자동으로 설정하는 값
  name      = models.CharField(max_length=50, default="최다민", null=True, blank=True)
  major     = models.CharField(max_length=50, default="경영학과", null=True, blank=True)
  age      = models.CharField(max_length=20, default="23", null=True, blank=True)
  club  = models.CharField(max_length=20, default="멋사", null=True, blank=True)