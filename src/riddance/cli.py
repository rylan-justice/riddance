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

import argparse

from riddance import __version__
from riddance.options import check_compatibility, debloat_os, list_os_info

parser = argparse.ArgumentParser(
    prog="riddance",
    description="Designed to remove bloatware and augment freedom",
    add_help=False,
)

parser.add_argument(
    "-h",
    "--help",
    action="help",
    help="display help",
)
parser.add_argument(
    "-v",
    "--version",
    action="version",
    help="show version",
    version=__version__,
)
parser.add_argument(
    "-l",
    "--list",
    action="store_true",
    help="list compatible operating systems and their versions",
)
parser.add_argument(
    "-c",
    "--check",
    action="store_true",
    help="check operating system and version compatibility",
)
parser.add_argument(
    "-d",
    "--debloat",
    action="store_true",
    help="debloat a compatible operating system",
)

args = parser.parse_args()


def main():
    if args.list:
        list_os_info()
        return

    if args.check:
        check_compatibility()
        return

    if args.debloat:
        try:
            debloat_os()
            return

        except (EOFError, KeyboardInterrupt):
            return

    parser.print_help()
