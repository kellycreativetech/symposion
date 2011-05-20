from tastypie import fields
from tastypie.resources import ModelResource
from symposion.speakers.models import Speaker

class SpeakerResource(ModelResource):
    
    class Meta:
        queryset = Speaker.objects.all()
        available_methods = ["get",]