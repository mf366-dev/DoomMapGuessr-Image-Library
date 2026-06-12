"""
maintenance/utils/add-images-to-db.py _(Version 3)_
--------------------------------------------

Author: Matthew

Description: Adds images to the MAPDAT4 database.

DateCreated: 12/06/2026 @ 16:20

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
from sqlite3 import Connection, Cursor, Row
from typing import Generator

from .generic import (
    EVALUATED_IMAGE_NAME_PATTERN,
    GITHUB_RAW,
    TO_BE_RANKED_IMAGE_NAME_PATTERN,
    get_relative_github_path,
    parse_coordinates_in_filename,
)


def find_image_files_to_add(
    directory: Path, /, recursive_lookup: bool = False
) -> list[tuple[Path, float, float, float, str]]:
    iterdir: Generator[Path, None, None] = directory.iterdir()

    images: list[tuple[Path, float, float, float, str]] = []

    for path in iterdir:
        if path.is_dir() and recursive_lookup:
            images += find_image_files_to_add(path, recursive_lookup=True)
            continue

        if path.is_file() and (
            re.match(TO_BE_RANKED_IMAGE_NAME_PATTERN, path.name)
            or re.match(EVALUATED_IMAGE_NAME_PATTERN, path.name)
        ):
            coords = parse_coordinates_in_filename(path.name)

            if coords is not None:
                images.append((path, *coords, path.suffix))

    return images


def add_images_to_database(
    connection: Connection,
    map_id: int,
    images: list[tuple[Path, float, float, float, str]],
) -> set[int]:
    connection.row_factory = Row
    cursor: Cursor = connection.cursor()
    errors: set[int] = set()

    for index, (path, x, y, z, ext) in enumerate(images):
        cursor.execute(
            """
            INSERT INTO Image (Source, X, Y, Z, MapId)
            VALUES (?, ?, ?, ?, ?)
            """,
            ("Lorem Ipsum", x, y, z, map_id),
        )
        image_id: int | None = cursor.lastrowid

        if not image_id:
            errors.add(index)

        imagename: str = f"img{str(image_id).zfill(10)}{ext}"
        filename: Path = path.parent.resolve(strict=True) / imagename
        github_rel_path: str | None = get_relative_github_path(path)

        if not github_rel_path:
            errors.add(index)

        github_url: str = f"{GITHUB_RAW}/{github_rel_path}"

        cursor.execute(
            """
            UPDATE Image SET Source = ? WHERE Id = ?
            """,
            (github_url, image_id),
        )

        path.rename(filename)

    connection.commit()
    return errors
