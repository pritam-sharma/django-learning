from django.db import models

class Service(models.Model):

    service_id = models.AutoField(primary_key=True)

    service_name = models.CharField(max_length=100)

    service_disc = models.TextField()

    class Meta:
        db_table = "services"
        managed = False
        
class User(models.Model):

    user_id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=100)

    mobile = models.CharField(max_length=20)

    email = models.EmailField(max_length=100, unique=True)

    password = models.CharField(max_length=100)

    class Meta:
        db_table = "users"
        managed = False

    def __str__(self):
        return self.name