# Generated by Django 4.1.2 on 2024-01-07 22:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produk', '0004_rename_expoedisi_cart_expedisi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addressuserchartitem',
            name='userprofile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='produk.usercartitem'),
        ),
    ]