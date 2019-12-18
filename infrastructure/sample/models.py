from django.db import models


class SampleData(models.Model):
    id_name = models.CharField(max_length=500)
    root_cause = models.CharField(max_length=500)
    cause = models.CharField(max_length=500)
    cause_type = models.CharField(max_length=500)
    channel = models.CharField(max_length=500)
    mark_result = models.CharField(max_length=500)

    def __str__(self):
        return self.id_name
