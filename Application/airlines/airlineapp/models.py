from django.db import models

class Countries(models.Model):
    name = models.CharField(primary_key=True, unique=True, max_length=255)
    iso_code = models.CharField(max_length=2)
    dafif_code = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "countries"
    
class Planes(models.Model):
    name = models.CharField(max_length=255)
    iata = models.CharField(max_length=3)
    icao = models.CharField(max_length=4)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "planes"

class Airlines(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    iata = models.CharField(max_length=2, default = None, blank=  False)
    icao = models.CharField(max_length=3, default = None, blank = False)
    callsign = models.CharField(max_length=255)
    active = models.CharField(max_length=255)
    country = models.ForeignKey(Countries, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "airlines"

class Airports(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.ForeignKey(Countries, null=True, on_delete=models.SET_NULL)
    iata = models.CharField(max_length=3, default = None, blank = False)
    icao = models.CharField(max_length=4, default = None, blank = False)
    latitude = models.DecimalField(default = None, blank = False, decimal_places=6, max_digits=12)
    longitude = models.DecimalField(default = None, blank = False, decimal_places=6, max_digits=12)
    altitude = models.IntegerField(null = False, blank = True)
    timezone = models.CharField(max_length=10, default = None, null = True)
    dst = models.CharField(max_length=1, default = "U")
    tz_db = models.CharField(max_length=100)
    type = models.CharField(max_length = 7, default = "airport", null = False, blank = False)
    source = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "airports"


class Routes(models.Model):
    airline_id = models.ForeignKey(Airlines, on_delete=models.CASCADE)
    from_airport = models.ForeignKey(Airports, on_delete=models.CASCADE, related_name='from_airport')
    to_airport = models.ForeignKey(Airports, on_delete=models.CASCADE, related_name='to_airport')
    codeshare = models.CharField(max_length=1, default="Y")
    stops = models.IntegerField(null = False, default = 0, blank = False)
    equipment = models.ManyToManyField(Planes, through="Equipment_list")

    class Meta:
        verbose_name_plural = "routes"

class Equipment_list(models.Model):
    plane = models.ForeignKey(Planes, on_delete=models.DO_NOTHING)
    route = models.ForeignKey(Routes, on_delete=models.DO_NOTHING)
