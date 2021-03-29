from django.db import models


class BaseModel(models.Model):
    created_at = models.DateField(auto_now_add=True)
    created_by = models.CharField(max_length=255)
    modified_by = models.CharField(max_length=255)
    modified_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class DriversEducation(BaseModel):
    school = models.CharField(max_length=255)
    instructor = models.CharField(max_length=255)


class MedicalType(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class MedicalProvider(BaseModel):
    medical_type = models.ForeignKey(MedicalType, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    address = models.CharField(max_length=255)
    contact_no = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    contact_person_address = models.CharField(max_length=255)
    contact_person_phone_number = models.CharField(max_length=255)
