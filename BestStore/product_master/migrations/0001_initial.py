# Generated by Django 2.2.1 on 2019-05-22 07:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Electronic', 'Electronic'), ('Cloth', 'Cloth'), ('Kid', 'Kid')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('added_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('merchant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('Mobile', 'Mobile'), ('TV', 'TV'), ('Shirt', 'Shirt'), ('Pant', 'Pant'), ('Toy', 'Toy'), ('Book', 'Book')], max_length=20)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_master.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=20)),
                ('color', models.CharField(choices=[('Black', 'Black'), ('Blue', 'Blue'), ('Red', 'Red'), ('Green', 'Green'), ('White', 'White'), ('Rose Gold', 'Rose Gold'), ('Grey', 'Grey')], max_length=20)),
                ('weight', models.CharField(max_length=20)),
                ('product', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='product_master.Product')),
                ('sub_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_master.SubCategory')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_master.Product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=models.ForeignKey(default='Mobile', on_delete=django.db.models.deletion.CASCADE, to='product_master.SubCategory'),
        ),
    ]
