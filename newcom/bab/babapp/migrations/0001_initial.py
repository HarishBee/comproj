# Generated by Django 5.0.4 on 2024-04-30 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Mobile', models.CharField(blank=True, max_length=10)),
                ('Email', models.EmailField(max_length=254, unique=True)),
                ('Date_of_birth', models.DateField()),
                ('Gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('password', models.CharField(max_length=25)),
            ],
        ),
    ]
