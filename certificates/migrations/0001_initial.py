# Generated by Django 5.1.4 on 2024-12-16 13:28

import django.db.models.deletion
import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CertificateType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('desc', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CertificateSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('has_image', models.BooleanField()),
                ('image_location', models.CharField(choices=[(1, 'اعلي اليمين'), (2, 'اعلي اليسار')], default=1, max_length=25)),
                ('certificate_content', tinymce.models.HTMLField()),
                ('CertificateType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CertificateType', to='certificates.certificatetype')),
            ],
        ),
    ]
