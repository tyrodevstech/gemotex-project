# Generated by Django 4.2.5 on 2023-10-09 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_main', '0015_alter_productsubcategorymodel_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='partnercompanymodel',
            options={'verbose_name': 'Buyers Company Logo', 'verbose_name_plural': 'Buyers Company Logos'},
        ),
        migrations.AlterField(
            model_name='aboutcardmodel',
            name='btn_link',
            field=models.URLField(null=True, verbose_name='button link'),
        ),
        migrations.AlterField(
            model_name='aboutcardmodel',
            name='btn_text',
            field=models.CharField(max_length=100, null=True, verbose_name='button text'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='tag',
            field=models.CharField(default='NEW', max_length=12, null=True),
        ),
    ]
