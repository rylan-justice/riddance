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

sys_compatible = {"Linux": False}


def list_os_info():
    """List compatible operating systems and their versions."""

    for sys in ("Linux",):
        print(f"{sys}:")

        for os_name, os_version in os_info[sys].items():
            os_versions = ", ".join(os_version)
            print(f"  {os_name} {os_versions}")


def get_sys_info():
    """."""

    return platform.system(), platform.release()


def get_distro_info():
    """."""

    distro_info = platform.freedesktop_os_release()

    return distro_info.get("NAME"), distro_info.get("VERSION")


def check_compatibility():
    """Check operating system and version compatibility."""

    sys_name, sys_version = get_sys_info()

    if sys_name == "Linux":
        try:
            distro_name, distro_version = get_distro_info()

            if (
                distro_name in os_info[sys_name]
                and distro_version in os_info[sys_name][distro_name]
            ):
                sys_compatible[sys_name] = True
                output_message(
                    f"compatible: {distro_name} {distro_version}", newline=False
                )

            else:
                error_message(
                    f"incompatible: {distro_name} {distro_version}", newline=False
                )

        except OSError:
            error_message("incompatible: Linux distribution", newline=False)

    else:
        error_message(f"incompatible: {sys_name} {sys_version}", newline=False)


def debloat_os():
    """Debloat a compatible operating system."""

    check_compatibility()

    if sys_compatible["Linux"]:
        debloat_linux()
