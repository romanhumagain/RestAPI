# Generated by Django 4.2.1 on 2024-02-10 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sports_type', models.CharField(max_length=100)),
                ('sports_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Persons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('phone_number', models.IntegerField()),
                ('sports', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sports', to='home.sports')),
            ],
        ),
    ]
