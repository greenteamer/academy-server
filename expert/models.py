from django.db import models


class Expert(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField()
    personal_life = models.TextField()
    statistic = models.TextField()

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
