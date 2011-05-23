from tastypie import fields
from tastypie.resources import ModelResource
from symposion.schedule.models import *
from symposion.speakers.api import SpeakerResource

class RecessResource(ModelResource):
    class Meta:
        queryset = Recess.objects.all()
        available_methods = ["get",]

class PlenaryResource(ModelResource):
    class Meta:
        queryset = Plenary.objects.all()
        available_methods = ["get",]

class PresentationResource(ModelResource):
    speaker = fields.ToOneField("symposion.api.SpeakerResource", "speaker", full=true, null=True)
    additional_speakers = fields.ToManyField("symposion.api.SpeakerResource", "additional_speakers", full=True, null=True)
    
    class Meta:
        queryset = Presentation.objects.all()
        available_methods = ["get",]

class SlotResource(ModelResource):
    presentation = fields.ToOneField("symposion.api.PresentationResource", "presentation", full=true, null=True)
    recess = fields.ToOneField("symposion.api.RecessResource", "recess", full=true, null=True)
    plenary = fields.ToOneField("symposion.api.PlenaryResource", "plenary", full=true, null=True)
    
    class Meta:
        queryset = Slot.objects.all()
        available_methods = ["get",]
