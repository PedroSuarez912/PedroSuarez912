# Generated by Django 4.1 on 2022-08-21 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Familiar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
                ('edad', models.IntegerField()),
                ('altura', models.FloatField()),
                ('matrimonio', models.BooleanField()),
                ('nacimiento', models.DateField()),
            ],
        ),
    ]
