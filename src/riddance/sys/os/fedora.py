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

import os
import platform

from riddance.sys.os.fl38we_gnome.utils import reboot_os as reboot_os_fl38we
from riddance.sys.os.fl38we_gnome.utils import \
    remove_packages as remove_packages_fl38we
from riddance.sys.os.fl39we_gnome.utils import reboot_os as reboot_os_fl39we
from riddance.sys.os.fl39we_gnome.utils import \
    remove_packages as remove_packages_fl39we
from riddance.utils import error_message, prompt_message

if platform.system() == "Linux":
    user_id = os.geteuid()


def debloat_fl38we_gnome():
    """Debloat Fedora Linux 38 (Workstation Edition) (GNOME)."""

    if user_id == 0:
        while True:
            debloat_os = prompt_message(
                "Would you like to proceed with debloating "
                "Fedora Linux 38 (Workstation Edition)? [Y/n]: "
            )

            if debloat_os == "" or debloat_os.startswith("y"):
                remove_packages_fl38we()
                reboot_os_fl38we()
                break

            elif debloat_os.startswith("n"):
                print("\nTerminated the debloating process")
                break

            else:
                error_message(f"invalid response: {debloat_os}")

    else:
        error_message("riddance requires elevated privileges to run this command")


def debloat_fl39we_gnome():
    """Debloat Fedora Linux 39 (Workstation Edition) (GNOME)."""

    if user_id == 0:
        while True:
            debloat_os = prompt_message(
                "Would you like to proceed with debloating "
                "Fedora Linux 39 (Workstation Edition)? [Y/n]: "
            )

            if debloat_os == "" or debloat_os.startswith("y"):
                remove_packages_fl39we()
                reboot_os_fl39we()
                break

            elif debloat_os.startswith("n"):
                print("\nTerminated the debloating process")
                break

            else:
                error_message(f"invalid response: {debloat_os}")

    else:
        error_message("riddance requires elevated privileges to run this command")
