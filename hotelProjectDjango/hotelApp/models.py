from django.db import models


class PredResults(models.Model):

    adults = models.FloatField()
    repeated_guest = models.FloatField()
    hotel_type = models.FloatField()
    direct_binary = models.FloatField()
    children = models.FloatField()
    babies = models.FloatField()
    cancellations_binary = models.FloatField()
    uncanceled_binary = models.FloatField()
    booking_changes = models.FloatField()
    waiting_list = models.FloatField()
    required_parking = models.FloatField()
    special_requests = models.FloatField()
    average_rate = models.FloatField()
    lead_time = models.FloatField()
    classification = models.CharField(max_length=30)

    def __str__(self):
        return self.classification

class Results(models.Model):
    pass
