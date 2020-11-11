from django.db import models

class User(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=50)
    e_mail = models.CharField(max_length=50)
    password = models.CharField(max_length=16)

    def __str__(self):
        return self.username+", "+self.fname + " " + self.lname


class Session(models.Model):
    userId = models.CharField(max_length=500)
