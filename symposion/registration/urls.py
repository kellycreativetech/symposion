from django.conf.urls.defaults import *
from symposion.registration.views import RegistrationView

urlpatterns = patterns("",
    url(r"^done/$", "symposion.registration.views.registration_success", name="registration_success"),
    url(r"^$", RegistrationView.as_view(), name="registration_register"),
)
