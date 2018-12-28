# *****************************************************************************
# Lomap: A toolkit to plan alchemical relative binding affinity calculations
# Copyright 2015 - 2019  UC Irvine and the Authors
#
# Authors: Dr Gaetano Calabro' and Dr David Mobley
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the MIT License along with this library;
# if not, see https://opensource.org/licenses/MIT
# *****************************************************************************

"""
Lomap
======

Alchemical free energy calculations hold increasing promise as an aid to drug 
discovery efforts. However, applications of these techniques in discovery 
projects have been relatively few, partly because of the difficulty of planning 
and setting up calculations. The Lead Optimization Mapper (LOMAP) is an 
automated algorithm to plan efficient relative free energy calculations between 
potential ligands within a substantial of compounds.

Authors: Gaetano Calabro' <gcalabro@eyesopen.com>
         David Mobley     <dmobley@uci.edu>


Licence: MIT

URL: https://github.com/nividic/Lomap


Using
-----
TESTING
"""

from . import toolkits
from .dbmol import DBMolecules