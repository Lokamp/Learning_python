from typing import Iterable


def replace_first(items: list) -> Iterable:
    if len(items) > 1:
        first_item = items.pop(0)
        items.append(first_item)
        return items
    else:
        return items


# second solution
# def replace_first(items: list) -> list:
#     return items[1:] + items[:1]
