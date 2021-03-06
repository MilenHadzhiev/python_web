# Generated by Django 3.1.2 on 2020-10-30 15:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pages',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1, message='Your book must have at least one page.')]),
        ),
    ]
