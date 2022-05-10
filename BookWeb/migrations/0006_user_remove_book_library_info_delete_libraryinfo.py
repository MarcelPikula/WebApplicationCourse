# Generated by Django 4.0.4 on 2022-05-10 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BookWeb', '0005_alter_libraryinfo_bookstand_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=16, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BookWeb.review')),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='library_info',
        ),
        migrations.DeleteModel(
            name='LibraryInfo',
        ),
    ]