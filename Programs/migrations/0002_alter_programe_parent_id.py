# Generated by Django 5.1.4 on 2024-12-12 12:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Programs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programe',
            name='parent_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child_prog', to='Programs.programe'),
        ),
    ]