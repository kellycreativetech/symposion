from django.template.response import TemplateResponse
from django.views.generic.edit import CreateView

from symposion.registration.forms import RegistrantForm
from symposion.registration.models import Registrant


class RegistrationView(CreateView):
    form_class = RegistrantForm
    model = Registrant
    template_name = "registration/register.html"
    
    success_url = "/register/done/"
    
    def get_success_url(self, *args, **kwargs):
        return self.success_url
    
    def get_form_kwargs(self, *args, **kwargs):
        kw = super(RegistrationView, self).get_form_kwargs(*args, **kwargs)
        kw.update({
            "ip": self.request.META.get("HTTP_X_CLUSTER_CLIENT_IP", None)
        })
        return kw


def registration_success(request):
    return TemplateResponse(request, "registration/done.html", {})