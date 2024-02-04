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

import getpass
import os
import shutil
import subprocess
import sys

from riddance.fedora.gnome.privacy import privacy_descriptions, privacy_settings
from riddance.utils import error_message, prompt_message

username = getpass.getuser()


def delete_firefox_config():
    """Delete Firefox configuration."""

    shutil.rmtree(f"/home/{username}/.mozilla", ignore_errors=True)


def remove_unneeded_dependencies():
    """Remove unneeded package dependencies."""

    subprocess.run(["sudo", "dnf", "-yq", "autoremove"], check=False)
    print("\nRemoved unneeded package dependencies")


def shred_bash_history():
    """Shred Bash history."""

    bash_history = f"/home/{username}/.bash_history"

    if os.path.exists(bash_history):
        subprocess.run(["shred", "-zu", bash_history], check=False)
        print("\nShredded Bash history")


def enhance_privacy():
    """Enhance operating system privacy."""

    privacy_enhancement = prompt_message(
        "Would you like to enhance operating system privacy? [Y/a/n]:"
    )

    if privacy_enhancement == "" or privacy_enhancement.startswith("y"):
        for privacy_setting in privacy_settings:
            privacy_description = privacy_descriptions[privacy_setting[1]]

            particular_privacy_setting = prompt_message(
                f"Would you like to {privacy_description}? [Y/n]:"
            )

            if (
                particular_privacy_setting == ""
                or particular_privacy_setting.startswith("y")
            ):
                subprocess.run(["gsettings", "set", *privacy_setting], check=False)

        bash_history_removal = prompt_message(
            "Would you like to remove Bash history? [y/N]:"
        )

        if bash_history_removal.startswith("y"):
            shred_bash_history()

    elif privacy_enhancement.startswith("a"):
        for privacy_setting in privacy_settings:
            subprocess.run(["gsettings", "set", *privacy_setting], check=False)

            privacy_description = privacy_descriptions[privacy_setting[1]]
            print(f"\n{privacy_description.capitalize()}")

        shred_bash_history()

    elif privacy_enhancement.startswith("n"):
        pass

    else:
        error_message(f"invalid response: '{privacy_enhancement}'")
        enhance_privacy()


def reboot_os():
    """Reboot the operating system."""

    reboot = prompt_message("Would you like to reboot the operating system? [Y/n]:")

    if reboot == "" or reboot.startswith("y"):
        subprocess.run(["reboot"], check=False)

    elif reboot.startswith("n"):
        sys.exit(0)

    else:
        error_message(f"invalid response: '{reboot}'")
        reboot_os()
