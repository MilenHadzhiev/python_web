# Generated by Django 3.1.2 on 2020-10-27 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0002_auto_20201027_0014'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='pet',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='pets.pet'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
