# Generated by Django 4.2.2 on 2023-06-12 19:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='brand',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='model',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='type',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.CreateModel(
            name='VehicleImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(blank=True, max_length=300, null=True)),
                ('title', models.CharField(blank=True, max_length=300, null=True)),
                ('detail', models.CharField(blank=True, max_length=2000, null=True)),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.vehicle')),
            ],
        ),
    ]
