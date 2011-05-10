from django.db import models
from django.contrib.auth.models import User

class Registrant(models.Model):
    TSHIRT_M_S = 1
    TSHIRT_M_M = 2
    TSHIRT_M_L = 3
    TSHIRT_M_XL = 4
    TSHIRT_M_XXL = 5
    TSHIRT_W_S = 6
    TSHIRT_W_M = 7
    TSHIRT_W_L = 8
    TSHIRT_W_XL = 9
    TSHIRTS = (
        (TSHIRT_M_S, "Men's Small"),
        (TSHIRT_M_S, "Men's Medium"),
        (TSHIRT_M_S, "Men's Large"),
        (TSHIRT_M_S, "Men's Extra Large"),
        (TSHIRT_M_S, "Men's 2X Large"),
        (TSHIRT_M_S, "Women's Small"),
        (TSHIRT_M_S, "Women's Medium"),
        (TSHIRT_M_S, "Women's Large"),
        (TSHIRT_M_S, "Women's Extra Large"),
    )

    user = models.ForeignKey(User, null=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField()
    will_buy_tshirt = models.BooleanField("I would buy a T-Shirt", default=True, help_text="We're looking for a T-shirt sponsor, but if we don't get one, we'll be asking for cash.")
    tshirt_size = models.SmallIntegerField("T-Shirt Size", choices=TSHIRTS)
