from django.db import models

# Create your models here.
RODZAJE_SILNIKA = (
    ("diezel", "Diezel"),
    ("benzyna", "Benzyna"),
    ("parowy", "Parowy"),
    ("elektryczny", "Elektryczny"),
    ("inny", "Inny")
)

class Engine(models.Model):
    nazwa =models.CharField(max_length=255)
    pojemnosc = models.IntegerField(null=True, blank=True)
    ilosc_cyl = models.IntegerField(null=True, blank=True)
    rodzaj_silnika = models.CharField(choices=RODZAJE_SILNIKA, max_length=255)
    opis = models.TextField()

    def __str__(self):
        return self.nazwa + " " + self.rodzaj_silnika
