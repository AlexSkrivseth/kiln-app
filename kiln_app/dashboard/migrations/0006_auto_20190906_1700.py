# Generated by Django 2.1.5 on 2019-09-06 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_auto_20190906_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='load',
            name='job',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='load',
            name='loadnumber',
            field=models.PositiveSmallIntegerField(blank=True),
        ),
    ]
