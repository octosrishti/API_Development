from django.db import models

from api.utils import slugify


class Market(models.Model):     
  
    
    market_id = models.IntegerField(blank=False, null=False, unique=True)
    date = models.DateTimeField(blank=False, null=False)
    user = models.CharField(blank=False,max_length=100, null=False)
    software = models.CharField(blank=False,max_length=50, null=False)
    department = models.CharField(blank=False,max_length=50, null=False)
    seats = models.IntegerField(blank=True, null=True, default=0)
    amount = models.IntegerField(blank=True, null=True, default=0)
    

    class Meta:
        db_table = 'market_value'
        verbose_name = "maketing"

    def __str__(self):
        return f'{self.entyr_id} {self.date} {self.user} {self.software} {self.seats} {self.amount}'

    def save(self, *args, **kwargs):
        if not self.id:
            super(Market, self).save(*args, **kwargs)
        self.slug = slugify(self.id)
        super(Market, self).save(*args, **kwargs)
