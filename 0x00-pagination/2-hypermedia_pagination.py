#!/usr/bin/env python3
"""sumary_line

Keyword arguments:
argument -- description
Return: return_description
"""


import csv
import math
from typing import List


index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """_summary_
        """
        self.__dataset = None

    def get_hyper(self, page: int = 1, page_size: int = 10):
        """_summary_

        Args:
            page (int, optional): _description_. Defaults to 1.
            page_size (int, optional): _description_. Defaults to 10.
        """
        start_index = (page - 1) * page_size
        end_index = (page * page_size)
        data = self.dataset()[start_index:end_index]
        next_page = None if end_index >= len(self.dataset()) else page + 1
        total_pages = math.ceil(len(self.dataset()) / page_size)
        prev_page = None if page == 1 else page - 1
        return {
            'page_size': len(self.dataset()),
            'page': page,
            'data': data,
            'next_page':  next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """_summary_
        Args:
            page (int, optional): _description_. Defaults to 1.
            page_size (int, optional): _description_. Defaults to 10.

        Returns:
            List[List]: _description_
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        data = self.dataset()
        try:
            return data[start:end]
        except IndexError:
            return []
