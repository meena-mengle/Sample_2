# Generated by Django 3.2.25 on 2024-05-26 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_alter_contact_enquiry_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='enquiry_type',
            field=models.CharField(choices=[('DESIGN_CONSULTATION', 'Rug Design Consultation'), ('PRODUCT_QUERY', 'Product Query'), ('ORDER_QUERY', 'Order Query'), ('DELIVERY_QUERY', 'Delivery Query'), ('OTHER', 'Other')], default='DS', max_length=254),
        ),
    ]
