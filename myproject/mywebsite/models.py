from django.db import models

class Service(models.Model):

    service_id = models.AutoField(primary_key=True)

    service_name = models.CharField(max_length=100)

    service_disc = models.TextField()

    class Meta:
        db_table = "services"
        managed = False