# SPDX-License-Identifier: GPL-3.0-or-later
#
# riddance: Designed to remove bloatware and augment freedom
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

"""Primary utilities for Fedora Linux 39 (Workstation Edition) with GNOME."""

import subprocess

from riddance.fedora.gnome.fl_39_we.packages import packages
from riddance.fedora.gnome.privacy import descriptions, settings
from riddance.fedora.gnome.utils import (
    delete_bash_history,
    delete_firefox_config,
    remove_unneeded_dependencies,
)
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
                print(f"Removed {name}")

                if name == "Firefox":
                    removed_firefox = True

                removed_package = True

        if removed_firefox:
            delete_firefox_config()

        if removed_package:
            remove_unneeded_dependencies()

    elif package_removal.startswith("a"):
        for package, name in packages.items():
            subprocess.run(
                ["sudo", "dnf", "--assumeyes", "--quiet", "remove", package],
                check=False,
            )
            print(f"Removed {name}")

        delete_firefox_config()

        remove_unneeded_dependencies()

    elif package_removal.startswith("n"):
        pass

    else:
        error_message(f"Invalid response '{package_removal}'")
        remove_packages()


def enhance_privacy():
    """Prompt the user to enhance operating system privacy."""

    privacy_enhancement = prompt_message(
        "Would you like to enhance operating system privacy? [Y/a/n]: "
    )

    if privacy_enhancement == "" or privacy_enhancement.startswith("y"):
        for privacy_setting in settings:
            privacy_description = descriptions[privacy_setting[1]][0]

            particular_privacy_setting = prompt_message(
                f"Would you like to {privacy_description}? [Y/n]: "
            )

            if (
                particular_privacy_setting == ""
                or particular_privacy_setting.startswith("y")
            ):
                subprocess.run(["gsettings", "set", *privacy_setting], check=False)

        bash_history_removal = prompt_message(
            "Would you like to remove Bash history? [y/N]: "
        )

        if bash_history_removal.startswith("y"):
            delete_bash_history()

    elif privacy_enhancement.startswith("a"):
        for privacy_setting in settings:
            subprocess.run(["gsettings", "set", *privacy_setting], check=False)

            privacy_description = descriptions[privacy_setting[1]][1]
            print(f"\n{privacy_description}")

        delete_bash_history()

    elif privacy_enhancement.startswith("n"):
        pass

    else:
        error_message(f"Invalid response '{privacy_enhancement}'")
        enhance_privacy()
