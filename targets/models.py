from django.db import models
from django.contrib.auth.models import User
class SaleLine(models.Model):
    code = models.IntegerField(unique=True)
    name= models.CharField(max_length=255)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "گروه فروش"
        verbose_name_plural = "گروههای فروش"

class ProductTargetGroup(models.Model):
    code = models.IntegerField(unique=True,verbose_name="کد گروه کالا")
    name = models.CharField(max_length=255,unique=True,verbose_name="نام گروه کالا")

    class Meta:
        verbose_name = "گروه محصول"
        verbose_name_plural = "گروه محصولات"
    def __str__(self):
        return self.name


class CenterD(models.Model):
    code = models.IntegerField(unique=True)
    name = models.CharField(unique=True,max_length=255,verbose_name="نام مرکز")
    lines = models.ManyToManyField(SaleLine)
    products_group = models.ManyToManyField(ProductTargetGroup)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name="مرکز توزیع"
        verbose_name_plural ="مرکز توزیع ها"
        ordering=("code",)


class CenterTargetDefinde(models.Model):
    center = models.ForeignKey(CenterD,on_delete=models.CASCADE,verbose_name="مرکز توزیع")
    Pgroup = models.ForeignKey(ProductTargetGroup,on_delete=models.CASCADE,verbose_name="گروه محصول")
    Qnty = models.IntegerField()
    accept = models.BooleanField(default=False)

    class Month(models.IntegerChoices):
        فروردین = 1
        اردیبهشت = 2
        خرداد = 3
        تیر = 4
        مرداد = 5
        شهرویور = 6
        مهر = 7
        آبان = 8
        آذر = 9
        دی = 10
        بهمن = 11
        اسفند = 12
    month = models.IntegerField(choices=Month.choices,verbose_name="ماه")
    class Meta:
        unique_together=('center','Pgroup','month')
        verbose_name = "اهداف مرکز توزیع"
        verbose_name_plural = "اهداف مراکز توزیع"

    def __str__(self):
        return f"{self.center}"

class Superviser(models.Model):
    code = models.IntegerField(unique=True)
    name = models.CharField(max_length=255)
    center = models.ForeignKey(CenterD,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "سرپرست"
        verbose_name_plural = "سرپرست ها"


class Visitor(models.Model):
    code = models.IntegerField(unique=True)
    name = models.CharField(max_length=255)
    cneter = models.ForeignKey(CenterD,on_delete=models.CASCADE)
    superviser = models.ForeignKey(Superviser,on_delete=models.DO_NOTHING)
    line = models.ForeignKey(SaleLine,on_delete=models.DO_NOTHING)
    status = models.BooleanField(default=False)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name="فروشنده"
        verbose_name_plural = "فروشندگان"


class SetVisitorTarget(models.Model):
    class Month(models.IntegerChoices):
        فروردین = 1
        اردیبهشت = 2
        خرداد = 3
        تیر = 4
        مرداد = 5
        شهرویور = 6
        مهر = 7
        آبان = 8
        آذر = 9
        دی = 10
        بهمن = 11
        اسفند = 12
    month = models.IntegerField(choices=Month.choices,verbose_name="ماه")
    visitor = models.ForeignKey(Visitor,on_delete=models.CASCADE)
    pgroup = models.ForeignKey(ProductTargetGroup,on_delete=models.CASCADE)
    qnty  = models.IntegerField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.visitor.name+str(self.month)+str(self.pgroup.name)
    class Meta:
        unique_together = ('month','visitor','pgroup')
        verbose_name = "تعریف هدف"
        verbose_name_plural = "تعریف اهداف"

class TargetAccess(models.Model):
    user = models.OneToOneField(User,unique=True,on_delete=models.CASCADE,verbose_name="نام کاربری")
    centers = models.ManyToManyField(CenterD,verbose_name="مراکز")


    def __str__(self):
        return self.user.username
    class Meta:
        verbose_name = "دسترسی اهداف"
        verbose_name_plural = "دسترسی های اهداف"

