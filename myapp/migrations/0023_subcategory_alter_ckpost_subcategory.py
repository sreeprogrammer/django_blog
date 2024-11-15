# Generated by Django 4.1.8 on 2024-11-12 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0022_alter_ckpost_subcategory_delete_subcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=600)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='myapp.category')),
            ],
        ),
        migrations.AlterField(
            model_name='ckpost',
            name='subCategory',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='myapp.subcategory'),
            preserve_default=False,
        ),
    ]