# Generated by Django 5.0.6 on 2024-05-27 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lim', '0003_patient_email_patient_phone_sample'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='pathologist_present',
            new_name='referring_doctor',
        ),
        migrations.AddField(
            model_name='patient',
            name='collected_by',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='status',
            field=models.CharField(choices=[('enabled', 'Enabled'), ('processing', 'Processing'), ('complete', 'Complete')], max_length=3000, null=True),
        ),
    ]
