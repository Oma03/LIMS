# Generated by Django 5.0.6 on 2024-07-04 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lim', '0007_remove_sample_patient_info_sample_age_sample_email_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='date_e',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='time_e',
            new_name='time',
        ),
        migrations.AlterField(
            model_name='patient',
            name='date_created',
            field=models.DateTimeField(auto_created=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='date_released',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='collection_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='sample_choice',
            field=models.CharField(choices=[('type1', 'Blood'), ('type2', 'Stool'), ('type3', 'Urine'), ('type4', 'Saliva')], max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='test_type',
            field=models.CharField(blank=True, choices=[('test1', 'CBC'), ('test2', 'BMP'), ('test3', 'BSL'), ('test4', 'Leukocytes'), ('test5', 'Occult blood'), ('test6', 'fat'), ('test7', 'RBC urine'), ('test8', 'Glucose urine'), ('test9', 'Protein urine'), ('test10', 'HIV'), ('test11', 'Hypogonadism'), ('test12', 'Cushing')], max_length=4000, null=True),
        ),
    ]
