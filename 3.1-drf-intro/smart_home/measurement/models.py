from django.db import models

class Sensor(models.Model):
    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'

    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self) -> str:
        return f'{self.pk} {self.name}'
    
class Measurement(models.Model):
    class Meta:
        verbose_name = 'Измерение'
        verbose_name_plural = 'Измерения'

    temperature = models.FloatField()
    date_time = models.DateTimeField(auto_now_add=True)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    
