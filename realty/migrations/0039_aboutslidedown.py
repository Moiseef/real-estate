# Generated by Django 4.1.7 on 2023-04-13 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realty', '0038_subscrib'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutSlideDown',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Image')),
            ],
        ),
    ]