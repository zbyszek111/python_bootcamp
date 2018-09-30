from django.db import models

# Create your models here.
CONTAINER_TYPES = (
    ("glassbottle", "Glass botle"),
    ("plasticbatlee","Plastic botlle"),
    ("box", "bpxes"),
)

class Container(models.Model):
    type= models.CharField(choices=CONTAINER_TYPES, max_length=50)