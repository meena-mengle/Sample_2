# Generated by Django 3.2.25 on 2024-05-26 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='rating',
            field=models.IntegerField(default=5, null=True),
        ),
    ]