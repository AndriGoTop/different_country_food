# Generated by Django 4.2.3 on 2023-07-31 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pictures',
            field=models.ManyToManyField(blank=True, to='articles.pictures', verbose_name='Изображения'),
        ),
    ]
