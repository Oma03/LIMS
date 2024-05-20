from django.db import models
from django.core.exceptions import ValidationError
import uuid

# Create your models here.


class Patient(models.Model):
    patient_lname = models.CharField(max_length=500)
    patient_fname = models.CharField(max_length=500)
    age = models.CharField(max_length=3)
    date_e = models.DateField(null=True)
    time_e = models.TimeField(null=True)
    TYPE_OF_SPECIMEN = [
        ('type1', 'Blood'),
        ('type2', 'Stool'),
        ('type3', 'Urine'),
        ('type4', 'Saliva'),
    ]
    TESTS = [
        ('test1', 'CBC'),
        ('test2', 'BMP'),
        ('test3', 'BSL'),
        ('test4', 'Leukocytes'),
        ('test5', 'Occult blood'),
        ('test6', 'fat'),
        ('test7', 'RBC urine'),
        ('test8', 'Glucose urine'),
        ('test9', 'Protein urine'),
        ('test10', 'HIV'),
        ('test11', 'Hypogonadism'),
        ('test12', 'Cushing'),
    ]
    BLOOD_TEST = [
        ('test1', 'CBC'),
        ('test2', 'BMP'),
        ('test3', 'BSL'),
    ]
    STOOL_TEST = [
        ('test4', 'Leukocytes'),
        ('test5', 'Occult blood'),
        ('test6', 'fat'),
    ]
    URINE_TEST = [
        ('test7', 'RBC urine'),
        ('test8', 'Glucose urine'),
        ('test9', 'Protein urine'),
    ]
    SALIVA_TEST = [
        ('test10', 'HIV'),
        ('test11', 'Hypogonadism'),
        ('test12', 'Cushing'),
    ]
    specimen_choice = models.CharField(choices=TYPE_OF_SPECIMEN, max_length=2000)
    specimen_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    test_type = models.CharField(max_length=4000, blank=True, null=True, choices=TESTS)

    def clean(self):
        super().clean()
        if self.specimen_choice == 'type1' and self.test_type not in dict(self.BLOOD_TEST):
            raise ValidationError({'test_type': 'Invalid test type for Blood test'})
        elif self.specimen_choice == 'type2' and self.test_type not in dict(self.STOOL_TEST):
            raise ValidationError({'test_type': 'Invalid test type for Stool test'})
        elif self.specimen_choice == 'type3' and self.test_type not in dict(self.URINE_TEST):
            raise ValidationError({'test_type': 'Invalid test type for Urine test'})
        elif self.specimen_choice == 'type4' and self.test_type not in dict(self.SALIVA_TEST):
            raise ValidationError({'test_type': 'Invalid test type for Saliva test'})

    pathologist_present = models.CharField(max_length=500)
    date_created = models.DateTimeField(auto_now_add=True)
    date_released = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.patient_fname} {self.patient_lname}"
