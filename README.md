# checkpoints

Cache results of functions returning pandas DataFrames.

## Installation

Add to the current Python site packages by running

```
$ pip install git+ssh://git@github.boozallencsn.com/Badart-William/checkpoints.git
```

Or add
`git+ssh://git@github.boozallencsn.com/Badart-William/checkpoints.git`
to your `requirements.txt` file, or add that URL to the
`dependency_links` section of your `setup.py` file and add
`checkpoints` to `install_requires`.

## Usage

The `checkpoints` module exports one function, `checkpoint`, which is
designed to be used as a decorator:

```python
import pandas as pd
from checkpoints import checkpoint

@checkpoint('data/preprocessed/my_func.csv')
def my_func(input_df: pd.DataFrame) -> pd.DataFrame:
    ...
```

But like any decorator can also be applied to just a single call-site
of the function to be cached:

```python
df.pipe(checkpoint('checkpoint.csv')(really_expensive_process))\
  .pipe(the_rest_of_my_pipeline)
```
