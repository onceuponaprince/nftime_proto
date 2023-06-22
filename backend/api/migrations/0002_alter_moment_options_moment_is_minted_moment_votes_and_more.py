# Generated by Django 4.2.2 on 2023-06-22 09:47

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='moment',
            options={'ordering': ['-created_at']},
        ),
        migrations.AddField(
            model_name='moment',
            name='is_minted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='moment',
            name='votes',
            field=models.ManyToManyField(related_name='moment_votes', through='api.MomentVote', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='momentvote',
            unique_together={('user', 'moment')},
        ),
    ]