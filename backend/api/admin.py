from django.contrib import admin
from .models import Moment, MomentVote

# Register your models here.

admin.site.register(Moment)
admin.site.register(MomentVote)