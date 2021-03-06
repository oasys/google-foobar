#!/usr/bin/env python3
from base64 import b64decode
from getpass import getpass
from itertools import cycle

message = """
EUYAGg1NCRIFSElfSkYUHQtPGEZaT04GBQ0fCg9JGQRRT1NFTQQAGwtLAQQSSEVFTQQVCQFcGBJR
T1NFTQgdDBxLCAgUAwxCRkFUDg1GBQQACgQABBVUT1QOSxQYAwYGAQQXSEIOSxMXDQsMHhJUT1QO
SxIXCQxCRkFUCQFBS0FMT04SAw9SSBM=
"""

key = getpass()
for m, k in zip(b64decode(message), cycle(key)):
    print(chr(m ^ ord(k)), end="")
print()
