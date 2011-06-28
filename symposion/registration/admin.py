from django.contrib import admin
from symposion.registration.models import Registrant

class RegistrantAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "email", "will_buy_tshirt", "tshirt_size", "remote_ip"]

admin.site.register(Registrant, RegistrantAdmin)
