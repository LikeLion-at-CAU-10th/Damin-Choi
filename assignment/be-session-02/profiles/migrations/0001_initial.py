from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='introduce',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='최다민', max_length=50, null=True)),
                ('major', models.CharField(blank=True, default='경영', max_length=50, null=True)),
                ('age', models.CharField(blank=True, default='23', max_length=20, null=True)),
                ('club', models.CharField(blank=True, default='멋사', max_length=20, null=True)),
            ],
        ),
    ]