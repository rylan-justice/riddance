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

from riddance.sys.os.distro.fedora.fl_38_we_gnome.utils import \
    enhance_privacy as enhance_privacy_fl_38_we_gnome
from riddance.sys.os.distro.fedora.fl_38_we_gnome.utils import \
    remove_packages as remove_packages_fl_38_we_gnome
from riddance.sys.os.distro.fedora.fl_39_we_gnome.utils import \
    enhance_privacy as enhance_privacy_fl_39_we_gnome
from riddance.sys.os.distro.fedora.fl_39_we_gnome.utils import \
    remove_packages as remove_packages_fl_39_we_gnome
from riddance.sys.os.distro.utils import reboot_os
from riddance.utils import error_message, prompt_message


def debloat_fl_38_we_gnome():
    """Debloat Fedora Linux 38 (Workstation Edition) (GNOME)."""

    while True:
        debloat_os = prompt_message(
            "Would you like to proceed with debloating "
            "Fedora Linux 38 (Workstation Edition)? [Y/n]: "
        )

        if debloat_os == "" or debloat_os.startswith("y"):
            remove_packages_fl_38_we_gnome()
            enhance_privacy_fl_38_we_gnome()
            reboot_os()
            break

        elif debloat_os.startswith("n"):
            print("\nTerminated the debloating process")
            break

        else:
            error_message(f"invalid response: {debloat_os}")


def debloat_fl_39_we_gnome():
    """Debloat Fedora Linux 39 (Workstation Edition) (GNOME)."""

    while True:
        debloat_os = prompt_message(
            "Would you like to proceed with debloating "
            "Fedora Linux 39 (Workstation Edition)? [Y/n]: "
        )

        if debloat_os == "" or debloat_os.startswith("y"):
            remove_packages_fl_39_we_gnome()
            enhance_privacy_fl_39_we_gnome()
            reboot_os()
            break

        elif debloat_os.startswith("n"):
            print("\nTerminated the debloating process")
            break

        else:
            error_message(f"invalid response: {debloat_os}")
