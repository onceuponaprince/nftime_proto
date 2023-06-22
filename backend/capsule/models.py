from django.db import models
from api.models import Moment


# Create your models here.

class SmartContract(models.Model):
    date = models.DateField(auto_now_add=True)
    contract_address = models.CharField(max_length=42)  # Ethereum addresses are 42 characters long
    ipfs_url = models.URLField()

    def __str__(self):
        return str(self.date)

class Memory(models.Model):
    moment = models.ForeignKey(Moment, related_name='moment_id', on_delete=models.DO_NOTHING)
    ipfs_url = models.URLField()

    class Meta:
        unique_together = ('moment', 'ipfs_url')
    
    def __str__(self):
        return str(self.ipfs_url)