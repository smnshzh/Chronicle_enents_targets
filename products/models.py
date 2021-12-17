from django.db import models


class ProductGroup (models.Model):
    code = models.IntegerField()
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class ProductInfo(models.Model):
    code1 = models.IntegerField(unique=True)
    code2 = models.IntegerField()
    name = models.CharField(max_length=255)
    group = models.ForeignKey(ProductGroup,on_delete=models.CASCADE)
    #gr
    weight = models.IntegerField()
    #cm
    height = models.FloatField()
    width = models.FloatField()
    lenght = models.FloatField()
    inBox = models.FloatField()


    def capacity(self):
        return self.height*self.width*self.lenght
    capacity = property(capacity)

    def total_weight(self):
        return self.weight*self.inBox
    total_weight = property(total_weight)

    def __str__(self):
        return self.name
class CarInfo (models.Model):
    code = models.IntegerField()
    name = models.CharField(max_length=255)
    #cm3
    capacity = models.FloatField()
    #gr
    weight = models.FloatField()
    def __str__(self):
        return self.name


