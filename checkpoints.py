"""checkpoints.py

Automatically cache the results of functions on pandas.DataFrames.

Will Badart <Badart_William@bah.com>
created: MAR 2020
"""

from functools import wraps
from os import path
import pandas as pd

__all__ = [
    'checkpoint'
]


def checkpoint(cache, **csv_args):
    """
    Return a decorator which automatically caches the result of a function
    which returns a pandas.DataFrame.

    Parameters
    ----------
    cache : str or path object
        The path to the file which contains the results of `func`.
    **csv_args : Optional[Mapping]
        Arguments to pass on to both `pandas.read_csv` to retrieve cached
        results and `pandas.DataFrame.to_csv` to save results. Should only
        contain parameters common to `read_csv` and `to_csv` (which is most of
        them).

    Returns
    -------
    _decorator : function
        A decorator which caches the result of any function returning a
        `pandas.DataFrame`.
    """
    def _decorator(func):
        @wraps(func)
        def _wrapper(*args, **kwargs):
            if path.exists(path):
                return pd.read_csv(cache, **csv_args)
            else:
                result = func(*args, **kwargs)
                result.to_csv(cache, **csv_args)
                return result
        return _wrapper
    return _decorator
