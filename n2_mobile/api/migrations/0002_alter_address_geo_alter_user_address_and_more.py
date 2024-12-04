# Generated by Django 5.1.3 on 2024-11-30 23:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='geo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.geo'),
        ),
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.address'),
        ),
        migrations.AlterField(
            model_name='user',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.company'),
        ),
    ]
