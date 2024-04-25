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

from riddance.fedora.gnome.core import enhance_privacy as enhance_privacy_we_gnome
from riddance.fedora.gnome.core import remove_packages as remove_packages_we_gnome


def fedora_linux_we_gnome():
    """Fedora Linux (Workstation Edition) with GNOME."""

    remove_packages_we_gnome()
    enhance_privacy_we_gnome()
