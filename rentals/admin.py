from django.contrib import admin
from .models import Rental, Owner, Student
# Register your models here.
class RentalAdmin(admin.ModelAdmin):
    list_display = ["owner", "name", "capacity", "unit_rent", "occupied", "vacant", "date_created"]

admin.site.register(Rental, RentalAdmin)

class OwnerAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "phone_number", "date_created", "date_updated"]

admin.site.register(Owner, OwnerAdmin)


class StudentAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "phone_number", "date_created", "date_updated"]

admin.site.register(Student, StudentAdmin)