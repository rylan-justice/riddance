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

from riddance.sys.os.fedora import (debloat_fl_38_we_gnome,
                                    debloat_fl_39_we_gnome)
from riddance.utils import error_message


def debloat_linux():
    """Debloat a compatible Linux distribution."""

    distro_version = platform.freedesktop_os_release()["VERSION"]
    desktop_environment = os.environ.get("XDG_CURRENT_DESKTOP")

    if desktop_environment is None:
        error_message("riddance requires the use of 'sudo -E' to run this command")

    # Fedora Linux 38 (Workstation Edition) (GNOME)
    if distro_version == "38 (Workstation Edition)" and desktop_environment == "GNOME":
        debloat_fl_38_we_gnome()

    # Fedora Linux 39 (Workstation Edition) (GNOME)
    elif (
        distro_version == "39 (Workstation Edition)" and desktop_environment == "GNOME"
    ):
        debloat_fl_39_we_gnome()

    else:
        if desktop_environment is not None:
            error_message(f"riddance is incompatible with {desktop_environment}")
