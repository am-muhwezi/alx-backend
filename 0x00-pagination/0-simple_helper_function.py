#!/usr/bin/env python3
"""Pagination helper function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """
    Calculate start and end indexes for pagination.

    Args:
        page (int): Current page number (1-indexed)
        page_size (int): Number of items per page

    Returns:
        tuple[int, int]: Tuple containing (start_index, end_index)

    Examples:
        >>> index_range(1, 7)  # First page
        (0, 7)
        >>> index_range(2, 7)  # Second page
        (7, 14)
        >>> index_range(3, 7)  # Third page
        (14, 21)
"""
    start = (page - 1) * page_size
    end = (start + page_size)
    return (start, end)
