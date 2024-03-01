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

"""Options module for Fedora Linux (Workstation Edition) with GNOME."""

from riddance.fedora.privacy import (
    privacy_descriptions,
    privacy_schemas,
    privacy_settings,
)
from riddance.fedora.utils import (
    delete_firefox_configuration,
    disable_file_history_duration,
    get_package_version,
    remove_unneeded_dependencies,
    run_subprocess,
    set_automatic_deletion_period,
    shred_bash_history,
)
from riddance.utils import output_message, prompt_message

packages = get_package_version()


def remove_distinct_packages():
    """Remove distinct packages."""

    removed_package = set()

    for package, description in packages.items():
        if prompt_message(f"Remove {description}? [y/N]:").startswith("y"):
            run_subprocess(["sudo", "dnf", "-yq", "remove", package])
            removed_package.add(description)

    if "Firefox" in removed_package:
        delete_firefox_configuration()

    if removed_package:
        remove_unneeded_dependencies()


def remove_all_packages():
    """Remove all packages."""

    for package in packages:
        run_subprocess(["sudo", "dnf", "-yq", "remove", package])

    delete_firefox_configuration()
    remove_unneeded_dependencies()


def enhance_distinct_privacy_settings():
    """Enhance distinct privacy settings."""

    unification = {
        "remember-recent-files": disable_file_history_duration,
        "remove-old-temp-files": set_automatic_deletion_period,
        "remove-old-trash-files": set_automatic_deletion_period,
    }

    for privacy_setting in privacy_settings:
        privacy_description = privacy_descriptions[privacy_setting[1]]
        distinct_privacy_setting = prompt_message(f"{privacy_description}? [Y/n]:")

        if distinct_privacy_setting == "" or distinct_privacy_setting.startswith("y"):
            run_subprocess(["gsettings", "set", *privacy_setting])
            output_message(f"operative: {privacy_description}")

            if privacy_setting[1] in unification:
                unification[privacy_setting[1]]()

    if prompt_message("Shred Bash history? [y/N]:").startswith("y"):
        shred_bash_history()


def enhance_all_privacy_settings():
    """Enhance all privacy settings."""

    for privacy_setting in privacy_settings:
        run_subprocess(["gsettings", "set", *privacy_setting])
        privacy_description = privacy_descriptions[privacy_setting[1]]
        output_message(f"operative: {privacy_description}")

    disable_file_history_duration()
    set_automatic_deletion_period()
    shred_bash_history()


def reset_privacy_enhancements():
    """Reset privacy enhancements."""

    for privacy_schema in privacy_schemas:
        run_subprocess(["gsettings", "reset-recursively", privacy_schema])

    output_message("Reset privacy enhancements")
