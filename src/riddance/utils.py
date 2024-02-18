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

"""Common primary utilities."""


def error_message(message, newline=True):
    """Display an error message."""

    end = "\n" if newline else ""
    print(f"{end}error: {message}")


def prompt_message(message):
    """Display a prompt message."""

    prompt = input(f"\n{message} ")
    return prompt.strip().lower()


def output_message(message, newline=True):
    """Display an output message."""

    end = "\n" if newline else ""
    print(f"{end}info: {message}")
