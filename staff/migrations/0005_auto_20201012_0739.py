# Generated by Django 3.1.2 on 2020-10-12 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0004_auto_20201011_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='Role',
            field=models.CharField(blank=True, choices=[('Teacher', 'Teacher'), ('Hall Staff', 'Hall Staff'), ('Register', 'Register')], max_length=100, null=True),
        ),
    ]
