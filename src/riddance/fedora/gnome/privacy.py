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

"""Privacy settings and descriptions for Fedora Linux (Workstation Edition) with GNOME."""

privacy_schemas = [
    "org.gnome.desktop.privacy",
    "org.gnome.online-accounts",
    "org.gnome.system.location",
]

privacy_settings = [
    [privacy_schemas[0], "disable-camera", "true"],
    [privacy_schemas[0], "disable-microphone", "true"],
    [privacy_schemas[0], "disable-sound-output", "true"],
    [privacy_schemas[0], "old-files-age", "0"],
    [privacy_schemas[0], "recent-files-max-age", "0"],
    [privacy_schemas[0], "remember-app-usage", "false"],
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
    "disable-sound-output": "disable sound output",
    "enabled": "disable location services",
    "old-files-age": "automatically delete trash and temporary files",  # TODO: (0 = 1 hour minimum) automatically delete period
    "recent-files-max-age": "discard recently used files",  # XXX:
    "remember-app-usage": "disable application usage monitoring and recording",  # XXX:
    "remember-recent-files": "disable recently used files",  # XXX:
    "remove-old-temp-files": "automatically remove temporary files",  # XXX:
    "remove-old-trash-files": "automatically remove trash files",  # XXX:
    "report-technical-problems": "disable automatic problem reporting",  # XXX:
    "whitelisted-providers": "disable online accounts",
}
