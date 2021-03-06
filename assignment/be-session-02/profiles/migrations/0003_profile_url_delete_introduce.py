# Generated by Django 4.0.6 on 2022-07-19 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_introduce_major'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='이름', max_length=20, null=True)),
                ('age', models.IntegerField(blank=True, default=0, null=True)),
                ('phone', models.CharField(blank=True, default='010-0000-0000', max_length=20, null=True)),
                ('pup_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=20, null=True)),
                ('link', models.URLField(blank=True, max_length=500, null=True)),
                ('is_completed', models.BooleanField(blank=True, default=False, null=True)),
                ('pup_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.profile')),
            ],
        ),
        migrations.DeleteModel(
            name='introduce',
        ),
    ]
