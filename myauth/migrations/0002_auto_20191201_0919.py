# Generated by Django 2.1.5 on 2019-12-01 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myauth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to='', verbose_name='サムネイル'),
        ),
    ]
