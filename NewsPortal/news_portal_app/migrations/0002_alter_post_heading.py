# Generated by Django 4.0.6 on 2022-08-16 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_portal_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='heading',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]