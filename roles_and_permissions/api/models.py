from django.db import models

# Create your models here.
class Permission(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=512, default='')
    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=52)
    permissions = models.ManyToManyField(Permission)
    description = models.CharField(max_length=512, default='')
    def __str__(self):
        return self.name



class UserRole(models.Model):
    ACTIVE = 'AC'
    REVOKED = 'REV'
    STATUS_CHOICES = ((ACTIVE, 'ACTIVE'), (REVOKED, 'REVOKED'))
    user_id = models.IntegerField()
    user_name = models.CharField(max_length=128)
    email = models.CharField(max_length=128) 
    event_id = models.CharField(max_length=64)
    group_id = models.IntegerField()
    role = models.ManyToManyField(Role)
    status = models.CharField(choices=STATUS_CHOICES, default='AC', max_length=8)
    change_date = models.DateTimeField()