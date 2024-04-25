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

from riddance.fedora.gnome.options import (
    enhance_all_privacy_settings,
    enhance_distinct_privacy_settings,
    remove_distinct_packages,
    reset_privacy_enhancements,
)
from riddance.utils import error_message, prompt_message


def remove_packages():
    """Remove pre-installed packages."""

    while True:
        package_removal = prompt_message("Remove pre-installed packages? [Y/a/n]:")

        if package_removal == "" or package_removal.startswith("y"):
            remove_distinct_packages()
            break

        if package_removal.startswith("a"):
            remove_distinct_packages(all_packages=True)
            break

        if package_removal.startswith("n"):
            break

        error_message(f"invalid response: '{package_removal}'")


def enhance_privacy():
    """Enhance operating system privacy."""

    while True:
        privacy_enhancement = prompt_message(
            "Enhance operating system privacy? [Y/a/r/n]:"
        )

        if privacy_enhancement == "" or privacy_enhancement.startswith("y"):
            enhance_distinct_privacy_settings()
            break

        if privacy_enhancement.startswith("a"):
            enhance_all_privacy_settings()
            break

        if privacy_enhancement.startswith("r"):
            reset_privacy_enhancements()
            break

        if privacy_enhancement.startswith("n"):
            break

        error_message(f"invalid response: '{privacy_enhancement}'")
