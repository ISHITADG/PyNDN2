# -*- Mode:python; c-file-style:"gnu"; indent-tabs-mode:nil -*- */
#
# Copyright (C) 2014 Regents of the University of California.
# Author: Jeff Thompson <jefft0@remap.ucla.edu>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# A copy of the GNU General Public License is in the file COPYING.

"""
This module defines constants used by the security library.
"""

class KeyType(object):
    RSA = 1
    AES = 2
    # DSA
    # DES
    # RC4
    # RC2
    EC = 3

class KeyClass(object):
    PUBLIC = 1
    PRIVATE = 2
    SYMMETRIC = 3
    
class DigestAlgorithm(object):
    SHA256 = 1
    # MD2
    # MD5
    # SHA1

class EncryptMode(object):
    DEFAULT = 1
    CFB_AES = 2
    # CBC_AES
