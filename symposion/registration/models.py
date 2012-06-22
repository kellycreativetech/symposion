from django.db import models
from django.contrib.auth.models import User

class Registrant(models.Model):
    NOSHIRT = -1
    TSHIRT_M_S = 1
    TSHIRT_M_M = 2
    TSHIRT_M_L = 3
    TSHIRT_M_XL = 4
    TSHIRT_M_XXL = 5
    TSHIRT_M_XXXL = 10
    TSHIRT_W_S = 6
    TSHIRT_W_M = 7
    TSHIRT_W_L = 8
    TSHIRT_W_XL = 9
    TSHIRTS = (
        (NOSHIRT, "Select a size"),
        (TSHIRT_M_S, "Men's Small"),
        (TSHIRT_M_M, "Men's Medium"),
        (TSHIRT_M_L, "Men's Large"),
        (TSHIRT_M_XL, "Men's Extra Large"),
        (TSHIRT_M_XXL, "Men's 2X Large"),
        (TSHIRT_M_XXXL, "Men's 3X Large"),
        (TSHIRT_W_S, "Women's Small"),
        (TSHIRT_W_M, "Women's Medium"),
        (TSHIRT_W_L, "Women's Large"),
        (TSHIRT_W_XL, "Women's Extra Large"),
    )

    user = models.ForeignKey(User, null=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField()
    will_buy_tshirt = models.BooleanField("I would buy a T-Shirt", help_text="We're looking for a T-shirt sponsor, but if we don't get one, we'll be asking for cash.")
    will_volunteer = models.BooleanField("Contact me, I'd like to voluteer", help_text="")
    tshirt_size = models.SmallIntegerField("T-Shirt Size", default=-1, choices=TSHIRTS,
        help_text="""We will ask for a $20 donation to support PyOhio when you pick up your t-shirt. Alternately please consider volunteering time. Only if you are willing to donate.""")
    remote_ip = models.IPAddressField(blank=True, null=True)
    location = models.CharField(help_text="City, and State or Country", max_length=128, blank=True, null=True)
