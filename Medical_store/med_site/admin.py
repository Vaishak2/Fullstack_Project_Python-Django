from django.contrib import admin
from .models import Medicine, Doctors
# Register your models here.

# admin.site.register(Medicine)

@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ('med_name', 'purpose', 'unit', 'stock')

@admin.register(Doctors)
class DoctorsAdmin(admin.ModelAdmin):
    list_display = ('doc_name', 'doc_spec', 'dep_name', 'doc_image')
