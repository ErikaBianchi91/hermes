# Generated by Django 4.1.7 on 2023-03-12 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Dish",
            fields=[
                ("name", models.CharField(max_length=50)),
                ("price", models.FloatField()),
                ("type", models.CharField(max_length=50)),
                ("gluten", models.BooleanField()),
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("lactose", models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name="Table",
            fields=[
                ("number", models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("request_time", models.TimeField()),
                (
                    "kitchen_start_time",
                    models.TimeField(blank=True, default=None, null=True),
                ),
                (
                    "kitchen_end_time",
                    models.TimeField(blank=True, default=None, null=True),
                ),
                (
                    "delivery_time",
                    models.TimeField(blank=True, default=None, null=True),
                ),
                (
                    "dish_name",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.dish",
                    ),
                ),
                (
                    "table",
                    models.ForeignKey(
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.table",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Meal",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("start", models.TimeField()),
                ("end", models.TimeField(blank=True, default=None, null=True)),
                (
                    "table",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.table"
                    ),
                ),
            ],
        ),
    ]