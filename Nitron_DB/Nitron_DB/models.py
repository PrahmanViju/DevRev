from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy
from django.db import models
from datetime import datetime

# Create your models here.
from django.db import models

class User(models.Model):
# Класс нанимающего студента

    class Meta:
        db_table = "students"
        name = "username"


    username = models.TextField(name="Юзернейм")
    birthdate = models.TextField()
    location= models.TextField(name="Местонахождение")
    status= models.TextField(name="статус")

    def __str__(self):
        return f"{self.status} {self.username}"


class Company(models.Model):
  

    class Meta:
        db_table = "company"
        cname = "Описание компании"
    

    company_name = models.TextField(cname="Наименование организации")
    company_address = models.TextField(cname="Адрес")
    
    city = models.TextField(cname="Город")

    def __str__(self):
        return self.company_name


class UserInField(models.Model):

    class Meta:
        db_table = "User"
        name = "User_info"

    user_number = models.TextField(name='Имя')
    company_id = models.ForeignKey(Company, on_delete=models.RESTRICT, name="Айди_компании")
    address_id = models.ForeignKey(User, on_delete=models.RESTRICT, name="Адрес_компании")
    status = models.TextField(name="Статус учебы")

 




class Order(models.Model):


#Еще не написан

    def save(self, *args, **kwargs):
        self.last_updated_dt = datetime.now()
        super().save(*args, **kwargs)