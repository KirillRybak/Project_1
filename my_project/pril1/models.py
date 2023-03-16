from django.db import models

class model1(models.Model):
    pole1 = models.IntegerField()
    pole2 =models.CharField(max_length=45)
    class Meta:
        verbose_name = "Модель"
        verbose_name_plural = "Модели"
    def __str__(self):
        return  self.pole2

class model2(models.Model):
    pole1 = models.IntegerField()
    pole2 = models.CharField(max_length=45)
    pole4 = models.ManyToManyField(model1)

    class Meta:
        verbose_name = "Модель"
        verbose_name_plural = "Модели"

    def __str__(self):
        return self.pole2