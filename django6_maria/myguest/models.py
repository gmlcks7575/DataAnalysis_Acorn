from django.db import models

# Create your models here.
class Guest(models.Model):
    #myno = models.AutoField(auto_created = True, primary_key = True) # 나만의 id 만들기
    title = models.CharField(max_length = 50)
    content = models.TextField()
    regdate = models.DateTimeField()
    
    class Meta:
        #ordering=('title',)
        ordering=('-id',)
        #ordering=('title','id')