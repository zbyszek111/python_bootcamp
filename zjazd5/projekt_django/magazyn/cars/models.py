from django.db import models
from engines.models import Engine
# Create your models here.

TYP_NADWOZIA =(
    ("sedan", "Sedan"),
    ("kombi", "Kombi"),
    ("wan", "Wan")
)

class Cars(models.Model):
    marka = models.CharField(max_length=255)
    model = models.TextField(max_length=255)
    typ_nadwozia = models.CharField(max_length=50, choices=TYP_NADWOZIA, blank=True, null=True)
    rok_prod = models.IntegerField()
    engine = models.ForeignKey(Engine, on_delete= models.DO_NOTHING)



    def __str__(self):
        return f"{self.marka} | {self.model} | {self.rok_prod}"