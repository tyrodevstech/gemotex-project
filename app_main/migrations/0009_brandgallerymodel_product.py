# Generated by Django 4.2.5 on 2023-10-07 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_main', '0008_brandgallerymodel_alter_headerslidermodel_bg_img_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='brandgallerymodel',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_main.productmodel'),
        ),
    ]
