# Generated by Django 4.0.6 on 2022-08-05 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_fish_breedingseason_fish_diet_fish_family_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fish',
            name='breedingSeason',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='fish',
            name='habitat',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
