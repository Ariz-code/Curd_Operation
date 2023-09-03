from django.db import models

# Create your models here.
class empolyee(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=40)
    email=models.EmailField(unique=True)
    mobile=models.BigIntegerField()
    def __str__(self):
        return self.name

