# Generated by Django 2.2.17 on 2020-12-26 08:44

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('resume_builder', '0007_auto_20201226_0839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='skills',
            field=jsonfield.fields.JSONField(null=True),
        ),
    ]
