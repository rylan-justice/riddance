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
        "Forbade apps from accessing the camera",
    ],
    "disable-microphone": [
        "forbid apps from accessing the microphone",
        "Forbade apps from accessing the microphone",
    ],
    "disable-sound-output": [
        "forbid apps from outputting sound",
        "Forbade apps from outputting sound",
    ],
    "enabled": [
        "disable geolocation services",
        "Disabled geolocation services",
    ],
    "hide-identity": [
        "hide personal information",
        "Hid personal information",
    ],
    "max-accuracy-level": [
        "set geolocation accuracy level to country",
        "Set geolocation accuracy level to country",
    ],
    "old-files-age": [
        "discard trash and temporary files",
        "Discarded trash and temporary files",
    ],
    "privacy-screen": [
        "enable privacy screen",
        "Enabled privacy screen",
    ],
    "recent-files-max-age": [
        "discard recently used files",
        "Discarded recently used files",
    ],
    "remember-app-usage": [
        "discard application usage",
        "Discarded application usage",
    ],
    "remember-recent-files": [
        "discard recently used files",
        "Discared recently used files",
    ],
    "remove-old-temp-files": [
        "discard temporary files",
        "Discarded temporary files",
    ],
    "remove-old-trash-files": [
        "discard trash files",
        "Discarded trash files",
    ],
    "report-technical-problems": [
        "cease technical problem reports",
        "Ceased technical problem reports",
    ],
    "send-software-usage-stats": [
        "cease application statistics telemetry",
        "Ceased application statistics telemetry",
    ],
    "show-full-name-in-top-bar": [
        "hide full name in top bar",
        "Hid full name in top bar",
    ],
    "usb-protection": [
        "protect USB devices",
        "Protected USB devices",
    ],
    "usb-protection-level": [
        "reject USB devices on lockscreen",
        "Rejected USB devices on lockscreen",
    ],
    "whitelisted-providers": [
        "hide Online Accounts services",
        "Hid Online Accounts services",
    ],
}
