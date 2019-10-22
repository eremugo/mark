# Generated by Django 2.1.1 on 2019-01-08 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('author', models.CharField(max_length=255)),
                ('pdf', models.FileField(upload_to='books/pdfs')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_title', models.CharField(blank=True, max_length=225)),
                ('news_body', models.TextField(blank=True)),
                ('news_subtitle', models.CharField(blank=True, max_length=255)),
                ('news_image', models.ImageField(blank=True, upload_to='news_image')),
                ('clip', models.FileField(null=True, upload_to='videos')),
                ('author', models.CharField(blank=True, max_length=255)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_title', models.CharField(blank=True, default='', max_length=100)),
                ('project_detail', models.TextField(blank=True)),
                ('project_summary', models.TextField(blank=True)),
                ('project_results', models.TextField(blank=True)),
                ('client', models.CharField(blank=True, default='', max_length=100)),
                ('Surface_area', models.CharField(blank=True, default='', max_length=100)),
                ('date_of_finish', models.DateField(blank=True, null=True)),
                ('project_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('service_surface', models.CharField(blank=True, default='', max_length=100)),
                ('location', models.CharField(blank=True, default='', max_length=100)),
                ('p_image', models.ImageField(blank=True, upload_to='p_image')),
            ],
        ),
        migrations.CreateModel(
            name='project_images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(blank=True, max_length=150)),
                ('project_image', models.ImageField(blank=True, upload_to='project_image')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_image', models.ImageField(blank=True, upload_to='staff_image')),
                ('staff_name', models.CharField(blank=True, default='', max_length=100)),
                ('staff_detail', models.TextField(blank=True)),
                ('staff_title', models.CharField(blank=True, default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='About',
            fields=[
                ('about_title', models.CharField(blank=True, default='', max_length=100)),
                ('about_body', models.TextField(blank=True)),
                ('mission_title', models.CharField(blank=True, default='', max_length=100)),
                ('mission_body', models.TextField(blank=True)),
                ('vision_title', models.CharField(blank=True, default='', max_length=100)),
                ('vision_body', models.TextField(blank=True)),
                ('stratergy_title', models.CharField(blank=True, default='', max_length=100)),
                ('stratergy_body', models.TextField(blank=True)),
                ('staff', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='cepat.Staff')),
            ],
        ),
    ]