# Generated by Django 3.1.3 on 2020-12-05 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ech',
            options={'verbose_name_plural': 'ECH'},
        ),
        migrations.AlterModelOptions(
            name='ecl',
            options={'verbose_name_plural': 'ECL'},
        ),
        migrations.AddField(
            model_name='ech',
            name='HSNME',
            field=models.CharField(db_column='HSNME', default=' ', max_length=30, verbose_name='Shop Name'),
            preserve_default=False,
        ),
    ]
