from typing import cast

from django.db import models
from src.entities.cart import Cart as CartEntity
from src.models.user import User

from ..cart import Cart
from ..report import Report


class CartHelper:
    @staticmethod
    def from_entity(user_sub: models.CharField, cart: CartEntity) -> "Cart":
        (cart) = Cart.objects.get_or_create(user=User.objects.get(sub=user_sub))
        return cast(
            Cart,
            cart.construct(report=[Report(**report.dict()) for report in cart.reports]),
        )
