# Generated by Django 5.0.6 on 2024-07-08 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='nome')),
                ('senha', models.CharField(max_length=500, verbose_name='senha')),
                ('criado', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]