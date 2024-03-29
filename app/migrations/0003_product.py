# Generated by Django 5.0.1 on 2024-02-05 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_register_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('product_image', models.FileField(null=True, upload_to='')),
            ],
        ),
    ]
