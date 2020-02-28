# Generated by Django 2.1.15 on 2020-02-26 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ingredients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('company', models.CharField(max_length=200)),
                ('quantity_per_unit', models.IntegerField()),
                ('date_bought', models.DateTimeField(verbose_name='date bought')),
            ],
        ),
    ]
