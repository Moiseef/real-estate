# Generated by Django 4.1.7 on 2023-04-11 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realty', '0036_alter_contact_email_alter_contact_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='instagram',
            field=models.URLField(blank=True, default='https://www.instagram.com/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='skype',
            field=models.URLField(blank=True, default='https://www.skype.com/en/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='whatsapp',
            field=models.URLField(blank=True, default='https://www.whatsapp.com/?lang=es'),
        ),
    ]
