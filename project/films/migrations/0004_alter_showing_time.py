# Generated by Django 4.0.2 on 2022-04-02 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0003_guesstransaction_rename_transaction_logintransaction_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='showing',
            name='time',
            field=models.CharField(max_length=50),
        ),
    ]