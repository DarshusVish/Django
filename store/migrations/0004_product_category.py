# Generated by Django 3.2.8 on 2021-10-29 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.category'),
        ),
    ]