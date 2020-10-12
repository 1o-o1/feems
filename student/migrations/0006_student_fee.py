# Generated by Django 3.1.2 on 2020-10-11 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_auto_20201011_1618'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_Fee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admission_fee', models.FloatField(null=True)),
                ('session_charge', models.FloatField(null=True)),
                ('exam_fee', models.FloatField(null=True)),
                ('hall_fee', models.FloatField(null=True)),
                ('library_fee', models.FloatField(null=True)),
                ('transport_fee', models.FloatField(null=True)),
                ('medical_fee', models.FloatField(null=True)),
                ('bank_sleep', models.BooleanField(default=True)),
                ('is_money_approved', models.BooleanField(default=False)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
        ),
    ]
