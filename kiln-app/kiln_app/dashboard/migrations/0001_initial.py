# Generated by Django 2.1.5 on 2019-09-06 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kiln',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(verbose_name=True)),
            ],
        ),
        migrations.CreateModel(
            name='Load',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fiber', models.FileField(null=True, upload_to='uploaded_files/')),
                ('job', models.CharField(max_length=30, null=True)),
                ('start', models.DateTimeField(auto_now_add=True)),
                ('end', models.DateTimeField(null=True)),
                ('loadnumber', models.PositiveSmallIntegerField(null=True)),
                ('kiln', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Kiln')),
            ],
        ),
        migrations.CreateModel(
            name='Reading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.DecimalField(decimal_places=2, max_digits=5)),
                ('humidity', models.DecimalField(decimal_places=2, max_digits=5)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('load', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Load')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('email', models.EmailField(blank=True, max_length=254)),
            ],
        ),
    ]