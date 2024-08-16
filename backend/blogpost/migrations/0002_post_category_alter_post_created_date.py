# Generated by Django 5.0.7 on 2024-07-21 07:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blogpost", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="category",
            field=models.CharField(
                choices=[("blog", "Blog Post"), ("review", "Review Post")],
                default="blog",
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="created_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
