# Generated by Django 3.2.7 on 2021-10-30 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_list_page', '0003_produkmasker_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produkmasker',
            name='image',
        ),
    ]
