from django.db import models

# Bed Model
class Bed(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('occupied', 'Occupied'),
    ]
    bed_number = models.CharField(max_length=10, unique=True)
    bed_type = models.CharField(max_length=50)  # ICU, Normal, etc.
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='available')

    def __str__(self):
        return f"Bed {self.bed_number} - {self.status}"

# Equipment Model
class Equipment(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    in_use = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.name} ({self.quantity - self.in_use} available)"

# Staff Model
class Staff(models.Model):
    ROLE_CHOICES = [
        ('doctor', 'Doctor'),
        ('nurse', 'Nurse'),
        ('support', 'Support Staff'),
    ]
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    shift = models.CharField(max_length=50)  # Morning, Evening, Night

    def __str__(self):
        return f"{self.name} - {self.role} ({self.shift})"

# Medicine Model
class Medicine(models.Model):
    name = models.CharField(max_length=100)
    stock = models.PositiveIntegerField()
    expiry_date = models.DateField()

    def __str__(self):
        return f"{self.name} (Stock: {self.stock})"

