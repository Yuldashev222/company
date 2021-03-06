# Generated by Django 4.0.3 on 2022-03-11 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='Company_logo/')),
                ('company_name', models.CharField(max_length=200)),
                ('info', models.TextField(blank=True, null=True)),
                ('company_email', models.EmailField(blank=True, max_length=200, null=True)),
                ('telegram_link', models.URLField(blank=True, null=True)),
                ('instagram_link', models.URLField(blank=True, null=True)),
                ('facebook_link', models.URLField(blank=True, null=True)),
                ('street', models.CharField(blank=True, max_length=300, null=True)),
                ('city', models.CharField(max_length=300)),
                ('state', models.CharField(max_length=300)),
                ('url', models.SlugField(max_length=200, unique=True)),
                ('date_created', models.DateField(auto_now=True)),
                ('date_updated', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Companies',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='post_and_products_images/')),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
            },
        ),
    ]
