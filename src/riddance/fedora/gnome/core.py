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

import sys

from riddance.fedora.gnome.options import (
    enhance_privacy_all_option,
    enhance_privacy_reset_option,
    enhance_privacy_yes_option,
    remove_packages_all_option,
    remove_packages_yes_option,
)
from riddance.utils import error_message, prompt_message


def remove_packages():
    """Remove pre-installed packages."""

    package_removal = prompt_message(
        "Would you like to remove pre-installed packages? [Y/a/n]:"
    )

    if package_removal == "" or package_removal.startswith("y"):
        remove_packages_yes_option()

    elif package_removal.startswith("a"):
        remove_packages_all_option()

    elif package_removal.startswith("n"):
        enhance_privacy()

    else:
        error_message(f"invalid response: '{package_removal}'")
        remove_packages()


def enhance_privacy():
    """Enhance operating system privacy."""

    privacy_enhancement = prompt_message(
        "Would you like to enhance operating system privacy? [Y/a/r/n]:"
    )

    if privacy_enhancement == "" or privacy_enhancement.startswith("y"):
        enhance_privacy_yes_option()

    elif privacy_enhancement.startswith("a"):
        enhance_privacy_all_option()

    elif privacy_enhancement.startswith("r"):
        enhance_privacy_reset_option()

    elif privacy_enhancement.startswith("n"):
        sys.exit()

    else:
        error_message(f"invalid response: '{privacy_enhancement}'")
        enhance_privacy()
