# Generated by Django 3.2.7 on 2021-11-04 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout_page', '0004_alter_checkout_telp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pengiriman',
            name='durasi',
            field=models.CharField(choices=[('Next Day (1 hari)', 'Next Day (1 hari) *Rp 10.000'), ('Reguler (2-4 hari)', 'Reguler (2-4 hari) *Rp 15.000')], max_length=100),
        ),
    ]
