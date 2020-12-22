# In a given list the first element should become the last one.
# An empty list or list with only one element should stay the same.

from typing import Iterable

# first solution
def replace_first(items: list) -> Iterable:
    if len(items) > 1:
        first_item = items.pop(0)
        items.append(first_item)
        return items
    else:
        return items


# second solution
def replace_first(items: list) -> list:
    return items[1:] + items[:1]
