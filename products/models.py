from django.db import models
class MainGroup(models.Model):
    code = models.IntegerField()
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name



class ProductGroup (models.Model):
    code = models.IntegerField()
    name = models.CharField(max_length=255)
    maingroup = models.ForeignKey(MainGroup,on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.name

class ProductInfo(models.Model):
    code1 = models.BigIntegerField(unique=True)
    code2 = models.BigIntegerField()
    name = models.CharField(max_length=255)
    group = models.ForeignKey(ProductGroup,on_delete=models.CASCADE)
    #gr
    weight = models.BigIntegerField()
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
print("3")
class CarInfo (models.Model):
    code = models.BigIntegerField()
    name = models.CharField(max_length=255)
    #cm3
    capacity = models.FloatField()
    #gr
    weight = models.FloatField()
    def __str__(self):
        return self.name


