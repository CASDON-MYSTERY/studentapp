from django.db import models
from institutions.models import Institution
from events.models import Event 

# Create your models here.

class Faculty(models.Model):
    name = models.CharField("name", max_length = 150)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE,related_name="institution")
    events = models.ManyToManyField(Event,related_name="faculty_events")
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Faculty'
        verbose_name_plural = 'Faculties'
