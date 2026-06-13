"""
maintenance/data/models.py
--------------------------------------------

Author: Matthew

Description: Defines dataclasses to be used instead of the default
Row objects SqLite3 provides.

DateCreated: 12/06/2026 @ 16:23

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

from dataclasses import dataclass
from typing import Self


@dataclass(frozen=True)
class Game:
    id: int
    title: str
    year_of_release: str

    @classmethod
    def from_row(cls, row: dict) -> Self:
        return cls(
            id=row["Id"], title=row["Title"], year_of_release=row["YearOfRelease"]
        )

    def to_dict(self) -> dict:
        return {
            "Id": self.id,
            "Title": self.title,
            "YearOfRelease": self.year_of_release,
        }


@dataclass(frozen=True)
class Episode:
    id: int
    title: str
    relative_position: int
    game_id: int

    @classmethod
    def from_row(cls, row: dict) -> Self:
        return cls(
            id=row["Id"],
            title=row["Title"],
            relative_position=row["RelativePosition"],
            game_id=row["GameId"],
        )

    def to_dict(self) -> dict:
        return {
            "Id": self.id,
            "Title": self.title,
            "RelativePosition": self.relative_position,
            "GameId": self.game_id,
        }


@dataclass(frozen=True)
class Map:
    id: int
    title: str
    relative_position: int
    secret_count: int
    difficulty_modifier: int
    hellkeep_warrens_status: int
    automap_view_source: str
    episode_id: int

    @classmethod
    def from_row(cls, row: dict) -> Self:
        return cls(
            id=row["Id"],
            title=row["Title"],
            relative_position=row["RelativePosition"],
            secret_count=row["SecretCount"],
            difficulty_modifier=row["DifficultyModifier"],
            hellkeep_warrens_status=row["HellKeepWarrensStatus"],
            automap_view_source=row["AutomapViewSource"],
            episode_id=row["EpisodeId"],
        )

    def to_dict(self) -> dict:
        return {
            "Id": self.id,
            "Title": self.title,
            "RelativePosition": self.relative_position,
            "SecretCount": self.secret_count,
            "DifficultyModifier": self.difficulty_modifier,
            "HellKeepWarrensStatus": self.hellkeep_warrens_status,
            "AutomapViewSource": self.automap_view_source,
            "EpisodeId": self.episode_id,
        }


@dataclass(frozen=True)
class Image:
    id: int
    source: str
    difficulty_level: int
    x: int
    y: int
    map_id: int

    @classmethod
    def from_row(cls, row: dict) -> Self:
        return cls(
            id=row["Id"],
            source=row["Source"],
            difficulty_level=row["DifficultyLevel"],
            x=row["X"],
            y=row["Y"],
            map_id=row["MapId"],
        )

    def to_dict(self) -> dict:
        return {
            "Id": self.id,
            "Source": self.source,
            "DifficultyLevel": self.difficulty_level,
            "X": self.x,
            "Y": self.y,
            "MapId": self.map_id,
        }
