# Generated by Django 3.1.2 on 2020-10-06 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django102', '0005_player'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='players',
            field=models.ManyToManyField(to='django102.Player'),
        ),
    ]
