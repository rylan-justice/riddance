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

"""Privacy schemas, settings, and descriptions for Fedora Linux Workstation Edition with GNOME."""

privacy_schemas = [
    "org.gnome.desktop.privacy",
    "org.gnome.online-accounts",
    "org.gnome.system.location",
]

privacy_settings = [
    [privacy_schemas[0], "disable-camera", "true"],
    [privacy_schemas[0], "disable-microphone", "true"],
    [privacy_schemas[0], "remember-recent-files", "false"],
    [privacy_schemas[0], "remove-old-temp-files", "true"],
    [privacy_schemas[0], "remove-old-trash-files", "true"],
    [privacy_schemas[0], "report-technical-problems", "false"],
    [privacy_schemas[1], "whitelisted-providers", "[]"],
    [privacy_schemas[2], "enabled", "false"],
]

privacy_descriptions = {
    "disable-camera": "disable camera access",
    "disable-microphone": "disable microphone access",
    "enabled": "disable location services",
    "remember-recent-files": "disable file history",
    "remove-old-temp-files": "automatically delete temporary files",
    "remove-old-trash-files": "automatically delete trash content",
    "report-technical-problems": "disable automatic problem reporting",
    "whitelisted-providers": "disable online accounts",
}
