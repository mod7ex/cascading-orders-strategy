import pandas as pd

def count_max_consecutive_losses(_series: pd.Series):
    _max_count = 0
    _count = 0

    for _item in _series: # row for reading, i for writing
        if _item < 0:
            _count += 1
        else:
            if _count > _max_count:
                _max_count = _count
            _count = 0
    return _max_count