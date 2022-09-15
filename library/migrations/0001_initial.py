# Generated by Django 4.1 on 2022-09-15 02:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_name', models.CharField(max_length=200)),
                ('b_author', models.CharField(max_length=200)),
                ('b_isbn_no', models.IntegerField()),
                ('b_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.book_category')),
            ],
        ),
    ]
