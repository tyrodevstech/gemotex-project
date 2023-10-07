# Generated by Django 4.2.5 on 2023-10-04 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_main', '0003_footerinformationmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(blank=True, max_length=225, null=True)),
            ],
            options={
                'verbose_name': 'Product Category',
                'verbose_name_plural': 'Product Categories',
            },
        ),
        migrations.CreateModel(
            name='ProductSubcategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_category_name', models.CharField(blank=True, max_length=225, null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_main.productcategorymodel')),
            ],
            options={
                'verbose_name': 'Product Subcategory',
                'verbose_name_plural': 'Product Subcategories',
            },
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=122, null=True, verbose_name='product title')),
                ('details', models.TextField(blank=True, max_length=325, null=True, verbose_name='product details')),
                ('info', models.TextField(blank=True, max_length=325, null=True, verbose_name='additional information')),
                ('tag', models.CharField(default='NEW', max_length=6, null=True)),
                ('cover_image', models.ImageField(null=True, upload_to='product-cover-image/%Y/%d/%b')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p_category', to='app_main.productcategorymodel')),
                ('subcategory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p_subcategory', to='app_main.productsubcategorymodel')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='ProductImagesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_title', models.CharField(max_length=122, null=True, verbose_name='image title')),
                ('image', models.ImageField(null=True, upload_to='products-images/%Y/%d/%b')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_main.productmodel')),
            ],
            options={
                'verbose_name': 'Product image',
                'verbose_name_plural': 'Product images',
            },
        ),
    ]