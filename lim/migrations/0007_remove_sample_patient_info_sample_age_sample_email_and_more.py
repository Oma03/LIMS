# Generated by Django 5.0.6 on 2024-07-01 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lim', '0006_rename_specimen_id_sample_sample_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sample',
            name='patient_info',
        ),
        migrations.AddField(
            model_name='sample',
            name='age',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='sample',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='sample',
            name='patient_fname',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='sample',
            name='patient_lname',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='sample',
            name='phone',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='sample',
            name='sample_choice',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='sample',
            name='test_type',
            field=models.CharField(blank=True, max_length=4000, null=True),
        ),
    ]