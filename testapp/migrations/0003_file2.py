# Generated by Django 4.1.5 on 2023-01-02 11:08

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("testapp", "0002_imagefield"),
    ]

    operations = [
        migrations.CreateModel(
            name="File2",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("testapp.file",),
        ),
    ]
