# Generated by Django 4.2.8 on 2024-08-14 17:57

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("core", "0007_delete_haribhakt"),
        ("mandal", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Haribhakt",
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
                    "created",
                    django_extensions.db.fields.CreationDateTimeField(
                        auto_now_add=True, verbose_name="created"
                    ),
                ),
                (
                    "modified",
                    django_extensions.db.fields.ModificationDateTimeField(
                        auto_now=True, verbose_name="modified"
                    ),
                ),
                (
                    "status",
                    models.IntegerField(
                        blank=True,
                        choices=[(0, "Active"), (1, "Deleted")],
                        default=0,
                        null=True,
                        verbose_name="The life cycle status of this object",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True,
                        max_length=1024,
                        null=True,
                        verbose_name="Name of Haribhakt",
                    ),
                ),
                (
                    "is_gunbhavi",
                    models.BooleanField(
                        default=False, verbose_name="Is Haribakt gunbhavi or not ?"
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        choices=[
                            ("Male", "Male"),
                            ("Female", "Female"),
                            ("Transgender", "Transgender"),
                            ("Other", "Other"),
                        ],
                        max_length=16,
                        verbose_name="Gender",
                    ),
                ),
                (
                    "is_head_of_family",
                    models.BooleanField(
                        default=False, verbose_name="Is Haribakt Head of Family ?"
                    ),
                ),
                (
                    "relation_with_hof",
                    models.CharField(
                        blank=True,
                        max_length=1024,
                        null=True,
                        verbose_name="Relation with Head of Family",
                    ),
                ),
                (
                    "contact_number_1",
                    models.CharField(
                        blank=True,
                        max_length=10,
                        null=True,
                        verbose_name="Contact number 1",
                    ),
                ),
                (
                    "contact_number_2",
                    models.CharField(
                        blank=True,
                        max_length=10,
                        null=True,
                        verbose_name="Contact number 2",
                    ),
                ),
                (
                    "contact_number_3",
                    models.CharField(
                        blank=True,
                        max_length=10,
                        null=True,
                        verbose_name="Contact number 3",
                    ),
                ),
                (
                    "birth_date",
                    models.DateField(
                        blank=True, null=True, verbose_name="Date of Birth"
                    ),
                ),
                (
                    "number_of_years_of_satsang",
                    models.SmallIntegerField(
                        blank=True, null=True, verbose_name="Number of years of satsang"
                    ),
                ),
                (
                    "nitya_pooja",
                    models.BooleanField(default=True, verbose_name="Nitya Pooja ?"),
                ),
                (
                    "tilak_chaandlo",
                    models.BooleanField(default=True, verbose_name="Tilak Chaandlo ?"),
                ),
                ("vyasan", models.BooleanField(default=False, verbose_name="Vyasan ?")),
                (
                    "vyasan_type",
                    models.CharField(
                        blank=True,
                        max_length=1024,
                        null=True,
                        verbose_name="Type of vyasan",
                    ),
                ),
                (
                    "onion_garlic",
                    models.BooleanField(
                        default=False, verbose_name="Onion and Garlic ?"
                    ),
                ),
                (
                    "weekly_sabha",
                    models.BooleanField(default=True, verbose_name="Weekly Sabha ?"),
                ),
                (
                    "poonam_sabha",
                    models.BooleanField(default=False, verbose_name="Poonam Pooja ?"),
                ),
                (
                    "ghar_sabha",
                    models.BooleanField(default=True, verbose_name="Ghar Sabha ?"),
                ),
                (
                    "vachnamrut_swami_ni_vaato_vanchan",
                    models.BooleanField(
                        default=True,
                        verbose_name="Vachnamrut Swami ni vaato nu Vaanchan ?",
                    ),
                ),
                (
                    "satsang_sikshan_pariksha",
                    models.BooleanField(
                        default=True, verbose_name="Satsang Sikshan Pariksha ?"
                    ),
                ),
                (
                    "monthtly_donation",
                    models.IntegerField(
                        blank=True, null=True, verbose_name="Monthly Donation ?"
                    ),
                ),
                (
                    "file",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.file",
                    ),
                ),
                (
                    "head_of_family",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="haribhakt.haribhakt",
                    ),
                ),
                (
                    "mandal",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mandal.mandal",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
