from django.core.management.base import BaseCommand
from symposion.registration.models import Registrant
import csv
import sys


class Command(BaseCommand):
    def handle(self, *args, **options):
        writer = csv.writer(sys.stdout)
        registrants = Registrant.objects.all()
        for r in registrants:
            writer.writerow([
                r.first_name,
                r.last_name,
                r.email,
                r.will_buy_tshirt,
                r.get_tshirt_size_display(),
                r.remote_ip,
                r.location,
            ])
