import functools
from collections.abc import Callable
from typing import Any, TypeVar, cast

from new_movies.user import Role, User
from new_movies.exceptions import ActionNotAllowed

F = TypeVar('F', bound=Callable[..., Any])


def require_role(require_role: Role) -> Callable[[F], F]:
    def permission_check_decorator(func: F) -> F:
        @functools.wraps(func)
        def wrapper(acting_user: User, *args: Any, **kwargs: Any) -> Any:
            if acting_user.role is not Role.ADMIN:
                raise ActionNotAllowed
            return func(acting_user, *args, **kwargs)
        return cast(F, wrapper)
    return permission_check_decorator
