# DoomMapGuessr Image Library (v3.0.0)
Image library for DoomMapGuessr v3.0.0. Does not contain the actual database.

## Contents
Contains screenshots used in the game [DoomMapGuessr (v3.0.0+)](https://github.com/MF366-Coding/DoomMapGuessr), by [Matthew](https://github.com/MF366-Coding).

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
5. Before screenshotting, register the position somewhere you'll remember (use cheat **`idmypos`**). It is up to the individual screenshotting to decide whether they wish to play with no monsters or with monsters. **Note:** you must not use a source port that doesn't display the Z coordinate.
6. Upon registering the position (X, Y and Z - angle is not necessary), remove all clutter from the screen (in GZDoom, this means setting screen size to the maximum value in order to remove all HUD) and take the actual screenshot.
7. Rename the screenshot to match the following convention: `<x_value>_Y<y_value>_Z<z_value>_TO-BE-RANKED.<format>` (example: `-551_35_0.png`). Only JPG/PNG are accepted, preferably with ratio 16:9, although 1:1 is equally acccepted.

**Actual Contribution**
1. Place the screenshot(s) in their correct folders, respecting the `Game -> Episode -> Map` structure.
2. Edit the `TODO.md` file, but **DON'T** mark the maps you screenshotted as complete - simply add a note next to them saying `TO BE EVALUATED AND RANKED`.
3. Create a Pull Request.

**Thank you for contributing!** :heart:
