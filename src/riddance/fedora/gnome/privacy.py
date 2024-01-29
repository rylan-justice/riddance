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
    ["org.gnome.desktop.privacy", "usb-protection", "true"],
    ["org.gnome.desktop.privacy", "usb-protection-level", "lockscreen"],
    ["org.gnome.online-accounts", "whitelisted-providers", "['']"],
    ["org.gnome.system.location", "enabled", "false"],
    ["org.gnome.system.location", "max-accuracy-level", "country"],
]

privacy_descriptions = {
    "disable-camera": [
        "disable camera access",
        "Disabled camera access",
    ],
    "disable-microphone": [
        "disable microphone access",
        "Disabled microphone access",
    ],
    "disable-sound-output": [
        "disable sound output",
        "Disabled sound output",
    ],
    "enabled": [
        "disable geolocation services",
        "Disabled geolocation services",
    ],
    "hide-identity": [
        "hide personal information from the screen and network",
        "Hid personal information from the screen and network",
    ],
    "max-accuracy-level": [
        "set the geolocation accuracy level to country",
        "Set the geolocation accuracy level to country",
    ],
    "old-files-age": [
        "always discard trash and temporary files",
        "Always discard trash and temporary files",
    ],
    "privacy-screen": [
        "enable the privacy screen if it is supported",
        "Enabled the privacy screen if it is supported",
    ],
    "recent-files-max-age": [
        "discard recently used files",
        "Discarded recently used files",
    ],
    "remember-app-usage": [
        "disable application usage monitoring and recording",
        "Disabled application usage monitoring and recording",
    ],
    "remember-recent-files": [
        "disable recently used files",
        "Disabled recently used files",
    ],
    "remove-old-temp-files": [
        "automatically remove temporary files",
        "Automatically removed temporary files",
    ],
    "remove-old-trash-files": [
        "automatically remove trash files",
        "Automatically removed trash files",
    ],
    "report-technical-problems": [
        "cease technical problem reports",
        "Ceased technical problem reports",
    ],
    "send-software-usage-stats": [
        "cease application statistics telemetry",
        "Ceased application statistics telemetry",
    ],
    "usb-protection": [
        "activate the USBGuard service",
        "Activated the USBGuard service",
    ],
    "usb-protection-level": [
        "reject USB devices on the lock screen",
        "Rejected USB devices on the lock screen",
    ],
    "whitelisted-providers": [
        "hide online account services",
        "Hid online account services",
    ],
}
