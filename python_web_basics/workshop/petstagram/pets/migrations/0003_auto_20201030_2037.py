# Generated by Django 3.1.2 on 2020-10-30 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0002_auto_20201030_1851'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='test',
            field=models.CharField(default=0, max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pet',
            name='type',
            field=models.CharField(choices=[('Cat', 'Cat'), ('Dog', 'Dog'), ('Parrot', 'Parrot'), ('Unknown', 'Unknown')], default='Unknown', max_length=7),
        ),
    ]
