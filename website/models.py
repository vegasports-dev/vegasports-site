from django.conf import settings
from django.db import models
from django.utils import timezone
# Create your models here.


# State Model
class States(models.Model):
    statename = models.CharField(max_length=30)
    statecode = models.CharField(max_length=3,default="NULL")
    sportsbooks = models.TextField()


    def bookkeepers(self):
        return self.sportsbooks 

    def __str__(self):
        return self.statename

# BookKeepers Model
class Books(models.Model):
    bookkeepername = models.CharField(max_length=30)
    states = models.TextField()
    wlecomeoffer = models.TextField()
    vsnotes = models.TextField()
    vsrank = models.IntegerField(primary_key=True)
    wlecomeofferrank = models.IntegerField(unique=True)
    logolink = models.CharField(max_length=30)
    BonusCode = models.CharField(max_length=30, default="VEGAS SPORTS")
    appstorerateing = models.FloatField(default=3.0)
    Deposit = models.CharField(max_length=100, default="VISA, MC, PayPal, VIPpreferred, Play+, Discover, Online Banking")

    def __str__(self):
        return self.bookkeepername