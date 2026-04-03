from django.db import models

class SensorData(models.Model):
    air_temperature = models.FloatField()
    process_temperature = models.FloatField()
    rotational_speed = models.FloatField()
    torque = models.FloatField()
    tool_wear = models.FloatField()
    machine_failure = models.IntegerField()

    def __str__(self):
        return f"Temp: {self.air_temperature}"