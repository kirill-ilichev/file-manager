# Generated by Django 2.2.3 on 2019-07-11 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folder',
            name='parentID',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
