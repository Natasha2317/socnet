from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models


class UserNet(AbstractUser):
    """ Custom user model
    """
    GENDER = (
        ('male', 'мужской'),
        ('female', 'женский')
    )
    first_login = models.DateTimeField(blank=True, null=True)
    phone = models.CharField('Телефон', max_length=11)
    avatar = models.ImageField(upload_to='user/avatar/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    github = models.CharField(max_length=500, blank=True, null=True)
    birthday = models.DateField('Дата рождения',null=True)
    gender = models.CharField('Пол', max_length=6, choices=GENDER, default='male')
    technology = models.ManyToManyField('Technology', related_name='users', blank=True)
    group = models.ManyToManyField('Group', related_name='users', blank=True)


class Technology(models.Model):
    """ Technology model
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Group(models.Model):
    """ Group model
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
