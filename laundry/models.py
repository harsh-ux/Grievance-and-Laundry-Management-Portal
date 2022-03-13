from django.db import models
from django.utils import timezone

# Create your models here.
CHOICES = [(i, i) for i in range(0, 11)]


class BLaundry(models.Model):
    student = models.ForeignKey("accounts.StudentProfile", on_delete=models.CASCADE)
    jeans = models.PositiveIntegerField(default=0, choices=CHOICES)
    pant = models.PositiveIntegerField(default=0, choices=CHOICES)
    pyjama = models.PositiveIntegerField(default=0, choices=CHOICES)
    shorts = models.PositiveIntegerField(default=0, choices=CHOICES)
    t_shirt = models.PositiveIntegerField(default=0, choices=CHOICES)
    bed_sheet = models.PositiveIntegerField(default=0, choices=CHOICES)
    pillow_cover = models.PositiveIntegerField(default=0, choices=CHOICES)
    towel = models.PositiveIntegerField(default=0, choices=CHOICES)
    turban = models.PositiveIntegerField(default=0, choices=CHOICES)
    upper_hood = models.PositiveIntegerField(default=0, choices=CHOICES)
    date = models.DateTimeField(auto_now_add=True)
    is_processed = models.BooleanField(default=False)
    is_delivered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.user.username}"
    
    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in BLaundry._meta.fields]
    
# "accounts.StudentProfile"
class GLaundry(models.Model):
    student = models.ForeignKey("accounts.StudentProfile", on_delete=models.CASCADE)
    jeans = models.PositiveIntegerField(default=0, choices=CHOICES)
    pant = models.PositiveIntegerField(default=0, choices=CHOICES)
    pyjama = models.PositiveIntegerField(default=0, choices=CHOICES)
    shorts = models.PositiveIntegerField(default=0, choices=CHOICES)
    t_shirt = models.PositiveIntegerField(default=0, choices=CHOICES)
    bed_sheet = models.PositiveIntegerField(default=0, choices=CHOICES)
    pillow_cover = models.PositiveIntegerField(default=0, choices=CHOICES)
    towel = models.PositiveIntegerField(default=0, choices=CHOICES)
    turban = models.PositiveIntegerField(default=0, choices=CHOICES)
    upper_hood = models.PositiveIntegerField(default=0, choices=CHOICES)

    kurta_salwar = models.PositiveIntegerField(default=0, choices=CHOICES)
    skirt = models.PositiveIntegerField(default=0, choices=CHOICES)
    dupatta = models.PositiveIntegerField(default=0, choices=CHOICES)
    date = models.DateTimeField(auto_now_add=True)
    is_processed = models.BooleanField(default=False)
    is_delivered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.name}"

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in GLaundry._meta.fields]

class Complaint(models.Model):
    HOSTEL_CHOICES=(
        ('B1','B1'),
        ('B2','B2'),
        ('B3','B3'),
        ('B4','B5'),
        ('G1','G1'),
        ('G2','G2'),
        ('G3','G3'),
        ('G4','G4'),
        ('G5','G5'),
        ('G6','G6'),
        ('I2','I2')
    )
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=500)
    complaint_pic = models.ImageField(upload_to=None, height_field=None, width_field=None)
    author = models.ForeignKey("accounts.StudentProfile", on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    hostel=models.CharField(max_length=2, choices=HOSTEL_CHOICES, default='B1')
