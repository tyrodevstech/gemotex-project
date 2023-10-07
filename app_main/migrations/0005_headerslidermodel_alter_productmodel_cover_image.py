# Generated by Django 4.2.5 on 2023-10-06 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_main', '0004_productcategorymodel_productsubcategorymodel_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeaderSliderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=125, null=True)),
                ('promo', models.TextField(max_length=225, null=True)),
                ('cta_text', models.CharField(blank=True, max_length=20, null=True, verbose_name='button text')),
                ('cta_link', models.URLField(blank=True, null=True, verbose_name='button link')),
                ('bg_img', models.ImageField(null=True, upload_to='Headersliderbg', verbose_name='background image')),
                ('active', models.BooleanField(default=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Header Slider',
                'verbose_name_plural': 'Header Sliders',
            },
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='cover_image',
            field=models.ImageField(help_text='Size Direction: W:800PX & H:975PX', null=True, upload_to='product-cover-image/%Y/%d/%b'),
        ),
    ]