# Generated by Django 5.0.6 on 2024-06-10 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='furniture',
            name='imagen',
            field=models.ImageField(default='assets/Logo.png', upload_to='media/'),
        ),
    ]