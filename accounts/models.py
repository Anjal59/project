from django.contrib.auth.models import AbstractUser
from django.db import models

ROLE_CHOICES = (
    ('admin', 'Admin'),
    ('office_staff', 'Office Staff'),
    ('librarian', 'Librarian'),
)

class CustomUser(AbstractUser):
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='office_staff')

    def is_admin(self):
        return self.role == 'admin'

    def is_office_staff(self):
        return self.role == 'office_staff'

    def is_librarian(self):
        return self.role == 'librarian'

