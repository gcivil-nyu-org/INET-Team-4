# Generated by Django 3.2.16 on 2022-11-03 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0009_auto_20221031_2018"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
