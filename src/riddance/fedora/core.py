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

from riddance.fedora.options import (
    enhance_privacy_all_option,
    enhance_privacy_reset_option,
    enhance_privacy_yes_option,
    remove_packages_all_option,
    remove_packages_yes_option,
)
from riddance.utils import error_message, prompt_message


def remove_packages_fedora_linux_we_gnome():
    """Remove pre-installed packages from Fedora Linux (Workstation Edition)
    with GNOME."""

    while True:
        package_removal = prompt_message("Remove pre-installed packages? [Y/a/n]:")

        if package_removal == "" or package_removal.startswith("y"):
            remove_packages_yes_option()
            break

        if package_removal.startswith("a"):
            remove_packages_all_option()
            break

        if package_removal.startswith("n"):
            break

        error_message(f"invalid response: '{package_removal}'")


def enhance_privacy_fedora_linux_we_gnome():
    """Enhance operating system privacy for Fedora Linux (Workstation Edition)
    with GNOME."""

    while True:
        privacy_enhancement = prompt_message(
            "Enhance operating system privacy? [Y/a/r/n]:"
        )

        if privacy_enhancement == "" or privacy_enhancement.startswith("y"):
            enhance_privacy_yes_option()
            break

        if privacy_enhancement.startswith("a"):
            enhance_privacy_all_option()
            break

        if privacy_enhancement.startswith("r"):
            enhance_privacy_reset_option()
            break

        if privacy_enhancement.startswith("n"):
            break

        error_message(f"invalid response: '{privacy_enhancement}'")
