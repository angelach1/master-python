# Generated by Django 4.1.2 on 2023-02-22 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0002_article_image_alter_article_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(default='null', upload_to=''),
        ),
    ]