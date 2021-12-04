import jdatetime
from django.db import models
from django_jalali.db import models as jmodels
from django.contrib.auth.models import User

class Center(models.Model):
    code = models.IntegerField(unique=True,verbose_name="کد")
    name = models.CharField(max_length=255,unique=True,verbose_name="نام")
    class Meta:
        verbose_name = "مرکز"
        verbose_name_plural = "مراکز"
    def __str__(self):
        return self.name

class Event(models.Model):

    title = models.CharField(max_length=225,verbose_name="عنوان")
    affected = models.ForeignKey(Center,on_delete=models.CASCADE,verbose_name="واحد تاثیر گذار")
    effected = models.ManyToManyField(Center,related_name="effected",verbose_name ="واحدهای تاثیر پذیر")
    recordDate = jmodels.jDateTimeField(default=jdatetime.datetime.now(),verbose_name="زمان ذخیره")
    eventDate = jmodels.jDateTimeField(verbose_name="زمان واقعه")
    description = models.TextField(verbose_name="شرح واقعه تاثیر پذیر")
    description2 = models.TextField(verbose_name="شرح واقعه گذار",null=True,blank=True)
    firstAccept = models.BooleanField(verbose_name="تایید اولیه",default=False)
    secendAccept = models.BooleanField(verbose_name="تایید دوم",default=False)
    creator = models.ForeignKey(User,on_delete=models.DO_NOTHING)

    def effectedList(self):

        return " - ".join([str(p) for p in self.effected.all()])
    effectedList = property(effectedList)
    effectedList.fget.short_description ="مراکز تاثیر پذیر"
    def date (self):
        return self.eventDate.date()
    date = property(date)
    date.fget.short_description = "تاریخ"

    class Meta:
        verbose_name = "واقعه"
        verbose_name_plural = " وقایع"

    def __str__(self):
        return self.affected.name


class Access(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,unique=True,verbose_name="نام کاربر")
    affect = models.ManyToManyField(Center,verbose_name="مراکز تاثیر پذیر زیر مجموعه")
    manager = models.ForeignKey(User,related_name="MANAGER",on_delete=models.DO_NOTHING,verbose_name="نام مدیر")
    isManager = models.BooleanField(default=False)




    def __str__(self):
        return self.user.first_name + " " + self.user.last_name


class MessageError(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    time = jmodels.jDateTimeField(default=jdatetime.datetime.now())
    message = models.TextField(max_length=5000)
    description = models.TextField(null=True,blank=True)
    inprocess= models.BooleanField(default=False)
    processed = models.BooleanField(default=False)
    def __str__(self):
        return self.user.username + "had" + self.message


class Setting (models.Model):

    can_add_visitors_target_without_center_target = models.BooleanField(verbose_name="امکان اضافه کردن اهداف ویزیتورها بدون هدف مرکز")


