# Generated by Django 4.2.7 on 2023-12-24 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default=' '),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='ProductVersion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_color', to='products.color')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='version', to='products.product')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_size', to='products.color')),
            ],
        ),
    ]
