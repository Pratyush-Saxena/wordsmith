# Generated by Django 3.0 on 2021-04-19 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_builder', '0010_userdata_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='payment_status',
            field=models.BooleanField(default=False),
        ),
    ]
