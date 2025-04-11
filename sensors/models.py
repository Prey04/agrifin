from django.db import models

class Device(models.Model):
    device_name = models.CharField(max_length=100)
    location = models.CharField(max_length=255, blank=True, null=True)
    installed_on = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)  # True = online, False = offline

    def __str__(self):
        return self.device_name
    
class SoilData(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    moisture = models.FloatField()  # % VWC
    pH = models.FloatField()
    temperature = models.FloatField()  # °C
    ec = models.FloatField()  # dS/m
    nitrogen = models.FloatField()  # mg/kg or ppm
    phosphorus = models.FloatField()
    potassium = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

class EnvironmentData(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    air_temperature = models.FloatField()
    humidity = models.FloatField()  # % RH
    rainfall = models.FloatField()  # mm/hr
    light_intensity = models.FloatField()  # Lux or PAR
    wind_speed = models.FloatField()  # optional, m/s
    timestamp = models.DateTimeField(auto_now_add=True)

# Vision Data
class VisionData(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='vision/')
    pest_type = models.CharField(max_length=100, blank=True, null=True)
    infestation_level = models.CharField(max_length=100, blank=True, null=True)
    disease_type = models.CharField(max_length=100, blank=True, null=True)
    growth_stage = models.CharField(max_length=100, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
