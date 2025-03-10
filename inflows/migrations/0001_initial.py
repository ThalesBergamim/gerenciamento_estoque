# Generated by Django 5.1.6 on 2025-02-18 23:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        ('supplier', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inflows',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='inflows', to='product.product')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='inflows', to='supplier.supplier')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
