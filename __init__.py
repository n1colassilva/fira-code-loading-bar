# loading_bar_module/__init__.py
"""
Loading Bar Module

A simple Python module for generating loading bars.

Example:
    >>> from loading_bar_module import generate_loading_bar
    >>> loading_bar = generate_loading_bar(50, 100, 50)
    >>> print(loading_bar)
    
"""
from .loading_bar import generate_loading_bar

__all__ = ['generate_loading_bar']
