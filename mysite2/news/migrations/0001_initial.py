# Generated by Django 4.2.7 on 2023-11-15 04:24

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='kategori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namakategori', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='berita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=255)),
                ('deskripsi', models.CharField(max_length=255, null=True)),
                ('isi', models.CharField(max_length=9999)),
                ('kategoriID', models.IntegerField(max_length=255)),
                ('gambar', models.ImageField(upload_to='media')),
                ('penulis', models.CharField(max_length=255)),
                ('fotopenulis', models.ImageField(upload_to='media')),
                ('publikasi', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('publish', 'publish'), ('draft', 'draft')], max_length=200)),
                ('kategori', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.kategori')),
            ],
        ),
        migrations.CreateModel(
            name='customuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('is_admin', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('password', models.CharField(max_length=255)),
                ('status', models.CharField(blank=True, choices=[('viewers', 'viewers'), ('admin', 'admin')], default='admin', max_length=255, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
