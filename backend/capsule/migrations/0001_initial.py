# Generated by Django 4.2.2 on 2023-06-22 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SmartContract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('contract_address', models.CharField(max_length=42)),
                ('ipfs_url', models.URLField()),
            ],
        ),
    ]