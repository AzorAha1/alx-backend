#!/usr/bin/env python3
"""

Keyword arguments:
argument -- description
Return: return_description
"""


from collections import OrderedDict
from base_caching import BaseCaching


class MRUCache(BaseCaching):
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
        
        self.cache_data[key] = item
        self.cache_data.move_to_end(key)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discard_key = next(iter(self.cache_data))
            print(f'DISCARD: {discard_key}')
            self.cache_data.pop(discard_key)

    def get(self, key):
        """get
        Args:
            key (_type_): _description_

        Returns:
            _type_: _description_
        """
        if key is None or key not in self.cache_data:
            return None
        
        self.cache_data.move_to_end(key)
        return self.cache_data.get(key)
