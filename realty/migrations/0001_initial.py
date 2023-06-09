# Generated by Django 4.0.3 on 2023-03-12 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home_articl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('mutetext', models.CharField(max_length=50, verbose_name='Mute')),
                ('full_text', models.TextField(verbose_name='Articl')),
                ('venue_image', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Image')),
            ],
        ),
    ]
