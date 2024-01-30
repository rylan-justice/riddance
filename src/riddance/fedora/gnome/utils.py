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

"""Utilities for Fedora Linux (Workstation Edition) (GNOME)."""

import getpass
import os
import shutil
import subprocess
import sys

from riddance.utils import error_message, prompt_message

username = getpass.getuser()


def delete_firefox_config():
    """Delete Firefox configuration."""

    shutil.rmtree(f"/home/{username}/.mozilla", ignore_errors=True)


def remove_unneeded_dependencies():
    """Remove unneeded package dependencies."""

    subprocess.run(["sudo", "dnf", "--assumeyes", "--quiet", "autoremove"], check=False)
    print("\nRemoved unneeded package dependencies")


def delete_bash_history():
    """Delete Bash history."""

    bash_history = f"/home/{username}/.bash_history"

    if os.path.exists(bash_history):
        os.remove(bash_history)
        print("\nDeleted Bash history")


def reboot_os():
    """Prompt the user to reboot the operating system."""

    reboot = prompt_message("Would you like to reboot the operating system? [Y/n]: ")

    if reboot == "" or reboot.startswith("y"):
        subprocess.run(["reboot"], check=False)

    elif reboot.startswith("n"):
        sys.exit(0)

    else:
        error_message(f"Invalid response '{reboot}'")
        reboot_os()
