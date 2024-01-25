# Generated by Django 4.2.1 on 2024-01-25 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
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
        migrations.AddField(
            model_name='persons',
            name='sports',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sports', to='home.sports'),
        ),
    ]
