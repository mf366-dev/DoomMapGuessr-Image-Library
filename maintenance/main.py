"""
maintenance/main.py _(Version 3)_
--------------------------------------------

Author: Matthew

Description: Maintenance toolkit for DoomMapGuessr's Image Library.

DateCreated: 29/03/2026 @ 19:34

Compatibility: Compatible with MAPDAT3.db only.

--------------------------------------------

License: MIT _(see below)_

> MIT License
> 
> Copyright (c) 2026 Matthew
> 
> Permission is hereby granted, free of charge, to any person obtaining a copy
> of this software and associated documentation files (the "Software"), to deal
> in the Software without restriction, including without limitation the rights
> to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
> copies of the Software, and to permit persons to whom the Software is
> furnished to do so, subject to the following conditions:
> 
> The above copyright notice and this permission notice shall be included in all
> copies or substantial portions of the Software.
> 
> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
> IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
> FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
> AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
> LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
> OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
> SOFTWARE.
"""


# [*] Imports
import os
import platform
import subprocess
from pathlib import Path
from collections import defaultdict
import re
import csv
import sqlite3
import requests


# [*] Constants
CONFIG: str = ""

DIFFICULTY_NAMES: list[str] = [
    "I'm too Young to Guess",
    "Guessing: not too rough",
    "Guess me Plenty",
    "Ultra-Guessing",
    "Guessmare!",
    "Guessmare!! PLUS"
]

DIFFICULTY_ABBREVIATION: list[str] = [
    "ITYTG",
    "GNTR",
    "GMP",
    "UG",
    "GM",
    "GM+"
]


# [*] Auxiliary Functions (I)
def get_cwd_path_object() -> Path:
    return Path(os.getcwd())

def get_full_difficulty_name(difficulty_level: int) -> str:
    """
    get_full_difficulty_name

    Returns the difficulty in the form of a string such as `<name> (<abbreviation>)`.

    :param int difficulty_level: the difficulty level to get (from 1 to 6, both ends included)
    :return str: the string described above
    """
    
    return f"{DIFFICULTY_NAMES[difficulty_level - 1]} ({DIFFICULTY_ABBREVIATION[difficulty_level - 1]})"

def get_pretty_header(header_text: str) -> str:
    return header_text # TODO: make this actually return a pretty header


# [*] Global Variables
database_path: str = f"{get_cwd_path_object().joinpath("./MAPDAT3.db")}"


if __name__ == '__main__':
    # TODO: run the actual entry point here
    pass
