# Generated by Django 3.1.3 on 2021-02-06 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sdns', '0001_initial'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='cts',
            constraint=models.UniqueConstraint(fields=('registro', 'reg', 'content'), name='unique_Cts'),
        ),
    ]