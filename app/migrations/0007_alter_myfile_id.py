# Generated by Django 4.1.5 on 2023-01-31 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_myfile_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myfile',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
