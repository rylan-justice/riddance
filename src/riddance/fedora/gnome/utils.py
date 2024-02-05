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
import platform
import shutil
import subprocess
import sys

from riddance.fedora.gnome.fl_38_we.packages import packages as packages_fl_38_we
from riddance.fedora.gnome.fl_39_we.packages import packages as packages_fl_39_we
from riddance.fedora.gnome.privacy import privacy_descriptions, privacy_settings
from riddance.utils import error_message, prompt_message

username = getpass.getuser()

if platform.system() == "Linux":
    distro_version = platform.freedesktop_os_release()["VERSION"]

    if distro_version == "38 (Workstation Edition)":
        packages = packages_fl_38_we

    elif distro_version == "39 (Workstation Edition)":
        packages = packages_fl_39_we


def delete_firefox_config():
    """Delete Firefox configuration."""

    shutil.rmtree(f"/home/{username}/.mozilla", ignore_errors=True)


def remove_unneeded_dependencies():
    """Remove unneeded package dependencies."""

    subprocess.run(["sudo", "dnf", "-yq", "autoremove"], check=False)
    print("\nRemoved unneeded package dependencies")


def remove_packages():
    """Remove pre-installed packages."""

    package_removal = prompt_message(
        "Would you like to remove pre-installed packages? [Y/a/n]:"
    )

    if package_removal == "" or package_removal.startswith("y"):
        removed_firefox = False
        removed_package = False

        for package, name in packages.items():
            distinct_package = prompt_message(
                f"Would you like to remove {name}? [y/N]:"
            )

            if distinct_package.startswith("y"):
                subprocess.run(["sudo", "dnf", "-yq", "remove", package], check=False)

                if name == "Firefox":
                    removed_firefox = True

                removed_package = True

        if removed_firefox:
            delete_firefox_config()

        if removed_package:
            remove_unneeded_dependencies()

    elif package_removal.startswith("a"):
        for package, name in packages.items():
            subprocess.run(["sudo", "dnf", "-yq", "remove", package], check=False)

        delete_firefox_config()

        remove_unneeded_dependencies()

    elif package_removal.startswith("n"):
        pass

    else:
        error_message(f"invalid response: '{package_removal}'")
        remove_packages()


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

            distinct_privacy_setting = prompt_message(
                f"Would you like to {privacy_description}? [Y/n]:"
            )

            if distinct_privacy_setting == "" or distinct_privacy_setting.startswith(
                "y"
            ):
                subprocess.run(["gsettings", "set", *privacy_setting], check=False)

        bash_history_removal = prompt_message(
            "Would you like to shred Bash history? [y/N]:"
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
    """Reboot operating system."""

    reboot = prompt_message("Would you like to reboot the operating system? [Y/n]:")

    if reboot == "" or reboot.startswith("y"):
        subprocess.run(["reboot"], check=False)

    elif reboot.startswith("n"):
        sys.exit()

    else:
        error_message(f"invalid response: '{reboot}'")
        reboot_os()
