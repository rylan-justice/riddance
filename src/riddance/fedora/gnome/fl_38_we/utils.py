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

"""Primary utilities for Fedora Linux 38 (Workstation Edition) with GNOME."""

import subprocess

from riddance.fedora.gnome.fl_38_we.packages import packages
from riddance.fedora.gnome.utils import (
    delete_firefox_config,
    remove_unneeded_dependencies,
)
from riddance.utils import error_message, prompt_message


def remove_packages():
    """Remove pre-installed packages."""

    package_removal = prompt_message(
        "Would you like to remove pre-installed packages? [Y/a/n]:"
    )

    if package_removal == "" or package_removal.startswith("y"):
        removed_firefox = False
        removed_package = False

        for package, name in packages.items():
            particular_package = prompt_message(
                f"Would you like to remove {name}? [y/N]:"
            )

            if particular_package.startswith("y"):
                subprocess.run(["sudo", "dnf", "-yq", "remove", package], check=False)

                if name == "Firefox":
                    removed_firefox = True

                removed_package = True

        if removed_firefox:
            delete_firefox_config()

        if removed_package:
            remove_unneeded_dependencies()

    elif package_removal.startswith("a"):
        for package, name in packages.items():
            subprocess.run(["sudo", "dnf", "-yq", "remove", package], check=False)

        delete_firefox_config()

        remove_unneeded_dependencies()

    elif package_removal.startswith("n"):
        pass

    else:
        error_message(f"invalid response: '{package_removal}'")
        remove_packages()
