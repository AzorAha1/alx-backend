#!/usr/bin/env python3
"""sumary_line

Keyword arguments:
argument -- description
Return: return_description
"""


from base_caching import BaseCaching
from collections import deque


class LIFOCache(BaseCaching):
    """_summary_

    Args:
        BaseCaching (_type_): _description_
    """
    def __init__(self):
        """_summary_
        """
        super().__init__()
        self.cache_data = {}
        self.key_in_order = []

    def put(self, key, item):
        """_summary_

        Args:
            key (_type_): _description_
            item (_type_): _description_
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discard_key = self.key_in_order.pop(-1)
            del self.cache_data[discard_key]
            print(f'DISCARD: {discard_key}')
        self.cache_data[key] = item
        if key not in self.key_in_order:
            self.key_in_order.append(key)

    def get(self, key):
        """_summary_

        Args:
            key (_type_): _description_

        Returns:
            _type_: _description_
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
