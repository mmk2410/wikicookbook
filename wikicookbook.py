#!/usr/bin/env python3

# Copyright (C) 2020-2021 Marcel Kapfer <opensource@mmk2410.org>
#
# This file is part of WikiCookBook.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""Launcher for WikiCookBook"""

import sys
import WikiCookBook.wikicookbook

if __name__ == "__main__":
    sys.exit(WikiCookBook.wikicookbook.main())
