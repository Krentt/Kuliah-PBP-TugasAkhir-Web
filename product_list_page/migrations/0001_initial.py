# Generated by Django 3.2.7 on 2021-10-28 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProdukMasker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
                ('rating', models.BigIntegerField()),
                ('deskripsi', models.CharField(max_length=255)),
                ('harga', models.BigIntegerField()),
                ('stok', models.BigIntegerField()),
            ],
        ),
    ]
