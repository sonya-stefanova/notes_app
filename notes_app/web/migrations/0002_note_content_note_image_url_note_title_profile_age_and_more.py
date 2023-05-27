# Generated by Django 4.2.1 on 2023-05-26 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='content',
            field=models.TextField(default='content'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='note',
            name='image_url',
            field=models.URLField(default='https://', verbose_name='Image URL'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='note',
            name='title',
            field=models.CharField(default='title', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='age',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(default='first_name', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='image_url',
            field=models.URLField(default='https://', verbose_name='Image URL'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(default='last_name', max_length=20),
            preserve_default=False,
        ),
    ]
