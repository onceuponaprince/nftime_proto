from django.db import models
from accounts.models import User

# Create your models here.
class Moment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=280, default='')
    desc = models.TextField(blank=True)
    image = models.ImageField(upload_to="moment_images")
    created_at = models.DateTimeField(auto_now_add=True)

class MomentVote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='vote_set')
    moment = models.ForeignKey(Moment, on_delete=models.CASCADE, related_name='vote_set', default='')
    created_at = models.DateTimeField(auto_now_add=True)