from __future__ import annotations
from typing import Protocol
import typing
if typing.TYPE_CHECKING:
    from new_movies.user import User


class Rentable(Protocol):
    def rent_by(self, user: User) -> None:
        ...
