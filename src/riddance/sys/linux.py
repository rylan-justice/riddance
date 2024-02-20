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

import os
import platform

from riddance.identifiers import os_info
from riddance.os.fedora import debloat_fl_we_gnome
from riddance.utils import error_message


def debloat_fedora_linux(distro_version, desktop_environment):
    """Debloat Fedora Linux."""

    if (
        distro_version in os_info["Linux"]["Fedora Linux"]
        and desktop_environment == "GNOME"
    ):
        debloat_fl_we_gnome()

    else:
        error_message(
            f"incompatible: Fedora Linux {distro_version} with {desktop_environment}"
        )


def debloat_linux():
    """Debloat a compatible Linux distribution."""

    if os.geteuid() != 0:
        try:
            distro_version = platform.freedesktop_os_release()["VERSION"]
            desktop_environment = os.environ["XDG_CURRENT_DESKTOP"]

            debloat_fedora_linux(distro_version, desktop_environment)

        except (OSError, KeyError):
            error_message("incompatible: desktop environment")

    else:
        error_message("'-d, --debloat' cannot be run as root")
