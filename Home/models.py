from django.db import models

# Create your models here.

class Grants(models.Model):
    fund_title = models.TextField()
    summary = models.TextField()
    opportunity_status = models.TextField()
    award_range = models.TextField()

    def __str__(self):
        return self.fund_title