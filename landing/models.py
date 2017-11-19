from django.db import models

# Create your models here.

class Subscriber(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=120)

    def __str__(self):
        return "{} {}".format(self.name, self.email)

    class Meta:
        verbose_name = 'MySubsriber'
        verbose_name_plural = 'A lot of Subscribers'
