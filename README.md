# DoomMapGuessr Image Library (v3.0.0)
Image library for DoomMapGuessr v3.0.0. Does not contain the actual database.

## Contents
Contains screenshots used in the game [DoomMapGuessr (v3.0.0+)](https://github.com/mf366-dev/DoomMapGuessr), by [Matthew](https://github.com/mf366-dev).

Screenshots are organized by:
* Game
* Episode
* Map

It is recommended to take a look at the DoomMapGuessr screenshot database to better understand the organization of the image library.

## Contibutions
Anyone is welcome to contribute to this image library, however certain rules must be followed.

**Setup**
1. Fork this repository.
2. Open your source port (preferably DSDA-Doom or GZDoom) with the WAD you want to screenshot.
3. Select the episode and map.
4. Move to the place you wish to take a screenshot of.
5. **(Not applicable to DOOM 64)** Before screenshotting, register the position somewhere you'll remember (use cheat **`idmypos`**). It is up to the individual screenshotting to decide whether they wish to play with no monsters or with monsters *(no monsters is recommended for most cases)*. **Note:** you must use a source port that displays the Z coordinate (e.g.: GZDoom).
6. **(Not applicable to DOOM 64)** Upon registering the position (X, Y and Z - angle is not necessary), remove all clutter from the screen (in GZDoom, this means setting screen size to the maximum value in order to remove all HUD) and take the actual screenshot.
7. **(Small note - not applicable to DOOM 64)** Some source ports (like GZDoom) sometimes display `-0` as a coordinate. Consider it to be `0`.
8. **(Not applicable to DOOM 64)** Rename the screenshot to match the following convention: `<x value>_<y value>_<z value>_TO-BE-RANKED.<format>` (example: `-551_35_0_TO-BE-RANKED.png`). Only JPG/PNG are accepted, preferably with ratio 16:9, although 1:1 is equally acccepted.
9. **(Applicable to DOOM 64 ONLY)** Rename the screenshot to match the following convention: `DOOM64_MAP<map number>_<screenshot index padded to len 3>_TO-BE-RANKED.<format>` (example: `DOOM64_MAP03_006_TO-BE-RANKED.jpg`). Only JPG/PNG are accepted, preferably with ratio 16:9, although 1:1 is equally acccepted. Screenshot index starts at 0.
10. **DO NOT MAKE CHANGES TO THE DATABASE!** Changes to the official database are forbidden. Your Pull Request may add 10000 screenshots for all I care - if it has DB changes, it's getting rejected.

**Note (not applicable to DOOM 64)**
The image library does not care about the coordinates - only DoomMapGuessr does. That's why screenshots that have been accepted, ranked, evaluated and added to the database by Matthew will have their names changed to something simpler, for simplification purposes.

**Actual Contribution**
1. Place the screenshot(s) in their correct folders, respecting the `Game -> Episode -> Map` structure.
2. Edit the `TODO.md` file, but **DON'T** mark the maps you screenshotted as complete - simply add a note next to them saying `TO BE EVALUATED AND RANKED`.
3. Create a Pull Request.

**Thank you for contributing!** :heart:
