# Generated by Django 4.2.5 on 2023-10-04 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_main', '0002_rename_contactinformation_contactinformationmodel_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterInformationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.TextField(max_length=325, null=True, verbose_name='short summary')),
                ('facebook_link', models.URLField(blank=True, null=True, verbose_name='Facebook Link')),
                ('twitter_link', models.URLField(blank=True, null=True, verbose_name='Twitter Link')),
                ('instagram_link', models.URLField(blank=True, null=True, verbose_name='Instagram Link')),
                ('youtube_link', models.URLField(blank=True, null=True, verbose_name='YouTube Link')),
            ],
            options={
                'verbose_name': 'Footer Information',
                'verbose_name_plural': 'Footer Informations',
                'ordering': ['-id'],
            },
        ),
    ]