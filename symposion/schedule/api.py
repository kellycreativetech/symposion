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
    speaker = fields.ToOneField("symposion.speakers.api.SpeakerResource", "speaker", full=True, null=True)
    additional_speakers = fields.ToManyField("symposion.speakers.api.SpeakerResource", "additional_speakers", full=True, null=True)
    
    class Meta:
        queryset = Presentation.objects.all()
        available_methods = ["get",]

class SlotResource(ModelResource):
    presentation = fields.ToOneField("symposion.schedule.api.PresentationResource", "presentation", full=True, null=True)
    recess = fields.ToOneField("symposion.schedule.api.RecessResource", "recess", full=True, null=True)
    plenary = fields.ToOneField("symposion.schedule.api.PlenaryResource", "plenary", full=True, null=True)
    
    class Meta:
        queryset = Slot.objects.all()
        available_methods = ["get",]
