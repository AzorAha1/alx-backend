#!/usr/bin/env python3
"""

Keyword arguments:
argument -- description
Return: return_description
"""


from collections import OrderedDict
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """_summary_

    Args:
        BaseCaching (_type_): _description_
    """
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """put

        Args:
            key (_type_): _description_
            item (_type_): _description_
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discard_key, _ = self.cache_data.popitem(last=False)
            print(f'DISCARD: {discard_key}')

    def get(self, key):
        """get
        Args:
            key (_type_): _description_

        Returns:
            _type_: _description_
        """
        if key is None or key not in self.cache_data:
            return None
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
        return self.cache_data[key]
