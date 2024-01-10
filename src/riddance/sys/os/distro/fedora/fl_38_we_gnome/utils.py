# SPDX-License-Identifier: GPL-3.0-or-later
#
# riddance: A tool designed to remove bloatware and restore freedom
# Copyright (C) 2024  Rylan Justice
#
# This file is part of riddance.
#
# riddance is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# riddance is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with riddance.  If not, see <https://www.gnu.org/licenses/>.

import subprocess

from riddance.sys.os.distro.fedora import (remove_firefox_config,
                                           remove_unneeded_dependencies)
from riddance.utils import error_message, prompt_message


def remove_packages():
    """Prompt the user to remove pre-installed packages."""

    packages = {
        "baobab": "Disk Usage Analyzer and Photos",
        "cheese": "Cheese",
        "desktop-backgrounds-gnome": "desktop-backgrounds-gnome",
        "eog": "Image Viewer",
        "evince": "Document Viewer",
        "fedora-bookmarks": "fedora-bookmarks",
        "fedora-chromium-config-gnome": "fedora-chromium-config-gnome",
        "fedora-workstation-backgrounds": "fedora-workstation-backgrounds",
        "gnome-abrt": "Problem Reporting",
        "gnome-backgrounds": "gnome-backgrounds",
        "gnome-boxes": "Boxes",
        "gnome-calculator": "Calculator",
        "gnome-calendar": "Calendar",
        "gnome-characters": "Characters",
        "gnome-clocks": "Clocks",
        "gnome-color-manager": "GNOME Color Manager",
        "gnome-connections": "Connections",
        "gnome-contacts": "Contacts",
        "gnome-disk-utility": "Disks",
        "gnome-font-viewer": "Fonts",
        "gnome-initial-setup": "gnome-initial-setup",
        "gnome-logs": "Logs",
        "gnome-maps": "Maps",
        "gnome-remote-desktop": "gnome-remote-desktop",
        "gnome-shell-extension-background-logo": "gnome-shell-extension-background-logo",
        "gnome-system-monitor": "System Monitor",
        "gnome-terminal": "Terminal",
        "gnome-text-editor": "Text Editor",
        "gnome-themes-extra": "gnome-themes-extra",
        "gnome-tour": "Tour",
        "gnome-user-docs": "gnome-user-docs",
        "gnome-user-share": "gnome-user-share",
        "gnome-weather": "Weather",
        "ibus-anthy": "Anthy",
        "ibus-hangul": "ibus-hangul",
        "ibus-libzhuyin": "Zhuyin",
        "ibus-typing-booster": "Typing Booster",
        "libpinyin": "Pinyin",
        "libreoffice-core": "LibreOffice Calc, LibreOffice Impress, and LibreOffice Writer",
        "m17n-lib": "Ibus M17N",
        "mediawriter": "Fedora Media Writer",
        "mozilla-filesystem": "Firefox",
        "nautilus": "Files",
        "rhythmbox": "Rhythmbox",
        "simple-scan": "Document Scanner",
        "totem": "Videos",
        "yelp": "Help",
    }

    package_removal = prompt_message(
        "Would you like to remove pre-installed packages? [Y/a/n]: "
    )

    if package_removal == "" or package_removal.startswith("y"):
        removed_firefox = False
        removed_package = False

        for package, name in packages.items():
            particular_package = prompt_message(
                f"Would you like to remove {name}? [y/N]: "
            )

            if particular_package.startswith("y"):
                subprocess.run(
                    ["sudo", "dnf", "--assumeyes", "--quiet", "remove", package],
                    check=False,
                )
                print(f"Removed: {name}")

                if name == "Firefox":
                    removed_firefox = True

                removed_package = True

        if removed_firefox:
            remove_firefox_config()

        if removed_package:
            remove_unneeded_dependencies()

    elif package_removal.startswith("a"):
        for package, name in packages.items():
            subprocess.run(
                ["sudo", "dnf", "--assumeyes", "--quiet", "remove", package],
                check=False,
            )
            print(f"Removed: {name}")

        remove_firefox_config()

        remove_unneeded_dependencies()

    elif package_removal.startswith("n"):
        pass

    else:
        error_message(f"invalid response: {package_removal}")
        remove_packages()
