# loading_bar_module/__init__.py
"""
Loading utilities

A simple Python module for creating loading bars and spinners.

Example:
    >>> from loading_bar_module import generate_loading_bar, generate spinner
    >>> loading_bar = generate_loading_bar(50, 100, 50)
    >>> loading_spinner = generate_spinner(50) 
    >>> print(loading_bar + loading_spinner)
    
"""
from .loading_bar import generate_loading_bar

__all__ = ['generate_loading_bar']
