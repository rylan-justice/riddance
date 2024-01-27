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

import sys


def error_message(message, newline=True):
    """Display an error message."""

    end = "\n" if newline else ""
    print(f"{end}error: {message}")


def prompt_message(message):
    """Display a prompt message."""

    try:
        prompt = input(f"\n{message}")
        return prompt.strip().lower()

    except (EOFError, KeyboardInterrupt):
        sys.exit(0)
