# Generated by Django 3.1.5 on 2021-01-10 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pictures', '0003_auto_20210110_1100'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='image',
            field=models.ImageField(null=True, upload_to='pictures/'),
        ),
        migrations.AlterField(
            model_name='image',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pictures.category'),
        ),
        migrations.AlterField(
            model_name='image',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pictures.location'),
        ),
    ]
