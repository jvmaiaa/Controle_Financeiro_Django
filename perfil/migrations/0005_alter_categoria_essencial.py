# Generated by Django 4.2.3 on 2023-07-07 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0004_alter_categoria_essencial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='essencial',
            field=models.BooleanField(default=False),
        ),
    ]