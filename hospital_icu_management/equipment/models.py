from django.db import models

class Equipment(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('in-use', 'In Use'),
        ('maintenance', 'Maintenance'),
        ('broken', 'Broken'),
        ('out of service', 'Out of Service'),
    ]

    equipment_id = models.CharField(max_length=50, unique=True)
    equipment_name = models.CharField(max_length=100)
    equipment_type = models.CharField(max_length=100)  # You can rename this to 'category' if you wish
    category = models.CharField(max_length=100, blank=True)  # Added for category column in table
    serial_number = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    purchase_date = models.DateField()
    warranty_expiry = models.DateField(blank=True, null=True)
    last_maintenance_date = models.DateField(blank=True, null=True)
    next_maintenance_date = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['equipment_name']

    def __str__(self):
        return f"{self.equipment_name} ({self.equipment_id})"


class MaintenanceLog(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='maintenance_logs')
    maintenance_date = models.DateTimeField(auto_now_add=True)
    maintenance_type = models.CharField(max_length=100)
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    performed_by = models.CharField(max_length=100)
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ['-maintenance_date']

    def __str__(self):
        return f"Maintenance: {self.equipment.equipment_name} - {self.maintenance_date.date()}"
