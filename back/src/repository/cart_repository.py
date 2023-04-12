from dataclasses import dataclass
from typing import Optional

from django.contrib.sessions.backends.cache import SessionStore
from django.core.exceptions import ObjectDoesNotExist
from src.entities.cart import Cart as CartEntity
from src.models import Cart as CartModel
from src.models import User
from src.models.model_helpers.cart import CartHelper


@dataclass
class CartRepository:
    user: Optional[User]
    session: SessionStore

    def get(self) -> CartEntity:
        if self.user is None:
            return CartEntity.parse_raw(self.session["cart"])
        else:
            return CartEntity.parse_obj(
                CartModel.objects.get(user=self.user.sub).__dict__
            )

    def get_or_create(self) -> CartEntity:
        try:
            return self.get()
        except (KeyError, CartModel.DoesNotExist):  # type: ignore
            cart = CartEntity(reports=[])
            self.save(cart)
            return cart

    def save(self, cart: CartEntity) -> None:
        if self.user is None:
            self.session["cart"] = cart.json()
        else:
            CartHelper.from_entity(self.user.sub, cart).save()
