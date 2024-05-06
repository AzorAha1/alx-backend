#!/usr/bin/env python3
"""sumary_line
Keyword arguments:
argument -- description
Return: return_description
"""


def index_range(page: int, page_size: int) -> tuple:
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
