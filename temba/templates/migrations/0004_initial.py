# Generated by Django 2.1.8 on 2019-07-01 21:00

import uuid

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [("orgs", "0055_initial"), ("channels", "0120_channellog_msg")]

    operations = [
        migrations.CreateModel(
            name="Template",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("uuid", models.UUIDField(default=uuid.uuid4)),
                ("name", models.CharField(max_length=64)),
                ("modified_on", models.DateTimeField(default=django.utils.timezone.now)),
                ("created_on", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "org",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, related_name="templates", to="orgs.Org"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TemplateTranslation",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("content", models.CharField(max_length=1280)),
                ("variable_count", models.IntegerField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("A", "approved"),
                            ("P", "pending"),
                            ("R", "rejected"),
                            ("U", "unsupported_language"),
                        ],
                        default="P",
                        max_length=1,
                    ),
                ),
                ("language", models.CharField(max_length=6)),
                ("external_id", models.CharField(max_length=64, null=True)),
                ("is_active", models.BooleanField(default=True)),
                ("channel", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to="channels.Channel")),
                (
                    "template",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="translations",
                        to="templates.Template",
                    ),
                ),
            ],
        ),
        migrations.AlterUniqueTogether(name="template", unique_together={("org", "name")}),
    ]
