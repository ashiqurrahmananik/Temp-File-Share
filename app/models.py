from django.db import models

# Create your models here.

class myfile(models.Model):
    uploadfile = models.FileField(upload_to='app',default="")
    date = models.DateField(auto_now_add=True)

