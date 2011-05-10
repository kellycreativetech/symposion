from django.template.response import TemplateResponse
from django.views.generic.edit import CreateView

from symposion.registration.forms import RegistrantForm
from symposion.registration.models import Registrant


class RegistrationView(CreateView):
    form_class = RegistrantForm
    model = Registrant
    template_name = "registration/register.html"
    
    success_url = "/register/done/"


def registration_success(request):
    return TemplateResponse(request, "registration/done.html", {})