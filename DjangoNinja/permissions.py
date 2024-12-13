from functools import wraps
from typing import Callable, List


def guard(permission_funcs: List[Callable], operator: str = 'and'):
    """
    A decorator to enforce permissions on a view function.
    The permission functions receive:
      - request
      - all the same *args and **kwargs as the view

    Args:
        permission_funcs: A list of callables that each accept (request, *args, **kwargs)
                          and return a boolean indicating permission granted.
        operator: 'and' or 'or' to determine how to combine multiple permissions.
    """
    if operator not in ('and', 'or'):
        raise ValueError("Invalid operator. Use 'and' or 'or'.")

    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if operator == 'and':
                has_permission = all(perm(request, *args, **kwargs) for perm in permission_funcs)
            else:
                has_permission = any(perm(request, *args, **kwargs) for perm in permission_funcs)

            if has_permission:
                return view_func(request, *args, **kwargs)
            return 403, {"message": "Permission denied"}

        return _wrapped_view

    return decorator
