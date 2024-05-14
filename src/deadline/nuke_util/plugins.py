from __future__ import annotations

import nuke
import os
from os.path import dirname
from sys import platform

def get_custom_plugin_paths() -> list[str]:
    """Returns the directories containing plugins for nuke"""
    plugin_dirs = nuke.pluginPath()

    # if the filename is in the install dir, ignore it.
    # Windows / Linux
    install_path = dirname(nuke.EXE_PATH)
    if platform.startswith("darwin"):
        # EXE_PATH: /Applications/Nuke15.0v2/Nuke15.0v2.app/Contents/MacOS/Nuke15.0
        # INSTALL_PATH: /Applications/Nuke15.0v2/Nuke15.0v2.app
        install_path = dirname(dirname(dirname(nuke.EXE_PATH)))

    return [path.replace("\\","/") for path in plugin_dirs if install_path not in path]

def set_custom_plugin_paths(plugin_paths: list[str]) -> None:
    """Set the knob on the root settings to update the OCIO config"""
    for path in plugin_paths:
        nuke.pluginAddPath(path)