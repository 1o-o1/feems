# Generated by Django 3.1.2 on 2020-10-18 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('final', '0002_auto_20201018_0648'),
    ]

    operations = [
        migrations.CreateModel(
            name='Semister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semister', models.CharField(max_length=10)),
                ('hall', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='final.student')),
            ],
        ),
    ]
