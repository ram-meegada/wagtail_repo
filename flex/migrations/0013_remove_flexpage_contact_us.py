# Generated by Django 4.2.3 on 2023-07-26 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0012_alter_flexpage_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flexpage',
            name='contact_us',
        ),
    ]