# Generated by Django 4.1.4 on 2022-12-17 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0002_ordermodel_orderitemsmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='pay_type',
            field=models.CharField(max_length=50, null=True),
        ),
    ]