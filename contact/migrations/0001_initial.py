# Generated by Django 3.2 on 2023-04-15 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('', 'Select Type *'), ('OR', 'Order Status'), ('PR', 'Product Enquiry'), ('CU', 'Custom Application Enquiry')], max_length=2)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('enquiry', models.TextField(max_length=1000)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Contact Us',
                'ordering': ['-date_created'],
            },
        ),
    ]
