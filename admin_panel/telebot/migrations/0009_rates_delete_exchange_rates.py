# Generated by Django 4.1.5 on 2023-01-21 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telebot', '0008_rename_curses_exchange_rates'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usd', models.IntegerField(help_text='usd', max_length=10, null=68.1, verbose_name='USD')),
                ('aed', models.FloatField(help_text='aed', max_length=10, null=18.1, verbose_name='USD')),
                ('eur', models.IntegerField(help_text='aed', max_length=10, null=74.1, verbose_name='USD')),
            ],
        ),
        migrations.DeleteModel(
            name='Exchange_rates',
        ),
    ]
