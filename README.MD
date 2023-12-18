[🇧🇷 version](langs/PT-BR.MD)
# Loading bar overview

This project provides a module for creating loading bars using [fira code's](https://github.com/tonsky/FiraCode) special loading bar glyphs.

![[/images/fira_symbols.png]]


## Overview

This project provides a function to generate loading bars:

```
generate_loading_bar(
    current_value = 50, # How much progress
    total_value = 100,  # Of how much
    bar_length = 100    # Optional, default is 100
    )
```

This code will generate you a nice loading bar:
![[images/loading_bar_example.png]]
For best results enable font ligatures

## Usage tip

In case you are less experienced this is how you can make it update instead of printing a new line, this is an example for it in use
```
for i in range(1, 100000):

    print(f'\r{generate_loading_bar(i, 100000, 100)}', end='')

```
the \r is called a return carriage, it returns the "printing cursor" back to the start of the line, in case you don't get the name it's in reference to typewriters

in the end of a print the default is for python to add a newline (\n) at the end of a line, by overwriting that default and using the return carriage we can make the command line write a line, erase it and write again in the same line