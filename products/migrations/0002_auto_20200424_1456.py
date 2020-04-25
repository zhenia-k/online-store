# Generated by Django 3.0.5 on 2020-04-24 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productimage',
            old_name='image',
            new_name='path',
        ),
        migrations.RemoveField(
            model_name='product',
            name='images',
        ),
        migrations.AddField(
            model_name='productimage',
            name='images',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Product', verbose_name='фото товара'),
        ),
        migrations.AlterField(
            model_name='product',
            name='translator',
            field=models.ManyToManyField(blank=True, to='products.Translator', verbose_name='переводчик'),
        ),
    ]