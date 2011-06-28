from django import forms
from symposion.registration.models import Registrant


class RegistrantForm(forms.ModelForm):
    ip = None
    
    def __init__(self, ip=None, *args, **kwargs):
        if ip:
            self.ip = ip
            print ip
        super(RegistrantForm, self).__init__(*args, **kwargs)
    
    def save(self, *args, **kwargs):
        if self.ip:
            temp_dict = kwargs.copy()
            temp_dict.update({"commit": False})
            registrant = super(RegistrantForm, self).save(*args, **temp_dict)
            registrant.remote_ip = self.ip
            if kwargs.get("commit", True):
                registrant.save()
            return registrant
        else:
            return super(RegistrantForm, self).save(*args, **kwargs)
    
    class Meta:
        exclude = ["user", "remote_ip"]
        model = Registrant
