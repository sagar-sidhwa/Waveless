# Generated by Django 3.0.1 on 2020-03-05 05:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('efarm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorydata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
                ('heading', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('img', models.ImageField(upload_to='')),
                ('e', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='efarm.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Productdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('price', models.FloatField(max_length=15)),
                ('img', models.ImageField(upload_to='')),
                ('c', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='efarm.Categorydata')),
            ],
        ),
    ]