from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.ImageField(upload_to='./upload/')
    release_date = models.DateField()
    lte_exists = models.BooleanField(default=True)
    slug = models.SlugField()
