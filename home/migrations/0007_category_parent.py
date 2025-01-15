# Generated by Django 5.1.4 on 2025-01-06 14:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_article_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='Parent',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='childeren', to='home.category', verbose_name='زیر دسته '),
        ),
    ]
