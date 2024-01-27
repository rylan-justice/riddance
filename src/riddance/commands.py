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

import platform

from riddance.identifiers import os_info
from riddance.sys.linux import debloat_linux
from riddance.utils import error_message

sys_compatible = {"Linux": False}


def list_os_info():
    """List compatible operating systems and their versions."""

    for sys in ["Linux"]:
        print(f"{sys}:")

        for os_name, os_version in os_info[sys].items():
            os_versions = ", ".join(os_version)
            print(f"\n    {os_name} {os_versions}")


def check_compatibility():
    """Check operating system and version compatibility."""

    sys_name = platform.system()
    sys_version = platform.release()

    if sys_name == "" or sys_version == "":
        error_message(
            "riddance is incompatible with your operating system", newline=False
        )

    if sys_name == "Linux":
        try:
            distro_info = platform.freedesktop_os_release()

            distro_name = distro_info["NAME"]
            distro_version = distro_info["VERSION"]

            if (
                distro_name in os_info["Linux"]
                and distro_version in os_info["Linux"][distro_name]
            ):
                sys_compatible[sys_name] = True
                print(f"riddance is compatible with {distro_name} {distro_version}")

            else:
                error_message(
                    f"riddance is incompatible with {distro_name} {distro_version}",
                    newline=False,
                )

        except (OSError, KeyError):
            error_message(
                "riddance is incompatible with your Linux distribution", newline=False
            )

    else:
        error_message(
            f"riddance is incompatible with {sys_name} {sys_version}",
            newline=False,
        )


def debloat_os():
    """Debloat a compatible operating system."""

    check_compatibility()

    if sys_compatible["Linux"]:
        debloat_linux()
