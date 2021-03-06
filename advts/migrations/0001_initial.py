# Generated by Django 3.2.9 on 2021-12-03 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Заголовок объявления')),
                ('description', models.TextField(verbose_name='Текст объявления')),
                ('price', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Цена')),
                ('address', models.CharField(max_length=128, verbose_name='Адрес')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата и вермя создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата и время последнего обновления')),
            ],
        ),
        migrations.CreateModel(
            name='AdvertImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='adverts/')),
                ('advert', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='images', to='advts.advert', verbose_name='Объявление')),
            ],
        ),
    ]
