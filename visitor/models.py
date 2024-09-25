# models.py
import random
import string
from django.db import models
from visitor.mixins import EncryptedFieldMixin
# from auth_app.models import SwarnaBoomiUser

class VisitorTable(models.Model):
    PROOF_TYPE_CHOICES = [
        (1, 'Aadhar'),
        (2, 'Driving License'),
        (3, 'Option 3'),
        (4, 'Option 4'),
    ]

    RETURN_STATUS_CHOICES = [
        (0, 'Pending'),
        (1, 'Approved'),
        (2, 'Rejected'),
    ]

    # user = models.ForeignKey(SwarnaBoomiUser, on_delete=models.CASCADE, null=True, blank=True)
    gatepass_id = models.CharField(unique=True, editable=False, max_length=20, null=True)
    place_of_visit = models.CharField(max_length=50)
    name = models.CharField(max_length=225, null=True)
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=50)
    mobile = models.BigIntegerField(blank=True)
    email = models.EmailField()
    address = models.TextField()
    photo = models.FileField(upload_to='profile/', null=True, blank=True)
    id_proof = models.FileField(upload_to='profile/', null=True, blank=True)
    id_proof1 = models.FileField(upload_to='profile/', null=True, blank=True)
    proof_type = models.CharField(choices=PROOF_TYPE_CHOICES, null=True, max_length=50)
    aprt_name = models.TextField()
    purpose = models.TextField()
    visit_person = models.CharField(max_length=225, null=True)
    in_time = models.TimeField(auto_now_add=True)
    out_time = models.TimeField(null=True, blank=True)
    visiting_mobile = models.CharField(max_length=225, null=True)
    date = models.DateField()
    extra_visitor = models.IntegerField()
    has_vehicle = models.BooleanField(default=False)
    id_number = models.CharField(null=True, max_length=26)
    date_of_birth = models.CharField(null=True, max_length=26)
    type_of_pass = models.CharField(max_length=10, null=True)
    expiry_status = models.CharField(null=True, max_length=100)
    approval_status = models.CharField(choices=RETURN_STATUS_CHOICES, default=0, max_length=100)
    pass_type = models.CharField(max_length=10, null=True)
    expiry_time = models.TimeField(null=True, blank=True)
    rfid_ref_no = models.ForeignKey('Rfid_Register', on_delete=models.CASCADE, null=True, blank=True)
    return_status = models.CharField(choices=RETURN_STATUS_CHOICES, default=0, max_length=50)

    def save(self, *args, **kwargs):
        if not self.gatepass_id:
            self.gatepass_id = self.generate_gatepass_id()

        # Encrypt fields
        self.name = EncryptedFieldMixin().encrypt(self.name)
        self.mobile = EncryptedFieldMixin().encrypt(self.mobile)
        self.visiting_mobile = EncryptedFieldMixin().encrypt(self.visiting_mobile)
        self.visit_person = EncryptedFieldMixin().encrypt(self.visit_person)
        self.address = EncryptedFieldMixin().encrypt(self.address)

        super().save(*args, **kwargs)

    def generate_gatepass_id(self):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

    def __str__(self):
        return f"{self.name} ({self.gatepass_id})"
    




class Rfid_Register(models.Model):
    rfid_number = models.CharField(max_length=50, unique=True)
    # user = models.ForeignKey(SwarnaBoomiUser, on_delete=models.CASCADE)
    # Add other relevant fields

    def __str__(self):
        return self.rfid_number
