# SPDX-License-Identifier: GPL-3.0-or-later
#
# riddance: A tool designed to remove bloatware and restore freedom
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

"""Privacy settings and descriptions for Fedora Linux (Workstation Edition) (GNOME)."""

privacy_settings = [
    ["org.gnome.desktop.privacy", "disable-camera", "true"],
    ["org.gnome.desktop.privacy", "disable-microphone", "true"],
    ["org.gnome.desktop.privacy", "disable-sound-output", "true"],
    ["org.gnome.desktop.privacy", "hide-identity", "true"],
    ["org.gnome.desktop.privacy", "old-files-age", "0"],
    ["org.gnome.desktop.privacy", "privacy-screen", "true"],
    ["org.gnome.desktop.privacy", "recent-files-max-age", "0"],
    ["org.gnome.desktop.privacy", "remember-app-usage", "false"],
    ["org.gnome.desktop.privacy", "remember-recent-files", "false"],
    ["org.gnome.desktop.privacy", "remove-old-temp-files", "true"],
    ["org.gnome.desktop.privacy", "remove-old-trash-files", "true"],
    ["org.gnome.desktop.privacy", "report-technical-problems", "false"],
    ["org.gnome.desktop.privacy", "send-software-usage-stats", "false"],
    ["org.gnome.desktop.privacy", "show-full-name-in-top-bar", "false"],
    ["org.gnome.desktop.privacy", "usb-protection", "true"],
    ["org.gnome.desktop.privacy", "usb-protection-level", "lockscreen"],
    ["org.gnome.online-accounts", "whitelisted-providers", "['']"],
    ["org.gnome.system.location", "enabled", "false"],
    ["org.gnome.system.location", "max-accuracy-level", "country"],
]

privacy_setting_descriptions = {
    "disable-camera": [
        "forbid apps from accessing the camera",
        "Forbid apps from accessing the camera",
    ],
    "disable-microphone": [
        "forbid apps from accessing the microphone",
        "Forbid apps from accessing the microphone",
    ],
    "disable-sound-output": [
        "forbid apps from outputting sound",
        "Forbid apps from outputting sound",
    ],
    "enabled": [
        "disable geolocation services",
        "Disabled geolocation services",
    ],
    "hide-identity": [
        "hide personal information",
        "Hid personal information",
    ],
    "max-accuracy-level": ["", ""],
    "old-files-age": ["", ""],
    "privacy-screen": ["", ""],
    "recent-files-max-age": ["", ""],
    "remember-app-usage": ["", ""],
    "remember-recent-files": ["", ""],
    "remove-old-temp-files": ["", ""],
    "remove-old-trash-files": ["", ""],
    "report-technical-problems": ["", ""],
    "send-software-usage-stats": ["", ""],
    "show-full-name-in-top-bar": ["", ""],
    "usb-protection": ["", ""],
    "usb-protection-level": ["", ""],
    "whitelisted-providers": ["", ""],
}
