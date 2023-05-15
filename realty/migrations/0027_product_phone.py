# Generated by Django 4.1.7 on 2023-04-09 10:57

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('realty', '0026_product_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='phone',
            field=phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31),
        ),
    ]