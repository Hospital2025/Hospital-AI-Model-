from django.contrib import admin
from .models import Bed, Equipment, Staff, Medicine

admin.site.register(Bed)
admin.site.register(Equipment)
admin.site.register(Staff)
admin.site.register(Medicine)

