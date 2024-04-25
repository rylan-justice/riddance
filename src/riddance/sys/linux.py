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

from riddance.os.fedora import fedora_linux_we_gnome
from riddance.utils import error_message


def debloat_fedora_linux(desktop_environment):
    """Debloat Fedora Linux."""

    desktop_environments = {
        "GNOME": fedora_linux_we_gnome,
    }

    if desktop_environment not in desktop_environments:
        error_message(f"incompatible: {desktop_environment}")
        return

    desktop_environments[desktop_environment]()


def debloat_linux():
    """Debloat a compatible Linux distribution."""

    if os.geteuid() == 0:
        error_message("'-d, --debloat' cannot be run as root")
        return

    try:
        desktop_environment = os.environ["XDG_CURRENT_DESKTOP"]

    except KeyError:
        error_message("incompatible: desktop environment")
        return

    debloat_fedora_linux(desktop_environment)
