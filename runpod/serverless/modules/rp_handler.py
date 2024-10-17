"""Retrieve handler info. """

import inspect
from typing import Callable

from .rp_types import RunpodServerlessWorkerHandler


def is_generator(handler: RunpodServerlessWorkerHandler) -> bool:
    """Check if handler is a generator function."""
    return inspect.isgeneratorfunction(handler) or inspect.isasyncgenfunction(handler)
