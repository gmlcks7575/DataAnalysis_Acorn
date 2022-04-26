from django.db import models

# Create your models here. table 선언
class Article(models.Model): #models.Model 상속 #논리적으로 선언
    code = models.CharField(max_length = 10) #varchar
    name = models.CharField(max_length = 20)
    price = models.IntegerField() #integer
    pub_date = models.DateTimeField() #date