#!/usr/bin/python
#
# namelist.py: A FontForge python script for generating namelist files.
#
# Usage: namelist.py Font.ttf NameList.nam

import fontforge, sys

font = fontforge.open(sys.argv[1])
font.saveNamelist(sys.argv[2])