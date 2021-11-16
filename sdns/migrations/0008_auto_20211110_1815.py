# Generated by Django 3.2.9 on 2021-11-10 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sdns', '0007_alter_domain_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cts',
            options={'verbose_name_plural': 'Registros CNAME, TXT, SPF'},
        ),
        migrations.AlterModelOptions(
            name='mx',
            options={'verbose_name_plural': 'Registros de servidores de email'},
        ),
        migrations.AlterModelOptions(
            name='ns',
            options={'verbose_name_plural': 'Registros de NameServers'},
        ),
        migrations.RemoveConstraint(
            model_name='cts',
            name='unique_Cts',
        ),
    ]