from django.db import models
from datetime import datetime
class data(models.Model):

    sale = models.FileField(upload_to='media/data')
    returnSale = models.FileField(upload_to='media/data')
    date = models.DateTimeField(default=datetime.now())
    name = models.CharField(max_length=255)
