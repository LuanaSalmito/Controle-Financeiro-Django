# Generated by Django 3.2.12 on 2023-11-28 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='sobrenome',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
