from django.core.management.base import BaseCommand
from symposion.registration.models import Registrant
import csv
import sys


class Command(BaseCommand):
    def handle(self, *args, **options):
        writer = csv.writer(sys.stdout)
        writer.writerow([
                "First Name",
                "Last Name",
                "Email",
                "Will buy shirt",
                "Will volunteer",
                "Shirt Size",
                "IP",
                "Location",
            ])
        registrants = Registrant.objects.all()
        for r in registrants:
            writer.writerow([
                r.first_name,
                r.last_name,
                r.email,
                r.will_buy_tshirt,
                r.will_volunteer,
                r.get_tshirt_size_display(),
                r.remote_ip,
                r.location,
            ])
