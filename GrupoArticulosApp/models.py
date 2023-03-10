from django.db import models

# Create your models here.


class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100,null=False,blank=False)

    class Meta:
        db_table='categoria'




