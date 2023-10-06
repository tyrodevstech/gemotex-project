# Generated by Django 4.2.5 on 2023-10-06 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_main', '0005_headerslidermodel_alter_productmodel_cover_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.TextField(max_length=525, null=True, verbose_name='client comment')),
                ('profile', models.ImageField(blank=True, null=True, upload_to='client-review-profiles', verbose_name='person image')),
                ('name', models.CharField(max_length=225, null=True, verbose_name='client name')),
                ('position', models.CharField(max_length=225, null=True, verbose_name='job description')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Client Review',
                'verbose_name_plural': 'Client Reviews',
                'ordering': ['-id'],
            },
        ),
        migrations.AlterField(
            model_name='headerslidermodel',
            name='bg_img',
            field=models.ImageField(help_text='image size: w-1920px x h-1100', null=True, upload_to='Headersliderbg', verbose_name='background image'),
        ),
        migrations.AlterField(
            model_name='headerslidermodel',
            name='promo',
            field=models.TextField(blank=True, max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='headerslidermodel',
            name='title',
            field=models.CharField(blank=True, max_length=125, null=True),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='cover_image',
            field=models.ImageField(help_text='image size: w-800px x h-975px', null=True, upload_to='product-cover-image/%Y/%d/%b'),
        ),
    ]
