# Generated by Django 2.1 on 2018-12-12 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monoku', '0004_usuarios'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='username',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
