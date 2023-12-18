"""
This module provides a spinner using fira code's spinner glyphs.
"""


def generate_spinner(iterator: int, update_frequency: int):
    """
    Generates a spinner glyph based on the loop iterations.

    Args:
        iterator (int): The current iteration or loop counter.
        update_frequency (int): The frequency at which the spinner should be updated.

    Returns:
        str: A Fira Code glyph representing the current state of the spinner.
    """
    glyphs: list[str] = ['\U0000EE06', '\U0000EE07', '\U0000EE08',
                         '\U0000EE09', '\U0000EE0A', '\U0000EE0B']

    spinner_index = (iterator // update_frequency) % len(glyphs)

    return glyphs[spinner_index]


for i in range(0, 100000):
    print(f'\r{generate_spinner(i, 2000)}', end='')
print("\rsuccess!")  # return carriage again to erase the spinner
