from django.contrib import admin

# Register your models here.
from .models import User
from .models import Admin
from .models import Equipment
from .models import Report
from .models import Reservation
from .models import AdminandEquipment

admin.site.register(Admin)
admin.site.register(User)
admin.site.register(Equipment)
admin.site.register(Reservation)
admin.site.register(Report)
admin.site.register(AdminandEquipment)