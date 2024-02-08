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

"""Core module for Fedora Linux (Workstation Edition) with GNOME."""

import platform
import subprocess
import sys

from riddance.fedora.gnome.packages import packages_38_we, packages_39_we
from riddance.fedora.gnome.privacy import (
    privacy_descriptions,
    privacy_schemas,
    privacy_settings,
)
from riddance.fedora.gnome.utils import (
    delete_firefox_config,
    remove_unneeded_dependencies,
    shred_bash_history,
)
from riddance.utils import error_message, output_message, prompt_message


def remove_packages():
    """Remove pre-installed packages."""

    package_removal = prompt_message(
        "Would you like to remove pre-installed packages? [Y/a/n]:"
    )

    if package_removal == "" or package_removal.startswith("y"):
        distro_version = platform.freedesktop_os_release()["VERSION"]

        if distro_version == "38 (Workstation Edition)":
            packages = packages_38_we

        elif distro_version == "39 (Workstation Edition)":
            packages = packages_39_we

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


def enhance_privacy():
    """Enhance operating system privacy."""

    privacy_enhancement = prompt_message(
        "Would you like to enhance operating system privacy? [Y/a/r/n]:"
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

                if privacy_setting[1] == "remember-recent-files":
                    subprocess.run(
                        [
                            "gsettings",
                            "set",
                            privacy_schemas[0],
                            "recent-files-max-age",
                            "0",
                        ],
                        check=False,
                    )

                if privacy_setting[1] in [
                    "remove-old-temp-files",
                    "remove-old-trash-files",
                ]:
                    subprocess.run(
                        ["gsettings", "set", privacy_schemas[0], "old-files-age", "0"],
                        check=False,
                    )

        bash_history_shredding = prompt_message(
            "Would you like to shred Bash history? [y/N]:"
        )

        if bash_history_shredding.startswith("y"):
            shred_bash_history()

    elif privacy_enhancement.startswith("a"):
        for privacy_setting in privacy_settings:
            subprocess.run(["gsettings", "set", *privacy_setting], check=False)

            privacy_description = privacy_descriptions[privacy_setting[1]]
            output_message(f"{privacy_description.capitalize()}")

        privacy_setting_extras = [
            "recent-files-max-age",
            "old-files-age",
        ]

        for privacy_settings_extra in privacy_setting_extras:
            subprocess.run(
                ["gsettings", "set", privacy_schemas[0], privacy_settings_extra, "0"],
                check=False,
            )

        shred_bash_history()

    elif privacy_enhancement.startswith("r"):
        for privacy_schema in privacy_schemas:
            subprocess.run(
                ["gsettings", "reset-recursively", privacy_schema], check=False
            )

        output_message("Reset privacy enhancements")

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
