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

import subprocess
import sys

from riddance.utils import error_message, prompt_message


def reboot_os():
    """Prompt the user to reboot the operating system."""

    reboot = prompt_message("Would you like to reboot the operating system? [Y/n]: ")

    if reboot == "" or reboot.startswith("y"):
        subprocess.run(["reboot"], check=False)

    elif reboot.startswith("n"):
        sys.exit(0)

    else:
        error_message(f"invalid response: {reboot}")
        reboot_os()
