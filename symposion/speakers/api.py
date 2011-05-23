from django.contrib.auth.models import User

from tastypie import fields
from tastypie.resources import ModelResource
from symposion.speakers.models import Speaker

class UserResource(ModelResource):
    
    class Meta:
        queryset = User.objects.all()
        exclude = ["password", "email", "is_superuser", "is_staff"]
        available_methods = ["get",]

class SpeakerResource(ModelResource):
    user = fields.ToOneField("symposion.speakers.api.UserResource", "user", full=True, null=True)
    
    class Meta:
        queryset = Speaker.objects.all()
        available_methods = ["get",]