# Generated by Django 5.1.6 on 2025-02-20 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
