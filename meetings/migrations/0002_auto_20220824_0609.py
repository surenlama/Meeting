# Generated by Django 3.1.4 on 2022-08-24 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetings',
            name='url',
            field=models.CharField(default='bhjkbjk', max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='meetings',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
