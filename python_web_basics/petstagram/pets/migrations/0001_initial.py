# Generated by Django 3.1.2 on 2020-10-26 22:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('CAT', 'cat'), ('DOG', 'dog'), ('PARROT', 'parrot')], max_length=6)),
                ('name', models.CharField(max_length=6)),
                ('age', models.IntegerField(verbose_name=django.core.validators.MinValueValidator(0))),
            ],
        ),
    ]
