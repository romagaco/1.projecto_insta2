# Generated by Django 5.2.4 on 2025-07-17 04:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Follow",
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
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Desde cuando lo sigue"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserProfile",
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
                (
                    "profile_picture",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="profile_pictures/",
                        verbose_name="Imagen de perfil",
                    ),
                ),
                (
                    "bio",
                    models.TextField(
                        blank=True, max_length=500, verbose_name="Biografia"
                    ),
                ),
                (
                    "birth_date",
                    models.DateField(
                        blank=True, null=True, verbose_name="fecha de nacimiento"
                    ),
                ),
                (
                    "followers",
                    models.ManyToManyField(
                        related_name="following",
                        through="profiles.Follow",
                        to="profiles.userprofile",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="profile",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "perfil",
                "verbose_name_plural": "perfiles",
            },
        ),
        migrations.AddField(
            model_name="follow",
            name="follower",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="follower_set",
                to="profiles.userprofile",
                verbose_name="¿Quien esta siguiendo?",
            ),
        ),
        migrations.AddField(
            model_name="follow",
            name="following",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="following_set",
                to="profiles.userprofile",
                verbose_name="¿A quien sigue?",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="follow",
            unique_together={("follower", "following")},
        ),
    ]
