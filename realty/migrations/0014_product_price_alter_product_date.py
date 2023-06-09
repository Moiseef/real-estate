# Generated by Django 4.0.3 on 2023-03-22 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realty', '0013_remove_product_short_description_product_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default='1', max_digits=10, verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Publication date'),
        ),
    ]
