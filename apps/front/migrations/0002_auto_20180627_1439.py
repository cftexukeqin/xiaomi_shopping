# Generated by Django 2.0.5 on 2018-06-27 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='telephone',
            field=models.CharField(max_length=11),
        ),
    ]
