# Generated by Django 2.2.13 on 2020-09-09 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0007_auto_20200909_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='picture',
            field=models.ImageField(upload_to='upload/books/%Y/%m/%d'),
        ),
    ]
