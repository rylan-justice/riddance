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

from riddance.fedora.fl_39_we_gnome.packages import packages
from riddance.fedora.utils import (remove_bash_history, remove_firefox_config,
                                   remove_unneeded_dependencies)
from riddance.utils import error_message, prompt_message


def remove_packages():
    """Prompt the user to remove pre-installed packages."""

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


def enhance_privacy():
    """Prompt the user to enhance operating system privacy."""

    privacy_settings = [
        ["org.gnome.desktop.privacy", "disable-camera", "true"],
        ["org.gnome.desktop.privacy", "disable-microphone", "true"],
        ["org.gnome.desktop.privacy", "hide-identity", "true"],
        ["org.gnome.desktop.privacy", "old-files-age", "0"],
        ["org.gnome.desktop.privacy", "privacy-screen", "true"],
        ["org.gnome.desktop.privacy", "recent-files-max-age", "0"],
        ["org.gnome.desktop.privacy", "remember-app-usage", "false"],
        ["org.gnome.desktop.privacy", "remember-recent-files", "false"],
        ["org.gnome.desktop.privacy", "remove-old-temp-files", "true"],
        ["org.gnome.desktop.privacy", "remove-old-trash-files", "true"],
        ["org.gnome.desktop.privacy", "report-technical-problems", "false"],
        ["org.gnome.desktop.privacy", "send-software-usage-stats", "false"],
        ["org.gnome.desktop.privacy", "show-full-name-in-top-bar", "false"],
        ["org.gnome.desktop.privacy", "usb-protection", "true"],
        ["org.gnome.desktop.privacy", "usb-protection-level", "lockscreen"],
        ["org.gnome.online-accounts", "whitelisted-providers", "['']"],
        ["org.gnome.system.location", "enabled", "false"],
        ["org.gnome.system.location", "max-accuracy-level", "country"],
    ]

    privacy_enhancements = prompt_message(
        "Would you like to enhance operating system privacy? [Y/n]: "
    )

    if privacy_enhancements == "" or privacy_enhancements.startswith("y"):
        for privacy_setting in privacy_settings:
            subprocess.run(["gsettings", "set", *privacy_setting], check=False)
        print("\nEnhanced operating system privacy")

        remove_bash_history()

    elif privacy_enhancements.startswith("n"):
        pass

    else:
        error_message(f"invalid response: {privacy_enhancements}")
        enhance_privacy()
