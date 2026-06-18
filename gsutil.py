import sys
ver = sys.version_info
if ver.major != 3 or ver.minor < 8 or ver.minor > 12:
  sys.exit("Error")

