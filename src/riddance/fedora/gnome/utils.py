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

"""Utilities for Fedora Linux Workstation Edition with GNOME."""

import getpass
import os
import platform
import shutil
import subprocess

from riddance.fedora.gnome.packages import packages_38_we, packages_39_we
from riddance.fedora.gnome.privacy import privacy_schemas
from riddance.utils import output_message

username = getpass.getuser()


def get_package_version():
    """Get package version for Fedora Linux Workstation Edition with GNOME."""

    distro_version = platform.freedesktop_os_release()["VERSION"]

    if distro_version == "38 (Workstation Edition)":
        return packages_38_we

    if distro_version == "39 (Workstation Edition)":
        return packages_39_we

    return None


def delete_firefox_configuration():
    """Delete Firefox configuration."""

    shutil.rmtree(f"/home/{username}/.mozilla", ignore_errors=True)


def remove_unneeded_dependencies():
    """Remove unneeded package dependencies."""

    subprocess.run(["sudo", "dnf", "-yq", "autoremove"], check=False)
    output_message("Removed unneeded package dependencies")


def disable_file_history_duration():
    """Disable file history duration."""

    subprocess.run(
        ["gsettings", "set", privacy_schemas[0], "recent-files-max-age", "0"],
        check=False,
    )


def set_automatic_deletion_period():
    """Set automatic deletion period for temporary files and trash content to one hour."""

    subprocess.run(
        ["gsettings", "set", privacy_schemas[0], "old-files-age", "0"],
        check=False,
    )


def shred_bash_history():
    """Shred Bash history."""

    bash_history = f"/home/{username}/.bash_history"

    if os.path.exists(bash_history):
        subprocess.run(["shred", "-zu", bash_history], check=False)
        output_message("Shred Bash history")
