#!/usr/bin/env python3
"""sumary_line
Keyword arguments:
argument -- description
Return: return_description
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """_summary_

    Args:
        BaseCaching (_type_): _description_
    """
    def __init__(self):
        """_summary_
        """
        super().__init__()
        self.cache_data = {}

    def put(self, key, item):
        """_summary_

        Args:
            key (_type_): _description_
            item (_type_): _description_
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        # if len(self.cache_data) > BaseCaching.MAX_ITEMS:
        #     discard_key, _ = self.cache_data.popitem()
        #     print(f'DISCARD {discard_key}')

    def get(self, key):
        """_summary_

        Args:
            key (_type_): _description_

        Returns:
            _type_: _description_
        """
        if key not in self.cache_data:
            return None
        return self.cache_data.get(key)
