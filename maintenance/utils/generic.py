"""
maintenance/utils/generic.py _(Version 3)_
--------------------------------------------

Author: Matthew

Description: Generic utils to be used by other utils.

DateCreated: 12/06/2026 @ 18:23

Compatibility: Compatible with MAPDAT4.db only.

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

import re
from pathlib import Path
from sys import path_hooks

# Constants
GITHUB_RAW: str = "https://raw.githubusercontent.com/mf366-dev/DoomMapGuessr-Image-Library/refs/heads/main"
EVALUATED_IMAGE_NAME_PATTERN: re.Pattern[str] = re.compile(
    r"^(-?\d+)_(-?\d+)_(-?\d+)\.(png|jpg|jpeg)$"
)
TO_BE_RANKED_IMAGE_NAME_PATTERN: re.Pattern[str] = re.compile(
    r"^(-?\d+)_(-?\d+)_(-?\d+)_TO-BE-RANKED\.(png|jpg|jpeg)$"
)


# Methods
def get_relative_github_path(path: Path | None = None) -> str | None:
    if not path:
        path = Path.cwd()

    parts: tuple[str, ...] = tuple(GITHUB_RAW) + path.parts

    for i, part in enumerate(parts):
        if part in ("A_Classic", "B_DOOM-64", "C_Others"):
            return "/".join(parts[i:])

    return None


def parse_coordinates_in_filename(s: str, /) -> tuple[float, float, float] | None:
    match_to_be_ranked: re.Match[str] | None = re.match(
        TO_BE_RANKED_IMAGE_NAME_PATTERN, s
    )
    match_evaluated: re.Match[str] | None = re.match(EVALUATED_IMAGE_NAME_PATTERN, s)

    if match_evaluated or match_to_be_ranked:
        match: re.Match[str] = (
            match_evaluated if match_to_be_ranked is None else match_to_be_ranked
        )

        x, y, z = match.groups()
        return (float(x), float(y), float(z))

    return None
