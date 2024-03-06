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

import platform

from riddance.identifiers import os_info
from riddance.sys.linux import debloat_linux
from riddance.utils import error_message, output_message

sys_name = platform.system()
sys_compatible = {"Linux": False}


def list_os_info():
    """List compatible operating systems and their versions."""

    for sys in ("Linux",):
        print(f"{sys}:")

        for os_name, os_version in os_info[sys].items():
            os_versions = ", ".join(os_version)
            print(f"  {os_name} {os_versions}")


def check_linux_compatibility():
    """Check Linux distribution and version compatibility."""

    try:
        distro_info = platform.freedesktop_os_release()
        distro_name, distro_version = distro_info["NAME"], distro_info["VERSION"]

        if (
            distro_name not in os_info[sys_name]
            and distro_version not in os_info[sys_name][distro_name]
        ):
            error_message(
                f"incompatible: {distro_name} {distro_version}", newline=False
            )
            return

        sys_compatible[sys_name] = True
        output_message(f"compatible: {distro_name} {distro_version}", newline=False)

    except (OSError, KeyError):
        error_message("incompatible: Linux distribution", newline=False)


def check_compatibility():
    """Check operating system and version compatibility."""

    if sys_name == "Linux":
        check_linux_compatibility()

    else:
        error_message(f"incompatible: {sys_name} {platform.release()}", newline=False)


def debloat_os():
    """Debloat a compatible operating system."""

    check_compatibility()

    if sys_compatible["Linux"]:
        debloat_linux()
