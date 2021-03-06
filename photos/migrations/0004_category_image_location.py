# Generated by Django 3.0.6 on 2020-05-25 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('photos', '0003_auto_20200525_1515'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'ordering': ['category'],
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'ordering': ['location'],
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image_file', models.ImageField(default='', upload_to='images/')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photos.Category')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photos.Location')),
            ],
            options={
                'ordering': ['image_name'],
            },
        ),
    ]
