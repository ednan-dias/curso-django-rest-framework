# Generated by Django 3.2.3 on 2021-05-20 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atracoes', '0001_initial'),
        ('core', '0002_alter_pontoturistico_aprovado'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='atrcoes',
            field=models.ManyToManyField(to='atracoes.Atracao'),
        ),
    ]
