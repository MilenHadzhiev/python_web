# Generated by Django 3.1.2 on 2020-12-02 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0005_auto_20201030_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='image_url',
            field=models.ImageField(upload_to='images'),
        ),
    ]