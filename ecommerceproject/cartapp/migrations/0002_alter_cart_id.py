# Generated by Django 4.1.5 on 2023-02-10 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='id',
            field=models.BigAutoField(auto_created=True, default=498.0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
