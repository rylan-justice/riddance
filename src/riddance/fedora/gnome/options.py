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

import subprocess

from riddance.fedora.gnome.privacy import (
    privacy_descriptions,
    privacy_schemas,
    privacy_settings,
)
from riddance.fedora.gnome.utils import (
    delete_firefox_configuration,
    disable_file_history_duration,
    get_package_version,
    remove_unneeded_dependencies,
    set_automatic_deletion_period,
    shred_bash_history,
)
from riddance.utils import output_message, prompt_message

packages = get_package_version()


def remove_packages_yes_option():
    """'Y'es option for remove_packages()."""

    removed_firefox = False
    removed_package = False

    for package, name in packages.items():
        distinct_package = prompt_message(f"Would you like to remove {name}? [y/N]:")

        if distinct_package.startswith("y"):
            subprocess.run(["sudo", "dnf", "-yq", "remove", package], check=False)

            if name == "Firefox":
                removed_firefox = True

            removed_package = True

    if removed_firefox:
        delete_firefox_configuration()

    if removed_package:
        remove_unneeded_dependencies()


def remove_packages_all_option():
    """'a'll option for remove_packages()."""

    for package in packages:
        subprocess.run(["sudo", "dnf", "-yq", "remove", package], check=False)

    delete_firefox_configuration()

    remove_unneeded_dependencies()


def enhance_privacy_yes_option():
    """'Y'es option for enhance_privacy()."""

    for privacy_setting in privacy_settings:
        privacy_description = privacy_descriptions[privacy_setting[1]]

        distinct_privacy_setting = prompt_message(
            f"Would you like to {privacy_description}? [Y/n]:"
        )

        if distinct_privacy_setting == "" or distinct_privacy_setting.startswith("y"):
            subprocess.run(["gsettings", "set", *privacy_setting], check=False)

            output_message(f"{privacy_description.capitalize()}")

            if privacy_setting[1] == "remember-recent-files":
                disable_file_history_duration()

            if privacy_setting[1] in [
                "remove-old-temp-files",
                "remove-old-trash-files",
            ]:
                set_automatic_deletion_period()

    bash_history_shredding = prompt_message(
        "Would you like to shred Bash history? [y/N]:"
    )

    if bash_history_shredding.startswith("y"):
        shred_bash_history()


def enhance_privacy_all_option():
    """'a'll option for enhance_privacy()."""

    for privacy_setting in privacy_settings:
        subprocess.run(["gsettings", "set", *privacy_setting], check=False)

        privacy_description = privacy_descriptions[privacy_setting[1]]
        output_message(f"{privacy_description.capitalize()}")

    disable_file_history_duration()

    set_automatic_deletion_period()

    shred_bash_history()


def enhance_privacy_reset_option():
    """'r'eset option for enhance_privacy()."""

    for privacy_schema in privacy_schemas:
        subprocess.run(["gsettings", "reset-recursively", privacy_schema], check=False)

    output_message("Reset privacy enhancements")
