# Generated by Django 3.1.7 on 2021-04-08 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20210409_0016'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='editor',
            options={},
        ),
        migrations.AddField(
            model_name='editor',
            name='phone_number',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
