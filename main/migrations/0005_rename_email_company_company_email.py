# Generated by Django 4.0.3 on 2022-03-11 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rename_name_company_company_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='email',
            new_name='company_email',
        ),
    ]