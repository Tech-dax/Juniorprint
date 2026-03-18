from colorama import init
init(autoreset=True)

import builtins
from .formatter import format_text

_original_print = builtins.print

def print_(*args, **kwargs):
    try:
        formatted_args = [format_text(str(arg)) for arg in args]
        _original_print(*formatted_args, **kwargs)
    except Exception:
        _original_print(*args, **kwargs)
