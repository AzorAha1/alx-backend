import csv
import math
from typing import List
"""sumary_line

Keyword arguments:
argument -- description
Return: return_description
"""


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """_summary_
        """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def index_range(self, page: int, page_size: int) -> tuple:
        """_summary_
        Args:
            page (int): _description_
            page_size (int): _description_

        Returns:
            tuple: _description_
        """
        start_index = (page - 1) * page_size
        end_index = (page * page_size)
        return (start_index, end_index)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """_summary_

        Args:
            page (int, optional): _description_. Defaults to 1.
            page_size (int, optional): _description_. Defaults to 10.

        Returns:
            List[List]: _description_
        """
        assert isinstance(page, int)\
            and page > 0,\
            "AssertionError raised when page and/or page_size are not ints"
        assert isinstance(page_size, int)\
            and page_size > 0,\
            "AssertionError raised when page and/or page_size are not ints"
        start, end = self.index_range(page, page_size)
        return self.dataset()[start:end]
