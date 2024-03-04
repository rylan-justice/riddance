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

"""Utilities for Fedora Linux (Workstation Edition) with GNOME."""

import platform
import shutil
import subprocess
from pathlib import Path

from riddance.fedora.packages import packages_38_we, packages_39_we
from riddance.fedora.privacy import privacy_schemas
from riddance.utils import output_message

home_directory = Path.home()


def get_package_version():
    """Get package version."""

    distro_versions = {
        "38 (Workstation Edition)": packages_38_we,
        "39 (Workstation Edition)": packages_39_we,
    }

    distro_version = platform.freedesktop_os_release()["VERSION"]
    return distro_versions[distro_version]


def run_subprocess(command):
    subprocess.run(command, check=False)


def delete_firefox_configuration():
    """Delete Firefox configuration."""

    shutil.rmtree(home_directory / ".mozilla", ignore_errors=True)


def remove_unneeded_dependencies():
    """Remove unneeded package dependencies."""

    run_subprocess(["sudo", "dnf", "-yq", "autoremove"])
    output_message("Removed unneeded package dependencies")


def disable_file_history_duration():
    """Disable file history duration."""

    run_subprocess(
        ["gsettings", "set", privacy_schemas[0], "recent-files-max-age", "0"]
    )


def set_automatic_deletion_period():
    """Set automatic deletion period for temporary files and trash content
    to one hour."""

    run_subprocess(["gsettings", "set", privacy_schemas[0], "old-files-age", "0"])


def shred_bash_history():
    """Shred Bash history."""

    bash_history = home_directory / ".bash_history"

    if bash_history.exists():
        run_subprocess(["shred", "-zu", bash_history])
        output_message("Shredded Bash history")
