#  c1222/utils.py
#  
#  Copyright 2013 Spencer J. McIntyre <SMcIntyre [at] SecureState [dot] net>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.

from struct import pack, unpack
import string
from binascii import hexlify, unhexlify
import CrcMoose # Get it from: http://www.nightmare.com/~ryb/code/CrcMoose.py

crc = CrcMoose.CRC_HDLC.calcString
crc_str = lambda x: pack("<H", crc(x))

def data_chksum(data):
	chksum = 0
	for i in unpack('B' * len(data), data):
		chksum += i
	return (((chksum - 1) & 0xff) ^ 0xff)

data_chksum_str = lambda x: chr(data_chksum(x))
