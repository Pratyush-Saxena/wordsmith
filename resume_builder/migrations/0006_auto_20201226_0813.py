# Generated by Django 2.2.17 on 2020-12-26 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_builder', '0005_auto_20201202_1108'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='edu',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='data',
            name='exp',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='Image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
