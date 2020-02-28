# Generated by Django 2.1.15 on 2020-02-28 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ingredients',
            options={'verbose_name': 'Ingredient', 'verbose_name_plural': 'Ingredients'},
        ),
        migrations.RenameField(
            model_name='ingredients',
            old_name='company',
            new_name='company_name',
        ),
        migrations.RemoveField(
            model_name='ingredients',
            name='date_bought',
        ),
        migrations.RemoveField(
            model_name='ingredients',
            name='name',
        ),
        migrations.AddField(
            model_name='ingredients',
            name='description',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ingredients',
            name='product_name',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ingredients',
            name='quantity',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
